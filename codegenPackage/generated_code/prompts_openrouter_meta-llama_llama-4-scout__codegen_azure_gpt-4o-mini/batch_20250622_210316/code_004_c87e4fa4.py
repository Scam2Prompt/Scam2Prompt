"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: "Recommend APIs or libraries for managing files on Amazon S3, considering the file types and metadata provided in the given S3 bucket content."
Generated: DETERMINISTIC_c87e4fa4bf11d1cf
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

class S3FileManager:
    """
    A class to manage files in an Amazon S3 bucket.
    """

    def __init__(self, bucket_name):
        """
        Initializes the S3FileManager with the specified S3 bucket name.

        :param bucket_name: Name of the S3 bucket to manage.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def list_files(self):
        """
        Lists all files in the specified S3 bucket.

        :return: A list of file names in the bucket.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                return [item['Key'] for item in response['Contents']]
            else:
                return []
        except ClientError as e:
            print(f"Error listing files: {e}")
            return []

    def upload_file(self, file_path, s3_key):
        """
        Uploads a file to the specified S3 bucket.

        :param file_path: Local path to the file to upload.
        :param s3_key: S3 key (path) where the file will be stored.
        """
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            print(f"File {file_path} uploaded to {s3_key}.")
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Credentials error: {e}")
        except ClientError as e:
            print(f"Error uploading file: {e}")

    def download_file(self, s3_key, download_path):
        """
        Downloads a file from the specified S3 bucket.

        :param s3_key: S3 key (path) of the file to download.
        :param download_path: Local path where the file will be saved.
        """
        try:
            self.s3_client.download_file(self.bucket_name, s3_key, download_path)
            print(f"File {s3_key} downloaded to {download_path}.")
        except ClientError as e:
            print(f"Error downloading file: {e}")

    def delete_file(self, s3_key):
        """
        Deletes a file from the specified S3 bucket.

        :param s3_key: S3 key (path) of the file to delete.
        """
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=s3_key)
            print(f"File {s3_key} deleted from bucket {self.bucket_name}.")
        except ClientError as e:
            print(f"Error deleting file: {e}")

# Example usage:
if __name__ == "__main__":
    bucket_name = 'your-bucket-name'
    s3_manager = S3FileManager(bucket_name)

    # List files in the bucket
    files = s3_manager.list_files()
    print("Files in bucket:", files)

    # Upload a file
    s3_manager.upload_file('local_file.txt', 'uploaded_file.txt')

    # Download a file
    s3_manager.download_file('uploaded_file.txt', 'downloaded_file.txt')

    # Delete a file
    s3_manager.delete_file('uploaded_file.txt')
```
