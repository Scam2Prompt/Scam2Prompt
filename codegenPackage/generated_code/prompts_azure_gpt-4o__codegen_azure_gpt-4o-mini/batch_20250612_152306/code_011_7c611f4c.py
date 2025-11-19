"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Suggest libraries for implementing a cloud-based storage system for managing student data and course materials, similar to the "Cloud Computing and Storage Basics" course offered by RSP Bharat.
Generated: DETERMINISTIC_7c611f4cdb6f2ed2
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for cloud storage and data management
import boto3  # AWS SDK for Python
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class CloudStorageManager:
    """
    A class to manage cloud-based storage for student data and course materials.
    This implementation uses AWS S3 for storage.
    """

    def __init__(self, aws_access_key, aws_secret_key, bucket_name):
        """
        Initializes the CloudStorageManager with AWS credentials and bucket name.

        :param aws_access_key: AWS access key ID
        :param aws_secret_key: AWS secret access key
        :param bucket_name: Name of the S3 bucket to use for storage
        """
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.bucket_name = bucket_name
        self.s3_client = self.create_s3_client()

    def create_s3_client(self):
        """
        Creates an S3 client using the provided AWS credentials.

        :return: S3 client
        """
        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key
            )
            return s3_client
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError("Invalid AWS credentials provided.") from e

    def upload_file(self, file_path, object_name):
        """
        Uploads a file to the specified S3 bucket.

        :param file_path: Path to the file to upload
        :param object_name: S3 object name (key) for the uploaded file
        :raises FileNotFoundError: If the file does not exist
        :raises Exception: For any other errors during upload
        """
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, object_name)
            print(f"File {file_path} uploaded to {self.bucket_name}/{object_name}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while uploading the file: {e}")

    def download_file(self, object_name, file_path):
        """
        Downloads a file from the specified S3 bucket.

        :param object_name: S3 object name (key) for the file to download
        :param file_path: Path where the file will be saved
        :raises Exception: For any errors during download
        """
        try:
            self.s3_client.download_file(self.bucket_name, object_name, file_path)
            print(f"File {object_name} downloaded from {self.bucket_name} to {file_path}.")
        except Exception as e:
            raise Exception(f"An error occurred while downloading the file: {e}")

    def list_files(self):
        """
        Lists all files in the specified S3 bucket.

        :return: List of file names in the bucket
        :raises Exception: For any errors during listing
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                return [item['Key'] for item in response['Contents']]
            else:
                return []
        except Exception as e:
            raise Exception(f"An error occurred while listing files: {e}")

# Example usage (uncomment to use):
# if __name__ == "__main__":
#     storage_manager = CloudStorageManager('your_access_key', 'your_secret_key', 'your_bucket_name')
#     storage_manager.upload_file('path/to/local/file.txt', 'file.txt')
#     storage_manager.download_file('file.txt', 'path/to/save/file.txt')
#     files = storage_manager.list_files()
#     print("Files in bucket:", files)
```
