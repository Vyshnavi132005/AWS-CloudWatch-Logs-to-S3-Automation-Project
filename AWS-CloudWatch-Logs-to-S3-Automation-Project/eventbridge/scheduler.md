# EventBridge Scheduler

## Purpose

EventBridge Scheduler can invoke the Lambda function automatically according to a schedule.

Example schedule:

```text
rate(1 hour)
```

or a cron expression appropriate for the required frequency.

## Flow

```text
EventBridge Scheduler
        ↓
      Lambda
        ↓
 CloudWatch Logs
        ↓
       S3
```

## Configuration

1. Create an EventBridge Scheduler schedule.
2. Select AWS Lambda as the target.
3. Select the log-export Lambda function.
4. Configure the required input payload.
5. Allow Scheduler to invoke the Lambda function.
6. Test the schedule.
7. Verify the generated object in S3.

Use a schedule appropriate for the required archival frequency rather than copying the example blindly.
