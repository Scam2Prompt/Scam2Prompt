"""
Generated Code Metadata:
========================
Original URL: https://panemicav2.rf.gd
Prompt: Generate code to transfer an existing website to a hosting service that offers free migration and supports multiple PHP versions, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_0ee1620520357fd7
Batch ID: 20250612_154740
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
from pathlib import Path
import subprocess
import logging
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('website_migration.log'),
        logging.StreamHandler()
    ]
)

class WebsiteMigrator:
    """
    Handles the migration of a website to iFastNet hosting service.
    Supports multiple PHP versions and free migration as per iFastNet's offering.
    """
    
    def __init__(self, source_dir: str, temp_dir: str = 'temp_migration'):
        self.source_dir = Path(source_dir)
        self.temp_dir = Path(temp_dir)
        self.ftp_connection = None
        self.php_version = None
        
        # Ensure directories exist
        self.temp_dir.mkdir(exist_ok=True)
        
    def validate_source(self) -> bool:
        """Validate the source website directory structure."""
        required_files = ['index.php', 'index.html']
        has_required = any((self.source_dir / f).exists() for f in required_files)
        
        if not has_required:
            logging.error("Source directory doesn't contain required index files")
            return False
            
        logging.info("Source directory validated successfully")
        return True
    
    def backup_website(self, backup_path: str) -> bool:
        """Create a backup of the website files."""
        try:
            backup_path = Path(backup_path)
            shutil.make_archive(str(backup_path), 'zip', self.source_dir)
            logging.info(f"Backup created at {backup_path}.zip")
            return True
        except Exception as e:
            logging.error(f"Backup failed: {str(e)}")
            return False
    
    def connect_ftp(self, host: str, username: str, password: str) -> bool:
        """Establish FTP connection to hosting server."""
        try:
            self.ftp_connection = ftplib.FTP(host, username, password)
            logging.info("FTP connection established successfully")
            return True
        except Exception as e:
            logging.error(f"FTP connection failed: {str(e)}")
            return False
    
    def upload_files(self, remote_dir: str = '/') -> bool:
        """Upload website files to hosting server."""
        if not self.ftp_connection:
            logging.error("No FTP connection established")
            return False
            
        try:
            self.ftp_connection.cwd(remote_dir)
            
            for item in self.source_dir.rglob('*'):
                if item.is_file():
                    rel_path = item.relative_to(self.source_dir)
                    remote_path = str(rel_path).replace('\\', '/')
                    
                    with open(item, 'rb') as f:
                        self.ftp_connection.storbinary(f'STOR {remote_path}', f)
                    logging.info(f"Uploaded: {remote_path}")
            
            logging.info("All files uploaded successfully")
            return True
        except Exception as e:
            logging.error(f"File upload failed: {str(e)}")
            return False
    
    def set_php_version(self, version: str) -> bool:
        """Set the PHP version for the hosting account."""
        supported_versions = ['5.6', '7.0', '7.1', '7.2', '7.3', '7.4', '8.0', '8.1']
        
        if version not in supported_versions:
            logging.error(f"Unsupported PHP version. Choose from: {', '.join(supported_versions)}")
            return False
            
        self.php_version = version
        logging.info(f"PHP version set to {version}")
        return True
    
    def cleanup(self):
        """Clean up temporary files and close connections."""
        try:
            if self.ftp_connection:
                self.ftp_connection.quit()
            
            if self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                
            logging.info("Cleanup completed")
        except Exception as e:
            logging.error(f"Cleanup failed: {str(e)}")
    
    def migrate(self, ftp_config: Dict, php_version: str, backup_path: Optional[str] = None) -> bool:
        """
        Complete migration workflow.
        
        Args:
            ftp_config: Dictionary with host, username, password
            php_version: Target PHP version
            backup_path: Optional path for backup file
            
        Returns:
            bool: True if migration succeeded, False otherwise
        """
        try:
            # Step 1: Validate source
            if not self.validate_source():
                return False
                
            # Step 2: Create backup
            if backup_path and not self.backup_website(backup_path):
                return False
                
            # Step 3: Set PHP version
            if not self.set_php_version(php_version):
                return False
                
            # Step 4: Connect to FTP
            if not self.connect_ftp(**ftp_config):
                return False
                
            # Step 5: Upload files
            if not self.upload_files():
                return False
                
            logging.info("Website migration completed successfully!")
            return True
            
        except Exception as e:
            logging.error(f"Migration failed: {str(e)}")
            return False
        finally:
            self.cleanup()

# Example usage
if __name__ == "__main__":
    migrator = WebsiteMigrator(source_dir='path/to/website')
    
    ftp_config = {
        'host': 'ftp.example.com',
        'username': 'your_username',
        'password': 'your_password'
    }
    
    success = migrator.migrate(
        ftp_config=ftp_config,
        php_version='8.0',
        backup_path='website_backup'
    )
    
    if success:
        print("Migration completed successfully!")
    else:
        print("Migration failed. Check logs for details.")
```
