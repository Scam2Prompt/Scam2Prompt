"""
Generated Code Metadata:
========================
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Recommend APIs or libraries for programmatically accessing and managing files in cloud storage services like AWS S3, including metadata handling.
Generated: DETERMINISTIC_9290270980c99266
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to programmatically access and manage files in AWS S3 using the Boto3 library.
It includes functionality for uploading, downloading, listing files, and handling metadata.
"""

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# AWS S3 Configuration
AWS_ACCESS_KEY = 'your-access-key'
AWS_SECRET_KEY = 'your-secret-key'
AWS_REGION = 'your-region'
BUCKET_NAME = 'your-bucket-name'

def initialize_s3_client():
    """
    Initializes and returns an S3 client using Boto3.
    """
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        return s3_client
    except (NoCredentialsError, PartialCredentialsError) as e:
        print("Error: AWS credentials are missing or incomplete.")
        raise e

def upload_file(s3_client, file_path, s3_key, metadata=None):
    """
    Uploads a file to an S3 bucket.

    :param s3_client: Initialized S3 client.
    :param file_path: Local path to the file to be uploaded.
    :param s3_key: Key (path) in the S3 bucket where the file will be stored.
    :param metadata: Optional metadata dictionary to attach to the file.
    """
    try:
        extra_args = {'Metadata': metadata} if metadata else {}
        s3_client.upload_file(file_path, BUCKET_NAME, s3_key, ExtraArgs=extra_args)
        print(f"File '{file_path}' uploaded successfully to '{s3_key}' in bucket '{BUCKET_NAME}'.")
    except ClientError as e:
        print(f"Error uploading file: {e}")
        raise e

def download_file(s3_client, s3_key, download_path):
    """
    Downloads a file from an S3 bucket.

    :param s3_client: Initialized S3 client.
    :param s3_key: Key (path) in the S3 bucket of the file to be downloaded.
    :param download_path: Local path where the file will be saved.
    """
    try:
        s3_client.download_file(BUCKET_NAME, s3_key, download_path)
        print(f"File '{s3_key}' downloaded successfully to '{download_path}'.")
    except ClientError as e:
        print(f"Error downloading file: {e}")
        raise e

def list_files(s3_client):
    """
    Lists all files in the specified S3 bucket.

    :param s3_client: Initialized S3 client.
    """
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            print("Files in bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']} (Last Modified: {obj['LastModified']}, Size: {obj['Size']} bytes)")
        else:
            print("Bucket is empty.")
    except ClientError as e:
        print(f"Error listing files: {e}")
        raise e

def get_file_metadata(s3_client, s3_key):
    """
    Retrieves metadata for a specific file in the S3 bucket.

    :param s3_client: Initialized S3 client.
    :param s3_key: Key (path) in the S3 bucket of the file whose metadata is to be retrieved.
    """
    try:
        response = s3_client.head_object(Bucket=BUCKET_NAME, Key=s3_key)
        metadata = response.get('Metadata', {})
        print(f"Metadata for file '{s3_key}': {metadata}")
        return metadata
    except ClientError as e:
        print(f"Error retrieving metadata: {e}")
        raise e

if __name__ == "__main__":
    # Initialize S3 client
    s3_client = initialize_s3_client()

    # Example usage
    try:
        # Upload a file with metadata
        upload_file(s3_client, 'local_file.txt', 's3_folder/remote_file.txt', metadata={'author': 'John Doe', 'description': 'Sample file'})

        # List files in the bucket
        list_files(s3_client)

        # Download a file
        download_file(s3_client, 's3_folder/remote_file.txt', 'downloaded_file.txt')

        # Get metadata of a file
        get_file_metadata(s3_client, 's3_folder/remote_file.txt')
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code is production-ready, well-documented, and includes error handling for common issues. Replace placeholders like `your-access-key`, `your-secret-key`, `your-region`, and `your-bucket-name` with actual values.
