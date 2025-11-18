"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Create a Python program to automate data backup and recovery processes, ensuring minimal downtime, as described in IMTS's managed IT services.
Generated: DETERMINISTIC_bcadbda029ee7550
Batch ID: 20250612_154344
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
LOG_FILE = "backup_recovery.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
SOURCE_DIR = "/path/to/source"  # Directory to be backed up
BACKUP_DIR = "/path/to/backup"  # Destination for backups
RECOVERY_DIR = "/path/to/recovery"  # Destination for recovered data
RETENTION_DAYS = 7  # Number of days to retain old backups

def create_backup():
    """
    Create a backup of the SOURCE_DIR into BACKUP_DIR with a timestamp.
    """
    try:
        if not os.path.exists(SOURCE_DIR):
            raise FileNotFoundError(f"The source directory '{SOURCE_DIR}' does not exist.")
        
        # Generate a timestamp for the backup folder name
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
        
        # Perform the backup
        shutil.copytree(SOURCE_DIR, backup_path)
        logging.info(f"Backup created successfully at {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise e

def clean_old_backups():
    """
    Remove backups older than RETENTION_DAYS from BACKUP_DIR.
    """
    try:
        now = datetime.datetime.now()
        for folder in os.listdir(BACKUP_DIR):
            folder_path = os.path.join(BACKUP_DIR, folder)
            if os.path.isdir(folder_path):
                # Extract the timestamp from the folder name and calculate its age
                try:
                    folder_timestamp = folder.split("_")[1]
                    folder_date = datetime.datetime.strptime(folder_timestamp, "%Y%m%d_%H%M%S")
                    age_days = (now - folder_date).days
                    
                    # Delete the folder if it exceeds the retention period
                    if age_days > RETENTION_DAYS:
                        shutil.rmtree(folder_path)
                        logging.info(f"Deleted old backup: {folder_path}")
                except ValueError:
                    # Skip folders that don't match the naming convention
                    logging.warning(f"Skipping non-conforming folder: {folder_path}")
    except Exception as e:
        logging.error(f"Failed to clean old backups: {e}")
        raise e

def recover_data(backup_name):
    """
    Recover a specific backup into RECOVERY_DIR.
    
    :param backup_name: Name of the backup folder to recover.
    """
    try:
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"The backup '{backup_name}' does not exist.")
        
        if os.path.exists(RECOVERY_DIR):
            # Clear recovery directory before recovery
            shutil.rmtree(RECOVERY_DIR)
        
        # Copy the backup data to the recovery directory
        shutil.copytree(backup_path, RECOVERY_DIR)
        logging.info(f"Recovery completed successfully from {backup_path} to {RECOVERY_DIR}")
    except Exception as e:
        logging.error(f"Failed to recover data: {e}")
        raise e

def main():
    """
    Main function to handle backup and recovery processes.
    """
    try:
        logging.info("Starting automated backup process...")
        create_backup()
        
        logging.info("Cleaning up old backups...")
        clean_old_backups()
        
        # Uncomment the following line to test recovery
        # recover_data("backup_20230101_123456")  # Replace with actual backup folder name

        logging.info("Backup process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during the backup/recovery process: {e}")

if __name__ == "__main__":
    main()
```
