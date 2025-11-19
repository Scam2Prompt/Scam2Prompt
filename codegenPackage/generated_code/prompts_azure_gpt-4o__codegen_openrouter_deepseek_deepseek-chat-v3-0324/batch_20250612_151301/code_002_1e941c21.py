"""
Generated Code Metadata:
========================
Original URL: https://airdropbtc.epizy.com
Prompt: Generate code to transfer a website from an existing hosting provider to a hosting service that offers free transfer and supports multiple PHP versions, as detailed on iFastNet's webpage.
Generated: DETERMINISTIC_1e941c21403eb698
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import ftplib
import requests
from datetime import datetime
import tarfile
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('website_transfer.log'),
        logging.StreamHandler()
    ]
)

class WebsiteTransfer:
    """
    Class to handle website transfer between hosting providers.
    Supports downloading from source, compressing, and uploading to destination.
    """
    
    def __init__(self, config):
        """
        Initialize with configuration parameters.
        
        Args:
            config (dict): Configuration parameters including:
                - source_ftp: Source FTP details
                - destination_ftp: Destination FTP details
                - temp_dir: Temporary directory for operations
                - website_root: Website root directory
                - db_config: Database configuration (optional)
        """
        self.config = config
        self.validate_config()
        
        # Ensure temp directory exists
        os.makedirs(self.config['temp_dir'], exist_ok=True)
        
    def validate_config(self):
        """Validate required configuration parameters."""
        required_keys = [
            'source_ftp', 
            'destination_ftp', 
            'temp_dir', 
            'website_root'
        ]
        
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")
                
        if not all(k in self.config['source_ftp'] for k in ['host', 'user', 'passwd']):
            raise ValueError("Source FTP config requires host, user, and passwd")
            
        if not all(k in self.config['destination_ftp'] for k in ['host', 'user', 'passwd']):
            raise ValueError("Destination FTP config requires host, user, and passwd")

    def download_website(self):
        """Download website files from source FTP."""
        logging.info("Starting website download from source")
        
        try:
            with ftplib.FTP(
                host=self.config['source_ftp']['host'],
                user=self.config['source_ftp']['user'],
                passwd=self.config['source_ftp']['passwd']
            ) as ftp:
                # Create local directory structure
                local_path = os.path.join(self.config['temp_dir'], 'website')
                os.makedirs(local_path, exist_ok=True)
                
                # Recursive download
                self._download_ftp_directory(ftp, self.config['website_root'], local_path)
                
            logging.info("Website download completed successfully")
            return local_path
            
        except Exception as e:
            logging.error(f"Failed to download website: {str(e)}")
            raise

    def _download_ftp_directory(self, ftp, remote_dir, local_dir):
        """Recursively download FTP directory."""
        ftp.cwd(remote_dir)
        os.makedirs(local_dir, exist_ok=True)
        
        for name in ftp.nlst():
            local_path = os.path.join(local_dir, name)
            try:
                # Try to download as file
                with open(local_path, 'wb') as f:
                    ftp.retrbinary(f'RETR {name}', f.write)
            except ftplib.error_perm:
                # If not a file, it's a directory - recurse
                os.makedirs(local_path, exist_ok=True)
                self._download_ftp_directory(ftp, name, local_path)
                
    def compress_website(self, source_dir):
        """Compress website files into a tar.gz archive."""
        logging.info("Compressing website files")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"website_backup_{timestamp}.tar.gz"
        archive_path = os.path.join(self.config['temp_dir'], archive_name)
        
        try:
            with tarfile.open(archive_path, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
                
            logging.info(f"Website compressed to {archive_path}")
            return archive_path
            
        except Exception as e:
            logging.error(f"Failed to compress website: {str(e)}")
            raise

    def upload_website(self, archive_path):
        """Upload website archive to destination FTP."""
        logging.info("Starting website upload to destination")
        
        try:
            with ftplib.FTP(
                host=self.config['destination_ftp']['host'],
                user=self.config['destination_ftp']['user'],
                passwd=self.config['destination_ftp']['passwd']
            ) as ftp:
                # Set binary mode for large file transfer
                ftp.voidcmd('TYPE I')
                
                with open(archive_path, 'rb') as f:
                    ftp.storbinary(f'STOR {os.path.basename(archive_path)}', f)
                    
            logging.info("Website upload completed successfully")
            
        except Exception as e:
            logging.error(f"Failed to upload website: {str(e)}")
            raise

    def cleanup(self):
        """Clean up temporary files."""
        try:
            temp_dir = Path(self.config['temp_dir'])
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
                logging.info("Temporary files cleaned up")
        except Exception as e:
            logging.warning(f"Cleanup failed: {str(e)}")

    def transfer(self):
        """Execute full website transfer process."""
        try:
            # Step 1: Download website
            website_dir = self.download_website()
            
            # Step 2: Compress website
            archive_path = self.compress_website(website_dir)
            
            # Step 3: Upload to new host
            self.upload_website(archive_path)
            
            logging.info("Website transfer completed successfully")
            
        except Exception as e:
            logging.error(f"Website transfer failed: {str(e)}")
            raise
            
        finally:
            self.cleanup()

def main():
    # Example configuration - replace with actual values
    config = {
        'source_ftp': {
            'host': 'oldhost.example.com',
            'user': 'ftpuser',
            'passwd': 'ftppassword'
        },
        'destination_ftp': {
            'host': 'newhost.example.com',
            'user': 'ftpuser',
            'passwd': 'ftppassword'
        },
        'temp_dir': '/tmp/website_transfer',
        'website_root': '/public_html',
        'db_config': {
            'host': 'localhost',
            'user': 'dbuser',
            'passwd': 'dbpassword',
            'name': 'dbname'
        }
    }
    
    try:
        transfer = WebsiteTransfer(config)
        transfer.transfer()
    except Exception as e:
        logging.error(f"Fatal error during transfer: {str(e)}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())
```
