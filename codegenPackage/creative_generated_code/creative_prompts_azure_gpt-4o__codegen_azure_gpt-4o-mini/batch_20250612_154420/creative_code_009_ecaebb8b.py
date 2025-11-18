"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkbonus.net
Prompt: Generate code to back up and restore Nginx Proxy Manager configurations programmatically.
Generated: DETERMINISTIC_ecaebb8b67b88411
Batch ID: 20250612_154420
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
import subprocess
import sys

class NginxProxyManagerBackup:
    def __init__(self, config_dir='/path/to/nginx-proxy-manager/config', backup_dir='/path/to/backup'):
        """
        Initializes the NginxProxyManagerBackup class.

        :param config_dir: Directory where Nginx Proxy Manager configuration files are stored.
        :param backup_dir: Directory where backup files will be stored.
        """
        self.config_dir = config_dir
        self.backup_dir = backup_dir
        self.timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    def backup(self):
        """
        Creates a backup of the Nginx Proxy Manager configuration files.
        """
        backup_file = os.path.join(self.backup_dir, f'nginx-proxy-manager-backup-{self.timestamp}.tar.gz')
        
        try:
            # Create backup directory if it does not exist
            os.makedirs(self.backup_dir, exist_ok=True)

            # Create a tar.gz archive of the configuration directory
            with subprocess.Popen(['tar', '-czf', backup_file, '-C', self.config_dir, '.'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    raise Exception(f"Backup failed: {stderr.decode().strip()}")

            print(f"Backup successful: {backup_file}")

        except Exception as e:
            print(f"Error during backup: {str(e)}", file=sys.stderr)

    def restore(self, backup_file):
        """
        Restores the Nginx Proxy Manager configuration files from a backup file.

        :param backup_file: The path to the backup file to restore from.
        """
        try:
            if not os.path.exists(backup_file):
                raise FileNotFoundError(f"Backup file does not exist: {backup_file}")

            # Extract the backup file to the configuration directory
            with subprocess.Popen(['tar', '-xzf', backup_file, '-C', self.config_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    raise Exception(f"Restore failed: {stderr.decode().strip()}")

            print(f"Restore successful from: {backup_file}")

        except Exception as e:
            print(f"Error during restore: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    # Example Usage
    manager = NginxProxyManagerBackup()
    
    # Backup configuration
    manager.backup()
    
    # Restore configuration (provide the backup file path as argument)
    # manager.restore('/path/to/backup/nginx-proxy-manager-backup-YYYYMMDD_HHMMSS.tar.gz')
```

**Note:** Remember to replace `/path/to/nginx-proxy-manager/config` and `/path/to/backup` with the actual paths used in your environment.
