"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-support.rf.gd
Prompt: Develop a tutorial on transferring an existing website to iFastNet, highlighting the unlimited disk space and bandwidth features.
Generated: DETERMINISTIC_f6b603362591ce3e
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tutorial Script: Transfer Existing Website to iFastNet Hosting
This script demonstrates a step-by-step process for transferring a website to iFastNet,
highlighting its unlimited disk space and bandwidth capabilities.

Requirements:
- Python >= 3.6
- External libraries: `paramiko` for SFTP transfer
"""

import paramiko
import os


class WebsiteTransfer:
    """
    A class to handle website file transfer to iFastNet hosting via SFTP.
    """

    def __init__(self, host, username, password, local_dir, remote_dir):
        """
        Initialize the WebsiteTransfer class.

        :param host: iFastNet server hostname (e.g., sftp.ifastnet.com)
        :param username: iFastNet account username
        :param password: iFastNet account password
        :param local_dir: Path to the local website directory
        :param remote_dir: Path to the remote directory on iFastNet
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_dir = local_dir
        self.remote_dir = remote_dir
        self.sftp = None

    def connect(self):
        """
        Establish connection to the iFastNet server.
        """
        try:
            # Create SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.username, password=self.password)

            # Start SFTP session
            self.sftp = ssh.open_sftp()
            print("Connected successfully to iFastNet server.")
        except Exception as e:
            print(f"Error connecting to iFastNet server: {str(e)}")
            raise

    def upload_directory(self):
        """
        Upload the entire local directory to the remote server.

        Handles both individual files and subdirectories.
        """
        try:
            # Ensure the remote directory exists
            self.ensure_remote_dir(self.remote_dir)

            # Walk through the local directory
            for root, dirs, files in os.walk(self.local_dir):
                # Calculate the relative path and target directory
                relative_path = os.path.relpath(root, self.local_dir)
                target_dir = os.path.join(self.remote_dir, relative_path)

                # Create remote subdirectory if it does not exist
                self.ensure_remote_dir(target_dir)

                # Upload files in the current directory
                for file in files:
                    local_file = os.path.join(root, file)
                    remote_file = os.path.join(target_dir, file)
                    self.sftp.put(local_file, remote_file)
                    print(f"Uploaded: {local_file} -> {remote_file}")
        except Exception as e:
            print(f"Error during upload: {str(e)}")
            raise

    def ensure_remote_dir(self, path):
        """
        Ensure that a remote directory exists, creating it if necessary.

        :param path: Remote directory path
        """
        try:
            self.sftp.listdir(path)  # Check if directory exists
        except FileNotFoundError:
            self.sftp.mkdir(path)  # Create directory if it does not exist
            print(f"Created remote directory: {path}")

    def disconnect(self):
        """
        Close the SFTP connection.
        """
        if self.sftp:
            self.sftp.close()
            print("Disconnected from iFastNet server.")


if __name__ == "__main__":
    # Replace the following placeholders with actual values
    HOST = "sftp.ifastnet.com"  # iFastNet SFTP host
    USERNAME = "your_username"  # iFastNet account username
    PASSWORD = "your_password"  # iFastNet account password
    LOCAL_DIR = "/path/to/your/local/website"  # Local website directory
    REMOTE_DIR = "/path/to/your/remote/directory"  # Remote directory on iFastNet

    # Initialize WebsiteTransfer
    transfer = WebsiteTransfer(HOST, USERNAME, PASSWORD, LOCAL_DIR, REMOTE_DIR)

    try:
        # Step 1: Connect to the server
        transfer.connect()

        # Step 2: Transfer the website files
        transfer.upload_directory()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Step 3: Disconnect from the server
        transfer.disconnect()
```
