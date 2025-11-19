"""
Generated Code Metadata:
========================
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Generate a Python script to list and download files from an AWS S3 bucket, considering the bucket's URL and authentication requirements.
Generated: DETERMINISTIC_04759d97279c59ce
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Constants for AWS S3
AWS_REGION = 'us-west-2'  # Change to your AWS region
BUCKET_NAME = 'your-bucket-name'  # Change to your S3 bucket name
DOWNLOAD_DIR = 'downloads'  # Directory to save downloaded files

def create_download_directory():
    """Create a directory for downloads if it doesn't exist."""
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

def list_files_in_bucket(s3_client):
    """List all files in the specified S3 bucket."""
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            return [item['Key'] for item in response['Contents']]
        else:
            return []
    except ClientError as e:
        print(f"Error listing files in bucket: {e}")
        return []

def download_file(s3_client, file_key):
    """Download a file from the S3 bucket."""
    try:
        local_file_path = os.path.join(DOWNLOAD_DIR, file_key)
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)  # Create directories if needed
        s3_client.download_file(BUCKET_NAME, file_key, local_file_path)
        print(f"Downloaded: {file_key} to {local_file_path}")
    except ClientError as e:
        print(f"Error downloading {file_key}: {e}")

def main():
    """Main function to list and download files from S3 bucket."""
    create_download_directory()

    # Create an S3 client
    try:
        s3_client = boto3.client('s3', region_name=AWS_REGION)
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Credentials error: {e}")
        return

    # List files in the bucket
    files = list_files_in_bucket(s3_client)
    if not files:
        print("No files found in the bucket.")
        return

    print("Files in bucket:")
    for file_key in files:
        print(f"- {file_key}")

    # Download each file
    for file_key in files:
        download_file(s3_client, file_key)

if __name__ == "__main__":
    main()
```
