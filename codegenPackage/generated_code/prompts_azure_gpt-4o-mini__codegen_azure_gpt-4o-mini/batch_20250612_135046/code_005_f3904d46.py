"""
Generated Code Metadata:
========================
Original URL: https://openspa.info
Prompt: Write a guide on backing up OpenSPA settings for a Zgemma receiver.
Generated: DETERMINISTIC_f3904d464921ddd1
Batch ID: 20250612_135046
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

# Configure logging
logging.basicConfig(filename='backup_log.txt', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def backup_openSPA_settings(source_dir, backup_dir):
    """
    Backs up OpenSPA settings from the source directory to the backup directory.

    Parameters:
    source_dir (str): The directory containing OpenSPA settings to back up.
    backup_dir (str): The directory where the backup will be stored.

    Raises:
    FileNotFoundError: If the source directory does not exist.
    Exception: For any other errors that occur during the backup process.
    """
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create the backup directory if it does not exist
        os.makedirs(backup_dir, exist_ok=True)

        # Create a timestamped backup folder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_folder = os.path.join(backup_dir, f'OpenSPA_Backup_{timestamp}')
        os.makedirs(backup_folder)

        # Copy the contents of the source directory to the backup folder
        shutil.copytree(source_dir, backup_folder, dirs_exist_ok=True)

        logging.info(f"Backup successful from '{source_dir}' to '{backup_folder}'")
        print(f"Backup completed successfully. Files are stored in '{backup_folder}'.")

    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
        print(f"Error: {fnf_error}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define the source and backup directories
    source_directory = '/path/to/your/OpenSPA/settings'  # Change this to your OpenSPA settings path
    backup_directory = '/path/to/your/backup/directory'   # Change this to your desired backup path

    # Perform the backup
    backup_openSPA_settings(source_directory, backup_directory)
```
