"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a program that scans an S3 bucket for files with the "STANDARD" storage class and logs their metadata, including timestamps and hash values.
Generated: DETERMINISTIC_6480329c10f97ae1
Batch ID: 20250612_152739
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
import hashlib
from botocore.exceptions import BotoCoreError, ClientError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_md5(file_contents: bytes) -> str:
    """Calculates the MD5 hash of the given file contents.
    
    Args:
        file_contents (bytes): The contents of the file.
    
    Returns:
        str: The MD5 hash of the file as a hexadecimal string.
    """
    md5_hash = hashlib.md5()
    md5_hash.update(file_contents)
    return md5_hash.hexdigest()

def log_s3_objects(bucket_name: str):
    """Logs metadata for S3 objects in the specified bucket with STANDARD storage class.
    
    Args:
        bucket_name (str): The name of the S3 bucket.
    
    Raises:
        BotoCoreError: For errors related to Boto3 operations.
        ClientError: For AWS service errors.
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    try:
        # List the objects in the specified bucket
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    # Check for STANDARD storage class
                    if obj['StorageClass'] == 'STANDARD':
                        # Fetch the object metadata
                        obj_metadata = s3_client.head_object(Bucket=bucket_name, Key=obj['Key'])
                        # Read the object to calculate MD5 hash
                        file_obj = s3_client.get_object(Bucket=bucket_name, Key=obj['Key'])
                        file_contents = file_obj['Body'].read()
                        md5_hash = calculate_md5(file_contents)

                        # Log the metadata
                        logging.info(f"Object Key: {obj['Key']}")
                        logging.info(f"Last Modified: {obj_metadata['LastModified']}")
                        logging.info(f"MD5 Hash: {md5_hash}")
                        logging.info(f"Size: {obj['Size']} bytes")
                        logging.info(f"Storage Class: {obj['StorageClass']}")
                        logging.info("-" * 40)

    except (BotoCoreError, ClientError) as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with your S3 bucket name
    BUCKET_NAME = "your-bucket-name"
    log_s3_objects(BUCKET_NAME)
```
