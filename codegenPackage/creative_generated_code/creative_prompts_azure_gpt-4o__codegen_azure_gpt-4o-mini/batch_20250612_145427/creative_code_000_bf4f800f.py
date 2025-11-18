"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truflation-governance.com
Prompt: Write code to automate the migration of a website to Hostinger, referencing Hostinger's recommended process for uploading website files.
Generated: DETERMINISTIC_bf4f800fd8775a3e
Batch ID: 20250612_145427
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
import ftplib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HostingerMigration:
    def __init__(self, host, port, username, password, local_directory, remote_directory):
        """
        Initialize the migration class with Hostinger credentials and directories.
        
        :param host: Hostinger server hostname or IP address
        :param port: Port for FTP/SFTP (usually 21 for FTP, 22 for SFTP)
        :param username: Username for the Hostinger account
        :param password: Password for the Hostinger account
        :param local_directory: Path to the local website files
        :param remote_directory: Path on the Hostinger server to upload files
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.local_directory = local_directory
        self.remote_directory = remote_directory
        self.ftp = None

    def connect_ftp(self):
        """Establishes an FTP connection to the Hostinger server."""
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.host, self.port)
            self.ftp.login(self.username, self.password)
            logging.info("Connected to the FTP server successfully.")
        except ftplib.all_errors as e:
            logging.error(f"FTP connection failed: {e}")
            raise

    def upload_files(self):
        """Uploads all files from the local directory to the remote directory."""
        try:
            os.chdir(self.local_directory)
            for root, dirs, files in os.walk('.'):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.join(self.remote_directory, os.path.relpath(local_file_path, start='.'))
                    with open(local_file_path, 'rb') as f:
                        self.ftp.storbinary(f'STOR {remote_file_path}', f)
                        logging.info(f"Uploaded {local_file_path} to {remote_file_path}")
        except Exception as e:
            logging.error(f"Error uploading files: {e}")
            raise

    def close_connection(self):
        """Closes the FTP connection."""
        if self.ftp:
            self.ftp.quit()
            logging.info("FTP connection closed.")

    def migrate(self):
        """Main method to handle the migration process."""
        try:
            self.connect_ftp()
            self.upload_files()
        finally:
            self.close_connection()

if __name__ == "__main__":
    # Replace with your actual credentials and paths
    HOST = 'ftp.hostinger.com'
    PORT = 21
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    LOCAL_DIRECTORY = '/path/to/local/website/files'
    REMOTE_DIRECTORY = '/public_html/'

    migration = HostingerMigration(HOST, PORT, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    migration.migrate()
```
