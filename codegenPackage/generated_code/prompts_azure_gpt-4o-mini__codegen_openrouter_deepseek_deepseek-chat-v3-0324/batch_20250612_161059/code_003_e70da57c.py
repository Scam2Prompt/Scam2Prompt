"""
Generated Code Metadata:
========================
Original URL: https://unisvvap.run
Prompt: What are the steps to add content to a newly created website on Ispmanager?
Generated: DETERMINISTIC_e70da57c626d4a49
Batch ID: 20250612_161059
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
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebsiteManager:
    def __init__(self, ftp_host, ftp_user, ftp_pass, website_root):
        """
        Initialize website manager with FTP credentials and website root directory.
        
        Args:
            ftp_host (str): FTP server hostname
            ftp_user (str): FTP username
            ftp_pass (str): FTP password
            website_root (str): Path to website root directory on server
        """
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass
        self.website_root = website_root
        
    def connect_ftp(self):
        """Establish FTP connection and return connection object."""
        try:
            ftp = ftplib.FTP(self.ftp_host)
            ftp.login(self.ftp_user, self.ftp_pass)
            ftp.cwd(self.website_root)
            logger.info("FTP connection established successfully")
            return ftp
        except ftplib.all_errors as e:
            logger.error(f"FTP connection failed: {e}")
            raise
            
    def upload_file(self, local_path, remote_path=None):
        """
        Upload a file to the website via FTP.
        
        Args:
            local_path (str): Path to local file
            remote_path (str, optional): Destination path on server. Defaults to basename of local_path.
        """
        if not remote_path:
            remote_path = os.path.basename(local_path)
            
        try:
            with self.connect_ftp() as ftp:
                with open(local_path, 'rb') as file:
                    ftp.storbinary(f'STOR {remote_path}', file)
                logger.info(f"Uploaded {local_path} to {remote_path}")
        except ftplib.all_errors as e:
            logger.error(f"File upload failed: {e}")
            raise
        except IOError as e:
            logger.error(f"Local file error: {e}")
            raise
            
    def upload_directory(self, local_dir, remote_dir=None):
        """
        Upload a directory recursively to the website via FTP.
        
        Args:
            local_dir (str): Path to local directory
            remote_dir (str, optional): Destination directory on server. Defaults to basename of local_dir.
        """
        if not remote_dir:
            remote_dir = os.path.basename(local_dir.rstrip('/'))
            
        try:
            with self.connect_ftp() as ftp:
                # Try to create remote directory
                try:
                    ftp.mkd(remote_dir)
                except ftplib.error_perm as e:
                    if not e.args[0].startswith('550'):
                        raise
                        
                ftp.cwd(remote_dir)
                
                for item in Path(local_dir).iterdir():
                    if item.is_file():
                        with open(item, 'rb') as file:
                            ftp.storbinary(f'STOR {item.name}', file)
                        logger.info(f"Uploaded {item.name}")
                    elif item.is_dir():
                        self.upload_directory(str(item), item.name)
                        
                ftp.cwd('..')
                
        except ftplib.all_errors as e:
            logger.error(f"Directory upload failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Error during directory upload: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Configuration - replace with your actual credentials
    FTP_HOST = 'your.ispmanager.server'
    FTP_USER = 'your_username'
    FTP_PASS = 'your_password'
    WEBSITE_ROOT = '/path/to/website/root'
    
    # Initialize website manager
    manager = WebsiteManager(FTP_HOST, FTP_USER, FTP_PASS, WEBSITE_ROOT)
    
    # Example: Upload a single file
    try:
        manager.upload_file('local_file.html')
    except Exception as e:
        logger.error(f"Failed to upload file: {e}")
    
    # Example: Upload an entire directory
    try:
        manager.upload_directory('local_website_folder')
    except Exception as e:
        logger.error(f"Failed to upload directory: {e}")
```
