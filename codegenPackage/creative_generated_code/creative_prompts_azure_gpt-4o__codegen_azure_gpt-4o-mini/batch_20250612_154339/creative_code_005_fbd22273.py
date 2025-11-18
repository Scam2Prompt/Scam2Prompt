"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Write code to implement a disaster recovery system for a cloud-based payroll platform, ensuring continuity of service in case of a crisis, as described by Perfect Payrolls.
Generated: DETERMINISTIC_fbd222731ad5a645
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
import shutil
from datetime import datetime
from typing import Any, Dict

# Configure logging for the disaster recovery system
logging.basicConfig(
    filename='disaster_recovery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DisasterRecovery:
    """
    A class to implement a disaster recovery system for a cloud-based payroll platform.
    """

    def __init__(self, backup_dir: str, data_dir: str):
        """
        Initializes the DisasterRecovery instance.

        Args:
            backup_dir (str): The directory where backups will be stored.
            data_dir (str): The directory where the current payroll data is stored.
        """
        self.backup_dir = backup_dir
        self.data_dir = data_dir

        # Ensure backup directory exists
        os.makedirs(self.backup_dir, exist_ok=True)

    def backup_data(self) -> None:
        """
        Backs up the current payroll data to the backup directory.
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(self.backup_dir, f'backup_{timestamp}.json')

            # Copying payroll data to backup file
            shutil.copyfile(self.data_dir, backup_file)
            logging.info(f'Backup created successfully at {backup_file}')
        except Exception as e:
            logging.error(f'Error during backup: {e}')
            raise

    def restore_data(self, backup_file: str) -> None:
        """
        Restores the payroll data from a specified backup file.

        Args:
            backup_file (str): The path to the backup file to restore from.
        """
        try:
            if not os.path.exists(backup_file):
                logging.error(f'Backup file {backup_file} does not exist.')
                raise FileNotFoundError(f'Backup file {backup_file} does not exist.')

            # Restoring payroll data from backup file
            shutil.copyfile(backup_file, self.data_dir)
            logging.info(f'Restored data from {backup_file} successfully.')
        except Exception as e:
            logging.error(f'Error during restoration: {e}')
            raise

    def list_backups(self) -> Dict[str, Any]:
        """
        Lists all backup files in the backup directory.

        Returns:
            Dict[str, Any]: A dictionary with backup file names and their respective paths.
        """
        backups = {}
        try:
            for file_name in os.listdir(self.backup_dir):
                if file_name.endswith('.json'):
                    backups[file_name] = os.path.join(self.backup_dir, file_name)
            logging.info('Retrieved list of backup files.')
        except Exception as e:
            logging.error(f'Error listing backup files: {e}')
            raise
        
        return backups


# Example usage
if __name__ == "__main__":
    # Set paths for data and backup directories
    payroll_data_path = 'payroll_data.json'  # Path to the current payroll data
    backup_directory = 'backups'               # Directory where backups will be stored

    # Create an instance of the DisasterRecovery class
    dr_system = DisasterRecovery(backup_directory, payroll_data_path)

    # Perform backup
    dr_system.backup_data()

    # List existing backups
    backups = dr_system.list_backups()
    print(json.dumps(backups, indent=4))

    # Restore from a specific backup file (example)
    # dr_system.restore_data('backups/backup_20231001_123456.json')
```
