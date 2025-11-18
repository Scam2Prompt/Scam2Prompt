"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whizzbridge.tech
Prompt: Write code to automate the migration of a website to Hostinger using FTP and the instructions provided on WhizzBridge.tech.
Generated: DETERMINISTIC_7b91b8dba170e8a7
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import ftplib
import logging

# Configure logging to capture the process
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FTPSiteMigrator:
    def __init__(self, host, username, password, local_directory, remote_directory):
        """
        Initialize the FTP migrator.

        :param host: FTP server address
        :param username: FTP username
        :param password: FTP password
        :param local_directory: Local directory containing website files
        :param remote_directory: Remote directory on the server to upload files
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_directory = local_directory
        self.remote_directory = remote_directory
        self.ftp = ftplib.FTP()

    def connect(self):
        """Connect to the FTP server."""
        try:
            logging.info(f"Connecting to FTP server {self.host}...")
            self.ftp.connect(self.host)
            self.ftp.login(self.username, self.password)
            logging.info("Successfully connected to the FTP server.")
        except ftplib.all_errors as e:
            logging.error(f"Failed to connect or login to FTP server: {e}")
            raise

    def upload_file(self, local_file, remote_file):
        """
        Upload a single file to the FTP server.

        :param local_file: Path to the local file
        :param remote_file: Path to the remote file
        """
        try:
            with open(local_file, 'rb') as f:
                logging.info(f"Uploading {local_file} to {remote_file}...")
                self.ftp.storbinary(f'STOR {remote_file}', f)
                logging.info(f"Successfully uploaded {local_file}.")
        except Exception as e:
            logging.error(f"Error uploading {local_file}: {e}")

    def upload_directory(self):
        """Upload all files and directories from the local directory to the remote directory."""
        try:
            os.chdir(self.local_directory)
            for dirpath, dirnames, filenames in os.walk('.'):
                remote_path = os.path.join(self.remote_directory, dirpath)
                
                # Create directory if it doesn't exist
                try:
                    self.ftp.mkd(remote_path)
                except ftplib.error_perm:
                    # Directory already exists
                    pass
                
                for filename in filenames:
                    local_file = os.path.join(dirpath, filename)
                    remote_file = os.path.join(remote_path, filename)
                    self.upload_file(local_file, remote_file)

            logging.info("All files uploaded successfully.")
        except Exception as e:
            logging.error(f"Error during directory upload: {e}")

    def disconnect(self):
        """Disconnect from the FTP server."""
        if self.ftp:
            self.ftp.quit()
            logging.info("Disconnected from the FTP server.")

def main():
    # Configuration variables (replace with your actual values)
    HOST = 'ftp.yourhostinger.com'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    LOCAL_DIRECTORY = 'path/to/your/local/website/files'
    REMOTE_DIRECTORY = '/public_html'

    migrator = FTPSiteMigrator(HOST, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)

    try:
        migrator.connect()
        migrator.upload_directory()
    finally:
        migrator.disconnect()

if __name__ == '__main__':
    main()
```
