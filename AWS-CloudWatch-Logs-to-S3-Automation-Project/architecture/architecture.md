# Architecture

## Log Collection Flow

EC2 → CloudWatch Agent → CloudWatch Logs

## Log Export Flows

### Manual
CloudWatch Logs → S3

### Lambda
CloudWatch Logs → Lambda → S3

### Scheduled Automation
EventBridge Scheduler → Lambda → CloudWatch Logs → S3

## Production Considerations

For production workloads, consider:

- Least-privilege IAM roles
- S3 Block Public Access
- S3 encryption
- Lifecycle policies
- CloudWatch retention policies
- CloudTrail auditing
- Error handling and retry logic
- Dead-letter queues where appropriate
