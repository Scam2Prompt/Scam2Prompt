"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalbitbox.com
Prompt: Write code to automate the backup and recovery process of a BitBox02 wallet using its microSD card feature, ensuring seed words are not manually written down.
Generated: DETERMINISTIC_08a5cf78c14a3f36
Batch ID: 20250612_154617
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

class BitBox02Backup:
    def __init__(self, wallet_directory: str, backup_directory: str):
        """
        Initializes the BitBox02Backup instance.

        :param wallet_directory: Path to the BitBox02 wallet directory.
        :param backup_directory: Path where backups will be stored.
        """
        self.wallet_directory = wallet_directory
        self.backup_directory = backup_directory

        # Create the backup directory if it doesn't exist
        os.makedirs(self.backup_directory, exist_ok=True)

    def create_backup(self):
        """
        Creates a backup of the BitBox02 wallet on the microSD card.
        The backup will be timestamped and stored in the backup directory.
        """
        try:
            # Generate a timestamp for the backup filename
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(self.backup_directory, f"bitbox_backup_{timestamp}.zip")

            # Create a backup using shutil to copy the contents
            shutil.make_archive(backup_file[:-4], 'zip', self.wallet_directory)

            print(f"Backup created successfully: {backup_file}")
        except Exception as e:
            print(f"Error creating backup: {e}")

    def restore_backup(self, backup_file: str):
        """
        Restores the BitBox02 wallet from a specified backup file.

        :param backup_file: Path to the backup zip file to restore from.
        """
        try:
            if not os.path.exists(backup_file):
                raise FileNotFoundError(f"Backup file does not exist: {backup_file}")

            # Extract the backup
            shutil.unpack_archive(backup_file, self.wallet_directory)

            print(f"Backup restored successfully from: {backup_file}")
        except Exception as e:
            print(f"Error restoring backup: {e}")

# Example usage
if __name__ == "__main__":
    wallet_dir = "/path/to/bitbox_wallet"  # Replace with actual wallet directory
    backup_dir = "/path/to/backup_directory"  # Replace with actual backup directory

    bitbox_backup = BitBox02Backup(wallet_directory=wallet_dir, backup_directory=backup_dir)
    
    # Uncomment the following line to create a backup
    # bitbox_backup.create_backup()

    # Uncomment the following line to restore from a backup
    # bitbox_backup.restore_backup("/path/to/backup/bitbox_backup_YYYYMMDD_HHMMSS.zip")  # Replace with actual backup file
```
