# Automated AWS Backup & Recovery Framework
A fully automated, serverless backup & disaster recovery system built using **AWS Backup, Lambda, SNS, and S3**.

## Architecture Overview
User Data → AWS Backup Plans → Backup Vaults → CloudWatch Events → Lambda → SNS → S3 Lifecycle

## Project Structure
infrastructure/
  ├── lambda/
  │   └── backup_event_handler.py
  ├── iam/
  │   └── lambda-role.json
  ├── backup-plans/
  │   ├── rds-backup-plan.json
  │   └── ebs-backup-plan.json
docs/
  └── runbook.md
diagrams/
  └── architecture-diagram.png

## Deployment Steps (examples)
1. Create IAM role for Lambda:
```bash
aws iam create-role --role-name BackupLambdaRole --assume-role-policy-document file://infrastructure/iam/lambda-role.json
```
2. Deploy backup plans:
```bash
aws backup create-backup-plan --backup-plan file://infrastructure/backup-plans/rds-backup-plan.json
```
3. Deploy Lambda:
```bash
zip lambda.zip infrastructure/lambda/backup_event_handler.py
aws lambda create-function --function-name BackupEventHandler --runtime python3.12 --handler backup_event_handler.lambda_handler --role arn:aws:iam::<account-id>:role/BackupLambdaRole --zip-file fileb://lambda.zip
```
