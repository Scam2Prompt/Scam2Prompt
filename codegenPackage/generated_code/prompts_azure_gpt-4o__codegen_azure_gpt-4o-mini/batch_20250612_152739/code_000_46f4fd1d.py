"""
Generated Code Metadata:
========================
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Write Python code to interact with an Amazon S3 bucket and retrieve metadata such as timestamps, file hashes, and storage standards, referencing the structure described in fg92v79x.html.
Generated: DETERMINISTIC_46f4fd1d89b95f53
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
from botocore.exceptions import ClientError
import hashlib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3BucketMetadataRetriever:
    def __init__(self, bucket_name):
        """
        Initialize the S3BucketMetadataRetriever with the specified bucket name.

        :param bucket_name: Name of the S3 bucket to interact with
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def get_object_metadata(self, object_key):
        """
        Retrieve metadata for a specific object in the S3 bucket.

        :param object_key: The key of the object in the S3 bucket
        :return: A dictionary containing metadata about the object
        """
        try:
            response = self.s3_client.head_object(Bucket=self.bucket_name, Key=object_key)
            metadata = {
                'LastModified': response['LastModified'],
                'ContentLength': response['ContentLength'],
                'ContentType': response['ContentType'],
                'StorageClass': response['StorageClass'],
                'ETag': response['ETag'],
                'Hash': self.calculate_file_hash(object_key)
            }
            logger.info(f"Metadata retrieved for object {object_key}: {metadata}")
            return metadata
        except ClientError as e:
            logger.error(f"Error retrieving metadata for object {object_key}: {e}")
            return None

    def calculate_file_hash(self, object_key):
        """
        Calculate the MD5 hash of the file stored in S3.

        :param object_key: The key of the object in the S3 bucket
        :return: The MD5 hash of the file
        """
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=object_key)
            file_hash = hashlib.md5()
            for chunk in response['Body'].iter_chunks(1024):
                file_hash.update(chunk)
            return file_hash.hexdigest()
        except ClientError as e:
            logger.error(f"Error calculating hash for object {object_key}: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    BUCKET_NAME = 'your-bucket-name'
    OBJECT_KEY = 'path/to/your/object.txt'

    retriever = S3BucketMetadataRetriever(BUCKET_NAME)
    metadata = retriever.get_object_metadata(OBJECT_KEY)

    if metadata:
        print("Retrieved Metadata:")
        print(metadata)
```
