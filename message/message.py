# -*- coding: utf-8 -*-

import json
import requests

def lambda_handler(event, context):
    print("-------------------------------------------")
    print(event)
    print("-------------------------------------------")

    body = json.loads(event["body"])
    print(body["events"][0])
    print(body["events"][0]["replyToken"])
    print(body["events"][0]["message"])

    payload = {
        "replyToken": body["events"][0]["replyToken"],
        "messages": [{
            "type": "text",
            "text": "Hello🐸",
        }]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer xxxxxx",
    }
    response = requests.post('https://api.line.me/v2/bot/message/reply', json.dumps(payload), headers=headers)
    print(response.json())
    return { "statusCode": "200", "body": { "hoge": "hoge" } }
