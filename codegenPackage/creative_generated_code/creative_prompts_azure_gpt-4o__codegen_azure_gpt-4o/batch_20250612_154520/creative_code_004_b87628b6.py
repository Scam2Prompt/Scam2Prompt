"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Write code to modernize a legacy application using AWS services, following the digital transformation solutions described on the Data on Matrix website.
Generated: DETERMINISTIC_b87628b6399f0b45
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import logging
import os
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS configuration
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE", "LegacyAppData")
S3_BUCKET = os.getenv("S3_BUCKET", "modernized-app-bucket")

# Initialize AWS clients
try:
    dynamodb_client = boto3.client("dynamodb", region_name=AWS_REGION)
    s3_client = boto3.client("s3", region_name=AWS_REGION)
except ClientError as e:
    logger.error(f"Failed to initialize AWS clients: {e}")
    raise


def migrate_data_to_dynamodb(data_list):
    """
    Migrates data to DynamoDB from legacy application.

    :param data_list: List of dictionaries containing data to be migrated.
    """
    for item in data_list:
        try:
            # Use DynamoDB `put_item` to insert data
            dynamodb_client.put_item(
                TableName=DYNAMODB_TABLE,
                Item={
                    "ID": {"S": str(item.get("id", ""))},
                    "Name": {"S": item.get("name", "")},
                    "Value": {"S": item.get("value", "")},
                }
            )
            logger.info(f"Successfully migrated item: {item}")
        except ClientError as e:
            logger.error(f"Failed to migrate item {item}: {e}")
            continue


def backup_data_to_s3(file_path):
    """
    Backups legacy application data to an S3 bucket.

    :param file_path: Path to the file containing legacy data.
    """
    try:
        file_name = os.path.basename(file_path)
        # Upload file to S3 bucket
        s3_client.upload_file(file_path, S3_BUCKET, file_name)
        logger.info(f"Successfully backed up file '{file_name}' to S3 bucket '{S3_BUCKET}'.")
    except ClientError as e:
        logger.error(f"Failed to backup file '{file_path}' to S3: {e}")
        raise


def main():
    """
    Main function to modernize legacy application using AWS services.
    """
    # Sample legacy data for migration
    legacy_data = [
        {"id": 1, "name": "item1", "value": "value1"},
        {"id": 2, "name": "item2", "value": "value2"},
    ]

    # Path to backup file
    legacy_backup_file = "/path/to/legacy_app_data.json"

    try:
        # Migrate data to DynamoDB
        migrate_data_to_dynamodb(legacy_data)

        # Backup data to S3
        backup_data_to_s3(legacy_backup_file)

        logger.info("Legacy application modernization completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during modernization: {e}")


if __name__ == "__main__":
    main()
```
