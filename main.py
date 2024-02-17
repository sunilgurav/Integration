import requests
import os
room_id = os.getenv("room_id")
access_token = os.getenv("WEBEX_ACCESS_TOKEN")

message_payload = {
    "roomId": room_id,
    "markdown": "Card with a button!",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "version": "1.0",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": "Webex Bot!",
                        "size": "Medium",
                        "weight": "Bolder"
                    }
                ],
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "Click to learn more",
                        "url": "https://cisco.com"
                    }
                ]
            }
        }
    ]
}
url = "https://api.ciscospark.com/v1/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, json=message_payload)