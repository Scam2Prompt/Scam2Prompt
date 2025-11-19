"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daniprisma.co.id
Prompt: Write a script to automate the deployment of a website on DatautamaNet Hosting.
Generated: DETERMINISTIC_2226c2b4ccef92a7
Batch ID: 20250612_155638
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
import sys

class WebsiteDeployer:
    def __init__(self, host, username, password, local_directory, remote_directory):
        """
        Initializes the WebsiteDeployer with the necessary credentials and paths.
        
        :param host: The hostname or IP address of the DatautamaNet server.
        :param username: The username for SSH login.
        :param password: The password for SSH login.
        :param local_directory: The local directory containing the website files.
        :param remote_directory: The remote directory where the website will be uploaded.
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_directory = local_directory
        self.remote_directory = remote_directory

    def connect(self):
        """
        Establishes an SSH connection to the server.
        
        :return: An SSH client object.
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.username, password=self.password)
            return ssh
        except paramiko.SSHException as e:
            print(f"SSH connection failed: {e}")
            sys.exit(1)

    def upload_files(self, ssh):
        """
        Uploads files from the local directory to the remote directory.
        
        :param ssh: An SSH client object.
        """
        try:
            sftp = ssh.open_sftp()
            for root, dirs, files in os.walk(self.local_directory):
                for file in files:
                    local_path = os.path.join(root, file)
                    # Create remote path
                    remote_path = os.path.join(self.remote_directory, os.path.relpath(local_path, self.local_directory))
                    remote_dir = os.path.dirname(remote_path)

                    # Create remote directory if it doesn't exist
                    try:
                        sftp.mkdir(remote_dir)
                    except IOError:
                        # Directory may already exist
                        pass

                    # Upload file
                    sftp.put(local_path, remote_path)
                    print(f"Uploaded {local_path} to {remote_path}")

            sftp.close()
        except Exception as e:
            print(f"An error occurred while uploading files: {e}")

    def deploy(self):
        """
        Main method to handle the deployment process.
        """
        ssh = self.connect()
        self.upload_files(ssh)
        ssh.close()
        print("Deployment completed successfully.")

if __name__ == "__main__":
    # Replace these values with your DatautamaNet hosting details
    HOST = "your_host"
    USERNAME = "your_username"
    PASSWORD = "your_password"
    LOCAL_DIRECTORY = "/path/to/local/website"
    REMOTE_DIRECTORY = "/path/to/remote/website"

    deployer = WebsiteDeployer(HOST, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    deployer.deploy()
```

**Note**: This script requires the `paramiko` library for SSH file transfer. You can install it using `pip install paramiko`. Replace the placeholders for `HOST`, `USERNAME`, `PASSWORD`, `LOCAL_DIRECTORY`, and `REMOTE_DIRECTORY` with your actual hosting details before executing the script.
