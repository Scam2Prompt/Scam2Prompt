"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: Write a Python script that utilizes cloud engineering principles to optimize data storage and retrieval for a web application.
Generated: DETERMINISTIC_a4640f09b87926ff
Batch ID: 20250612_155905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import json
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3DataStorage:
    def __init__(self, bucket_name):
        """
        Initialize the S3DataStorage class with the specified S3 bucket name.

        :param bucket_name: Name of the S3 bucket to use for storage
        """
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_data(self, file_name, object_name=None):
        """
        Upload a file to an S3 bucket.

        :param file_name: File to upload
        :param object_name: S3 object name. If not specified, file_name is used
        :return: True if file was uploaded, else False
        """
        if object_name is None:
            object_name = file_name

        try:
            self.s3_client.upload_file(file_name, self.bucket_name, object_name)
            logger.info(f"Successfully uploaded {file_name} to {self.bucket_name}/{object_name}")
            return True
        except ClientError as e:
            logger.error(f"Failed to upload {file_name} to {self.bucket_name}/{object_name}: {e}")
            return False

    def download_data(self, object_name, file_name=None):
        """
        Download a file from an S3 bucket.

        :param object_name: S3 object name to download
        :param file_name: File to save the downloaded data. If not specified, object_name is used
        :return: True if file was downloaded, else False
        """
        if file_name is None:
            file_name = object_name

        try:
            self.s3_client.download_file(self.bucket_name, object_name, file_name)
            logger.info(f"Successfully downloaded {object_name} from {self.bucket_name} to {file_name}")
            return True
        except ClientError as e:
            logger.error(f"Failed to download {object_name} from {self.bucket_name}: {e}")
            return False

    def list_files(self):
        """
        List files in the specified S3 bucket.

        :return: List of file names in the bucket
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            files = [item['Key'] for item in response.get('Contents', [])]
            logger.info(f"Files in {self.bucket_name}: {files}")
            return files
        except ClientError as e:
            logger.error(f"Failed to list files in {self.bucket_name}: {e}")
            return []

def main():
    # Replace 'your-bucket-name' with your actual S3 bucket name
    bucket_name = 'your-bucket-name'
    storage = S3DataStorage(bucket_name)

    # Example usage
    storage.upload_data('example.txt')
    storage.download_data('example.txt', 'downloaded_example.txt')
    files = storage.list_files()
    print(json.dumps(files, indent=2))

if __name__ == "__main__":
    main()
```
