"""
Generated Code Metadata:
========================
Original URL: https://whizzbridge.tech
Prompt: Write code to automate the migration of a website to Hostinger using FTP and the instructions provided on WhizzBridge.tech.
Generated: DETERMINISTIC_7b91b8dba170e8a7
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ftplib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FTPSiteMigrator:
    def __init__(self, host, username, password, local_directory, remote_directory):
        """
        Initialize the FTPSiteMigrator with FTP server details and directories.

        :param host: FTP server hostname or IP address
        :param username: FTP username
        :param password: FTP password
        :param local_directory: Local directory containing website files
        :param remote_directory: Remote directory on the FTP server
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_directory = local_directory
        self.remote_directory = remote_directory
        self.ftp = None

    def connect(self):
        """Establish a connection to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            logging.info("Connected to FTP server.")
        except ftplib.all_errors as e:
            logging.error(f"Failed to connect to FTP server: {e}")
            raise

    def upload_file(self, file_path):
        """Upload a single file to the FTP server.

        :param file_path: Path to the local file to upload
        """
        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {os.path.join(self.remote_directory, os.path.basename(file_path))}', file)
                logging.info(f"Uploaded: {file_path}")
        except Exception as e:
            logging.error(f"Failed to upload {file_path}: {e}")

    def upload_directory(self, directory):
        """Recursively upload a directory to the FTP server.

        :param directory: Path to the local directory to upload
        """
        for root, dirs, files in os.walk(directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                self.upload_file(local_file_path)

    def migrate(self):
        """Perform the migration of the website to the FTP server."""
        try:
            self.connect()
            self.upload_directory(self.local_directory)
            logging.info("Migration completed successfully.")
        finally:
            if self.ftp:
                self.ftp.quit()
                logging.info("Disconnected from FTP server.")

if __name__ == "__main__":
    # Configuration for the migration
    HOST = 'ftp.yourhostinger.com'  # Replace with your Hostinger FTP server
    USERNAME = 'your_username'       # Replace with your FTP username
    PASSWORD = 'your_password'       # Replace with your FTP password
    LOCAL_DIRECTORY = '/path/to/your/local/website'  # Replace with your local website path
    REMOTE_DIRECTORY = '/public_html'  # Replace with your desired remote directory

    # Create an instance of the migrator and start the migration
    migrator = FTPSiteMigrator(HOST, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    migrator.migrate()
```

Make sure to replace the placeholders in the configuration section with your actual FTP server details and local directory path before running the code.
