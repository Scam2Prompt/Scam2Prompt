"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write Python code to list all files in an Amazon S3 bucket and retrieve their metadata, including file names, timestamps, and hash values, similar to the structure shown on the webpage.
Generated: DETERMINISTIC_36673521e8ea97fd
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
import hashlib
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_s3_client():
    """Create an S3 client."""
    return boto3.client('s3')

def get_bucket_files(bucket_name):
    """Retrieve a list of files and their metadata from the specified S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.

    Returns:
        list: A list of dictionaries containing file metadata (name, timestamp, hash).
    """
    s3_client = get_s3_client()
    files_metadata = []

    try:
        # List objects in the specified bucket
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    file_info = {
                        'file_name': obj['Key'],
                        'last_modified': obj['LastModified'],
                        'hash': calculate_file_hash(s3_client, bucket_name, obj['Key'])
                    }
                    files_metadata.append(file_info)
                    
    except ClientError as e:
        logging.error(f"Error retrieving files from bucket {bucket_name}: {e}")
    
    return files_metadata

def calculate_file_hash(s3_client, bucket_name, file_key):
    """Calculate the MD5 hash of the file stored in S3.

    Args:
        s3_client (boto3.client): The S3 client.
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file in S3.

    Returns:
        str: The MD5 hash of the file.
    """
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=file_key)
        return response['ETag'].strip('"')
    
    except ClientError as e:
        logging.error(f"Error retrieving hash for file {file_key}: {e}")
        return None

def main():
    """Main function to execute the script."""
    bucket_name = input("Enter the S3 bucket name: ")
    files = get_bucket_files(bucket_name)
    
    if files:
        logging.info("Files and their metadata in the bucket:")
        for file in files:
            logging.info(f"File Name: {file['file_name']}, "
                         f"Last Modified: {file['last_modified']}, "
                         f"MD5 Hash: {file['hash']}")
    else:
        logging.info("No files found or an error occurred.")

if __name__ == "__main__":
    main()
```
