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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("backup.log"),
        logging.StreamHandler()
    ]
)

class DataBackup:
    def __init__(self, source_dir, backup_dir):
        """
        Initializes the DataBackup instance.

        :param source_dir: Directory to back up.
        :param backup_dir: Destination directory for the backup.
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir

    def create_backup(self):
        """
        Creates a backup of the source directory to the backup directory.
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(self.backup_dir, f"backup_{timestamp}")
            shutil.copytree(self.source_dir, backup_path)
            logging.info(f"Backup created successfully at {backup_path}")
        except FileNotFoundError as e:
            logging.error(f"Source directory not found: {e}")
        except PermissionError as e:
            logging.error(f"Permission denied: {e}")
        except Exception as e:
            logging.error(f"An error occurred during backup: {e}")

    def restore_backup(self, backup_path):
        """
        Restores data from the specified backup directory to the source directory.

        :param backup_path: The path to the backup directory to restore from.
        """
        try:
            if not os.path.exists(backup_path):
                raise FileNotFoundError(f"Backup directory does not exist: {backup_path}")
            shutil.rmtree(self.source_dir)  # Remove current data before restoring
            shutil.copytree(backup_path, self.source_dir)
            logging.info(f"Data restored successfully from {backup_path} to {self.source_dir}")
        except FileNotFoundError as e:
            logging.error(f"Backup path not found: {e}")
        except PermissionError as e:
            logging.error(f"Permission denied: {e}")
        except Exception as e:
            logging.error(f"An error occurred during restoration: {e}")

if __name__ == "__main__":
    # Example usage
    SOURCE_DIR = "/path/to/source/directory"  # Change to your source directory
    BACKUP_DIR = "/path/to/backup/directory"  # Change to your backup directory

    backup_manager = DataBackup(SOURCE_DIR, BACKUP_DIR)

    # Create a backup
    backup_manager.create_backup()

    # Restore from a specific backup (uncomment to use)
    # BACKUP_PATH = "/path/to/specific/backup/directory"  # Specify the backup path
    # backup_manager.restore_backup(BACKUP_PATH)
```
