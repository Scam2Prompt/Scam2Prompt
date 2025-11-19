"""
Generated Code Metadata:
========================
Original URL: https://web-promo.net
Prompt: Provide a step-by-step guide to automate backups for websites hosted on Xserver using Python.
Generated: DETERMINISTIC_055886c4e3eda20a
Batch ID: 20250612_154319
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
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Create a backup of the specified directory.

    :param source_dir: The directory to back up.
    :param backup_dir: The directory where the backup will be stored.
    :raises FileNotFoundError: If the source directory does not exist.
    :raises Exception: For any other errors that occur during backup.
    """
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = Path(backup_dir) / f"backup_{timestamp}"
        backup_path.mkdir(parents=True, exist_ok=True)

        # Copy the contents of the source directory to the backup directory
        shutil.copytree(source_dir, backup_path, dirs_exist_ok=True)
        logging.info(f"Backup created successfully at '{backup_path}'.")

    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
    except Exception as e:
        logging.error(f"An error occurred while creating the backup: {e}")

def main():
    # Define the source directory (the website files) and the backup directory
    source_directory = "/path/to/your/website"  # Change this to your website's directory
    backup_directory = "/path/to/your/backup"    # Change this to your desired backup location

    # Create a backup
    create_backup(source_directory, backup_directory)

if __name__ == "__main__":
    main()
```

Make sure to replace `"/path/to/your/website"` and `"/path/to/your/backup"` with the actual paths on your server.
