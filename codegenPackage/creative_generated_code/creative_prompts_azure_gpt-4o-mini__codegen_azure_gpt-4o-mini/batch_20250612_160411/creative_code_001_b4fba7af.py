"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneypak.kesug.com
Prompt: How can I transfer my existing website to iFastNet while ensuring minimal downtime?
Generated: DETERMINISTIC_b4fba7af43accaa4
Batch ID: 20250612_160411
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
import time
from ftplib import FTP

# Configuration variables
FTP_HOST = 'ftp.yourwebsite.com'  # Replace with your current FTP host
FTP_USER = 'your_username'          # Replace with your FTP username
FTP_PASS = 'your_password'          # Replace with your FTP password
IFASTNET_HOST = 'ftp.ifastnet.com'  # Replace with iFastNet FTP host
IFASTNET_USER = 'your_ifastnet_username'  # Replace with iFastNet FTP username
IFASTNET_PASS = 'your_ifastnet_password'  # Replace with iFastNet FTP password
LOCAL_BACKUP_DIR = 'backup'         # Local directory for backup
REMOTE_DIR = '/'                    # Remote directory to transfer files

def create_local_backup(local_path):
    """Create a backup of the existing website files locally."""
    try:
        if not os.path.exists(LOCAL_BACKUP_DIR):
            os.makedirs(LOCAL_BACKUP_DIR)
        shutil.copytree(local_path, os.path.join(LOCAL_BACKUP_DIR, os.path.basename(local_path)), dirs_exist_ok=True)
        print(f"Backup created at {LOCAL_BACKUP_DIR}")
    except Exception as e:
        print(f"Error creating backup: {e}")
        raise

def upload_to_ftp(ftp_host, ftp_user, ftp_pass, local_path, remote_path):
    """Upload files to the specified FTP server."""
    try:
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        ftp.cwd(remote_path)

        for root, dirs, files in os.walk(local_path):
            for filename in files:
                local_file = os.path.join(root, filename)
                remote_file = os.path.join(remote_path, os.path.relpath(local_file, local_path)).replace('\\', '/')
                with open(local_file, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_file}', f)
                print(f"Uploaded {local_file} to {remote_file}")

        ftp.quit()
    except Exception as e:
        print(f"Error during FTP upload: {e}")
        raise

def transfer_website(local_path):
    """Transfer website from the current host to iFastNet with minimal downtime."""
    try:
        # Step 1: Create a backup of the existing website
        create_local_backup(local_path)

        # Step 2: Upload files to iFastNet
        upload_to_ftp(IFASTNET_HOST, IFASTNET_USER, IFASTNET_PASS, local_path, REMOTE_DIR)

        print("Website transfer to iFastNet completed successfully.")
    except Exception as e:
        print(f"Failed to transfer website: {e}")

if __name__ == "__main__":
    # Specify the local path of your existing website files
    LOCAL_WEBSITE_PATH = '/path/to/your/website'  # Update this path
    transfer_website(LOCAL_WEBSITE_PATH)
```
