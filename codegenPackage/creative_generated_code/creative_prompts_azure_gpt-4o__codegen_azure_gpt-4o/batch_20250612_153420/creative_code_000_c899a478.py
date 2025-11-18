"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.net
Prompt: Write Python code to automate the backup and staging process for a website hosted on Sakura's rental server, using the features described on their platform.
Generated: DETERMINISTIC_c899a478997c7386
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import datetime
import logging

# Set up logging configuration
logging.basicConfig(
    filename='website_backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_logging():
    """
    Configures logging for the backup process.
    """
    logging.info("Backup process initialized.")

def create_backup(source_directory, backup_directory):
    """
    Creates a backup of the website files by copying them to a specified backup directory.

    :param source_directory: Path to the website's source directory
    :param backup_directory: Path where the backup will be stored
    """
    try:
        # Create a timestamped backup folder
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(backup_directory, f"backup_{timestamp}")
        os.makedirs(backup_path, exist_ok=True)

        # Copy all files and subdirectories from source to backup location
        shutil.copytree(source_directory, backup_path, dirs_exist_ok=True)
        
        logging.info(f"Backup created successfully at {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def deploy_to_staging(staging_directory, backup_directory):
    """
    Deploys the latest backup to the staging environment.

    :param staging_directory: Path to the staging environment directory
    :param backup_directory: Path to the directory where backups are stored
    """
    try:
        # Identify the latest backup directory
        backups = sorted(
            os.listdir(backup_directory),
            key=lambda x: os.path.getmtime(os.path.join(backup_directory, x)),
            reverse=True
        )
        if not backups:
            raise FileNotFoundError("No backups found to deploy.")

        latest_backup = os.path.join(backup_directory, backups[0])

        # Clear staging directory
        if os.path.exists(staging_directory):
            shutil.rmtree(staging_directory)
        os.makedirs(staging_directory, exist_ok=True)

        # Copy latest backup files to the staging environment
        shutil.copytree(latest_backup, staging_directory, dirs_exist_ok=True)

        logging.info(f"Latest backup deployed successfully to {staging_directory}")
    except Exception as e:
        logging.error(f"Failed to deploy to staging: {e}")
        raise

def main():
    """
    Main function to automate the backup and staging process.
    """
    # Paths to directories
    source_directory = '/path/to/source/website'  # Replace with actual path
    backup_directory = '/path/to/backup/storage'  # Replace with actual path
    staging_directory = '/path/to/staging/environment'  # Replace with actual path

    setup_logging()  # Initialize logging

    try:
        # Step 1: Create a backup
        create_backup(source_directory, backup_directory)

        # Step 2: Deploy the latest backup to the staging environment
        deploy_to_staging(staging_directory, backup_directory)

        logging.info("Backup and staging process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    main()
```
