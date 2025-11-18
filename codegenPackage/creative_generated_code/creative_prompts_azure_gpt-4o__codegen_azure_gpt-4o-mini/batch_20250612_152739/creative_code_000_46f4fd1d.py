"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Write Python code to interact with an Amazon S3 bucket and retrieve metadata such as timestamps, file hashes, and storage standards, referencing the structure described in fg92v79x.html.
Generated: DETERMINISTIC_46f4fd1d89b95f53
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
from botocore.exceptions import ClientError
import hashlib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class S3MetadataRetriever:
    """
    A class to interact with an Amazon S3 bucket and retrieve metadata about the objects.
    """

    def __init__(self, bucket_name):
        """
        Initialize the S3 client and set the bucket name.

        :param bucket_name: The name of the S3 bucket to interact with.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def get_object_metadata(self, object_key):
        """
        Retrieve metadata for a specified object in the S3 bucket.

        :param object_key: The key of the object whose metadata is to be retrieved.
        :return: A dictionary containing metadata or None if an error occurred.
        """
        try:
            # Fetch the object metadata
            response = self.s3_client.head_object(Bucket=self.bucket_name, Key=object_key)
            metadata = {
                'LastModified': response['LastModified'],
                'ContentLength': response['ContentLength'],
                'ContentType': response['ContentType'],
                'StorageClass': response['StorageClass'],
                'ETag': response['ETag'],  # This is the file hash (MD5)
            }
            return metadata
        except ClientError as e:
            logging.error(f"Failed to retrieve metadata for {object_key}: {e}")
            return None

    def get_file_hash(self, object_key):
        """
        Calculate the MD5 hash of the file stored in S3.

        :param object_key: The key of the object whose hash is to be calculated.
        :return: The MD5 hash of the object or None if an error occurred.
        """
        try:
            # Get the object
            obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=object_key)
            # Read and calculate the MD5 hash
            hash_md5 = hashlib.md5()
            for chunk in iter(lambda: obj['Body'].read(4096), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except ClientError as e:
            logging.error(f"Failed to retrieve object {object_key} for hash calculation: {e}")
            return None

    def list_objects(self):
        """
        List all objects in the specified S3 bucket.

        :return: A list of object keys in the bucket.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            else:
                logging.info("No objects found in the bucket.")
                return []
        except ClientError as e:
            logging.error(f"Failed to list objects in bucket {self.bucket_name}: {e}")
            return []

# Example usage
if __name__ == '__main__':
    bucket_name = 'your-bucket-name'  # Replace with your bucket name
    retriever = S3MetadataRetriever(bucket_name)

    # List all objects in the bucket
    objects = retriever.list_objects()
    for obj_key in objects:
        metadata = retriever.get_object_metadata(obj_key)
        if metadata:
            logging.info(f"Metadata for {obj_key}: {metadata}")
            file_hash = retriever.get_file_hash(obj_key)
            if file_hash:
                logging.info(f"MD5 Hash for {obj_key}: {file_hash}")
```

Make sure to replace `'your-bucket-name'` with the actual name of your S3 bucket before running the code. Ensure that you have the necessary permissions and configurations set up for AWS SDK (boto3) to interact with S3.
