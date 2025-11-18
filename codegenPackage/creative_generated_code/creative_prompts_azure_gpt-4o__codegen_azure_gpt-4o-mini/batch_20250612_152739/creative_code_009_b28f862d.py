"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a script to compare the metadata of two files in an S3 bucket, focusing on timestamps and hash values, as described in the fg92v79x.html documentation.
Generated: DETERMINISTIC_b28f862dff0503e9
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
import botocore
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_file_metadata(bucket_name, file_key):
    """
    Retrieve the metadata for a given file in an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file in the S3 bucket.

    Returns:
        dict: A dictionary containing the last modified time and ETag (hash value) of the file.
    """
    s3 = boto3.client('s3')
    
    try:
        # Get the object metadata
        response = s3.head_object(Bucket=bucket_name, Key=file_key)
        return {
            'LastModified': response['LastModified'],
            'ETag': response['ETag'].strip('"')  # ETag is returned with quotes
        }
    except botocore.exceptions.ClientError as e:
        logger.error(f"Error retrieving metadata for {file_key} in bucket {bucket_name}: {e}")
        return None

def compare_metadata(bucket_name, file_key_1, file_key_2):
    """
    Compare the metadata of two files in an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key_1 (str): The key of the first file.
        file_key_2 (str): The key of the second file.

    Returns:
        bool: True if the files have the same metadata, False otherwise.
    """
    metadata_1 = get_file_metadata(bucket_name, file_key_1)
    metadata_2 = get_file_metadata(bucket_name, file_key_2)

    # Check if both metadata retrievals were successful
    if metadata_1 is None or metadata_2 is None:
        logger.error("Metadata comparison failed due to previous errors.")
        return False

    # Compare timestamps and hash values (ETags)
    same_last_modified = metadata_1['LastModified'] == metadata_2['LastModified']
    same_etag = metadata_1['ETag'] == metadata_2['ETag']

    if same_last_modified and same_etag:
        logger.info(f"Files '{file_key_1}' and '{file_key_2}' have the same metadata.")
    else:
        logger.info(f"Files '{file_key_1}' and '{file_key_2}' differ in metadata.")

    return same_last_modified and same_etag

if __name__ == "__main__":
    # Example usage
    BUCKET_NAME = 'your-bucket-name'
    FILE_KEY_1 = 'path/to/your/first/file.txt'
    FILE_KEY_2 = 'path/to/your/second/file.txt'

    result = compare_metadata(BUCKET_NAME, FILE_KEY_1, FILE_KEY_2)
    print(f"Metadata comparison result: {result}")
```
