"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiar.mx
Prompt: Generate a step-by-step Python script for uploading website files to a hosting platform, following the guidance provided on kiar.mx.
Generated: DETERMINISTIC_d6d8dedcd431fe24
Batch ID: 20250612_154646
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def create_ssh_client(server_ip, server_port, username, password):
    """
    Create an SSH client connection.

    :param server_ip: IP address of the server
    :param server_port: Port on which the server is listening
    :param username: Username for the server
    :param password: Password for the server
    :return: An SSH client instance
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, port=server_port, username=username, password=password)
        logging.info("SSH connection established.")
        return ssh
    except Exception as e:
        logging.error(f"Failed to connect to {server_ip}:{server_port}, Error: {e}")
        raise

def upload_files(ssh_client, local_path, remote_path):
    """
    Upload files from local path to remote path.

    :param ssh_client: An active SSH client instance
    :param local_path: Path to local files/folders to upload
    :param remote_path: Destination path on the server
    """
    try:
        with SCPClient(ssh_client.get_transport()) as scp:
            # Upload files
            scp.put(local_path, remote_path, recursive=True)
            logging.info(f"Files uploaded from {local_path} to {remote_path}.")
    except Exception as e:
        logging.error(f"Failed to upload files, Error: {e}")
        raise

def main():
    # Server details
    SERVER_IP = 'your_server_ip'  # Replace with your server IP
    SERVER_PORT = 22                # Replace with your server port, usually 22 for SSH
    USERNAME = 'your_username'      # Replace with your username
    PASSWORD = 'your_password'      # Replace with your password

    # File paths
    LOCAL_PATH = 'path/to/local/files'  # Replace with your local files path
    REMOTE_PATH = 'path/to/remote/destination'  # Replace with your destination path

    try:
        # Step 1: Create SSH client
        ssh_client = create_ssh_client(SERVER_IP, SERVER_PORT, USERNAME, PASSWORD)

        # Step 2: Upload files
        upload_files(ssh_client, LOCAL_PATH, REMOTE_PATH)

    finally:
        # Step 3: Close SSH connection
        if ssh_client:
            ssh_client.close()
            logging.info("SSH connection closed.")

if __name__ == "__main__":
    main()
```
