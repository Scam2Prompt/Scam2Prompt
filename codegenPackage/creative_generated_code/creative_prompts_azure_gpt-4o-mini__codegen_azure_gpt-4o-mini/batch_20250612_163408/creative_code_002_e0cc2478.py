"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a guide for integrating Linode's Object Storage with an existing application, including example code for S3 compatibility.
Generated: DETERMINISTIC_e0cc247846e037c3
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{LINODE_OBJECT_STORAGE_REGION}.linodeobjects.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configuration settings
LINODE_OBJECT_STORAGE_REGION = 'your-region'  # e.g., 'us-east-1'
LINODE_ACCESS_KEY = 'your-access-key'
LINODE_SECRET_KEY = 'your-secret-key'
LINODE_BUCKET_NAME = 'your-bucket-name'

def create_s3_client():
    """
    Creates an S3 client to interact with Linode's Object Storage.

    Returns:
        boto3.client: A configured S3 client.
    """
    try:
        # Create a session using Linode's Object Storage credentials
        session = boto3.session.Session()
        s3_client = session.client(
            service_name='s3',
            endpoint_url=f'https://{LINODE_OBJECT_STORAGE_REGION}.linodeobjects.com',
            aws_access_key_id=LINODE_ACCESS_KEY,
            aws_secret_access_key=LINODE_SECRET_KEY,
        )
        return s3_client
    except (NoCredentialsError, PartialCredentialsError) as e:
        raise Exception("Invalid AWS credentials provided.") from e

def upload_file(file_name, object_name=None):
    """
    Uploads a file to Linode's Object Storage.

    Args:
        file_name (str): The path to the file to upload.
        object_name (str, optional): The name of the object in the storage. If not specified, file_name is used.

    Raises:
        Exception: If the upload fails.
    """
    s3_client = create_s3_client()
    
    if object_name is None:
        object_name = file_name

    try:
        # Upload the file
        s3_client.upload_file(file_name, LINODE_BUCKET_NAME, object_name)
        print(f"File '{file_name}' uploaded to '{LINODE_BUCKET_NAME}/{object_name}'.")
    except Exception as e:
        raise Exception(f"Failed to upload '{file_name}'.") from e

def list_files():
    """
    Lists all files in the specified Linode Object Storage bucket.

    Raises:
        Exception: If the retrieval of the file list fails.
    """
    s3_client = create_s3_client()
    
    try:
        # Retrieve the list of files in the bucket
        response = s3_client.list_objects_v2(Bucket=LINODE_BUCKET_NAME)
        if 'Contents' in response:
            print("Files in bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print("Bucket is empty.")
    except Exception as e:
        raise Exception("Failed to list files in the bucket.") from e

if __name__ == '__main__':
    # Example usage
    try:
        upload_file('path/to/your/file.txt')
        list_files()
    except Exception as e:
        print(f"Error: {e}")
```
