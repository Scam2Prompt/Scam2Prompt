"""
Generated Code Metadata:
========================
Original URL: https://bncdgndkdfrjkxicebgmgjnguqfdgekftxkingptwqqeb.66ghz.com
Prompt: Write a script to automate the transfer of a website from an existing hosting provider to a hosting service offering free domain names and unlimited disk space, as advertised by iFastNet.
Generated: DETERMINISTIC_3f5aa552559acb38
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# website_transfer.py

import os
import sys
import argparse
import paramiko
import ftplib
from getpass import getpass

# Define constants
IFASTNET_FTP_HOST = 'ftp.ifastnet.com'
IFASTNET_FTP_PORT = 21

def connect_to_ftp(host, port, username, password):
    """
    Establish a connection to the FTP server.

    Args:
        host (str): FTP host
        port (int): FTP port
        username (str): FTP username
        password (str): FTP password

    Returns:
        ftplib.FTP: FTP connection object
    """
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port)
        ftp.login(user=username, passwd=password)
        return ftp
    except ftplib.all_errors as e:
        print(f"FTP connection failed: {e}")
        sys.exit(1)

def upload_files_to_ftp(ftp, local_dir, remote_dir):
    """
    Upload files to the FTP server.

    Args:
        ftp (ftplib.FTP): FTP connection object
        local_dir (str): Local directory path
        remote_dir (str): Remote directory path
    """
    try:
        ftp.cwd(remote_dir)
    except ftplib.all_errors:
        ftp.mkd(remote_dir)
        ftp.cwd(remote_dir)

    for filename in os.listdir(local_dir):
        local_file_path = os.path.join(local_dir, filename)
        if os.path.isfile(local_file_path):
            with open(local_file_path, 'rb') as file:
                ftp.storbinary(f'STOR {filename}', file)

def transfer_website(existing_host, existing_username, existing_password, existing_port=22):
    """
    Transfer website from existing hosting provider to iFastNet.

    Args:
        existing_host (str): Existing hosting provider host
        existing_username (str): Existing hosting provider username
        existing_password (str): Existing hosting provider password
        existing_port (int): Existing hosting provider SSH port
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=existing_host, username=existing_username, password=existing_password, port=existing_port)

        sftp = ssh.open_sftp()
        remote_dir = '/path/to/remote/website'
        local_dir = '/path/to/local/website'

        # Get files from existing hosting provider
        files = sftp.listdir(remote_dir)

        # Create a local directory if it doesn't exist
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        # Download files from existing hosting provider
        for file in files:
            remote_file_path = os.path.join(remote_dir, file)
            local_file_path = os.path.join(local_dir, file)
            sftp.get(remote_file_path, local_file_path)

        ssh.close()

        # Connect to iFastNet FTP
        ifastnet_username = input("Enter iFastNet FTP username: ")
        ifastnet_password = getpass("Enter iFastNet FTP password: ")
        ftp = connect_to_ftp(IFASTNET_FTP_HOST, IFASTNET_FTP_PORT, ifastnet_username, ifastnet_password)

        # Upload files to iFastNet FTP
        upload_files_to_ftp(ftp, local_dir, '/public_html')

        ftp.quit()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transfer website to iFastNet')
    parser.add_argument('--existing-host', required=True, help='Existing hosting provider host')
    parser.add_argument('--existing-username', required=True, help='Existing hosting provider username')
    parser.add_argument('--existing-password', required=True, help='Existing hosting provider password')
    parser.add_argument('--existing-port', type=int, default=22, help='Existing hosting provider SSH port')

    args = parser.parse_args()

    transfer_website(args.existing_host, args.existing_username, args.existing_password, args.existing_port)
```
