"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Suggest libraries for implementing a cloud-based storage system for managing student data and course materials, similar to the "Cloud Computing and Storage Basics" course offered by RSP Bharat.
Generated: DETERMINISTIC_7c611f4cdb6f2ed2
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class CloudStorageManager:
    """
    A class to manage cloud-based storage for student data and course materials.
    This class uses Amazon S3 for storage management.
    """

    def __init__(self, bucket_name):
        """
        Initializes the CloudStorageManager with the specified S3 bucket.

        :param bucket_name: The name of the S3 bucket where data will be stored.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def upload_file(self, file_path, s3_key):
        """
        Uploads a file to the specified S3 bucket.

        :param file_path: The local path to the file to be uploaded.
        :param s3_key: The S3 key (path) where the file will be stored.
        :raises FileNotFoundError: If the specified file does not exist.
        :raises NoCredentialsError: If AWS credentials are not available.
        :raises PartialCredentialsError: If AWS credentials are incomplete.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            print(f"Successfully uploaded {file_path} to {self.bucket_name}/{s3_key}")
        except NoCredentialsError:
            print("Error: AWS credentials not found.")
            raise
        except PartialCredentialsError:
            print("Error: Incomplete AWS credentials.")
            raise
        except Exception as e:
            print(f"Error uploading file: {e}")
            raise

    def download_file(self, s3_key, download_path):
        """
        Downloads a file from the specified S3 bucket.

        :param s3_key: The S3 key (path) of the file to be downloaded.
        :param download_path: The local path where the file will be downloaded.
        :raises NoCredentialsError: If AWS credentials are not available.
        :raises PartialCredentialsError: If AWS credentials are incomplete.
        """
        try:
            self.s3_client.download_file(self.bucket_name, s3_key, download_path)
            print(f"Successfully downloaded {self.bucket_name}/{s3_key} to {download_path}")
        except NoCredentialsError:
            print("Error: AWS credentials not found.")
            raise
        except PartialCredentialsError:
            print("Error: Incomplete AWS credentials.")
            raise
        except Exception as e:
            print(f"Error downloading file: {e}")
            raise

    def list_files(self):
        """
        Lists all files in the specified S3 bucket.

        :return: A list of file names in the S3 bucket.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                return [item['Key'] for item in response['Contents']]
            else:
                print("The bucket is empty.")
                return []
        except Exception as e:
            print(f"Error listing files: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    bucket_name = 'your-s3-bucket-name'
    storage_manager = CloudStorageManager(bucket_name)

    # Upload a file
    try:
        storage_manager.upload_file('path/to/local/file.txt', 'course_materials/file.txt')
    except Exception as e:
        print(f"Upload failed: {e}")

    # Download a file
    try:
        storage_manager.download_file('course_materials/file.txt', 'path/to/download/file.txt')
    except Exception as e:
        print(f"Download failed: {e}")

    # List files in the bucket
    try:
        files = storage_manager.list_files()
        print("Files in bucket:", files)
    except Exception as e:
        print(f"Listing files failed: {e}")
```
