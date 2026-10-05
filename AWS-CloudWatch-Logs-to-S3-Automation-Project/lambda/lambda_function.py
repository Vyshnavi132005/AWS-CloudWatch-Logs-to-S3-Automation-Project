import os
import json
import boto3
from datetime import datetime, timezone

logs = boto3.client("logs")
s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]
LOG_GROUP_NAME = os.environ["LOG_GROUP_NAME"]
S3_PREFIX = os.environ.get("S3_PREFIX", "cloudwatch-logs")

def lambda_handler(event, context):
    # Optional scheduler payload:
    # {
    #   "log_group_name": "/aws/ec2/nginx/access",
    #   "start_time_ms": 0,
    #   "end_time_ms": 0
    # }

    log_group = event.get("log_group_name", LOG_GROUP_NAME)

    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    start_ms = int(event.get("start_time_ms", now_ms - 3600000))
    end_ms = int(event.get("end_time_ms", now_ms))

    response = logs.filter_log_events(
        logGroupName=log_group,
        startTime=start_ms,
        endTime=end_ms
    )

    lines = []
    for item in response.get("events", []):
        timestamp = item.get("timestamp", "")
        message = item.get("message", "").rstrip()
        lines.append(f"{timestamp} {message}")

    content = "\n".join(lines)
    timestamp = datetime.now(timezone.utc).strftime("%Y/%m/%d/%H%M%S")
    safe_group = log_group.strip("/").replace("/", "_") or "log-group"
    key = f"{S3_PREFIX}/{safe_group}/{timestamp}.log"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=content.encode("utf-8"),
        ContentType="text/plain"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "CloudWatch logs exported to S3",
            "bucket": BUCKET_NAME,
            "key": key,
            "events_exported": len(lines)
        })
    }
