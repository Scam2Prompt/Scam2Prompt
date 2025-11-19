"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Describe the steps to transfer an existing website to iFastNet hosting and provide a sample code for the migration process.
Generated: DETERMINISTIC_ab6c2e4d093ac710
Batch ID: 20250612_155544
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
from scp import SCPClient

class WebsiteMigration:
    def __init__(self, source_dir, destination_dir, hostname, username, password):
        """
        Initialize the WebsiteMigration class.

        :param source_dir: Local directory containing website files
        :param destination_dir: Destination directory on the server
        :param hostname: Hostname of the iFastNet server
        :param username: Username for server authentication
        :param password: Password for server authentication
        """
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.hostname = hostname
        self.username = username
        self.password = password
    
    def connect_to_server(self):
        """
        Establish SSH connection to the iFastNet server.

        :return: SSH client instance
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.hostname, username=self.username, password=self.password)
            print("Connection to server established successfully.")
            return ssh
        except paramiko.SSHException as e:
            print(f"Error connecting to the server: {e}")
            raise

    def upload_files(self):
        """
        Upload website files from local directory to the iFastNet server.
        """
        try:
            # Connect to the server
            ssh = self.connect_to_server()
            scp = SCPClient(ssh.get_transport())

            # Upload files
            for root, dirs, files in os.walk(self.source_dir):
                for file in files:
                    local_path = os.path.join(root, file)
                    remote_path = os.path.join(self.destination_dir, os.path.relpath(local_path, self.source_dir))
                    scp.put(local_path, remote_path)
                    print(f"Uploaded: {local_path} to {remote_path}")

            scp.close()
            ssh.close()
            print("File upload completed successfully.")
        except Exception as e:
            print(f"An error occurred during file upload: {e}")
            raise

    def migrate_website(self):
        """
        Execute the complete migration process.
        """
        print("Starting website migration...")
        self.upload_files()
        print("Website migration completed.")

if __name__ == "__main__":
    # Configuration
    SOURCE_DIRECTORY = "/path/to/local/website"
    DESTINATION_DIRECTORY = "/path/to/destination/on/server"
    HOSTNAME = "your_ifastnet_hostname"
    USERNAME = "your_ifastnet_username"
    PASSWORD = "your_ifastnet_password"

    # Create a migration instance and perform the migration
    migration = WebsiteMigration(SOURCE_DIRECTORY, DESTINATION_DIRECTORY, HOSTNAME, USERNAME, PASSWORD)
    migration.migrate_website()
```

Make sure to replace the placeholder values for `SOURCE_DIRECTORY`, `DESTINATION_DIRECTORY`, `HOSTNAME`, `USERNAME`, and `PASSWORD` with your actual values before running the code.
