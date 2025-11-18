"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Generate code to create a backup of data on a server using the guidelines provided in Media Temple's KnowledgeBase articles.
Generated: DETERMINISTIC_8e47416104e506ac
Batch ID: 20250612_151639
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='backup.log',
                    filemode='a')

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the source directory to the backup directory.

    Parameters:
    source_dir (str): The path to the source directory to backup.
    backup_dir (str): The path to the backup directory where the backup will be stored.

    Raises:
    ValueError: If source_dir does not exist or is not a directory.
    OSError: If an error occurs during the backup process.
    """
    # Check if the source directory exists and is a directory
    if not os.path.exists(source_dir):
        logging.error(f"Source directory '{source_dir}' does not exist.")
        raise ValueError(f"Source directory '{source_dir}' does not exist.")

    if not os.path.isdir(source_dir):
        logging.error(f"Source path '{source_dir}' is not a directory.")
        raise ValueError(f"Source path '{source_dir}' is not a directory.")

    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)

    # Generate backup folder name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")

    try:
        # Copy the entire source directory to the backup directory
        shutil.copytree(source_dir, backup_folder)
        logging.info(f"Backup created successfully at '{backup_folder}'.")
    except OSError as e:
        logging.error(f"Error occurred while creating backup: {e}")
        raise OSError(f"Error occurred while creating backup: {e}")

if __name__ == "__main__":
    # Example usage
    SOURCE_DIRECTORY = "/path/to/source/directory"
    BACKUP_DIRECTORY = "/path/to/backup/directory"

    try:
        create_backup(SOURCE_DIRECTORY, BACKUP_DIRECTORY)
    except Exception as e:
        logging.critical(f"Backup process failed: {e}")
```
