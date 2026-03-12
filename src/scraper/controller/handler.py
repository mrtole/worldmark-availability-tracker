# src/scraper/controller/handler.py
import os
import boto3
import json

sqs = boto3.client("sqs", region_name="us-east-1")  # region can be anything for local testing
QUEUE_URL = os.environ.get("QUEUE_URL", "http://localhost:4566/000000000000/worldmark-scrape-queue")  # for local testing

def lambda_handler(event, context):
    message = {
        "resort_id": "depobay",
        "startDate": "2026-07-01",
        "endDate": "2026-09-01"
    }
    print(f"Sending message to SQS: {message}")
    # For local testing, you can skip actual SQS send
    # sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(message))
    return {"statusCode": 200, "body": json.dumps({"message": "Controller executed"})}