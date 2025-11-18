"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspended-website.com
Prompt: Generate code to transfer a website from an existing hosting provider to iFastNet using cPanel tools.
Generated: DETERMINISTIC_70dec986f236e3df
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import paramiko
from ftplib import FTP
from datetime import datetime

# Configuration: Add your credentials and settings here
SOURCE_HOST = "source_host.com"
SOURCE_USERNAME = "source_username"
SOURCE_PASSWORD = "source_password"

DESTINATION_HOST = "ifastnet_host.com"
DESTINATION_USERNAME = "ifastnet_username"
DESTINATION_PASSWORD = "ifastnet_password"

LOCAL_BACKUP_DIR = "backup"  # Local directory to temporarily store backups
REMOTE_BACKUP_FILENAME = "website_backup.tar.gz"  # Backup file name

def create_local_backup_dir():
    """
    Ensure the local backup directory exists
    """
    if not os.path.exists(LOCAL_BACKUP_DIR):
        os.makedirs(LOCAL_BACKUP_DIR)

def download_backup_via_ftp(source_host, username, password, local_backup_path):
    """
    Download backup file from the source hosting provider via FTP.
    """
    try:
        ftp = FTP(source_host)
        ftp.login(user=username, passwd=password)

        # Switch to cPanel backup directory (may vary; adjust if needed)
        ftp.cwd("/backup_directory/")  
        
        # Download the backup file
        with open(local_backup_path, "wb") as file:
            ftp.retrbinary(f"RETR {REMOTE_BACKUP_FILENAME}", file.write)
        
        print(f"Backup downloaded successfully to {local_backup_path}")
        ftp.quit()
    except Exception as e:
        print(f"Error during FTP download: {e}")
        raise

def upload_backup_via_sftp(dest_host, username, password, local_backup_path):
    """
    Upload backup file to iFastNet via SFTP.
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(dest_host, username=username, password=password)

        sftp = ssh.open_sftp()

        # Define the destination path (iFastNet backup directory; adjust as needed)
        remote_backup_path = f"/home/{username}/backup/{REMOTE_BACKUP_FILENAME}"
        
        # Upload the file
        sftp.put(local_backup_path, remote_backup_path)
        print(f"Backup uploaded successfully to {remote_backup_path}")
        
        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"Error during SFTP upload: {e}")
        raise

def migrate_website():
    """
    Migrate the website from the source host to iFastNet.
    """
    try:
        create_local_backup_dir()
        local_backup_path = os.path.join(LOCAL_BACKUP_DIR, REMOTE_BACKUP_FILENAME)

        print("Downloading backup from source hosting provider...")
        download_backup_via_ftp(SOURCE_HOST, SOURCE_USERNAME, SOURCE_PASSWORD, local_backup_path)

        print("Uploading backup to iFastNet hosting provider...")
        upload_backup_via_sftp(DESTINATION_HOST, DESTINATION_USERNAME, DESTINATION_PASSWORD, local_backup_path)

        print("Website migration completed successfully.")
    except Exception as e:
        print(f"Error during migration process: {e}")

if __name__ == "__main__":
    print("Starting website migration...")
    migrate_website()
```

### Notes:
- This script assumes that the source hosting provider supports FTP access and the destination hosting provider (iFastNet) supports SFTP.
- Replace placeholders such as credentials and directories with actual values relevant to your hosting setup.
- Adjust paths like `/backup_directory/` and `/home/{username}/backup/` based on the hosting providers' configurations.
- Ensure `paramiko` is installed (`pip install paramiko`) before running the script.
