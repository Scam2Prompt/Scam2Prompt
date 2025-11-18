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

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("backup_log.log"),
                              logging.StreamHandler()])

class DataBackup:
    def __init__(self, source_dir, backup_dir):
        """
        Initializes the DataBackup class with source and backup directories.

        :param source_dir: The directory where the data to be backed up is located.
        :param backup_dir: The directory where backups will be stored.
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir

    def backup_data(self):
        """
        Performs the backup of data from the source directory to the backup directory.
        Creates a timestamped backup folder to avoid overwriting previous backups.
        """
        try:
            # Create a timestamped backup folder
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_folder = os.path.join(self.backup_dir, f"backup_{timestamp}")
            os.makedirs(backup_folder, exist_ok=True)
            logging.info(f"Backup folder created: {backup_folder}")

            # Copy all files and subdirectories from source to backup
            shutil.copytree(self.source_dir, backup_folder)
            logging.info(f"Backup completed successfully from {self.source_dir} to {backup_folder}")

        except Exception as e:
            logging.error(f"Error during backup: {e}")

    def restore_data(self, backup_folder):
        """
        Restores data from a specified backup folder to the source directory.

        :param backup_folder: The folder containing the backup data to be restored.
        """
        try:
            # Ensure the backup folder exists
            if not os.path.exists(backup_folder):
                raise FileNotFoundError(f"The specified backup folder does not exist: {backup_folder}")

            # Clear the source directory before restoration
            for item in os.listdir(self.source_dir):
                item_path = os.path.join(self.source_dir, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

            # Copy all data from the backup folder to the source directory
            shutil.copytree(backup_folder, self.source_dir)
            logging.info(f"Data restored successfully from {backup_folder} to {self.source_dir}")

        except Exception as e:
            logging.error(f"Error during restoration: {e}")

if __name__ == "__main__":
    # Define source and backup directories
    source_directory = "/path/to/source_directory"  # Update to your source directory
    backup_directory = "/path/to/backup_directory"  # Update to your backup directory

    # Create a DataBackup instance
    data_backup = DataBackup(source_directory, backup_directory)

    # Perform backup
    data_backup.backup_data()
    
    # Uncomment the following line to restore data from a specific backup folder
    # data_backup.restore_data("/path/to/specific_backup_folder")  # Update to your specific backup folder
```

Make sure to update `/path/to/source_directory` and `/path/to/backup_directory` with the actual paths you want to use for the backup and source directories.
