"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.syncsitebuilder.xyz
Prompt: Write code to upload a website to a hosting service, referencing DreamHost's admin panel for configuration.
Generated: DETERMINISTIC_2007288da5b19a72
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import paramiko
from scp import SCPClient

# Configuration for DreamHost FTP/SFTP settings
DREAMHOST_FTP_HOST = 'your_ftp_host.dreamhost.com'  # Replace with your DreamHost FTP host
DREAMHOST_FTP_USERNAME = 'your_username'              # Replace with your DreamHost username
DREAMHOST_FTP_PASSWORD = 'your_password'              # Replace with your DreamHost password
REMOTE_DIRECTORY = '/path/to/your/website/'           # Replace with your remote directory on DreamHost

def create_ssh_client(host, user, password):
    """
    Create and return an SSH client connected to the specified host using the provided credentials.

    :param host: The hostname or IP address of the server
    :param user: The username for authentication
    :param password: The password for authentication
    :return: An instance of an SSH client
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=password)
        return ssh
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
        raise

def upload_files(ssh, local_directory, remote_directory):
    """
    Upload files from a local directory to a remote directory using SCP.

    :param ssh: An active SSH client
    :param local_directory: The local directory path containing files to upload
    :param remote_directory: The remote directory path to upload files to
    """
    try:
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_directory, remote_directory, recursive=True)
            print(f"Successfully uploaded files from {local_directory} to {remote_directory}")
    except Exception as e:
        print(f"Error during file upload: {e}")
        raise

def main():
    """
    Main function to upload the website to DreamHost.
    """
    local_directory = './my_website'  # Local directory containing website files
    
    # Check if local directory exists
    if not os.path.exists(local_directory):
        print(f"Local directory '{local_directory}' does not exist.")
        return

    try:
        # Create an SSH client
        ssh_client = create_ssh_client(DREAMHOST_FTP_HOST, DREAMHOST_FTP_USERNAME, DREAMHOST_FTP_PASSWORD)
        # Upload files to the remote directory
        upload_files(ssh_client, local_directory, REMOTE_DIRECTORY)
    finally:
        # Ensure the SSH connection is closed
        ssh_client.close()

if __name__ == '__main__':
    main()
```

### Notes:
- Ensure you replace placeholders (like `your_ftp_host`, `your_username`, etc.) with actual DreamHost credentials and paths.
- The `paramiko` and `scp` Python packages need to be installed to run this script. You can install them using `pip install paramiko scp`.
- The script uploads files from a specified local directory to a remote directory on DreamHost via SFTP.
- Proper error handling is included to ensure any issues during connection or file transfer are reported.
