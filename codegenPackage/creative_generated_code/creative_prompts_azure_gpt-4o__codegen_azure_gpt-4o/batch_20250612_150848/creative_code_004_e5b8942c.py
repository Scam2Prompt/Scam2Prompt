"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.epizy.com
Prompt: Create a script to transfer a website from an existing hosting provider to a service that offers free transfer, as described on the iFastNet hosting webpage.
Generated: DETERMINISTIC_e5b8942cea2da0ea
Batch ID: 20250612_150848
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
import requests
from ftplib import FTP

# Configuration settings for the transfer
OLD_HOSTING_DETAILS = {
    "ftp_server": "old-hosting-ftp.example.com",
    "ftp_user": "old_user",
    "ftp_password": "old_password",
    "remote_directory": "/public_html"
}

NEW_HOSTING_DETAILS = {
    "ftp_server": "new-hosting-ftp.ifastnet.com",
    "ftp_user": "new_user",
    "ftp_password": "new_password",
    "remote_directory": "/public_html"
}

LOCAL_BACKUP_DIRECTORY = "website_backup"

def download_website_from_old_host():
    """
    Downloads the website files from the old hosting provider using FTP.
    """
    try:
        print("Connecting to the old hosting FTP server...")
        ftp = FTP(OLD_HOSTING_DETAILS["ftp_server"])
        ftp.login(OLD_HOSTING_DETAILS["ftp_user"], OLD_HOSTING_DETAILS["ftp_password"])
        ftp.cwd(OLD_HOSTING_DETAILS["remote_directory"])
        
        # Ensure local backup directory exists
        if not os.path.exists(LOCAL_BACKUP_DIRECTORY):
            os.makedirs(LOCAL_BACKUP_DIRECTORY)
        
        # Download files recursively
        print("Downloading files from the old hosting provider...")
        def download_file(filename):
            local_path = os.path.join(LOCAL_BACKUP_DIRECTORY, filename)
            with open(local_path, "wb") as file:
                ftp.retrbinary(f"RETR {filename}", file.write)
        
        def traverse_directory(directory="/"):
            ftp.cwd(directory)
            items = ftp.nlst()
            for item in items:
                try:
                    ftp.cwd(item)  # If this succeeds, it's a directory
                    traverse_directory(item)
                    ftp.cwd("..")  # Go back up a level after processing
                except Exception:
                    download_file(item)  # If it's not a directory, download
                
        traverse_directory()
        ftp.quit()
        print("Download completed.")
    except Exception as e:
        print(f"Error while downloading files: {e}")

def upload_website_to_new_host():
    """
    Uploads the website files to the new hosting provider using FTP.
    """
    try:
        print("Connecting to the new hosting FTP server...")
        ftp = FTP(NEW_HOSTING_DETAILS["ftp_server"])
        ftp.login(NEW_HOSTING_DETAILS["ftp_user"], NEW_HOSTING_DETAILS["ftp_password"])
        ftp.cwd(NEW_HOSTING_DETAILS["remote_directory"])
        
        # Upload files recursively
        print("Uploading files to the new hosting provider...")
        def upload_file(filepath):
            with open(filepath, "rb") as file:
                filename = os.path.basename(filepath)
                ftp.storbinary(f"STOR {filename}", file)
        
        def traverse_and_upload(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    upload_file(os.path.join(root, file))
        
        traverse_and_upload(LOCAL_BACKUP_DIRECTORY)
        ftp.quit()
        print("Upload completed.")
    except Exception as e:
        print(f"Error while uploading files: {e}")

def main():
    """
    Main function to handle the transfer process from old hosting to new hosting.
    """
    print("Starting website transfer...")
    download_website_from_old_host()
    upload_website_to_new_host()
    print("Website transfer completed successfully.")

if __name__ == "__main__":
    main()
```
