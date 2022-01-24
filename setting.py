from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    # slack channel name
    slack_channel = "slack_channel"
    slack_token = "slack_token"
    flag_list = ['hardfork', 'fork']
    git_release = {
        "ETH": {
            "code": "ETH",
            "repo": "https://github.com/ethereum/go-ethereum/releases",
            "release": "https://api.github.com/repos/ethereum/go-ethereum/releases",
            "git": "github"
        }, "AVAX": {
            "code": "AVAX",
            "repo": "https://github.com/ava-labs/avalanchego/releases",
            "release": "https://api.github.com/repos/ava-labs/avalanchego/releases",
            "git": "github"
        }
    }

    slack_template = {
        "header": {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Coin Release Update"
            }
        },
        "divider": {
            "type": "divider"
        },
        "section": {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ""
            }
        },
        "context": {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": ""
                }
            ]
        }
    }


@lru_cache()
def get_settings():
    return Settings()
