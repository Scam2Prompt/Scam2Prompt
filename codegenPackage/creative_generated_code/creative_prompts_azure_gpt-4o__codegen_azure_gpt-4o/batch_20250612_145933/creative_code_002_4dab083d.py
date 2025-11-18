"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arastrum.com
Prompt: Provide code examples for uploading website files to a hosting platform, specifically Hostinger, based on the instructions from Arastrum.
Generated: DETERMINISTIC_4dab083d01a43332
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from ftplib import FTP

# Configuration for Hostinger FTP upload
HOSTINGER_FTP_HOST = "ftp.yourwebsite.com"  # Replace with your Hostinger FTP host
FTP_USERNAME = "your_ftp_username"          # Replace with your FTP username
FTP_PASSWORD = "your_ftp_password"          # Replace with your FTP password
LOCAL_DIRECTORY = "./website_files"         # Local directory containing website files
REMOTE_DIRECTORY = "/"                      # Remote directory on the server to upload files

def upload_to_hostinger():
    """
    Upload files from a local directory to a Hostinger hosting platform via FTP.
    """
    try:
        # Establish FTP connection
        ftp = FTP(HOSTINGER_FTP_HOST)
        ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)
        ftp.cwd(REMOTE_DIRECTORY)  # Navigate to the remote directory
        
        # Walk through local directory to upload files
        for root, dirs, files in os.walk(LOCAL_DIRECTORY):
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.relpath(local_file_path, LOCAL_DIRECTORY).replace("\\", "/")
                
                # Upload file to the remote server
                with open(local_file_path, 'rb') as f:
                    ftp.storbinary(f"STOR {remote_file_path}", f)
                    print(f"Uploaded: {remote_file_path}")
        
        # Close FTP connection
        ftp.quit()
        print("All files uploaded successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    upload_to_hostinger()
```

```sh
# Note for user:
# 1. Ensure the `website_files` directory contains the files you want to upload.
# 2. Replace placeholders (FTP host, username, password) with your actual Hostinger account details.
# 3. Run the script in a Python 3 environment.
```
