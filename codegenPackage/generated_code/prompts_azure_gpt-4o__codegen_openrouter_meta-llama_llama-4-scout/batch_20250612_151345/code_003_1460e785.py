"""
Generated Code Metadata:
========================
Original URL: https://eth.fanclub.rocks
Prompt: Write a guide for transferring an existing website to a hosting service that offers free transfer, unlimited disk space, and modern cPanel, as described on iFastNet.
Generated: DETERMINISTIC_1460e78553d54950
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# website_transfer_guide.py

import os
import shutil
import ftplib
from getpass import getpass

def connect_to_ftp(host, username, password):
    """
    Establish a connection to the FTP server.

    Args:
        host (str): FTP host
        username (str): FTP username
        password (str): FTP password

    Returns:
        ftplib.FTP: FTP connection object
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        return ftp
    except ftplib.all_errors as e:
        print(f"Error connecting to FTP: {e}")
        return None

def transfer_website(ftp, local_dir, remote_dir):
    """
    Transfer the website files to the remote FTP server.

    Args:
        ftp (ftplib.FTP): FTP connection object
        local_dir (str): Local directory path
        remote_dir (str): Remote directory path
    """
    try:
        # Navigate to the remote directory
        ftp.cwd(remote_dir)

        # Transfer files
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_dir, os.path.relpath(local_file_path, local_dir))
                with open(local_file_path, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_file_path}', f)
        print("Website transferred successfully!")
    except ftplib.all_errors as e:
        print(f"Error transferring website: {e}")

def main():
    # iFastNet FTP details
    host = input("Enter FTP host: ")
    username = input("Enter FTP username: ")
    password = getpass("Enter FTP password: ")

    # Local website directory
    local_dir = input("Enter local website directory path: ")

    # Remote website directory
    remote_dir = input("Enter remote website directory path: ")

    # Establish FTP connection
    ftp = connect_to_ftp(host, username, password)
    if ftp:
        # Transfer website
        transfer_website(ftp, local_dir, remote_dir)
        # Close FTP connection
        ftp.quit()

if __name__ == "__main__":
    main()
```
