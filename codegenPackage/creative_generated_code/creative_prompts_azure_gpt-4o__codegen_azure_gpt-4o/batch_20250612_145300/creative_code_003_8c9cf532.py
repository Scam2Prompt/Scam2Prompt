"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: Write code to securely back up the site root directory managed by aaPanel to a remote server.
Generated: DETERMINISTIC_8c9cf5329fa961f0
Batch ID: 20250612_145300
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
import paramiko
from datetime import datetime

# Configuration
SITE_ROOT = "/www/wwwroot"  # Path to the site root directory managed by aaPanel
BACKUP_DIR = "/backups"  # Local backup directory
REMOTE_SERVER = {
    "host": "your_remote_server.com",
    "port": 22,
    "username": "your_username",
    "password": "your_password",  # Use SSH key authentication instead for better security
    "remote_backup_dir": "/remote/backups",  # Remote directory to store backups
}

# Function to create a compressed backup of the site root
def create_backup():
    try:
        # Ensure the local backup directory exists
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        # Create a timestamped backup file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"site_backup_{timestamp}.tar.gz")

        # Compress the site root directory
        shutil.make_archive(backup_file[:-7], 'gztar', SITE_ROOT)

        return backup_file
    except Exception as e:
        raise RuntimeError(f"Failed to create backup: {e}")

# Function to upload the backup to a remote server
def upload_backup(backup_file):
    try:
        # Establish an SFTP connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            REMOTE_SERVER["host"],
            port=REMOTE_SERVER["port"],
            username=REMOTE_SERVER["username"],
            password=REMOTE_SERVER["password"],
        )

        sftp = ssh.open_sftp()

        # Ensure the remote backup directory exists
        try:
            sftp.stat(REMOTE_SERVER["remote_backup_dir"])
        except FileNotFoundError:
            sftp.mkdir(REMOTE_SERVER["remote_backup_dir"])

        # Upload the backup file
        remote_file_path = os.path.join(
            REMOTE_SERVER["remote_backup_dir"], os.path.basename(backup_file)
        )
        sftp.put(backup_file, remote_file_path)

        # Close the SFTP connection
        sftp.close()
        ssh.close()

        return remote_file_path
    except Exception as e:
        raise RuntimeError(f"Failed to upload backup: {e}")

if __name__ == "__main__":
    try:
        # Create a local backup
        print("Creating backup...")
        backup_file = create_backup()
        print(f"Backup created at {backup_file}")

        # Upload the backup to the remote server
        print("Uploading backup to remote server...")
        remote_path = upload_backup(backup_file)
        print(f"Backup successfully uploaded to {remote_path}")

    except Exception as error:
        print(f"Error: {error}")
```
