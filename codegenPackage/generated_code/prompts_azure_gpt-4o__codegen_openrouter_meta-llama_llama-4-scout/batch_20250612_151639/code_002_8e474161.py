"""
Generated Code Metadata:
========================
Original URL: https://syneoshealthls.com
Prompt: Generate code to create a backup of data on a server using the guidelines provided in Media Temple's KnowledgeBase articles.
Generated: DETERMINISTIC_8e47416104e506ac
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Server Data Backup Script**
=====================================

```python
import os
import shutil
import datetime
import tarfile
import logging

# Set up logging configuration
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the source directory and saves it to the backup directory.

    Args:
        source_dir (str): The directory to be backed up.
        backup_dir (str): The directory where the backup will be saved.

    Returns:
        str: The path to the backup file.
    """
    try:
        # Check if source and backup directories exist
        if not os.path.exists(source_dir):
            logging.error(f"Source directory '{source_dir}' does not exist.")
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            logging.info(f"Backup directory '{backup_dir}' created.")

        # Create a timestamped backup file name
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file_name = f"backup_{timestamp}.tar.gz"
        backup_file_path = os.path.join(backup_dir, backup_file_name)

        # Create a tarball of the source directory
        with tarfile.open(backup_file_path, "w:gz") as tar:
            tar.add(source_dir)

        logging.info(f"Backup created: {backup_file_path}")
        return backup_file_path

    except Exception as e:
        logging.error(f"Error creating backup: {e}")
        raise

def main():
    # Define source and backup directories
    source_dir = "/path/to/source/directory"
    backup_dir = "/path/to/backup/directory"

    try:
        backup_file_path = create_backup(source_dir, backup_dir)
        logging.info(f"Backup complete: {backup_file_path}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")

if __name__ == "__main__":
    main()
```

**Crontab Entry for Automated Backups**
----------------------------------------

```bash
# m h  dom mon dow   command
0 0 * * * python /path/to/backup/script.py
```
