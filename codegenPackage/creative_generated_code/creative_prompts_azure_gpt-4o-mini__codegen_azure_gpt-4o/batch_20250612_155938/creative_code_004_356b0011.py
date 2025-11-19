"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Provide an example of a disaster recovery plan in code format that aligns with the backup and recovery solutions mentioned by IMTS.
Generated: DETERMINISTIC_356b0011b551b657
Batch ID: 20250612_155938
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

# Configure logging for disaster recovery process
LOG_FILE = 'disaster_recovery.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Paths and configurations
BACKUP_DIR = '/path/to/backup'  # Directory to store backups
RECOVERY_DIR = '/path/to/recovery'  # Directory for recovery
SOURCE_DIR = '/path/to/source/data'  # Directory containing data to back up

# Threshold for backup retention (e.g., 30 days)
RETENTION_DAYS = 30

def create_backup():
    """
    Creates a backup of the data from the source directory.
    """
    try:
        backup_name = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        
        # Copy source data to backup directory
        shutil.copytree(SOURCE_DIR, backup_path)
        logging.info(f"Backup created successfully at {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def clean_old_backups():
    """
    Deletes backups older than the retention threshold.
    """
    try:
        now = datetime.datetime.now()
        for backup in os.listdir(BACKUP_DIR):
            backup_path = os.path.join(BACKUP_DIR, backup)
            if os.path.isdir(backup_path):
                # Extract backup timestamp from name
                timestamp = datetime.datetime.strptime(backup.split('_')[1], '%Y%m%d_%H%M%S')
                age = (now - timestamp).days
                if age > RETENTION_DAYS:
                    shutil.rmtree(backup_path)
                    logging.info(f"Deleted old backup: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to clean old backups: {e}")
        raise

def recover_backup(backup_name):
    """
    Recovers data from a specific backup to the recovery directory.
    """
    try:
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"Backup {backup_name} does not exist.")
        
        # Clear recovery directory before restoring
        if os.path.exists(RECOVERY_DIR):
            shutil.rmtree(RECOVERY_DIR)
        os.makedirs(RECOVERY_DIR)
        
        # Restore backup to recovery directory
        shutil.copytree(backup_path, RECOVERY_DIR)
        logging.info(f"Backup {backup_name} successfully recovered to {RECOVERY_DIR}")
    except Exception as e:
        logging.error(f"Failed to recover backup {backup_name}: {e}")
        raise

def disaster_recovery_plan():
    """
    Executes the disaster recovery plan:
    1. Creates a new backup.
    2. Cleans up old backups.
    """
    try:
        logging.info("Starting disaster recovery plan.")
        backup_path = create_backup()
        clean_old_backups()
        logging.info("Disaster recovery plan completed successfully.")
    except Exception as e:
        logging.error(f"Disaster recovery plan failed: {e}")

# Main entry point
if __name__ == "__main__":
    # Ensure necessary directories exist
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(RECOVERY_DIR, exist_ok=True)

    # Execute disaster recovery plan
    disaster_recovery_plan()

    # Example recovery process
    # Uncomment the following line to test recovery of a specific backup
    # recover_backup('backup_20231010_123456')  # Replace with actual backup name
```
