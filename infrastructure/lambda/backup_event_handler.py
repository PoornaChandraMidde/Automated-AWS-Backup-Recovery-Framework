import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))
    # Example processing of AWS Backup event
    for record in event.get('Records', []):
        logger.info("Record: %s", record)
    return {"status": "ok"}
