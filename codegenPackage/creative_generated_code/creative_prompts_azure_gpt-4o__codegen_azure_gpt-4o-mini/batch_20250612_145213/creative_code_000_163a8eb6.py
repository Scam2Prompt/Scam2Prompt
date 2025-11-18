"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: Write a Python script to configure routine backups for a Windows server, referencing the methods described by WF Computing for data security and backup configuration.
Generated: DETERMINISTIC_163a8eb614231d6e
Batch ID: 20250612_145213
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

# Configure logging for the backup process
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to create a backup of specified directory
def create_backup(source_dir, backup_dir):
    try:
        # Generate a timestamped backup folder name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")

        # Ensure the backup directory exists
        os.makedirs(backup_folder, exist_ok=True)

        # Copy the contents of the source directory to the backup folder
        shutil.copytree(source_dir, os.path.join(backup_folder, os.path.basename(source_dir)))
        logging.info(f'Successfully backed up {source_dir} to {backup_folder}')

    except FileNotFoundError as e:
        logging.error(f"Source directory not found: {e}")
    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
    except Exception as e:
        logging.error(f"An error occurred during backup: {e}")

# Function to schedule backups at regular intervals
def schedule_backups(source_dir, backup_dir, interval_minutes=60):
    while True:
        create_backup(source_dir, backup_dir)
        logging.info(f'Scheduled backup completed. Waiting for next backup in {interval_minutes} minutes.')
        time.sleep(interval_minutes * 60)  # Wait for the specified interval

if __name__ == "__main__":
    # Define the source directory to back up and the backup destination directory
    SOURCE_DIRECTORY = "C:\\path\\to\\your\\source_directory"  # Change this to your source directory
    BACKUP_DIRECTORY = "C:\\path\\to\\your\\backup_directory"  # Change this to your backup directory
    BACKUP_INTERVAL = 60  # Set the backup interval in minutes

    # Start the backup scheduling
    schedule_backups(SOURCE_DIRECTORY, BACKUP_DIRECTORY, BACKUP_INTERVAL)
```
