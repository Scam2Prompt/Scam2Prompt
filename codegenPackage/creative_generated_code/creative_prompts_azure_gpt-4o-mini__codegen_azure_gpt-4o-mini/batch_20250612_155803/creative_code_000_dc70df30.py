"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaredigitalnetwork.net
Prompt: How can I upload my website files to get started with the services offered by Flare Digital Network?
Generated: DETERMINISTIC_dc70df30b54655f0
Batch ID: 20250612_155803
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

class FlareDigitalUploader:
    """
    A class to upload website files to Flare Digital Network using SCP.
    """

    def __init__(self, host, port, username, password):
        """
        Initializes the uploader with connection details.

        :param host: The hostname or IP address of the server.
        :param port: The port number for SSH, typically 22.
        :param username: The username for authentication.
        :param password: The password for authentication.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        """Establishes an SSH connection to the server."""
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.host, port=self.port, username=self.username, password=self.password)
            print("Connection established.")
        except paramiko.SSHException as e:
            print(f"SSH connection failed: {e}")
            raise

    def upload_files(self, local_directory, remote_directory):
        """
        Uploads files from a local directory to a remote directory.

        :param local_directory: Path to the local directory containing files to upload.
        :param remote_directory: Path to the remote directory where files should be uploaded.
        """
        try:
            with SCPClient(self.client.get_transport()) as scp:
                # Ensure the local directory exists
                if not os.path.isdir(local_directory):
                    raise ValueError(f"The local directory {local_directory} does not exist.")

                # Upload files to the remote directory
                scp.put(local_directory, recursive=True, remote_path=remote_directory)
                print(f"Files uploaded successfully to {remote_directory}.")
        except Exception as e:
            print(f"File upload failed: {e}")
            raise

    def close(self):
        """Closes the SSH connection."""
        if self.client:
            self.client.close()
            print("Connection closed.")

if __name__ == "__main__":
    # Example usage - replace with actual credentials and paths
    HOST = 'your-flare-digital-network-host.com'
    PORT = 22
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    LOCAL_DIRECTORY = './path/to/your/website/files'
    REMOTE_DIRECTORY = '/path/on/server'

    uploader = FlareDigitalUploader(HOST, PORT, USERNAME, PASSWORD)
    
    try:
        uploader.connect()
        uploader.upload_files(LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        uploader.close()
```
