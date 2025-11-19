"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-nftclaim.free.nf
Prompt: Write a script to automate the transfer of an existing website to iFastNet Web Hosting.
Generated: DETERMINISTIC_f057a7312dabf921
Batch ID: 20250612_155401
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

class WebsiteTransfer:
    def __init__(self, host, username, password, local_dir, remote_dir):
        """
        Initialize the WebsiteTransfer class with necessary parameters.

        :param host: str - Hostname or IP address of the iFastNet server
        :param username: str - SSH username for the iFastNet server
        :param password: str - SSH password for the iFastNet server
        :param local_dir: str - Local directory containing the website files
        :param remote_dir: str - Remote directory on the server to upload files
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_dir = local_dir
        self.remote_dir = remote_dir

    def create_ssh_client(self):
        """
        Create an SSH client to connect to the server.

        :return: SSHClient - An instance of the SSHClient
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.username, password=self.password)
            return ssh
        except Exception as e:
            print(f"Error creating SSH client: {e}")
            raise

    def transfer_files(self):
        """
        Transfer files from the local directory to the remote directory on the server.
        """
        try:
            ssh = self.create_ssh_client()
            with SCPClient(ssh.get_transport()) as scp:
                # Check if the local directory exists
                if not os.path.exists(self.local_dir):
                    raise FileNotFoundError(f"Local directory {self.local_dir} does not exist.")

                # Upload files to the remote directory
                scp.put(self.local_dir + '/*', recursive=True, remote_path=self.remote_dir)
                print(f"Successfully transferred files from {self.local_dir} to {self.remote_dir}.")
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        except Exception as e:
            print(f"Error during file transfer: {e}")
        finally:
            ssh.close()

if __name__ == "__main__":
    # Define connection parameters and directories
    HOST = "your_ifastnet_host"
    USERNAME = "your_username"
    PASSWORD = "your_password"
    LOCAL_DIR = "/path/to/your/local/website"
    REMOTE_DIR = "/path/to/your/remote/website"

    # Create a WebsiteTransfer instance and start the transfer
    website_transfer = WebsiteTransfer(HOST, USERNAME, PASSWORD, LOCAL_DIR, REMOTE_DIR)
    website_transfer.transfer_files()
```
