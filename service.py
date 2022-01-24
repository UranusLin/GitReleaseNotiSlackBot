
import setting
import utils

setting = setting.get_settings()


# get all coin repo
async def get_all_release():
    data = setting.chain_release
    result = {
        "count": len(data),
        "data": data
    }
    return result


# get release from name
async def get_release_from_name(name: str):
    return setting.chain_release.get(name)


# get repo and send msg
async def get_release_and_send_msg():
    result = await utils.get_all_url()
    # for sorting by date_ago
    result.sort(key=lambda x: x.published_at, reverse=True)
    temp = []
    # ever 10 chain will send message cause slack blocks limit 50 blocks in one time
    while len(result) > 0:
        temp.append(result.pop())
        if len(temp) == 10:
            await utils.send_channel_message(await utils.format_slack_msg(temp))
            temp = []
    if len(temp) > 0:
        await utils.send_channel_message(await utils.format_slack_msg(temp))
    return result
