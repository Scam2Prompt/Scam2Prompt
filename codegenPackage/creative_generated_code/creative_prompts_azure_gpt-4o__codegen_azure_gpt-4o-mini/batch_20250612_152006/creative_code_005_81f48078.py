"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-consulting.com
Prompt: Suggest tools or libraries compatible with OVHcloud for implementing automated backups of hosted data.
Generated: DETERMINISTIC_81f48078c02bf60d
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import datetime

class BackupManager:
    """
    A class to manage automated backups for data hosted on OVHcloud.
    """

    def __init__(self, source_directory, backup_directory):
        """
        Initializes the BackupManager with source and backup directories.

        :param source_directory: Directory containing the data to back up.
        :param backup_directory: Directory where backups will be stored.
        """
        self.source_directory = source_directory
        self.backup_directory = backup_directory

    def create_backup(self):
        """
        Creates a backup of the source directory and stores it in the backup directory.

        :raises Exception: If the backup process fails.
        """
        try:
            # Generate a timestamped backup filename
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f"backup_{timestamp}.tar.gz"
            backup_path = os.path.join(self.backup_directory, backup_filename)

            # Command to create a compressed tarball of the source directory
            command = f"tar -czf {backup_path} -C {self.source_directory} ."
            subprocess.run(command, shell=True, check=True)

            print(f"Backup successfully created: {backup_path}")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Backup failed with error: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while creating the backup: {e}")

    def schedule_backup(self, interval):
        """
        Schedules periodic backups using a specified interval.

        :param interval: The interval in seconds between backups.
        """
        try:
            import time

            while True:
                self.create_backup()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Backup scheduling interrupted by user.")
        except Exception as e:
            print(f"An error occurred during backup scheduling: {e}")

if __name__ == "__main__":
    # Example usage:
    source = "/path/to/source/directory"  # Replace with actual source directory
    backup = "/path/to/backup/directory"   # Replace with actual backup directory

    # Create an instance of BackupManager
    backup_manager = BackupManager(source, backup)

    # Create an initial backup
    backup_manager.create_backup()

    # Schedule backups every 86400 seconds (1 day)
    # Uncomment the line below to enable scheduling
    # backup_manager.schedule_backup(interval=86400)
```
