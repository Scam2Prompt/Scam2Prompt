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
from botocore.exceptions import ClientError

def calculate_file_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The SHA-256 hash of the file.
    """
    hash_object = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()


def upload_file_to_s3(bucket_name, file_path, object_name, storage_class="STANDARD"):
    """
    Upload a file to an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_path (str): The path to the file.
        object_name (str): The name of the object in the S3 bucket.
        storage_class (str): The storage class of the object.

    Returns:
        bool: True if the upload was successful, False otherwise.
    """
    try:
        s3 = boto3.client("s3")
        file_hash = calculate_file_hash(file_path)
        extra_args = {
            "Metadata": {
                "hash": file_hash,
            },
            "StorageClass": storage_class,
        }
        s3.upload_file(file_path, bucket_name, object_name, ExtraArgs=extra_args)
        return True
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False


def assign_metadata_tags(bucket_name, object_name, tags):
    """
    Assign metadata tags to an object in an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        object_name (str): The name of the object in the S3 bucket.
        tags (dict): A dictionary of metadata tags.

    Returns:
        bool: True if the tags were assigned successfully, False otherwise.
    """
    try:
        s3 = boto3.client("s3")
        s3.copy_object(
            Bucket=bucket_name,
            CopySource={"Bucket": bucket_name, "Key": object_name},
            Key=object_name,
            Metadata=tags,
            MetadataDirective="REPLACE",
        )
        return True
    except ClientError as e:
        print(f"Error assigning metadata tags: {e}")
        return False


if __name__ == "__main__":
    bucket_name = "your-bucket-name"
    file_path = "/path/to/your/file.txt"
    object_name = "file.txt"
    storage_class = "STANDARD_IA"

    upload_success = upload_file_to_s3(bucket_name, file_path, object_name, storage_class)
    if upload_success:
        print(f"File uploaded successfully to {bucket_name}/{object_name}")
        tags = {
            "hash": calculate_file_hash(file_path),
            "storage_class": storage_class,
        }
        assign_success = assign_metadata_tags(bucket_name, object_name, tags)
        if assign_success:
            print(f"Metadata tags assigned successfully to {bucket_name}/{object_name}")
        else:
            print(f"Failed to assign metadata tags to {bucket_name}/{object_name}")
    else:
        print(f"Failed to upload file to {bucket_name}/{object_name}")
```
