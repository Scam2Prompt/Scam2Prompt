"""
Generated Code Metadata:
========================
Original URL: https://web-promo.net
Prompt: Provide a step-by-step guide to automate backups for websites hosted on Xserver using Python.
Generated: DETERMINISTIC_055886c4e3eda20a
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import paramiko
import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class XServerBackup:
    def __init__(self, host, username, password, port=22):
        """
        Initialize XServerBackup object.

        Args:
            host (str): XServer host IP or hostname.
            username (str): XServer username.
            password (str): XServer password.
            port (int): XServer SSH port. Defaults to 22.
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect_to_server(self):
        """
        Establish SSH connection to XServer.

        Returns:
            bool: True if connection is successful, False otherwise.
        """
        try:
            self.ssh_client.connect(hostname=self.host, username=self.username, password=self.password, port=self.port)
            logging.info(f"Connected to {self.host} via SSH.")
            return True
        except paramiko.AuthenticationException:
            logging.error(f"Authentication failed for {self.host}.")
            return False
        except Exception as e:
            logging.error(f"Error connecting to {self.host}: {str(e)}")
            return False

    def get_website_directories(self):
        """
        Retrieve a list of website directories from XServer.

        Returns:
            list: List of website directories.
        """
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command("ls /var/www/")
            website_directories = stdout.read().decode().splitlines()
            logging.info(f"Retrieved website directories: {website_directories}")
            return website_directories
        except Exception as e:
            logging.error(f"Error retrieving website directories: {str(e)}")
            return []

    def create_backup(self, website_directory, backup_directory):
        """
        Create a backup of a website directory.

        Args:
            website_directory (str): Website directory to backup.
            backup_directory (str): Local backup directory.

        Returns:
            bool: True if backup is successful, False otherwise.
        """
        try:
            # Create local backup directory if it doesn't exist
            if not os.path.exists(backup_directory):
                os.makedirs(backup_directory)

            # Create backup filename
            backup_filename = f"{website_directory}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"

            # Create backup on XServer
            stdin, stdout, stderr = self.ssh_client.exec_command(f"tar -czf /tmp/{backup_filename} /var/www/{website_directory}")
            if stdout.channel.recv_exit_status() != 0:
                logging.error(f"Error creating backup for {website_directory}.")
                return False

            # Download backup from XServer
            self.ssh_client.open_sftp().get(f"/tmp/{backup_filename}", os.path.join(backup_directory, backup_filename))

            # Remove backup from XServer
            stdin, stdout, stderr = self.ssh_client.exec_command(f"rm /tmp/{backup_filename}")

            logging.info(f"Backup created for {website_directory}: {backup_filename}")
            return True
        except Exception as e:
            logging.error(f"Error creating backup for {website_directory}: {str(e)}")
            return False

    def close_connection(self):
        """
        Close SSH connection to XServer.
        """
        self.ssh_client.close()
        logging.info(f"Disconnected from {self.host}.")

def main():
    # XServer connection details
    host = "your-xserver-host"
    username = "your-xserver-username"
    password = "your-xserver-password"

    # Local backup directory
    backup_directory = "/path/to/local/backup/directory"

    # Create XServerBackup object
    xserver_backup = XServerBackup(host, username, password)

    # Connect to XServer
    if not xserver_backup.connect_to_server():
        return

    # Get website directories
    website_directories = xserver_backup.get_website_directories()

    # Create backups for each website directory
    for website_directory in website_directories:
        xserver_backup.create_backup(website_directory, backup_directory)

    # Close XServer connection
    xserver_backup.close_connection()

if __name__ == "__main__":
    main()
```
