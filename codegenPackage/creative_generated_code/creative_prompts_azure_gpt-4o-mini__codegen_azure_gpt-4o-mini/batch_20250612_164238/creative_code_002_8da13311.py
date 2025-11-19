"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-webnode.rf.gd
Prompt: How can I transfer my existing website to iFastNet hosting while ensuring I maintain unlimited bandwidth and disk space?
Generated: DETERMINISTIC_8da133116cc5a799
Batch ID: 20250612_164238
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

class WebsiteTransfer:
    def __init__(self, local_directory, remote_directory, host, username, password):
        """
        Initializes the WebsiteTransfer class.
        
        :param local_directory: Local directory path of the website files.
        :param remote_directory: Remote directory path on the iFastNet server.
        :param host: The iFastNet server hostname or IP address.
        :param username: Username for SSH access.
        :param password: Password for SSH access.
        """
        self.local_directory = local_directory
        self.remote_directory = remote_directory
        self.host = host
        self.username = username
        self.password = password

    def connect_to_server(self):
        """
        Establish a connection to the remote server.
        
        :return: SSH client instance or None if connection fails.
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.username, password=self.password)
            return ssh
        except paramiko.SSHException as e:
            print(f"Failed to connect to {self.host}: {e}")
            return None

    def transfer_files(self):
        """
        Transfers files from the local directory to the remote directory.
        """
        ssh = self.connect_to_server()
        if not ssh:
            print("Connection to the server failed. Aborting transfer.")
            return

        sftp = ssh.open_sftp()
        try:
            # Ensure the remote directory exists
            try:
                sftp.stat(self.remote_directory)
            except FileNotFoundError:
                print(f"Remote directory {self.remote_directory} not found. Creating it.")
                sftp.mkdir(self.remote_directory)
            
            # Transfer files
            for root, dirs, files in os.walk(self.local_directory):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.join(self.remote_directory, os.path.relpath(local_file_path, self.local_directory))
                    
                    # Create remote directories if they do not exist
                    remote_dir = os.path.dirname(remote_file_path)
                    try:
                        sftp.stat(remote_dir)
                    except FileNotFoundError:
                        print(f"Creating remote directory: {remote_dir}")
                        sftp.mkdir(remote_dir)

                    print(f"Transferring {local_file_path} to {remote_file_path}")
                    sftp.put(local_file_path, remote_file_path)

        except Exception as e:
            print(f"An error occurred during file transfer: {e}")
        finally:
            sftp.close()
            ssh.close()

if __name__ == "__main__":
    # Set your parameters here
    local_directory = "/path/to/your/local/website"
    remote_directory = "/path/to/your/remote/website"
    host = "your_ifastnet_host"
    username = "your_ifastnet_username"
    password = "your_ifastnet_password"

    # Create an instance of WebsiteTransfer
    website_transfer = WebsiteTransfer(local_directory, remote_directory, host, username, password)
    
    # Start the file transfer
    website_transfer.transfer_files()
```

**Note**: Replace the placeholders in the `if __name__ == "__main__":` block with your actual paths and credentials. Always handle sensitive information like passwords securely and consider using environment variables or a secure vault.
