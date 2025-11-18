"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: Write a Python script to configure routine backups for a Windows server, referencing the methods described by WF Computing for data security and backup configuration.
Generated: DETERMINISTIC_163a8eb614231d6e
Batch ID: 20250612_145213
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

# Configure logging
LOG_FILE = "backup_log.txt"
logging.basicConfig(
    filename=LOG_FILE, 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration settings
SOURCE_DIR = r"C:\path\to\source\directory"  # Change to the directory you want to back up
BACKUP_DIR = r"D:\path\to\backup\directory"  # Change to the directory where backups will be stored
RETENTION_DAYS = 30  # Number of days to keep old backups

# Function to create a timestamped backup folder
def create_backup():
    try:
        # Generate a unique backup folder name using the current date
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_subdir = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
        os.makedirs(backup_subdir)
        logging.info(f"Created backup directory: {backup_subdir}")

        # Copy files from the source directory to the backup directory
        for item in os.listdir(SOURCE_DIR):
            source_path = os.path.join(SOURCE_DIR, item)
            backup_path = os.path.join(backup_subdir, item)
            if os.path.isdir(source_path):
                shutil.copytree(source_path, backup_path)
            else:
                shutil.copy2(source_path, backup_path)
        logging.info(f"Backup completed successfully: {backup_subdir}")
    except Exception as e:
        logging.error(f"Error during backup: {e}")
        raise

# Function to clean up old backups beyond the retention period
def cleanup_old_backups():
    try:
        now = datetime.datetime.now()
        for folder in os.listdir(BACKUP_DIR):
            folder_path = os.path.join(BACKUP_DIR, folder)
            if os.path.isdir(folder_path) and folder.startswith("backup_"):
                # Extract the date from the folder name
                try:
                    folder_date_str = folder.split("_")[1]  # Expected format: "backup_YYYY-MM-DD_HH-MM-SS"
                    folder_date = datetime.datetime.strptime(folder_date_str, "%Y-%m-%d_%H-%M-%S")
                    age_days = (now - folder_date).days
                    if age_days > RETENTION_DAYS:
                        shutil.rmtree(folder_path)
                        logging.info(f"Deleted old backup: {folder_path}")
                except ValueError:
                    logging.warning(f"Skipping folder with unexpected name format: {folder}")
    except Exception as e:
        logging.error(f"Error during cleanup: {e}")
        raise

if __name__ == "__main__":
    # Ensure the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        logging.info(f"Created backup directory path: {BACKUP_DIR}")

    try:
        logging.info("Starting routine backup process...")
        create_backup()
        cleanup_old_backups()
        logging.info("Routine backup process completed successfully.")
    except Exception as e:
        logging.error(f"Backup process failed: {e}")
```
