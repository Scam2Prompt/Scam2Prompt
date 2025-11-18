"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneypak.kesug.com
Prompt: Generate a script to transfer a website from an existing hosting provider to iFastNet, ensuring compatibility with unlimited bandwidth and disk space.
Generated: DETERMINISTIC_d5d73c041b87dc1c
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script for transferring a website to iFastNet hosting using FTP. Note that this script assumes you have valid credentials for both your existing host and iFastNet hosting, and that both support FTP access.

```python
import ftplib
import os
import sys

# Function to connect to an FTP server
def connect_to_ftp(server, username, password):
    try:
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {server}")
        return ftp
    except ftplib.all_errors as e:
        print(f"Error connecting to FTP server: {server} - {e}")
        sys.exit(1)

# Function to download files from the source FTP server
def download_files(ftp, local_dir):
    try:
        os.makedirs(local_dir, exist_ok=True)
        ftp.cwd("/")  # Start from the root directory

        def recursive_download(current_dir):
            os.makedirs(os.path.join(local_dir, current_dir), exist_ok=True)
            ftp.cwd(current_dir)
            items = ftp.nlst()

            for item in items:
                if is_directory(ftp, item):
                    recursive_download(item)
                else:  # It's a file
                    local_file_path = os.path.join(local_dir, current_dir, item)
                    with open(local_file_path, "wb") as f:
                        ftp.retrbinary(f"RETR {item}", f.write)
                        print(f"Downloaded: {local_file_path}")

            ftp.cwd("..")  # Go back to the parent directory

        recursive_download("")
    except Exception as e:
        print(f"Error downloading files: {e}")
        sys.exit(1)

# Function to upload files to the destination FTP server
def upload_files(ftp, local_dir):
    try:
        ftp.cwd("/")  # Start from the root directory

        def recursive_upload(current_dir, remote_dir):
            ftp.cwd(remote_dir)
            for item in os.listdir(current_dir):
                local_path = os.path.join(current_dir, item)
                remote_path = os.path.join(remote_dir, item)

                if os.path.isdir(local_path):
                    try:
                        ftp.mkd(remote_path)
                    except ftplib.error_perm:
                        pass  # Directory already exists
                    recursive_upload(local_path, remote_path)
                else:  # It's a file
                    with open(local_path, "rb") as f:
                        ftp.storbinary(f"STOR {item}", f)
                        print(f"Uploaded: {remote_path}")

            ftp.cwd("..")  # Go back to the parent directory

        recursive_upload(local_dir, "/")
    except Exception as e:
        print(f"Error uploading files: {e}")
        sys.exit(1)

# Utility function to check if a path is a directory on an FTP server
def is_directory(ftp, name):
    try:
        ftp.cwd(name)
        ftp.cwd("..")
        return True
    except ftplib.error_perm:
        return False

# Main function for transferring the website
def transfer_website(source_ftp_server, source_username, source_password, dest_ftp_server, dest_username, dest_password, local_backup_dir):
    print("Connecting to the source FTP server...")
    source_ftp = connect_to_ftp(source_ftp_server, source_username, source_password)

    print("Downloading website files from the source server...")
    download_files(source_ftp, local_backup_dir)
    source_ftp.quit()

    print("Connecting to the destination FTP server (iFastNet)...")
    dest_ftp = connect_to_ftp(dest_ftp_server, dest_username, dest_password)

    print("Uploading website files to the destination server...")
    upload_files(dest_ftp, local_backup_dir)
    dest_ftp.quit()

    print("Website transfer completed successfully.")

# Entry point
if __name__ == "__main__":
    # Replace these values with your credentials and configuration
    SOURCE_FTP_SERVER = "source_host.com"
    SOURCE_USERNAME = "source_user"
    SOURCE_PASSWORD = "source_pass"
    DEST_FTP_SERVER = "ifastnet_host.com"
    DEST_USERNAME = "ifastnet_user"
    DEST_PASSWORD = "ifastnet_pass"
    LOCAL_BACKUP_DIR = "website_backup"

    transfer_website(SOURCE_FTP_SERVER, SOURCE_USERNAME, SOURCE_PASSWORD,
                     DEST_FTP_SERVER, DEST_USERNAME, DEST_PASSWORD,
                     LOCAL_BACKUP_DIR)
```

Make sure to replace the placeholder values (`source_host.com`, `source_user`, etc.) with actual credentials and server details. This script handles errors and the recursive transfer of files and directories, ensuring compatibility with iFastNet hosting's unlimited bandwidth and disk space.
