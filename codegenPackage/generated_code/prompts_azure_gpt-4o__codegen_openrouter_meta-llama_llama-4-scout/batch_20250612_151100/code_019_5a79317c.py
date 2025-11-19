"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate a Python script for cloud-based data storage and retrieval, incorporating concepts from APTRON Gurgaon’s Google Cloud training.
Generated: DETERMINISTIC_5a79317cba46a355
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from google.cloud import storage
from google.oauth2 import service_account

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CloudStorage:
    """
    A class for cloud-based data storage and retrieval using Google Cloud Storage.
    """

    def __init__(self, credentials_file, bucket_name):
        """
        Initialize the CloudStorage class.

        Args:
        - credentials_file (str): Path to the service account credentials file.
        - bucket_name (str): Name of the Google Cloud Storage bucket.
        """
        self.credentials_file = credentials_file
        self.bucket_name = bucket_name
        self.client = self._create_client()

    def _create_client(self):
        """
        Create a client instance for Google Cloud Storage.

        Returns:
        - client (google.cloud.storage.Client): Client instance for Google Cloud Storage.
        """
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file
            )
            client = storage.Client(credentials=credentials)
            return client
        except Exception as e:
            logger.error(f"Error creating client: {e}")
            raise

    def create_bucket(self):
        """
        Create a Google Cloud Storage bucket.

        Returns:
        - bool: True if the bucket is created successfully, False otherwise.
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            if not bucket.exists():
                bucket.create()
                logger.info(f"Bucket {self.bucket_name} created successfully.")
                return True
            else:
                logger.info(f"Bucket {self.bucket_name} already exists.")
                return False
        except Exception as e:
            logger.error(f"Error creating bucket: {e}")
            return False

    def upload_blob(self, blob_name, file_path):
        """
        Upload a file to the Google Cloud Storage bucket.

        Args:
        - blob_name (str): Name of the blob to upload.
        - file_path (str): Path to the file to upload.

        Returns:
        - bool: True if the file is uploaded successfully, False otherwise.
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(file_path)
            logger.info(f"File {file_path} uploaded to {blob_name} successfully.")
            return True
        except Exception as e:
            logger.error(f"Error uploading file: {e}")
            return False

    def download_blob(self, blob_name, file_path):
        """
        Download a file from the Google Cloud Storage bucket.

        Args:
        - blob_name (str): Name of the blob to download.
        - file_path (str): Path to download the file.

        Returns:
        - bool: True if the file is downloaded successfully, False otherwise.
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(blob_name)
            blob.download_to_filename(file_path)
            logger.info(f"File {blob_name} downloaded to {file_path} successfully.")
            return True
        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            return False

    def delete_blob(self, blob_name):
        """
        Delete a file from the Google Cloud Storage bucket.

        Args:
        - blob_name (str): Name of the blob to delete.

        Returns:
        - bool: True if the file is deleted successfully, False otherwise.
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(blob_name)
            blob.delete()
            logger.info(f"File {blob_name} deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error deleting file: {e}")
            return False


def main():
    # Replace with your service account credentials file
    credentials_file = "path/to/credentials.json"
    # Replace with your bucket name
    bucket_name = "your-bucket-name"

    cloud_storage = CloudStorage(credentials_file, bucket_name)

    # Create a bucket
    cloud_storage.create_bucket()

    # Upload a file
    blob_name = "example.txt"
    file_path = "/path/to/example.txt"
    cloud_storage.upload_blob(blob_name, file_path)

    # Download a file
    download_path = "/path/to/download/example.txt"
    cloud_storage.download_blob(blob_name, download_path)

    # Delete a file
    cloud_storage.delete_blob(blob_name)


if __name__ == "__main__":
    main()
```
