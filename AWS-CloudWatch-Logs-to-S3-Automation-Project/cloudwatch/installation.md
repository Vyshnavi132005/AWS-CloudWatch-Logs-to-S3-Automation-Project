# CloudWatch Agent Installation

The exact installation command depends on the operating system and AWS environment.

## General Steps

1. Launch an EC2 instance.
2. Attach an IAM role that allows the instance to publish CloudWatch metrics/logs.
3. Install the Amazon CloudWatch Agent.
4. Place the agent configuration file on the instance.
5. Start the CloudWatch Agent.
6. Verify the log groups and log streams in CloudWatch Logs.

## Example Linux Commands

```bash
sudo yum update -y
sudo yum install -y amazon-cloudwatch-agent
```

For Ubuntu, use the appropriate package installation method for the installed Ubuntu release.

Copy the configuration file and start the agent using the CloudWatch Agent control script.

> Commands can vary by AMI. Verify the package name and service commands for your selected operating system.
