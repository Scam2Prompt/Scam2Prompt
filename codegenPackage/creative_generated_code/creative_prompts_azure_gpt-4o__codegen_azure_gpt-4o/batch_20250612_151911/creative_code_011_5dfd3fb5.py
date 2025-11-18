"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a script to automate data backup and recovery for a growing business, based on CyberConnect's IT services.
Generated: DETERMINISTIC_5dfd3fb56d96ea24
Batch ID: 20250612_151911
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

# Configure logging for the backup script
LOG_FILE = "backup.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Directory paths for backup and recovery
SOURCE_DIR = "/path/to/source/directory"  # Replace with the actual source directory path
BACKUP_DIR = "/path/to/backup/directory"  # Replace with the actual backup directory path

# Ensure both paths exist
if not os.path.exists(SOURCE_DIR):
    raise FileNotFoundError(f"Source directory '{SOURCE_DIR}' does not exist.")

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)  # Create backup directory if it doesn't exist

def create_backup():
    """
    Creates a backup of the source directory by copying all contents
    to a timestamped subdirectory in the backup folder.
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_subdir = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
        shutil.copytree(SOURCE_DIR, backup_subdir)
        
        logging.info(f"Backup created successfully at {backup_subdir}")
        print(f"Backup created successfully at {backup_subdir}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        print(f"Failed to create backup: {e}")

def recover_backup(backup_subdir):
    """
    Recovers data from the specified backup subdirectory to the source directory.
    
    Args:
        backup_subdir (str): Path to the backup subdirectory to restore from.
    """
    try:
        # Validate the backup subdirectory exists
        if not os.path.exists(backup_subdir):
            raise FileNotFoundError(f"Backup subdirectory '{backup_subdir}' does not exist.")
        
        # Clear the source directory before restoring files
        for item in os.listdir(SOURCE_DIR):
            item_path = os.path.join(SOURCE_DIR, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        
        # Restore files from backup
        for item in os.listdir(backup_subdir):
            source_path = os.path.join(backup_subdir, item)
            destination_path = os.path.join(SOURCE_DIR, item)
            if os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
            else:
                shutil.copy2(source_path, destination_path)
        
        logging.info(f"Recovery completed successfully from {backup_subdir}")
        print(f"Recovery completed successfully from {backup_subdir}")
    except Exception as e:
        logging.error(f"Failed to recover backup: {e}")
        print(f"Failed to recover backup: {e}")

if __name__ == "__main__":
    print("Welcome to the Backup & Recovery System!")
    print("1. Create Backup")
    print("2. Recover Backup")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        create_backup()
    elif choice == "2":
        backup_subdir = input("Enter the path to the backup subdirectory: ")
        recover_backup(backup_subdir)
    else:
        print("Invalid choice! Please select 1 or 2.")
```
