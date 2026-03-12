import json

def lambda_handler(event, context):
    print("Received event:", event)  # <-- Add this to debug
    query_params = event.get("queryStringParameters") or {}

    response_body = {
        "message": "WorldMark tracker API working",
        "query_params": query_params
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response_body),
        "headers": {"Content-Type": "application/json"}
    }