"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Develop a data backup and recovery plan for a small business with 1-10 employees, including recommendations for secure data storage and rapid recovery in case of a cyberattack.
Generated: DETERMINISTIC_24f78f64413a493d
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_backup_recovery.py

import os
import datetime
import shutil
import logging
from pathlib import Path
import boto3
from botocore.exceptions import NoCredentialsError

# Set up logging configuration
logging.basicConfig(filename='data_backup_recovery.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(data_dir, backup_dir):
    """
    Creates a backup of the data directory.

    Args:
        data_dir (str): The path to the data directory.
        backup_dir (str): The path to the backup directory.

    Returns:
        str: The path to the backup file.
    """
    try:
        # Create the backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Generate a timestamp for the backup file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = f"backup_{timestamp}.zip"

        # Create the full path to the backup file
        backup_file_path = os.path.join(backup_dir, backup_file)

        # Use shutil to create a zip archive of the data directory
        shutil.make_archive(backup_file_path.replace('.zip', ''), 'zip', data_dir)

        # Rename the archive to include the .zip extension
        os.rename(f"{backup_file_path.replace('.zip', '')}.zip", backup_file_path)

        logging.info(f"Backup created: {backup_file_path}")
        return backup_file_path

    except Exception as e:
        logging.error(f"Error creating backup: {e}")
        return None

def upload_to_s3(local_file, bucket_name):
    """
    Uploads a file to an S3 bucket.

    Args:
        local_file (str): The path to the local file.
        bucket_name (str): The name of the S3 bucket.

    Returns:
        bool: True if the upload was successful, False otherwise.
    """
    try:
        s3 = boto3.client('s3')
        s3.upload_file(local_file, bucket_name, os.path.basename(local_file))
        logging.info(f"Uploaded {local_file} to {bucket_name}")
        return True

    except FileNotFoundError:
        logging.error(f"The file {local_file} was not found")
        return False
    except NoCredentialsError:
        logging.error("Credentials not available")
        return False
    except Exception as e:
        logging.error(f"Error uploading to S3: {e}")
        return False

def recover_from_backup(backup_file_path, recovery_dir):
    """
    Recovers data from a backup file.

    Args:
        backup_file_path (str): The path to the backup file.
        recovery_dir (str): The path to the recovery directory.

    Returns:
        bool: True if the recovery was successful, False otherwise.
    """
    try:
        # Check if the backup file exists
        if not os.path.exists(backup_file_path):
            logging.error(f"Backup file not found: {backup_file_path}")
            return False

        # Extract the backup file to the recovery directory
        shutil.unpack_archive(backup_file_path, recovery_dir)

        logging.info(f"Recovered data to {recovery_dir}")
        return True

    except Exception as e:
        logging.error(f"Error recovering from backup: {e}")
        return False

if __name__ == "__main__":
    # Define configuration
    data_dir = "/path/to/data"
    backup_dir = "/path/to/backup"
    s3_bucket_name = "your-bucket-name"
    recovery_dir = "/path/to/recovery"

    # Create a backup
    backup_file_path = create_backup(data_dir, backup_dir)

    if backup_file_path:
        # Upload the backup to S3
        upload_to_s3(backup_file_path, s3_bucket_name)

    # Recover from a backup
    recover_from_backup(backup_file_path, recovery_dir)
```
