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
from datetime import datetime

# Constants
SOURCE_DIR = "path/to/source/directory"  # Replace with the directory to back up
BACKUP_DIR = "path/to/backup/directory"  # Replace with the backup destination directory
LOG_FILE = "backup_log.txt"  # Log file to record backup operations

def create_backup(source, destination):
    """
    Creates a backup of the source directory into the destination directory.
    """
    try:
        # Ensure the source directory exists
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source directory '{source}' does not exist.")

        # Ensure the destination directory exists, create if not
        if not os.path.exists(destination):
            os.makedirs(destination)

        # Generate a timestamped backup folder name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_folder = os.path.join(destination, f"backup_{timestamp}")

        # Copy the source directory to the backup folder
        shutil.copytree(source, backup_folder)

        # Log the successful backup
        log_message = f"Backup created successfully: {backup_folder}\n"
        log_operation(log_message)

        print("Backup completed successfully.")
    except Exception as e:
        # Log any errors encountered during the backup process
        log_message = f"Error during backup: {str(e)}\n"
        log_operation(log_message)
        print(f"An error occurred: {e}")

def log_operation(message):
    """
    Logs a message to the log file.
    """
    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")
    except Exception as e:
        print(f"Failed to write to log file: {e}")

if __name__ == "__main__":
    # Run the backup operation
    create_backup(SOURCE_DIR, BACKUP_DIR)
```
