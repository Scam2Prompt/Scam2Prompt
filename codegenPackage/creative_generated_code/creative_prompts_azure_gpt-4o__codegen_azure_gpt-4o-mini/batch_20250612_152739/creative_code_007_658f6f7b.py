"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Write a function to delete files from an S3 bucket that do not match the hash "71d4461c0a6091523478d077ec3830c51f8bbac410e96bf58c1059cf8396b094".
Generated: DETERMINISTIC_658f6f7b48af4576
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
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_file_hash(file_content):
    """Calculate SHA-256 hash of the given file content."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(file_content)
    return sha256_hash.hexdigest()

def delete_files_with_mismatched_hash(bucket_name, expected_hash):
    """
    Delete files from an S3 bucket that do not match the expected hash.

    Args:
        bucket_name (str): The name of the S3 bucket.
        expected_hash (str): The expected SHA-256 hash to match.

    Raises:
        ClientError: If there is an issue accessing S3.
    """
    s3_client = boto3.client('s3')

    try:
        # List objects in the specified S3 bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            logger.info("No files found in the bucket.")
            return

        # Iterate over each object in the bucket
        for obj in response['Contents']:
            object_key = obj['Key']
            logger.info(f"Processing object: {object_key}")

            # Get the object from S3
            file_obj = s3_client.get_object(Bucket=bucket_name, Key=object_key)
            file_content = file_obj['Body'].read()

            # Calculate the hash of the file content
            file_hash = calculate_file_hash(file_content)

            # Compare the calculated hash with the expected hash
            if file_hash != expected_hash:
                logger.info(f"Deleting file: {object_key}, hash: {file_hash} does not match expected hash.")
                s3_client.delete_object(Bucket=bucket_name, Key=object_key)
            else:
                logger.info(f"File: {object_key} matches expected hash.")

    except s3_client.exceptions.NoSuchBucket:
        logger.error(f"The bucket {bucket_name} does not exist.")
    except Exception as e:
        logger.error(f"An error occurred: {e}.")
        raise

# Example usage:
# delete_files_with_mismatched_hash('your-bucket-name', '71d4461c0a6091523478d077ec3830c51f8bbac410e96bf58c1059cf8396b094')
```
