"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogifts.s3.us-east-2.amazonaws.com
Prompt: What are the best practices for addressing S3 buckets to avoid permanent redirect issues, specifically for the cryptogifts bucket?
Generated: DETERMINISTIC_2cb9ad540b4f40fd
Batch ID: 20250612_160703
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

class S3BucketManager:
    def __init__(self, bucket_name):
        """
        Initialize the S3BucketManager with a specific S3 bucket.

        :param bucket_name: Name of the S3 bucket
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def get_bucket_location(self):
        """
        Retrieve the location of the S3 bucket.

        :return: Location of the bucket or None if an error occurred
        """
        try:
            response = self.s3_client.get_bucket_location(Bucket=self.bucket_name)
            return response['LocationConstraint']
        except ClientError as e:
            print(f"Error fetching bucket location: {e}")
            return None

    def generate_presigned_url(self, object_key):
        """
        Generate a presigned URL for accessing an object in the S3 bucket.

        :param object_key: The key of the object in the S3 bucket
        :return: Presigned URL or None if an error occurred
        """
        try:
            response = self.s3_client.generate_presigned_url('get_object',
                Params={'Bucket': self.bucket_name, 'Key': object_key},
                ExpiresIn=3600)  # URL valid for 1 hour
            return response
        except ClientError as e:
            print(f"Error generating presigned URL: {e}")
            return None

    def list_objects(self):
        """
        List all objects in the S3 bucket.

        :return: List of object keys or None if an error occurred
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            else:
                return []
        except ClientError as e:
            print(f"Error listing objects in bucket: {e}")
            return None

def main():
    # Define the S3 bucket name
    bucket_name = 'cryptogifts'
    
    # Initialize the S3 bucket manager
    bucket_manager = S3BucketManager(bucket_name)

    # Fetch and print the bucket location
    location = bucket_manager.get_bucket_location()
    print(f"Bucket Location: {location}")

    # List and print objects in the bucket
    objects = bucket_manager.list_objects()
    if objects is not None:
        print(f"Objects in bucket '{bucket_name}': {objects}")
    
    # Example of generating a presigned URL for an object
    if objects:
        presigned_url = bucket_manager.generate_presigned_url(objects[0])
        print(f"Presigned URL for '{objects[0]}': {presigned_url}")

if __name__ == "__main__":
    main()
```
