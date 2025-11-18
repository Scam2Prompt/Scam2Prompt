"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truflation-governance.com
Prompt: Write a Python script to interact with Hostinger's hosting environment and upload website files programmatically.
Generated: DETERMINISTIC_1061068ec58fd855
Batch ID: 20250612_145427
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
from pathlib import Path

class HostingerUploader:
    def __init__(self, hostname, port, username, password):
        """
        Initializes the HostingerUploader instance with connection details.
        
        :param hostname: The hostname or IP address of the Hostinger server.
        :param port: The port on which to connect (default is usually 22 for SSH).
        :param username: The SSH username for the Hostinger account.
        :param password: The SSH password for the Hostinger account.
        """
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.sftp_client = None
        self.ssh_client = None

    def connect(self):
        """Establishes an SSH connection to the Hostinger server."""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.hostname, port=self.port, username=self.username, password=self.password)
            self.sftp_client = SCPClient(self.ssh_client.get_transport())
            print("Connection established successfully.")
        except paramiko.SSHException as e:
            print(f"Failed to connect to {self.hostname}: {e}")
            raise

    def upload_files(self, local_path, remote_path):
        """
        Uploads files from the local directory to the specified remote directory.
        
        :param local_path: The local directory containing files to upload.
        :param remote_path: The remote directory where files will be uploaded.
        """
        try:
            if not Path(local_path).is_dir():
                raise ValueError(f"Local path '{local_path}' is not a valid directory.")
            
            self.sftp_client.put(local_path, remote_path, recursive=True)
            print(f"Files uploaded from '{local_path}' to '{remote_path}'.")
        except Exception as e:
            print(f"Error uploading files: {e}")
            raise

    def disconnect(self):
        """Closes the SSH connection."""
        if self.sftp_client:
            self.sftp_client.close()
        if self.ssh_client:
            self.ssh_client.close()
        print("Disconnected from the server.")

def main():
    # Connection details (should be securely managed, e.g., environment variables)
    HOSTNAME = 'your_hostinger_hostname'
    PORT = 22  # Default SSH port
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    
    # Create an instance of the uploader
    uploader = HostingerUploader(HOSTNAME, PORT, USERNAME, PASSWORD)

    try:
        uploader.connect()  # Establish connection
        local_directory = '/path/to/local/website/files'  # Local directory to upload
        remote_directory = '/path/to/remote/directory'  # Remote directory on Hostinger
        uploader.upload_files(local_directory, remote_directory)  # Upload files
    finally:
        uploader.disconnect()  # Ensure disconnection

if __name__ == "__main__":
    main()
```
