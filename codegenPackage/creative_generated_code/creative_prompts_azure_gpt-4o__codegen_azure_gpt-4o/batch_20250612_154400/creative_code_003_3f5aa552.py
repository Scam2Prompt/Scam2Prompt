"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bncdgndkdfrjkxicebgmgjnguqfdgekftxkingptwqqeb.66ghz.com
Prompt: Write a script to automate the transfer of a website from an existing hosting provider to a hosting service offering free domain names and unlimited disk space, as advertised by iFastNet.
Generated: DETERMINISTIC_3f5aa552559acb38
Batch ID: 20250612_154400
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
import ftplib
import requests

# --- Configuration Section ---
# Replace these placeholders with actual values
OLD_HOST = "old_host.com"
OLD_HOST_USERNAME = "old_username"
OLD_HOST_PASSWORD = "old_password"
NEW_HOST = "ftp.ifastnet.com"
NEW_HOST_USERNAME = "new_username"
NEW_HOST_PASSWORD = "new_password"
LOCAL_BACKUP_DIR = "./website_backup"

# --- Helper Functions ---
def download_files_from_old_host(ftp_client, local_directory):
    """
    Recursively downloads all files and directories from the old host's FTP server.
    """
    os.makedirs(local_directory, exist_ok=True)
    for item in ftp_client.nlst():
        if is_file(ftp_client, item):
            local_path = os.path.join(local_directory, os.path.basename(item))
            with open(local_path, 'wb') as local_file:
                ftp_client.retrbinary(f"RETR {item}", local_file.write)
        else:
            new_local_dir = os.path.join(local_directory, os.path.basename(item))
            ftp_client.cwd(item)
            download_files_from_old_host(ftp_client, new_local_dir)
            ftp_client.cwd("..")

def is_file(ftp_client, item):
    """
    Checks if an FTP item is a file or directory.
    """
    try:
        ftp_client.size(item)
        return True
    except ftplib.error_perm:
        return False

def upload_files_to_new_host(ftp_client, local_directory):
    """
    Recursively uploads all files and directories to the new host's FTP server.
    """
    for item in os.listdir(local_directory):
        local_path = os.path.join(local_directory, item)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as local_file:
                ftp_client.storbinary(f"STOR {item}", local_file)
        else:
            ftp_client.mkd(item)
            ftp_client.cwd(item)
            upload_files_to_new_host(ftp_client, local_path)
            ftp_client.cwd("..")

# --- Execution Section ---
try:
    # Step 1: Connect to the old host and download the website files
    print("Connecting to old hosting provider...")
    old_host_ftp = ftplib.FTP(OLD_HOST, OLD_HOST_USERNAME, OLD_HOST_PASSWORD)
    print("Downloading website files from old host...")
    download_files_from_old_host(old_host_ftp, LOCAL_BACKUP_DIR)
    old_host_ftp.quit()
    print(f"Website files successfully downloaded to {LOCAL_BACKUP_DIR}.")

    # Step 2: Connect to the new host and upload the website files
    print("Connecting to new hosting provider...")
    new_host_ftp = ftplib.FTP(NEW_HOST, NEW_HOST_USERNAME, NEW_HOST_PASSWORD)
    print("Uploading website files to new host...")
    upload_files_to_new_host(new_host_ftp, LOCAL_BACKUP_DIR)
    new_host_ftp.quit()
    print("Website files successfully uploaded to new host.")

    print("Website transfer completed successfully.")

except ftplib.all_errors as e:
    print(f"FTP error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Clean up temporary local files
    if os.path.exists(LOCAL_BACKUP_DIR):
        shutil.rmtree(LOCAL_BACKUP_DIR)
        print(f"Temporary local backup directory {LOCAL_BACKUP_DIR} deleted.")
```
