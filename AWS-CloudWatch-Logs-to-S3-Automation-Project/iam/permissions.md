# IAM Permissions

## EC2 / CloudWatch Agent Role

The EC2 instance needs permissions to publish logs and metrics to CloudWatch.

For learning environments, an AWS-managed CloudWatch Agent policy may be used. For production, create a custom least-privilege policy.

## Lambda Execution Role

The Lambda function requires permissions similar to:

- `logs:DescribeLogStreams`
- `logs:GetLogEvents`
- `logs:FilterLogEvents`
- `s3:PutObject`

The role should restrict access to the specific CloudWatch log groups and S3 bucket/prefix used by the project.

## EventBridge Scheduler Role

The scheduler needs permission to invoke the target Lambda function:

- `lambda:InvokeFunction`

Avoid broad administrator permissions for production workloads.
