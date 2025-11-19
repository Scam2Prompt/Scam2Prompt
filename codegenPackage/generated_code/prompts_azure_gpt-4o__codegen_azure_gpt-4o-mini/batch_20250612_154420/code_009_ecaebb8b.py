"""
Generated Code Metadata:
========================
Original URL: https://linkbonus.net
Prompt: Generate code to back up and restore Nginx Proxy Manager configurations programmatically.
Generated: DETERMINISTIC_ecaebb8b67b88411
Batch ID: 20250612_154420
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
import tarfile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NginxProxyManagerBackup:
    def __init__(self, config_dir='/etc/nginx-proxy-manager', backup_dir='/backups/nginx-proxy-manager'):
        """
        Initialize the backup manager with the configuration and backup directories.

        :param config_dir: Directory where Nginx Proxy Manager configurations are stored.
        :param backup_dir: Directory where backups will be stored.
        """
        self.config_dir = config_dir
        self.backup_dir = backup_dir

    def create_backup(self):
        """
        Create a backup of the Nginx Proxy Manager configurations.

        :raises Exception: If the backup process fails.
        """
        try:
            # Create backup directory if it doesn't exist
            os.makedirs(self.backup_dir, exist_ok=True)

            # Generate a timestamp for the backup file
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(self.backup_dir, f'nginx_proxy_manager_backup_{timestamp}.tar.gz')

            # Create a tar.gz archive of the configuration directory
            with tarfile.open(backup_file, 'w:gz') as tar:
                tar.add(self.config_dir, arcname=os.path.basename(self.config_dir))

            logging.info(f'Backup created successfully: {backup_file}')
        except Exception as e:
            logging.error(f'Error creating backup: {e}')
            raise

    def restore_backup(self, backup_file):
        """
        Restore Nginx Proxy Manager configurations from a backup file.

        :param backup_file: Path to the backup file to restore from.
        :raises FileNotFoundError: If the backup file does not exist.
        :raises Exception: If the restore process fails.
        """
        if not os.path.isfile(backup_file):
            logging.error(f'Backup file not found: {backup_file}')
            raise FileNotFoundError(f'Backup file not found: {backup_file}')

        try:
            # Extract the backup file to the configuration directory
            with tarfile.open(backup_file, 'r:gz') as tar:
                tar.extractall(path=self.config_dir)

            logging.info(f'Backup restored successfully from: {backup_file}')
        except Exception as e:
            logging.error(f'Error restoring backup: {e}')
            raise

if __name__ == '__main__':
    # Example usage
    backup_manager = NginxProxyManagerBackup()

    # Create a backup
    try:
        backup_manager.create_backup()
    except Exception as e:
        logging.error(f'Failed to create backup: {e}')

    # Restore a backup (provide the correct path to the backup file)
    # try:
    #     backup_manager.restore_backup('/backups/nginx-proxy-manager/nginx_proxy_manager_backup_YYYYMMDD_HHMMSS.tar.gz')
    # except Exception as e:
    #     logging.error(f'Failed to restore backup: {e}')
```
