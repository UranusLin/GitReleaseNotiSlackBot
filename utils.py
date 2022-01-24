import asyncio
import aiohttp
import arrow
from typing import List
import copy

import setting
from model import Release
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

setting = setting.get_settings()
repos = []
slack_token = setting.slack_token
client = WebClient(token=slack_token)


# async to get all repos but need notice 1 hour just can get 60 requests
async def get(url, session):
    try:
        async with session.get(url=url.get("release")) as response:
            resp = await response.json()
            await process_response(resp[0], url)
            print("Successfully got url {} with resp.".format(url.get("release")))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def main(urls):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[get(url, session) for url in urls])
    print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))


# get all url form setting.py git_release
async def get_all_url():
    global repos
    repos = []
    data = setting.git_release
    urls = []
    for i, j in data.items():
        if j.get("release"):
            urls.append(j)
    await main(urls)
    print(repos)
    return repos


# to process GitLab or GitHub API response
async def process_response(res: dict, url: dict):
    global repos
    if url.get("git") == "github":
        # for GitHub
        release = Release(
            Protocol=url.get("code"),
            name=res.get("name"),
            tag_name=res.get("tag_name"),
            published_at=res.get("published_at"),
            url=res.get("html_url"),
            date_ago=await calculate_day_age(res.get("published_at")),
            body=res.get("body"),
        )
        repos.append(release)
    else:
        # for gitlab
        release = Release(
            Protocol=url.get("code"),
            name=res.get("name"),
            tag_name=res.get("tag_name"),
            published_at=res.get("released_at"),
            url=res.get("_links").get("self"),
            date_ago=await calculate_day_age(res.get("released_at")),
        )
        repos.append(release)


# calculate time ago
async def calculate_day_age(published_at: str):
    return "{} day ago".format((arrow.utcnow() - arrow.get(published_at)).days)


# send message to channel
async def send_channel_message(blocks: list):
    try:
        # Posting a message in slack_channel
        response = client.chat_postMessage(
            channel=setting.slack_channel,
            text=None,
            blocks=blocks),
        print(response)
    except SlackApiError as e:
        print(e)
        assert e.response["error"]


# format msg to slack blocks template
async def format_slack_msg(result: List[Release]) -> list:
    msg = [setting.slack_template.get("header"), setting.slack_template.get("divider")]
    for i in result:
        protocol = copy.deepcopy(setting.slack_template.get("section"))
        protocol["text"]["text"] = i.Protocol
        msg.append(protocol)
        # check if flag in body
        if i.body:
            flag_list = await check_flag(i.body)
            if len(flag_list) > 0:
                for flag in flag_list:
                    context = copy.deepcopy(setting.slack_template.get("context"))
                    context["elements"][0]["text"] = flag
                    msg.append(context)
        section = copy.deepcopy(setting.slack_template.get("section"))
        section["text"]["text"] = "release time: {3}  ({4}) \n\n " \
                                  "release name: {0} \n\n " \
                                  "release tag: {1} \n\n " \
                                  "release url: {2} \n\n".format(i.name, i.tag_name, i.url, i.published_at,
                                                                 i.date_ago)
        msg.append(section)
        msg.append(setting.slack_template.get("divider"))
    return msg


# check if flag in body text will add pin template
async def check_flag(text: str) -> list:
    # get flag list from setting
    flag_list = []
    for flag in setting.flag_list:
        if flag in text:
            flag_list.append(":pushpin: Here's {} in body.".format(flag))
    return flag_list
