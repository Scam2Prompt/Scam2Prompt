"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Develop a data backup and recovery plan for a small business with 1-10 employees, including recommendations for secure data storage and rapid recovery in case of a cyberattack.
Generated: DETERMINISTIC_24f78f64413a493d
Batch ID: 20250622_205541
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
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='backup_recovery.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DataBackupRecovery:
    def __init__(self, source_dir, backup_dir, encryption_key=None):
        """
        Initialize the DataBackupRecovery class.

        :param source_dir: Directory containing the data to back up.
        :param backup_dir: Directory where backups will be stored.
        :param encryption_key: Optional encryption key for securing backups.
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

    def backup_data(self):
        """
        Create a backup of the source directory.
        """
        try:
            # Create a timestamped backup directory
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(self.backup_dir, f"backup_{timestamp}")
            os.makedirs(backup_path, exist_ok=True)

            # Copy files to the backup directory
            for item in os.listdir(self.source_dir):
                s = os.path.join(self.source_dir, item)
                d = os.path.join(backup_path, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, False, None)
                else:
                    shutil.copy2(s, d)

            # Encrypt the backup
            self.encrypt_backup(backup_path)

            logging.info(f"Backup completed successfully: {backup_path}")
        except Exception as e:
            logging.error(f"Error during backup: {e}")

    def encrypt_backup(self, backup_path):
        """
        Encrypt the backup files in the specified directory.

        :param backup_path: Path to the backup directory to encrypt.
        """
        try:
            for root, dirs, files in os.walk(backup_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                    encrypted_data = self.cipher.encrypt(file_data)
                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)

            logging.info(f"Backup encrypted successfully: {backup_path}")
        except Exception as e:
            logging.error(f"Error during encryption: {e}")

    def recover_data(self, backup_path):
        """
        Recover data from a specified backup directory.

        :param backup_path: Path to the backup directory to recover from.
        """
        try:
            # Decrypt the backup
            self.decrypt_backup(backup_path)

            # Restore files to the original source directory
            for item in os.listdir(backup_path):
                s = os.path.join(backup_path, item)
                d = os.path.join(self.source_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, False, None)
                else:
                    shutil.copy2(s, d)

            logging.info(f"Data recovered successfully from: {backup_path}")
        except Exception as e:
            logging.error(f"Error during recovery: {e}")

    def decrypt_backup(self, backup_path):
        """
        Decrypt the backup files in the specified directory.

        :param backup_path: Path to the backup directory to decrypt.
        """
        try:
            for root, dirs, files in os.walk(backup_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        encrypted_data = f.read()
                    decrypted_data = self.cipher.decrypt(encrypted_data)
                    with open(file_path, 'wb') as f:
                        f.write(decrypted_data)

            logging.info(f"Backup decrypted successfully: {backup_path}")
        except Exception as e:
            logging.error(f"Error during decryption: {e}")

# Example usage
if __name__ == "__main__":
    source_directory = '/path/to/source'
    backup_directory = '/path/to/backup'

    backup_recovery = DataBackupRecovery(source_directory, backup_directory)
    backup_recovery.backup_data()
    # To recover data, uncomment the line below and provide the backup path
    # backup_recovery.recover_data('/path/to/backup/backup_timestamp')
```
