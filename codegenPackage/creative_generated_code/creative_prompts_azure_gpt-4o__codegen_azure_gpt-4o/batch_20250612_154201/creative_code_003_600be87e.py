"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimeth.epizy.com
Prompt: Write a script to automate the transfer of a website from an existing hosting provider to a platform that supports free transfer and modern cPanel.
Generated: DETERMINISTIC_600be87ee13fce1e
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import ftplib
import paramiko
from datetime import datetime

# -----------------------------------------------
# Script to automate the transfer of a website 
# from an old hosting provider to a new hosting 
# provider that supports free transfer and modern cPanel.
# -----------------------------------------------

# Configuration for old hosting provider FTP
OLD_HOST = "ftp.oldprovider.com"
OLD_USERNAME = "old_user"
OLD_PASSWORD = "old_password"

# Configuration for new hosting provider SFTP
NEW_HOST = "sftp.newprovider.com"
NEW_USERNAME = "new_user"
NEW_PASSWORD = "new_password"
NEW_UPLOAD_DIR = "/public_html"  # Target directory on the new hosting platform

# Backup settings
BACKUP_DIR = "./backup"  # Local directory to store backup files temporarily

def download_website_from_old_provider():
    """
    Downloads all website files from the old hosting provider via FTP.
    """
    try:
        print("Connecting to old hosting provider via FTP...")
        ftp = ftplib.FTP(OLD_HOST)
        ftp.login(OLD_USERNAME, OLD_PASSWORD)
        
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        os.chdir(BACKUP_DIR)
        
        print("Downloading files from old hosting provider...")
        for item in ftp.nlst():  # List all files and directories
            if is_file(ftp, item):
                download_file(ftp, item)
            else:
                download_directory(ftp, item)
        ftp.quit()
        print("Download completed successfully.")
    except Exception as e:
        print(f"Error occurred while downloading website: {e}")
        raise

def is_file(ftp, item):
    """
    Determine if an item is a file or directory.
    """
    try:
        ftp.size(item)
        return True
    except ftplib.error_perm:
        return False

def download_file(ftp, filename):
    """
    Download a file from the FTP server.
    """
    try:
        with open(filename, "wb") as f:
            ftp.retrbinary(f"RETR {filename}", f.write)
        print(f"Downloaded file: {filename}")
    except Exception as e:
        print(f"Error occurred while downloading file {filename}: {e}")
        raise

def download_directory(ftp, directory):
    """
    Recursively download a directory from the FTP server.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)
        ftp.cwd(directory)
        
        for item in ftp.nlst():
            if is_file(ftp, item):
                download_file(ftp, item)
            else:
                download_directory(ftp, item)
        
        ftp.cwd("..")
        os.chdir("..")
    except Exception as e:
        print(f"Error occurred while downloading directory {directory}: {e}")
        raise

def upload_website_to_new_provider():
    """
    Uploads all website files to the new hosting provider via SFTP.
    """
    try:
        print("Connecting to new hosting provider via SFTP...")
        transport = paramiko.Transport((NEW_HOST, 22))
        transport.connect(username=NEW_USERNAME, password=NEW_PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)
        
        print("Uploading files to new hosting provider...")
        for root, dirs, files in os.walk(BACKUP_DIR):
            relative_path = os.path.relpath(root, BACKUP_DIR)
            target_path = os.path.join(NEW_UPLOAD_DIR, relative_path)
            create_remote_directory(sftp, target_path)
            
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(target_path, file)
                sftp.put(local_file, remote_file)
                print(f"Uploaded file: {remote_file}")
        
        sftp.close()
        transport.close()
        print("Upload completed successfully.")
    except Exception as e:
        print(f"Error occurred while uploading website: {e}")
        raise

def create_remote_directory(sftp, remote_directory):
    """
    Creates a remote directory if it doesn't exist.
    """
    try:
        sftp.stat(remote_directory)
    except FileNotFoundError:
        sftp.mkdir(remote_directory)
        print(f"Created remote directory: {remote_directory}")

def main():
    """
    Main function to handle the website transfer process.
    """
    try:
        print("Starting website transfer process...")
        download_website_from_old_provider()
        upload_website_to_new_provider()
        print("Website transfer process completed successfully.")
    except Exception as e:
        print(f"An error occurred during the transfer process: {e}")

if __name__ == "__main__":
    main()
```
