"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a guide for integrating Linode Object Storage with an S3-compatible application, including configuration steps and API examples.
Generated: DETERMINISTIC_616694f87305287f
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-endpoint-url": {
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Configuration for Linode Object Storage
# Replace 'your-access-key', 'your-secret-key', and 'your-endpoint-url' with your actual Linode Object Storage credentials.
ACCESS_KEY = 'your-access-key'
SECRET_KEY = 'your-secret-key'
ENDPOINT_URL = 'https://your-endpoint-url'

# Bucket name - replace with your desired bucket name
BUCKET_NAME = 'your-bucket-name'

# Object key - the name under which the object will be stored in the bucket
OBJECT_KEY = 'example-object.txt'

# Local file path to upload
LOCAL_FILE_PATH = 'path/to/your/local/file.txt'


def create_s3_client():
    """
    Create and return an S3 client using Linode Object Storage credentials.
    """
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            endpoint_url=ENDPOINT_URL
        )
        return s3_client
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: Invalid credentials - {e}")
        raise
    except Exception as e:
        print(f"Error: Unable to create S3 client - {e}")
        raise


def create_bucket(s3_client, bucket_name):
    """
    Create a new bucket in Linode Object Storage.
    """
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error: Unable to create bucket '{bucket_name}' - {e}")
        raise


def upload_file(s3_client, bucket_name, object_key, file_path):
    """
    Upload a file to the specified bucket using Linode Object Storage.
    """
    try:
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"File '{file_path}' uploaded successfully as '{object_key}' in bucket '{bucket_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    except ClientError as e:
        print(f"Error: Unable to upload file to bucket - {e}")
        raise
    except Exception as e:
        print(f"Error: An unexpected error occurred during file upload - {e}")
        raise


def list_objects(s3_client, bucket_name):
    """
    List all objects in the specified bucket.
    """
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Objects in bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Error: Unable to list objects in bucket - {e}")
        raise


def delete_bucket(s3_client, bucket_name):
    """
    Delete the specified bucket and all its contents.
    """
    try:
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted object '{obj['Key']}' from bucket '{bucket_name}'.")

        # Delete the bucket itself
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except ClientError as e:
        print(f"Error: Unable to delete bucket '{bucket_name}' - {e}")
        raise


if __name__ == "__main__":
    try:
        # Initialize S3 client
        s3_client = create_s3_client()

        # Step 1: Create a bucket
        create_bucket(s3_client, BUCKET_NAME)

        # Step 2: Upload a file
        upload_file(s3_client, BUCKET_NAME, OBJECT_KEY, LOCAL_FILE_PATH)

        # Step 3: List objects in the bucket
        list_objects(s3_client, BUCKET_NAME)

        # Step 4: Delete the bucket (optional cleanup)
        # Uncomment the line below if you want to delete the bucket and its contents
        # delete_bucket(s3_client, BUCKET_NAME)

    except Exception as e:
        print(f"Fatal error: {e}")
```

This code is designed to be production-ready, well-documented within the code comments, and includes proper error handling. Ensure you replace the placeholder values (`your-access-key`, `your-secret-key`, `your-endpoint-url`, `your-bucket-name`, etc.) with actual credentials and values for Linode Object Storage.
