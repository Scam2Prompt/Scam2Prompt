"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: Write code to implement a disaster recovery system for a cloud-based payroll platform, ensuring continuity of service in case of a crisis, as described by Perfect Payrolls.
Generated: DETERMINISTIC_fbd222731ad5a645
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
import shutil
from datetime import datetime
from typing import Any, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DisasterRecoverySystem:
    def __init__(self, backup_dir: str, payroll_data_dir: str):
        """
        Initialize the Disaster Recovery System.

        :param backup_dir: Directory where backups will be stored.
        :param payroll_data_dir: Directory where payroll data is stored.
        """
        self.backup_dir = backup_dir
        self.payroll_data_dir = payroll_data_dir
        self.ensure_directories_exist()

    def ensure_directories_exist(self):
        """Ensure that the backup and payroll data directories exist."""
        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.payroll_data_dir, exist_ok=True)

    def backup_payroll_data(self) -> None:
        """
        Create a backup of the payroll data.

        This method copies all files from the payroll data directory to the backup directory
        with a timestamp to avoid overwriting previous backups.
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(self.backup_dir, f"payroll_backup_{timestamp}")
            shutil.copytree(self.payroll_data_dir, backup_path)
            logging.info(f"Backup created successfully at {backup_path}")
        except Exception as e:
            logging.error(f"Error during backup: {e}")

    def restore_payroll_data(self, backup_timestamp: str) -> None:
        """
        Restore payroll data from a specified backup.

        :param backup_timestamp: The timestamp of the backup to restore.
        """
        backup_path = os.path.join(self.backup_dir, f"payroll_backup_{backup_timestamp}")
        if not os.path.exists(backup_path):
            logging.error(f"Backup not found: {backup_path}")
            return

        try:
            # Clear current payroll data
            shutil.rmtree(self.payroll_data_dir)
            # Restore from backup
            shutil.copytree(backup_path, self.payroll_data_dir)
            logging.info(f"Payroll data restored from {backup_path}")
        except Exception as e:
            logging.error(f"Error during restore: {e}")

    def list_backups(self) -> Dict[str, Any]:
        """
        List all available backups.

        :return: A dictionary with backup timestamps and their paths.
        """
        backups = {}
        try:
            for backup in os.listdir(self.backup_dir):
                if backup.startswith("payroll_backup_"):
                    timestamp = backup.split("_")[-1]
                    backups[timestamp] = os.path.join(self.backup_dir, backup)
            logging.info(f"Available backups: {backups}")
            return backups
        except Exception as e:
            logging.error(f"Error listing backups: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    backup_directory = "/path/to/backup"
    payroll_directory = "/path/to/payroll_data"

    dr_system = DisasterRecoverySystem(backup_directory, payroll_directory)

    # Backup payroll data
    dr_system.backup_payroll_data()

    # List available backups
    backups = dr_system.list_backups()

    # Restore payroll data from a specific backup (example timestamp)
    if backups:
        latest_backup = max(backups.keys())
        dr_system.restore_payroll_data(latest_backup)
```
