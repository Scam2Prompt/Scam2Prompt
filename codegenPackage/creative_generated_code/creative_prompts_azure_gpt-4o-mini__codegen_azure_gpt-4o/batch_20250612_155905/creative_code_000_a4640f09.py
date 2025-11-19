"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitaldhara.com
Prompt: Write a Python script that utilizes cloud engineering principles to optimize data storage and retrieval for a web application.
Generated: DETERMINISTIC_a4640f09b87926ff
Batch ID: 20250612_155905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import json
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CloudStorageManager:
    """
    A class to manage optimized data storage and retrieval using AWS S3.
    Implements cloud engineering principles to ensure scalability and efficiency.
    """

    def __init__(self, bucket_name, region_name='us-east-1'):
        """
        Initialize the CloudStorageManager with the S3 bucket name and region.

        :param bucket_name: Name of the S3 bucket to connect to.
        :param region_name: AWS region where the bucket is located (default: 'us-east-1').
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3', region_name=region_name)

    def upload_file(self, file_path, object_key):
        """
        Upload a file to the S3 bucket.

        :param file_path: Local path to the file being uploaded.
        :param object_key: Desired key (name) for the object in the S3 bucket.
        :return: True if successful, False otherwise.
        """
        try:
            logging.info(f"Uploading file '{file_path}' to bucket '{self.bucket_name}' with key '{object_key}'...")
            self.s3_client.upload_file(file_path, self.bucket_name, object_key)
            logging.info("Upload completed successfully.")
            return True
        except FileNotFoundError:
            logging.error(f"File '{file_path}' not found.")
        except NoCredentialsError:
            logging.error("AWS credentials not found.")
        except PartialCredentialsError:
            logging.error("Incomplete AWS credentials provided.")
        except Exception as e:
            logging.error(f"An error occurred during file upload: {e}")
        return False

    def download_file(self, object_key, download_path):
        """
        Download a file from the S3 bucket.

        :param object_key: Key (name) of the object in the S3 bucket.
        :param download_path: Local path to save the downloaded file.
        :return: True if successful, False otherwise.
        """
        try:
            logging.info(f"Downloading file with key '{object_key}' from bucket '{self.bucket_name}'...")
            self.s3_client.download_file(self.bucket_name, object_key, download_path)
            logging.info(f"File downloaded successfully to '{download_path}'.")
            return True
        except FileNotFoundError:
            logging.error(f"Download path '{download_path}' not found.")
        except NoCredentialsError:
            logging.error("AWS credentials not found.")
        except PartialCredentialsError:
            logging.error("Incomplete AWS credentials provided.")
        except Exception as e:
            logging.error(f"An error occurred during file download: {e}")
        return False

    def list_objects(self):
        """
        List all objects in the S3 bucket.

        :return: List of object keys if successful, None otherwise.
        """
        try:
            logging.info(f"Listing all objects in bucket '{self.bucket_name}'...")
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                object_keys = [obj['Key'] for obj in response['Contents']]
                logging.info(f"Found {len(object_keys)} object(s) in the bucket.")
                return object_keys
            logging.info("Bucket is empty.")
            return []
        except NoCredentialsError:
            logging.error("AWS credentials not found.")
        except PartialCredentialsError:
            logging.error("Incomplete AWS credentials provided.")
        except Exception as e:
            logging.error(f"An error occurred while listing objects: {e}")
        return None

    def delete_file(self, object_key):
        """
        Delete a file from the S3 bucket.

        :param object_key: Key (name) of the object to delete.
        :return: True if successful, False otherwise.
        """
        try:
            logging.info(f"Deleting file with key '{object_key}' from bucket '{self.bucket_name}'...")
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_key)
            logging.info("File deleted successfully.")
            return True
        except NoCredentialsError:
            logging.error("AWS credentials not found.")
        except PartialCredentialsError:
            logging.error("Incomplete AWS credentials provided.")
        except Exception as e:
            logging.error(f"An error occurred during file deletion: {e}")
        return False


def main():
    """
    Main function to test the CloudStorageManager class functionality.
    """
    # Specify the S3 bucket name
    bucket_name = 'your-bucket-name'

    # Initialize the CloudStorageManager
    storage_manager = CloudStorageManager(bucket_name)

    # Example file paths and object keys
    local_file_path = 'example.txt'  # File to upload
    object_key = 'example.txt'      # Key in the S3 bucket
    download_path = 'downloaded_example.txt'

    # Upload a file
    storage_manager.upload_file(local_file_path, object_key)

    # List objects in the bucket
    objects = storage_manager.list_objects()
    if objects:
        logging.info(f"Objects in bucket: {objects}")

    # Download a file
    storage_manager.download_file(object_key, download_path)

    # Delete a file
    storage_manager.delete_file(object_key)


if __name__ == "__main__":
    main()
```
