"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Design a data backup and recovery system for a small business, using cloud storage and automated backup solutions."
Generated: DETERMINISTIC_adfdf9a15ea2d12d
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import time
import logging
from datetime import datetime
from pathlib import Path
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataBackupSystem:
    def __init__(self, local_directory, cloud_bucket_name, aws_access_key, aws_secret_key):
        """
        Initialize the DataBackupSystem with local directory and cloud storage details.

        :param local_directory: Directory to back up
        :param cloud_bucket_name: Name of the S3 bucket for cloud storage
        :param aws_access_key: AWS access key for authentication
        :param aws_secret_key: AWS secret key for authentication
        """
        self.local_directory = Path(local_directory)
        self.cloud_bucket_name = cloud_bucket_name
        self.s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    def backup_to_local(self):
        """
        Create a timestamped backup of the local directory.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_directory = self.local_directory.parent / f"{self.local_directory.name}_backup_{timestamp}"
        
        try:
            shutil.copytree(self.local_directory, backup_directory)
            logging.info(f"Local backup created at: {backup_directory}")
        except Exception as e:
            logging.error(f"Error creating local backup: {e}")

    def backup_to_cloud(self):
        """
        Upload the local backup to the specified S3 bucket.
        """
        try:
            for file in self.local_directory.rglob('*'):
                if file.is_file():
                    s3_file_path = str(file.relative_to(self.local_directory))
                    self.s3_client.upload_file(str(file), self.cloud_bucket_name, s3_file_path)
                    logging.info(f"Uploaded {file} to {self.cloud_bucket_name}/{s3_file_path}")
        except (NoCredentialsError, PartialCredentialsError) as e:
            logging.error("AWS credentials are not valid. Please check your configuration.")
        except Exception as e:
            logging.error(f"Error uploading to cloud: {e}")

    def automated_backup(self, interval_minutes):
        """
        Run automated backups at specified intervals.

        :param interval_minutes: Time interval in minutes for automated backups
        """
        while True:
            self.backup_to_local()
            self.backup_to_cloud()
            logging.info(f"Next backup scheduled in {interval_minutes} minutes.")
            time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    # Configuration for the backup system
    LOCAL_DIRECTORY = '/path/to/your/data'  # Change to your local directory
    CLOUD_BUCKET_NAME = 'your-s3-bucket-name'  # Change to your S3 bucket name
    AWS_ACCESS_KEY = 'your-access-key'  # Change to your AWS access key
    AWS_SECRET_KEY = 'your-secret-key'  # Change to your AWS secret key
    BACKUP_INTERVAL_MINUTES = 60  # Set the backup interval in minutes

    # Create an instance of the DataBackupSystem
    backup_system = DataBackupSystem(LOCAL_DIRECTORY, CLOUD_BUCKET_NAME, AWS_ACCESS_KEY, AWS_SECRET_KEY)

    # Start automated backup process
    try:
        backup_system.automated_backup(BACKUP_INTERVAL_MINUTES)
    except KeyboardInterrupt:
        logging.info("Backup process interrupted by user.")
```
