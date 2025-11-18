"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to interact with Linode's Object Storage using its S3-compatible API. Include functionality to upload, list, and delete files.
Generated: DETERMINISTIC_8ff458a8104f085c
Batch ID: 20250612_151018
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

class LinodeObjectStorage:
    """
    A class to interact with Linode's Object Storage using its S3-compatible API.
    """

    def __init__(self, access_key: str, secret_key: str, region: str, bucket_name: str):
        """
        Initializes the LinodeObjectStorage instance.

        :param access_key: The access key for Linode's Object Storage.
        :param secret_key: The secret key for Linode's Object Storage.
        :param region: The region where the bucket is located.
        :param bucket_name: The name of the bucket to interact with.
        """
        self.s3_client = boto3.client(
            's3',
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        self.bucket_name = bucket_name

    def upload_file(self, file_path: str, object_name: str) -> None:
        """
        Uploads a file to the specified bucket.

        :param file_path: The local path to the file to upload.
        :param object_name: The name of the object in the bucket.
        """
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, object_name)
            print(f"File {file_path} uploaded to {self.bucket_name}/{object_name}.")
        except ClientError as e:
            print(f"Error uploading file: {e}")

    def list_files(self) -> None:
        """
        Lists all files in the specified bucket.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                print("Files in bucket:")
                for obj in response['Contents']:
                    print(f"- {obj['Key']}")
            else:
                print("Bucket is empty.")
        except ClientError as e:
            print(f"Error listing files: {e}")

    def delete_file(self, object_name: str) -> None:
        """
        Deletes a file from the specified bucket.

        :param object_name: The name of the object to delete.
        """
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_name)
            print(f"File {object_name} deleted from {self.bucket_name}.")
        except ClientError as e:
            print(f"Error deleting file: {e}")

# Example usage (uncomment and set your credentials to use)
# if __name__ == "__main__":
#     linode_storage = LinodeObjectStorage(
#         access_key='your_access_key',
#         secret_key='your_secret_key',
#         region='us-east-1',  # replace with your region
#         bucket_name='your_bucket_name'
#     )
#     linode_storage.upload_file('path/to/local/file.txt', 'uploaded_file.txt')
#     linode_storage.list_files()
#     linode_storage.delete_file('uploaded_file.txt')
```

Make sure to replace the placeholder comments with your actual Linode Object Storage credentials and details when running the code.
