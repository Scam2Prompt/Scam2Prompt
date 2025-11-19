"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openspa.info
Prompt: Write a guide on backing up OpenSPA settings for a Zgemma receiver.
Generated: DETERMINISTIC_f3904d464921ddd1
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for backing up OpenSPA settings on a Zgemma receiver.

This script creates a backup of the OpenSPA settings by copying
configuration files and related data to a specified destination folder.

Requirements:
- Python 3.x
- Access to the Zgemma receiver filesystem (e.g., via mounted storage or SSH)

Usage:
- Update the `SOURCE_DIR` and `BACKUP_DIR` variables as needed.
"""

import os
import shutil
from datetime import datetime

# Define the source directory (typically where OpenSPA settings are stored on the receiver)
SOURCE_DIR = "/etc/enigma2"

# Define the backup directory (where backup files will be stored)
# Ensure this is writable and accessible
BACKUP_DIR = "/path/to/backup/directory"

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the OpenSPA settings.

    Args:
        source_dir (str): Path to the source directory containing OpenSPA settings.
        backup_dir (str): Path to the backup directory where the files will be stored.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If the backup directory is not writable.
        Exception: For other runtime errors.
    """
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Ensure the backup directory exists, create if it doesn't
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Create a timestamped subfolder for the backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_subdir = os.path.join(backup_dir, f"backup_{timestamp}")
        os.makedirs(backup_subdir)

        # Copy all files and subdirectories from the source to the backup folder
        shutil.copytree(source_dir, backup_subdir, dirs_exist_ok=True)

        print(f"Backup successful! Files backed up to: {backup_subdir}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: {perm_error}. Please ensure you have write permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function that initiates the backup process.
    """
    print("Starting OpenSPA settings backup...")
    create_backup(SOURCE_DIR, BACKUP_DIR)
    print("Backup process completed.")

if __name__ == "__main__":
    main()
```
