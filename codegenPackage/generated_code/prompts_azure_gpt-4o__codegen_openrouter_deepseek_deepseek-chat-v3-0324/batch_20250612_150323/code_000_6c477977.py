"""
Generated Code Metadata:
========================
Original URL: https://arbitriunm.cloud
Prompt: Write code to automate the migration of a website to Hostinger using FTP and provide steps for uploading files as described on the Hostinger platform.
Generated: DETERMINISTIC_6c477977e5b9d16f
Batch ID: 20250612_150323
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
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hostinger_migration.log'),
        logging.StreamHandler()
    ]
)

class HostingerMigrator:
    def __init__(self, host, username, password, local_dir, remote_dir='/'):
        """
        Initialize the Hostinger FTP migrator.
        
        Args:
            host (str): FTP host address
            username (str): FTP username
            password (str): FTP password
            local_dir (str): Local directory containing website files
            remote_dir (str): Remote directory on Hostinger (default: root)
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_dir = Path(local_dir)
        self.remote_dir = remote_dir
        self.ftp = None

    def connect(self):
        """Establish FTP connection to Hostinger."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            logging.info("Successfully connected to Hostinger FTP")
            
            # Change to remote directory if specified
            if self.remote_dir != '/':
                self.ftp.cwd(self.remote_dir)
                logging.info(f"Changed to remote directory: {self.remote_dir}")
                
            return True
        except ftplib.all_errors as e:
            logging.error(f"FTP connection error: {str(e)}")
            return False

    def upload_file(self, local_path, remote_path):
        """Upload a single file to Hostinger."""
        try:
            with open(local_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
            logging.info(f"Uploaded: {local_path} -> {remote_path}")
            return True
        except ftplib.all_errors as e:
            logging.error(f"Error uploading {local_path}: {str(e)}")
            return False
        except IOError as e:
            logging.error(f"File error {local_path}: {str(e)}")
            return False

    def create_remote_dir(self, dir_path):
        """Create a directory on Hostinger if it doesn't exist."""
        try:
            self.ftp.mkd(dir_path)
            logging.info(f"Created remote directory: {dir_path}")
            return True
        except ftplib.error_perm as e:
            if '550' in str(e):
                logging.debug(f"Directory already exists: {dir_path}")
                return True
            logging.error(f"Error creating directory {dir_path}: {str(e)}")
            return False

    def upload_directory(self, local_path=None, remote_path=''):
        """
        Recursively upload a directory to Hostinger.
        
        Args:
            local_path (Path): Local directory path (default: self.local_dir)
            remote_path (str): Remote directory path (default: '')
        """
        if local_path is None:
            local_path = self.local_dir

        try:
            for item in local_path.iterdir():
                item_remote_path = f"{remote_path}/{item.name}" if remote_path else item.name
                
                if item.is_file():
                    self.upload_file(item, item_remote_path)
                elif item.is_dir():
                    self.create_remote_dir(item_remote_path)
                    self.upload_directory(item, item_remote_path)
                    
        except Exception as e:
            logging.error(f"Error processing directory {local_path}: {str(e)}")

    def migrate(self):
        """Main method to perform the migration."""
        if not self.connect():
            return False

        try:
            logging.info(f"Starting migration from {self.local_dir} to {self.remote_dir}")
            self.upload_directory()
            logging.info("Migration completed successfully")
            return True
        except Exception as e:
            logging.error(f"Migration failed: {str(e)}")
            return False
        finally:
            if self.ftp:
                self.ftp.quit()
                logging.info("FTP connection closed")

if __name__ == "__main__":
    # Example usage
    migrator = HostingerMigrator(
        host='ftp.hostinger.com',
        username='your_username',
        password='your_password',
        local_dir='./website_files',
        remote_dir='/public_html'
    )
    
    if migrator.migrate():
        print("Website migration completed successfully!")
    else:
        print("Website migration failed. Check the log for details.")
```
