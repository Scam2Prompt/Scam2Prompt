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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='disaster_recovery_plan.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class DisasterRecoveryPlan:
    def __init__(self, source_dir, backup_dir):
        """
        Initializes the DisasterRecoveryPlan with source and backup directories.

        :param source_dir: Directory containing critical data to back up
        :param backup_dir: Directory where backups will be stored
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        logging.info("Disaster recovery plan initialized.")

    def backup_data(self):
        """
        Back up the source directory to the backup directory.
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = os.path.join(self.backup_dir, f'backup_{timestamp}')
            
            # Create the backup directory if it does not exist
            os.makedirs(backup_path, exist_ok=True)
            logging.info(f"Backing up data from {self.source_dir} to {backup_path}.")

            # Copy the contents of the source directory to the backup directory
            shutil.copytree(self.source_dir, backup_path)
            logging.info("Backup completed successfully.")

        except Exception as e:
            logging.error(f"Failed to back up data: {e}")

    def restore_data(self, backup_path):
        """
        Restore data from a specified backup path to the source directory.

        :param backup_path: Path to the backup directory to restore from
        """
        try:
            logging.info(f"Restoring data from {backup_path} to {self.source_dir}.")

            # Remove the current data in the source directory
            if os.path.exists(self.source_dir):
                shutil.rmtree(self.source_dir)

            # Restore the backup to the source directory
            shutil.copytree(backup_path, self.source_dir)
            logging.info("Data restoration completed successfully.")

        except Exception as e:
            logging.error(f"Failed to restore data: {e}")

    def list_backups(self):
        """
        List all available backup directories.
        """
        try:
            backups = os.listdir(self.backup_dir)
            logging.info("Available backups:")
            for backup in backups:
                logging.info(backup)

            return backups

        except Exception as e:
            logging.error(f"Failed to list backups: {e}")
            return []

if __name__ == "__main__":
    # Example usage
    source_directory = '/path/to/critical/data'
    backup_directory = '/path/to/backup/location'

    dr_plan = DisasterRecoveryPlan(source_directory, backup_directory)

    # Perform backup
    dr_plan.backup_data()

    # List backups
    dr_plan.list_backups()

    # Restore from a specific backup (example)
    # dr_plan.restore_data('/path/to/backup/location/backup_YYYYMMDD_HHMMSS')
```
