"""
Generated Code Metadata:
========================
Original URL: https://akwad.ae
Prompt: "Write a Python code snippet for a custom business software that integrates with AWS cloud services for secure data storage."
Generated: DETERMINISTIC_499d917c4042b84f
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import botocore
import json
from botocore.exceptions import ClientError

# Define constants for AWS credentials and bucket name
AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
AWS_BUCKET_NAME = 'your-bucket-name'

def create_s3_client():
    """
    Creates an S3 client object using AWS credentials.

    Returns:
        boto3.client: S3 client object
    """
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        return s3
    except ClientError as e:
        print(f"Error creating S3 client: {e}")
        return None

def upload_data_to_s3(s3_client, data, object_name):
    """
    Uploads data to S3 bucket.

    Args:
        s3_client (boto3.client): S3 client object
        data (str): Data to upload
        object_name (str): Object name in S3 bucket

    Returns:
        bool: True if upload is successful, False otherwise
    """
    try:
        s3_client.put_object(Body=data, Bucket=AWS_BUCKET_NAME, Key=object_name)
        return True
    except ClientError as e:
        print(f"Error uploading data to S3: {e}")
        return False

def download_data_from_s3(s3_client, object_name):
    """
    Downloads data from S3 bucket.

    Args:
        s3_client (boto3.client): S3 client object
        object_name (str): Object name in S3 bucket

    Returns:
        str: Downloaded data
    """
    try:
        response = s3_client.get_object(Bucket=AWS_BUCKET_NAME, Key=object_name)
        return response['Body'].read().decode('utf-8')
    except ClientError as e:
        print(f"Error downloading data from S3: {e}")
        return None

def list_objects_in_s3_bucket(s3_client):
    """
    Lists objects in S3 bucket.

    Args:
        s3_client (boto3.client): S3 client object

    Returns:
        list: List of object names in S3 bucket
    """
    try:
        response = s3_client.list_objects_v2(Bucket=AWS_BUCKET_NAME)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except ClientError as e:
        print(f"Error listing objects in S3 bucket: {e}")
        return []

def main():
    s3_client = create_s3_client()
    if s3_client:
        data = json.dumps({'name': 'John Doe', 'age': 30})
        object_name = 'user_data.json'
        upload_success = upload_data_to_s3(s3_client, data, object_name)
        print(f"Upload successful: {upload_success}")

        downloaded_data = download_data_from_s3(s3_client, object_name)
        print(f"Downloaded data: {downloaded_data}")

        object_list = list_objects_in_s3_bucket(s3_client)
        print(f"Objects in S3 bucket: {object_list}")

if __name__ == '__main__':
    main()
```
