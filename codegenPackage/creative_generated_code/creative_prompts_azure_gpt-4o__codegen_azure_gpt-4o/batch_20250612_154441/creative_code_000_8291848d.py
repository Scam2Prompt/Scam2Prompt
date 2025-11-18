"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-protocol.42web.io
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, as described on the iFastNet hosting page.
Generated: DETERMINISTIC_8291848dde818b05
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Deploy a Web Application on iFastNet Hosting Service
This script uploads a web application directory to an iFastNet hosting service
via FTP. Ensure you have your FTP credentials and hosting details ready.
"""

import ftplib
import os
import sys

# Configuration Parameters
FTP_HOST = "ftp.yourdomain.com"  # Replace with your FTP host
FTP_USERNAME = "your_username"   # Replace with your FTP username
FTP_PASSWORD = "your_password"   # Replace with your FTP password
LOCAL_APP_DIR = "./web_app"      # Local directory of your web application
REMOTE_APP_DIR = "/public_html"  # Remote directory on the hosting service

def upload_file(ftp, local_file_path, remote_file_path):
    """
    Upload a single file to the FTP server.
    :param ftp: FTP connection object.
    :param local_file_path: Path to the local file.
    :param remote_file_path: Path to the remote file.
    """
    try:
        with open(local_file_path, 'rb') as file:
            ftp.storbinary(f"STOR {remote_file_path}", file)
        print(f"Uploaded: {local_file_path} -> {remote_file_path}")
    except Exception as e:
        print(f"Failed to upload {local_file_path}: {e}")

def upload_directory(ftp, local_dir, remote_dir):
    """
    Recursively upload a directory and its contents to the FTP server.
    :param ftp: FTP connection object.
    :param local_dir: Path to the local directory.
    :param remote_dir: Path to the remote directory.
    """
    try:
        # Try creating the remote directory
        ftp.mkd(remote_dir)
    except ftplib.error_perm:
        # Directory likely already exists
        pass
    
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = os.path.join(remote_dir, item)
        
        if os.path.isdir(local_path):
            # If item is a directory, call recursively
            upload_directory(ftp, local_path, remote_path)
        else:
            # If item is a file, upload it
            upload_file(ftp, local_path, remote_path)

def deploy_web_app():
    """
    Deploy the web application by uploading files and folders to the FTP server.
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USERNAME, FTP_PASSWORD)
        print("Connection established successfully.")
        
        # Upload the web application
        upload_directory(ftp, LOCAL_APP_DIR, REMOTE_APP_DIR)
        print("Web application deployed successfully.")
        
        # Close the connection
        ftp.quit()
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    print("Starting web application deployment...")
    deploy_web_app()
```
