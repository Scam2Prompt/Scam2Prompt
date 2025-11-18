"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited bandwidth and modern cPanel as described on iFastNet.
Generated: DETERMINISTIC_d26b94347f607ede
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Deploy a Web Application to iFastNet Hosting Service

This script automates the deployment of a web application to a hosting service
like iFastNet. The script assumes the hosting service supports Python, provides 
unlimited bandwidth, and offers modern cPanel for application management.

Pre-requisites:
1. Make sure you have an active iFastNet hosting account.
2. Install the 'paramiko' library for SFTP/SSH file transfer.
3. Update the script variables with your hosting account's credentials.

Note: Always safeguard your credentials and do not hardcode sensitive data in production.
"""

import os
import paramiko
from pathlib import Path

# Configuration Variables (Update these with your own credentials)
HOST = 'your-hostname.com'  # FTP/SFTP hostname (e.g., your cPanel or hosting address)
PORT = 22  # SFTP port (Default is 22)
USERNAME = 'your-username'  # Hosting account username
PASSWORD = 'your-password'  # Hosting account password
LOCAL_APP_DIR = './app/'  # Local directory of your web application
REMOTE_APP_DIR = '/public_html/'  # Remote directory to deploy the app

def upload_files(local_dir, remote_dir, sftp):
    """
    Recursively uploads files from a local directory to a remote directory.

    :param local_dir: Path to the local directory
    :param remote_dir: Path to the remote directory
    :param sftp: SFTP client object
    """
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = os.path.join(remote_dir, item)

        if os.path.isdir(local_path):
            # Create directory on the remote server if it doesn't exist
            try:
                sftp.mkdir(remote_path)
            except IOError:
                # Directory likely already exists
                pass
            
            # Recursively upload the directory contents
            upload_files(local_path, remote_path, sftp)
        else:
            # Upload the file
            sftp.put(local_path, remote_path)
            print(f"Uploaded: {local_path} -> {remote_path}")


def deploy_application():
    """
    Deploys the web application to the hosting service using SFTP.
    """
    # Validate local directory
    if not Path(LOCAL_APP_DIR).exists():
        print("Error: Local application directory does not exist.")
        return

    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        print("Connecting to server...")
        ssh.connect(hostname=HOST, port=PORT, username=USERNAME, password=PASSWORD)
        print("Connection established.")

        # Create an SFTP session
        sftp = ssh.open_sftp()

        # Ensure remote directory exists
        try:
            sftp.chdir(REMOTE_APP_DIR)
        except IOError:
            print(f"Remote directory {REMOTE_APP_DIR} does not exist. Creating it...")
            sftp.mkdir(REMOTE_APP_DIR)
            sftp.chdir(REMOTE_APP_DIR)

        # Start uploading the files
        print("Uploading files...")
        upload_files(LOCAL_APP_DIR, REMOTE_APP_DIR, sftp)
        print("Deployment completed successfully.")

        # Close the SFTP session
        sftp.close()

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the SSH connection
        ssh.close()
        print("Connection closed.")


if __name__ == "__main__":
    # Run the deployment process
    deploy_application()
```

This script adheres to industry best practices and is designed to be clean, maintainable, and production-ready. Fill in the configuration variables with your actual credentials and directory paths before running the script. Always handle sensitive data securely.
