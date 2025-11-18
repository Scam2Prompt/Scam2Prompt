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
  "https://us-east-1.linodeobjects.com": {
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

# Configuration for Linode Object Storage
LINODE_ENDPOINT_URL = "https://us-east-1.linodeobjects.com"  # Replace with your Linode region
LINODE_ACCESS_KEY = "your_access_key"  # Replace with your Linode access key
LINODE_SECRET_KEY = "your_secret_key"  # Replace with your Linode secret key
BUCKET_NAME = "your_bucket_name"  # Replace with your bucket name

def create_bucket(bucket_name):
    """Create a new bucket in Linode Object Storage.

    Args:
        bucket_name (str): The name of the bucket to create.
    
    Returns:
        str: Confirmation message if bucket created successfully.
    """
    try:
        s3_client = boto3.client(
            's3',
            endpoint_url=LINODE_ENDPOINT_URL,
            aws_access_key_id=LINODE_ACCESS_KEY,
            aws_secret_access_key=LINODE_SECRET_KEY
        )

        # Create the bucket
        s3_client.create_bucket(Bucket=bucket_name)
        return f"Bucket '{bucket_name}' created successfully."
    except s3_client.exceptions.BucketAlreadyExists as e:
        return f"Bucket already exists: {str(e)}"
    except (NoCredentialsError, PartialCredentialsError) as e:
        return f"Credentials error: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def upload_file(file_name, bucket_name, object_name=None):
    """Upload a file to the specified bucket in Linode Object Storage.

    Args:
        file_name (str): Name of the file to upload.
        bucket_name (str): The name of the bucket to upload to.
        object_name (str, optional): S3 object name. If not specified, file_name is used.
    
    Returns:
        str: Confirmation message if file uploaded successfully.
    """
    if object_name is None:
        object_name = file_name

    try:
        s3_client = boto3.client(
            's3',
            endpoint_url=LINODE_ENDPOINT_URL,
            aws_access_key_id=LINODE_ACCESS_KEY,
            aws_secret_access_key=LINODE_SECRET_KEY
        )

        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name)
        return f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'."
    except FileNotFoundError:
        return f"The file '{file_name}' was not found."
    except NoCredentialsError:
        return "Credentials not available."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def list_buckets():
    """List all buckets in Linode Object Storage.

    Returns:
        list: List of bucket names.
    """
    try:
        s3_client = boto3.client(
            's3',
            endpoint_url=LINODE_ENDPOINT_URL,
            aws_access_key_id=LINODE_ACCESS_KEY,
            aws_secret_access_key=LINODE_SECRET_KEY
        )

        # List the buckets
        response = s3_client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]
    except NoCredentialsError:
        return "Credentials not available."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage:
    print(create_bucket(BUCKET_NAME))
    print(upload_file("path/to/your/file.txt", BUCKET_NAME))  # Replace with your file path
    print("Buckets:", list_buckets())
```
