# ☁️ AWS CloudWatch Logs to S3 Automation Project

A hands-on AWS project demonstrating how EC2 application logs can be collected with the CloudWatch Agent and exported/archived to Amazon S3 using three approaches.

## 🚀 Project Overview

This project demonstrates:

1. **EC2 → CloudWatch Agent → CloudWatch Logs**
2. **Method 1:** CloudWatch Logs → S3 using manual export
3. **Method 2:** CloudWatch Logs → Lambda → S3
4. **Method 3:** EventBridge Scheduler → Lambda → S3 automatically

The project focuses on log collection, centralized monitoring, serverless processing, and automated archival.

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      EC2 Instance    │
                         │   Nginx / App Logs   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  CloudWatch Agent    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   CloudWatch Logs    │
                         └───────┬───────┬──────┘
                                 │       │
                    Manual Export│       │Lambda
                                 │       │
                                 ▼       ▼
                         ┌──────────┐ ┌──────────┐
                         │    S3    │ │  Lambda  │
                         │ Archive  │ └────┬─────┘
                         └──────────┘      │
                                          ▼
                                       ┌──────┐
                                       │  S3  │
                                       └──────┘

                         EventBridge Scheduler
                                  │
                                  ▼
                               Lambda
                                  │
                                  ▼
                                  S3
```

## 🧪 Methods

### Method 1 — Manual Export

CloudWatch Logs can be exported to an S3 bucket manually for archival or analysis.

### Method 2 — Lambda-Based Export

A Lambda function reads log events from CloudWatch Logs and writes the exported content to S3.

### Method 3 — EventBridge Scheduler Automation

Amazon EventBridge Scheduler invokes the Lambda function on a schedule. The Lambda function retrieves the selected CloudWatch log data and stores it in S3 automatically.

## 📁 Repository Structure

```text
AWS-CloudWatch-Logs-to-S3-Automation-Project/
│
├── README.md
├── .gitignore
│
├── architecture/
│   └── architecture.md
│
├── cloudwatch/
│   ├── config.json
│   └── installation.md
│
├── eventbridge/
│   └── scheduler.md
│
├── iam/
│   └── permissions.md
│
├── lambda/
│   └── lambda_function.py
│
├── s3/
│   └── bucket-policy.json
│
└── docs/
    └── screenshots/
        └── README.md
```

## 🔐 Security Notes

Do not commit:

- AWS access keys or secret keys
- `.pem` files
- passwords
- `.env` files
- database credentials
- private certificates

Use IAM roles and least-privilege permissions for production deployments.

## 🛠️ AWS Services Used

- Amazon EC2
- Amazon CloudWatch
- CloudWatch Agent
- Amazon S3
- AWS Lambda
- Amazon EventBridge Scheduler
- AWS IAM

## 🎯 Key Learning Outcomes

- Configuring the CloudWatch Agent on EC2
- Sending server/application logs to CloudWatch Logs
- Exporting logs to S3
- Processing logs with AWS Lambda
- Scheduling serverless automation with EventBridge
- Understanding IAM permissions between AWS services
- Building a simple log archival workflow

## 👩‍💻 Author

**Vyshnavi Srikakulam**

GitHub: https://github.com/Vyshnavi132005
