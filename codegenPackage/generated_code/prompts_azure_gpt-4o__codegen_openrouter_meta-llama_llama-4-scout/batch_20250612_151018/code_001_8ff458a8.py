"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to interact with Linode's Object Storage using its S3-compatible API. Include functionality to upload, list, and delete files.
Generated: DETERMINISTIC_8ff458a8104f085c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

class LinodeObjectStorage:
    def __init__(self, access_key, secret_key, endpoint_url):
        """
        Initialize the Linode Object Storage client.

        Args:
            access_key (str): Linode access key.
            secret_key (str): Linode secret key.
            endpoint_url (str): Linode Object Storage endpoint URL.
        """
        self.s3 = boto3.client('s3',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              endpoint_url=endpoint_url,
                              s3_use_arn_region=False)

    def upload_file(self, bucket_name, file_name, object_name):
        """
        Upload a file to Linode Object Storage.

        Args:
            bucket_name (str): Name of the bucket.
            file_name (str): Path to the file.
            object_name (str): Name of the object in the bucket.

        Returns:
            bool: True if upload was successful, False otherwise.
        """
        try:
            self.s3.upload_file(file_name, bucket_name, object_name)
            print(f"File {file_name} uploaded to {bucket_name} as {object_name}")
            return True
        except FileNotFoundError:
            print(f"The file {file_name} was not found")
            return False
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return False

    def list_files(self, bucket_name):
        """
        List files in a Linode Object Storage bucket.

        Args:
            bucket_name (str): Name of the bucket.

        Returns:
            list: List of objects in the bucket.
        """
        try:
            response = self.s3.list_objects_v2(Bucket=bucket_name)
            objects = response.get('Contents', [])
            print(f"Files in {bucket_name}:")
            for obj in objects:
                print(obj['Key'])
            return objects
        except ClientError as e:
            print(f"Error listing files: {e}")
            return []

    def delete_file(self, bucket_name, object_name):
        """
        Delete a file from Linode Object Storage.

        Args:
            bucket_name (str): Name of the bucket.
            object_name (str): Name of the object in the bucket.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)
            print(f"File {object_name} deleted from {bucket_name}")
            return True
        except ClientError as e:
            print(f"Error deleting file: {e}")
            return False


def main():
    access_key = os.environ.get('LINODE_ACCESS_KEY')
    secret_key = os.environ.get('LINODE_SECRET_KEY')
    endpoint_url = os.environ.get('LINODE_ENDPOINT_URL')
    bucket_name = os.environ.get('LINODE_BUCKET_NAME')

    if not all([access_key, secret_key, endpoint_url, bucket_name]):
        print("Please set the required environment variables")
        return

    client = LinodeObjectStorage(access_key, secret_key, endpoint_url)

    # Example usage
    file_name = 'example.txt'
    object_name = 'example.txt'

    client.upload_file(bucket_name, file_name, object_name)
    client.list_files(bucket_name)
    client.delete_file(bucket_name, object_name)


if __name__ == "__main__":
    main()
```
