# WorldMark Availability Tracker

A serverless AWS application that tracks availability for WorldMark resorts.

## Architecture

EventBridge → Scraper Controller → SQS → Worker Lambdas → DynamoDB

Frontend:
React → CloudFront → S3

Backend:
API Gateway → Lambda → DynamoDB