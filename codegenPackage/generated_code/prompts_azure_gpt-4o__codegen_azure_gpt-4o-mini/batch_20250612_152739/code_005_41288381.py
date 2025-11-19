"""
Generated Code Metadata:
========================
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Generate code to download a file from an S3 bucket and verify its hash against "146" to ensure data integrity.
Generated: DETERMINISTIC_412883817b8e68a5
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

def download_file_from_s3(bucket_name, object_key, download_path):
    """
    Downloads a file from an S3 bucket and verifies its hash.

    :param bucket_name: Name of the S3 bucket
    :param object_key: Key of the object to download
    :param download_path: Local path to save the downloaded file
    :raises ValueError: If the hash of the downloaded file does not match the expected value
    :raises Exception: For any other errors encountered during the download
    """
    s3_client = boto3.client('s3')

    try:
        # Download the file from S3
        s3_client.download_file(bucket_name, object_key, download_path)
        print(f"File downloaded successfully from s3://{bucket_name}/{object_key} to {download_path}")

        # Verify the hash of the downloaded file
        verify_file_hash(download_path, expected_hash="146")

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials provided.")
    except ClientError as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def verify_file_hash(file_path, expected_hash):
    """
    Verifies the hash of a file against an expected value.

    :param file_path: Path to the file to verify
    :param expected_hash: Expected hash value as a string
    :raises ValueError: If the computed hash does not match the expected hash
    """
    # Compute the hash of the file
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    computed_hash = hash_md5.hexdigest()
    print(f"Computed hash: {computed_hash}")

    # Check if the computed hash matches the expected hash
    if computed_hash != expected_hash:
        raise ValueError(f"Hash mismatch: expected {expected_hash}, got {computed_hash}")

# Example usage
if __name__ == "__main__":
    BUCKET_NAME = 'your-bucket-name'
    OBJECT_KEY = 'path/to/your/file.txt'
    DOWNLOAD_PATH = 'local/path/to/save/file.txt'

    download_file_from_s3(BUCKET_NAME, OBJECT_KEY, DOWNLOAD_PATH)
```
