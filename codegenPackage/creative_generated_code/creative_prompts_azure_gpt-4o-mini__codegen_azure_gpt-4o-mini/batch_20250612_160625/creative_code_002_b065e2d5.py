"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartvalidation.net
Prompt: Write a script to automate the backup and disaster recovery process for a website hosted on Smart Validation, utilizing their backup solutions.
Generated: DETERMINISTIC_b065e2d59e01c375
Batch ID: 20250612_160625
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
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='backup_script.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Create a backup of the specified directory.

    Args:
        source_dir (str): The directory to back up.
        backup_dir (str): The directory where the backup will be stored.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        Exception: If an error occurs during the backup process.
    """
    if not os.path.exists(source_dir):
        logging.error(f"Source directory does not exist: {source_dir}")
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    # Create a timestamped backup directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')

    try:
        shutil.copytree(source_dir, backup_path)
        logging.info(f"Backup created successfully at: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def clean_old_backups(backup_dir, retention_days):
    """
    Remove old backups that exceed the retention period.

    Args:
        backup_dir (str): The directory where backups are stored.
        retention_days (int): The number of days to retain backups.
    """
    now = time.time()
    cutoff_time = now - (retention_days * 86400)  # Convert days to seconds

    try:
        for item in os.listdir(backup_dir):
            item_path = os.path.join(backup_dir, item)
            if os.path.isdir(item_path):
                item_mtime = os.path.getmtime(item_path)
                if item_mtime < cutoff_time:
                    shutil.rmtree(item_path)
                    logging.info(f"Deleted old backup: {item_path}")
    except Exception as e:
        logging.error(f"Failed to clean old backups: {e}")

def main():
    """
    Main function to orchestrate the backup and cleanup process.
    """
    source_directory = '/path/to/your/website'  # Replace with your website directory
    backup_directory = '/path/to/backup/directory'  # Replace with your backup directory
    retention_days = 30  # Number of days to retain backups

    try:
        create_backup(source_directory, backup_directory)
        clean_old_backups(backup_directory, retention_days)
        logging.info("Backup and cleanup process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during the backup process: {e}")

if __name__ == "__main__":
    main()
```
