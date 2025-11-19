"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Generate Python code to upload files to an S3 bucket and assign metadata tags, including hash values and storage class, as described in the webpage content.
Generated: DETERMINISTIC_329405f32747ecdc
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import hashlib
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of the file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def upload_file_to_s3(file_path, bucket_name, object_name=None, storage_class='STANDARD'):
    """
    Upload a file to an S3 bucket and assign metadata tags.

    :param file_path: Path to the file to upload
    :param bucket_name: Name of the S3 bucket
    :param object_name: S3 object name. If not specified, file_name is used
    :param storage_class: Storage class for the uploaded file
    :raises ValueError: If the file does not exist
    :raises Exception: For other errors during upload
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise ValueError(f"The file {file_path} does not exist.")

    # Use the file name as the object name if not provided
    if object_name is None:
        object_name = os.path.basename(file_path)

    # Calculate the file hash
    file_hash = calculate_file_hash(file_path)

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file with metadata
        s3_client.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=object_name,
            ExtraArgs={
                'StorageClass': storage_class,
                'Metadata': {
                    'FileHash': file_hash
                }
            }
        )
        print(f"File {file_path} uploaded to {bucket_name}/{object_name} with hash {file_hash}.")

    except (NoCredentialsError, PartialCredentialsError) as e:
        print("Credentials not available. Please configure your AWS credentials.")
        raise e
    except ClientError as e:
        print(f"Failed to upload {file_path} to {bucket_name}/{object_name}. Error: {e}")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e

# Example usage
if __name__ == "__main__":
    try:
        upload_file_to_s3('path/to/your/file.txt', 'your-s3-bucket-name', storage_class='STANDARD_IA')
    except Exception as e:
        print(f"Error: {e}")
```
