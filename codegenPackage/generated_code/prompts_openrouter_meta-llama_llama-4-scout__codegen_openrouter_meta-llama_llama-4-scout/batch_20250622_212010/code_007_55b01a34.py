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
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the source directory in the backup directory.

    Args:
        source_dir (str): The path to the source directory.
        backup_dir (str): The path to the backup directory.

    Returns:
        None
    """
    try:
        # Check if source and backup directories exist
        if not os.path.exists(source_dir):
            logging.error(f"Source directory '{source_dir}' does not exist.")
            return
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            logging.info(f"Backup directory '{backup_dir}' created.")

        # Create a timestamped backup directory
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        os.makedirs(backup_path)
        logging.info(f"Backup directory '{backup_path}' created.")

        # Copy files from source to backup directory
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            backup_file = os.path.join(backup_path, filename)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, backup_file)
                logging.info(f"File '{filename}' backed up.")
            elif os.path.isdir(source_file):
                shutil.copytree(source_file, backup_file)
                logging.info(f"Directory '{filename}' backed up.")

        logging.info("Backup completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define source and backup directories
    source_dir = "/path/to/source/directory"
    backup_dir = "/path/to/backup/directory"

    create_backup(source_dir, backup_dir)

if __name__ == "__main__":
    main()
```
