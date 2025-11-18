"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumpromo.epizy.com
Prompt: Develop a script to automate the transfer of an existing website to a hosting provider that offers free and simple SSL, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_c1da0fcc9694deb1
Batch ID: 20250612_154226
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
import paramiko
from pathlib import Path

# Configuration variables
LOCAL_WEBSITE_DIR = Path('/path/to/local/website')
REMOTE_HOST = 'example.ifastnet.com'
REMOTE_PORT = 22
USERNAME = 'your_username'
PASSWORD = 'your_password'
REMOTE_WEBSITE_DIR = '/path/to/remote/website'

def transfer_website(local_dir, remote_host, remote_port, username, password, remote_dir):
    """
    Transfers the website files from the local directory to the remote server.

    :param local_dir: Path to the local website directory
    :param remote_host: The remote host address
    :param remote_port: The port to connect to the remote server
    :param username: Username for the remote server
    :param password: Password for the remote server
    :param remote_dir: Path to the remote website directory
    """
    try:
        # Initialize SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote server
        client.connect(remote_host, port=remote_port, username=username, password=password)
        sftp = client.open_sftp()

        # Create remote directory if it doesn't exist
        try:
            sftp.mkdir(remote_dir)
        except IOError:
            # Directory already exists, ignore the error
            pass

        # Transfer files
        for item in local_dir.iterdir():
            remote_file_path = Path(remote_dir) / item.name
            if item.is_dir():
                # Recursively upload directories
                transfer_website(item, remote_host, remote_port, username, password, remote_file_path)
            else:
                # Upload files
                print(f"Transferring file: {item} to {remote_file_path}")
                sftp.put(str(item), str(remote_file_path))

        # Close SFTP session and SSH client
        sftp.close()
        client.close()
        print("Transfer completed successfully.")

    except Exception as e:
        print(f"An error occurred during transfer: {e}")

if __name__ == '__main__':
    # Ensure the local website directory exists
    if not LOCAL_WEBSITE_DIR.is_dir():
        print(f"Local website directory does not exist: {LOCAL_WEBSITE_DIR}")
        exit(1)

    # Start the transfer process
    transfer_website(LOCAL_WEBSITE_DIR, REMOTE_HOST, REMOTE_PORT, USERNAME, PASSWORD, REMOTE_WEBSITE_DIR)
```
