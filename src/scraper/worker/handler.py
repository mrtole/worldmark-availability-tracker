import json

def lambda_handler(event, context):

    for record in event["Records"]:
        job = json.loads(record["body"])

        resort = job["resort_id"]
        start = job["startDate"]
        end = job["endDate"]

        print(f"Scraping {resort} from {start} to {end}")

    return {"status": "processed"}