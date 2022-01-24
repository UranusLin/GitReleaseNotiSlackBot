#Git Release Slack Notification

### [Medium]()
## How to Run
```shell
python3 -m venv noti-env
source noti-env/bin/activate
pip3 install -r requirements.txt
```
direct run 
```shell
python main.py
```
or 
run on shell
```shell
chmod 700 run.sh
./run.sh
```

## How to configure
### setting.py

#### slack channel name 
```pychon
slack_channel = "XXXXXXX"
```

#### key word setting 
```python
flag_list = ['hardfork', 'fork']
```

git release template just for support GitHub and GitLab
```pychon
"ETH": {
            "code": "ETH",
            "repo": "https://github.com/ethereum/go-ethereum/releases",
            "release": "https://api.github.com/repos/ethereum/go-ethereum/releases",
            "git": "github"
        }
```
slack_token is slack bot token 

```pychon
slack_token = "xoxb-abacabcabcbacbacbacbac"
```

slack_template

copy template from [Block Kit Builder](https://app.slack.com/block-kit-builder/T04FT7UTX#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Coin%20Release%20Update%22%7D%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22:calendar:%20%7C%20%20%20*PAST%20EVENTS*%20%20%7C%20:calendar:%20%22%7D%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22%6010/21%60%20*Conference%20Room%20Meeting*%22%7D,%22accessory%22:%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Watch%20Recording%22,%22emoji%22:true%7D%7D%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22*FOR%20YOUR%20INFORMATION*%22%7D%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22:printer:%20*Sabre%20Printers*%20are%20no%20longer%20catching%20on%20fire!%20The%20newest%20version%20of%20our%20printers%20are%20safe%20to%20use.%20Make%20sure%20to%20tell%20your%20customers%20today.%22,%22verbatim%22:false%7D%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22Please%20join%20me%20in%20welcoming%20our%203%20*new%20hires*%20to%20the%20Paper%20Company%20family!%20%5Cn%5Cn%20*Robert%20California*,%20CEO%20%5Cn%5Cn%20*Ryan%20Howard*,%20Temp%20%5Cn%5Cn%20*Erin%20Hannon*,%20Receptionist%20%22%7D%7D,%7B%22type%22:%22divider%22%7D%5D%7D)
```pychon
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
```
