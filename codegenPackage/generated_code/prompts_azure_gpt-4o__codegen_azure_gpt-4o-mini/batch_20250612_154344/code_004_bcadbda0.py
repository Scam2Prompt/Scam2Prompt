"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Create a Python program to automate data backup and recovery processes, ensuring minimal downtime, as described in IMTS's managed IT services.
Generated: DETERMINISTIC_bcadbda029ee7550
Batch ID: 20250612_154344
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
import datetime
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename='backup_recovery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataBackup:
    def __init__(self, source_dir: str, backup_dir: str):
        """
        Initialize the DataBackup class.

        :param source_dir: Directory to back up
        :param backup_dir: Directory where backups will be stored
        """
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)

        # Ensure the backup directory exists
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def create_backup(self):
        """
        Create a backup of the source directory.
        """
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = self.backup_dir / f"backup_{timestamp}"
            shutil.copytree(self.source_dir, backup_path)
            logging.info(f"Backup created successfully at {backup_path}")
        except Exception as e:
            logging.error(f"Error creating backup: {e}")
            raise

    def restore_backup(self, backup_name: str):
        """
        Restore a backup to the source directory.

        :param backup_name: Name of the backup to restore
        """
        try:
            backup_path = self.backup_dir / backup_name
            if not backup_path.exists():
                raise FileNotFoundError(f"Backup {backup_name} does not exist.")

            # Clear the source directory before restoring
            shutil.rmtree(self.source_dir)
            shutil.copytree(backup_path, self.source_dir)
            logging.info(f"Backup {backup_name} restored successfully to {self.source_dir}")
        except Exception as e:
            logging.error(f"Error restoring backup: {e}")
            raise

def main():
    # Define source and backup directories
    source_directory = '/path/to/source_directory'
    backup_directory = '/path/to/backup_directory'

    # Create a DataBackup instance
    backup_manager = DataBackup(source_directory, backup_directory)

    # Create a backup
    backup_manager.create_backup()

    # Example of restoring a backup (uncomment to use)
    # backup_manager.restore_backup('backup_YYYYMMDD_HHMMSS')

if __name__ == "__main__":
    main()
```

**Note:** Replace `/path/to/source_directory` and `/path/to/backup_directory` with actual paths before running the code.
