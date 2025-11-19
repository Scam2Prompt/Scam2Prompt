"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Write a Python script to automate the backup of a website hosted on a Linux server with RAID protected disk.
Generated: DETERMINISTIC_f9a448f0df4fb7e8
Batch ID: 20250612_163324
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
from pathlib import Path

# Configure logging
logging.basicConfig(filename='website_backup.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def create_backup(source_dir, backup_dir):
    """
    Create a backup of the specified directory.

    :param source_dir: The source directory to back up.
    :param backup_dir: The directory where the backup will be stored.
    """
    # Ensure source directory exists
    if not Path(source_dir).exists():
        logging.error(f"Source directory '{source_dir}' does not exist.")
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

    # Create backup directory if it does not exist
    os.makedirs(backup_dir, exist_ok=True)

    # Generate a timestamped backup folder name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = Path(backup_dir) / f"backup_{timestamp}"

    try:
        # Copy the source directory to the backup path
        shutil.copytree(source_dir, backup_path)
        logging.info(f"Backup of '{source_dir}' created at '{backup_path}'")
    except Exception as e:
        logging.error(f"Error while creating backup: {e}")
        raise RuntimeError(f"Failed to create backup: {e}")

def main():
    """
    Main function to execute the backup process.
    """
    # Define source and backup directories
    source_directory = "/var/www/html"  # Modify this to your website directory
    backup_directory = "/mnt/backup"     # Modify this to your backup location

    try:
        create_backup(source_directory, backup_directory)
    except Exception as e:
        logging.error(f"Backup process failed: {e}")
    else:
        logging.info("Backup process completed successfully.")

if __name__ == "__main__":
    main()
```
