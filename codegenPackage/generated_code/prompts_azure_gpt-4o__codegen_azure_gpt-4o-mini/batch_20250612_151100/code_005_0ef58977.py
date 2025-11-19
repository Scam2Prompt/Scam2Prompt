"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Develop a cloud computing solution using AWS or Azure, referencing the skills taught in APTRON Gurgaon’s Cloud Computing training.
Generated: DETERMINISTIC_0ef589773bb60d6c
Batch ID: 20250612_151100
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

class S3BucketManager:
    """
    A class to manage S3 buckets in AWS.
    """

    def __init__(self, aws_access_key, aws_secret_key, region_name):
        """
        Initializes the S3BucketManager with AWS credentials and region.

        :param aws_access_key: AWS access key ID
        :param aws_secret_key: AWS secret access key
        :param region_name: AWS region name
        """
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )

    def create_bucket(self, bucket_name):
        """
        Creates an S3 bucket.

        :param bucket_name: Name of the bucket to create
        :raises ClientError: If the bucket creation fails
        """
        try:
            self.s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        except ClientError as e:
            print(f"Error creating bucket: {e}")

    def upload_file(self, file_name, bucket_name, object_name=None):
        """
        Uploads a file to an S3 bucket.

        :param file_name: File to upload
        :param bucket_name: Bucket to upload to
        :param object_name: S3 object name. If not specified, file_name is used
        :raises ClientError: If the file upload fails
        """
        if object_name is None:
            object_name = file_name

        try:
            self.s3_client.upload_file(file_name, bucket_name, object_name)
            print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
        except ClientError as e:
            print(f"Error uploading file: {e}")

    def list_buckets(self):
        """
        Lists all S3 buckets.

        :raises ClientError: If the bucket listing fails
        """
        try:
            response = self.s3_client.list_buckets()
            print("Existing buckets:")
            for bucket in response['Buckets']:
                print(f"  {bucket['Name']}")
        except ClientError as e:
            print(f"Error listing buckets: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your AWS credentials and desired region
    AWS_ACCESS_KEY = 'your_access_key'
    AWS_SECRET_KEY = 'your_secret_key'
    REGION_NAME = 'us-west-2'

    # Initialize the S3 bucket manager
    s3_manager = S3BucketManager(AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME)

    # Create a new bucket
    s3_manager.create_bucket('my-unique-bucket-name-12345')

    # List existing buckets
    s3_manager.list_buckets()

    # Upload a file to the newly created bucket
    s3_manager.upload_file('path/to/your/file.txt', 'my-unique-bucket-name-12345')
```

Make sure to replace `'your_access_key'`, `'your_secret_key'`, and `'my-unique-bucket-name-12345'` with your actual AWS credentials and a unique bucket name.
