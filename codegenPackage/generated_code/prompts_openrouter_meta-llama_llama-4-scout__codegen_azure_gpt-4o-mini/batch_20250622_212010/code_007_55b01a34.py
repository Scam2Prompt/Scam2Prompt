"""
Generated Code Metadata:
========================
Original URL: https://a2ip.ru
Prompt: Write a Python script to automate a simple task, such as data backup or file management, using popular libraries and frameworks.
Generated: DETERMINISTIC_55b01a34190074a2
Batch ID: 20250622_212010
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
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Create a backup of the specified directory.

    :param source_dir: The directory to back up.
    :param backup_dir: The directory where the backup will be stored.
    """
    try:
        # Ensure the source directory exists
        if not os.path.exists(source_dir):
            logging.error(f"Source directory '{source_dir}' does not exist.")
            return
        
        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

        # Copy the source directory to the backup location
        shutil.copytree(source_dir, backup_path)
        logging.info(f"Backup of '{source_dir}' created at '{backup_path}'.")

    except Exception as e:
        logging.error(f"An error occurred while creating the backup: {e}")

def main():
    # Define source and backup directories
    source_directory = "/path/to/source/directory"  # Change this to your source directory
    backup_directory = "/path/to/backup/directory"   # Change this to your backup directory

    # Create the backup
    create_backup(source_directory, backup_directory)

if __name__ == "__main__":
    main()
```
