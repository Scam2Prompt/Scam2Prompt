"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Generate Python code to upload files to an S3 bucket and assign metadata tags, including hash values and storage class, as described in the webpage content.
Generated: DETERMINISTIC_329405f32747ecdc
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
import os
from botocore.exceptions import BotoCoreError, ClientError

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
    except Exception as e:
        raise Exception(f"Error calculating hash for {file_path}: {str(e)}")
    return hash_sha256.hexdigest()

def upload_file_to_s3(file_path, bucket_name, object_name=None, storage_class="STANDARD"):
    """Upload a file to an S3 bucket with metadata.

    Args:
        file_path (str): The path to the file to upload.
        bucket_name (str): The name of the S3 bucket.
        object_name (str, optional): The name of the object in S3. Defaults to None.
        storage_class (str, optional): The storage class to use. Defaults to "STANDARD".

    Raises:
        Exception: Raises an exception if the upload fails.
    """
    # If no object name is specified, use the file name
    if object_name is None:
        object_name = os.path.basename(file_path)

    # Calculate file hash
    file_hash = calculate_file_hash(file_path)

    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Prepare metadata
    metadata = {
        'Hash': file_hash,
        'StorageClass': storage_class
    }

    try:
        # Upload the file
        s3_client.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=object_name,
            ExtraArgs={
                'Metadata': metadata,
                'StorageClass': storage_class
            }
        )
        print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}' with metadata: {metadata}")
    except (BotoCoreError, ClientError) as e:
        raise Exception(f"Failed to upload file to S3: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        upload_file_to_s3(
            file_path='path/to/your/file.txt',
            bucket_name='your-bucket-name',
            storage_class='STANDARD_IA'
        )
    except Exception as e:
        print(f"Error: {e}")
```
