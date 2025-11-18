"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://365cash.us
Prompt: Generate a script to upload website files to a hosting server, ensuring compatibility with Hostinger's file management system.
Generated: DETERMINISTIC_979665f08f9ca565
Batch ID: 20250612_154215
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
from stat import S_ISDIR

class SFTPUploader:
    """
    A class to handle the upload of files to a remote server using SFTP.
    """

    def __init__(self, hostname, port, username, password):
        """
        Initialize the SFTPUploader with server details.

        :param hostname: The hostname or IP address of the server.
        :param port: The port number for the SFTP connection.
        :param username: The username for authentication.
        :param password: The password for authentication.
        """
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.sftp = None

    def connect(self):
        """Establish an SFTP connection to the server."""
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname, self.port, self.username, self.password)
            self.sftp = self.client.open_sftp()
        except Exception as e:
            print(f"Failed to connect to {self.hostname}:{self.port} - {e}")
            raise

    def upload_directory(self, local_path, remote_path):
        """
        Upload a directory and its contents to the remote server.

        :param local_path: The local directory path to upload.
        :param remote_path: The remote directory path to upload to.
        """
        try:
            # Create remote directory if it does not exist
            self.sftp.mkdir(remote_path)
        except IOError:
            # Ignore error if directory already exists
            pass

        # Iterate through the local directory
        for item in os.listdir(local_path):
            local_item_path = os.path.join(local_path, item)
            remote_item_path = os.path.join(remote_path, item)

            if os.path.isdir(local_item_path):
                # Recursively upload the directory
                self.upload_directory(local_item_path, remote_item_path)
            else:
                # Upload the file
                self.upload_file(local_item_path, remote_item_path)

    def upload_file(self, local_file_path, remote_file_path):
        """
        Upload a single file to the remote server.

        :param local_file_path: The local file path to upload.
        :param remote_file_path: The destination path on the remote server.
        """
        try:
            self.sftp.put(local_file_path, remote_file_path)
            print(f"Uploaded {local_file_path} to {remote_file_path}")
        except Exception as e:
            print(f"Failed to upload {local_file_path} - {e}")

    def close(self):
        """Close the SFTP connection."""
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

def main():
    # Configuration for the SFTP connection
    HOSTNAME = "your_hostinger_hostname"  # Replace with your Hostinger hostname
    PORT = 22  # Default SFTP port
    USERNAME = "your_username"  # Replace with your username
    PASSWORD = "your_password"  # Replace with your password

    # Local and remote paths
    LOCAL_PATH = "/path/to/your/local/website/files"  # Replace with your local path
    REMOTE_PATH = "/path/to/your/remote/website/directory"  # Replace with your remote path

    uploader = SFTPUploader(HOSTNAME, PORT, USERNAME, PASSWORD)

    try:
        uploader.connect()
        uploader.upload_directory(LOCAL_PATH, REMOTE_PATH)
    finally:
        uploader.close()

if __name__ == "__main__":
    main()
```
