"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: How can I transfer my existing website to iFastNet Web Hosting, and what are the steps to set up a free SSL certificate?
Generated: DETERMINISTIC_2fa356669de76fe5
Batch ID: 20250622_212843
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
import subprocess
import requests
from pathlib import Path
import tarfile
import zipfile

class WebsiteMigrator:
    """
    A class to handle website migration to iFastNet Web Hosting and SSL setup.
    """
    
    def __init__(self, source_dir, temp_dir="/tmp/website_backup"):
        """
        Initialize the migrator with source directory and temporary backup location.
        
        Args:
            source_dir (str): Path to the website source files
            temp_dir (str): Temporary directory for backup (default: /tmp/website_backup)
        """
        self.source_dir = Path(source_dir)
        self.temp_dir = Path(temp_dir)
        self.backup_file = self.temp_dir / "website_backup.tar.gz"
        
    def validate_source(self):
        """
        Validate that the source directory exists and contains website files.
        
        Raises:
            FileNotFoundError: If source directory doesn't exist
            ValueError: If source directory doesn't contain index.html/php files
        """
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory {self.source_dir} not found")
            
        required_files = ['index.html', 'index.php']
        if not any((self.source_dir / f).exists() for f in required_files):
            raise ValueError("Source directory doesn't contain required index files")
    
    def create_backup(self):
        """
        Create a compressed backup of the website files.
        
        Returns:
            str: Path to the created backup file
        """
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        
        with tarfile.open(self.backup_file, "w:gz") as tar:
            tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))
            
        return str(self.backup_file)
    
    def transfer_files(self, ftp_host, ftp_user, ftp_pass, remote_path="/public_html"):
        """
        Transfer website files to iFastNet hosting via FTP.
        
        Args:
            ftp_host (str): FTP hostname
            ftp_user (str): FTP username
            ftp_pass (str): FTP password
            remote_path (str): Remote path to upload to (default: /public_html)
        """
        try:
            import ftplib
            with ftplib.FTP(ftp_host) as ftp:
                ftp.login(user=ftp_user, passwd=ftp_pass)
                ftp.cwd(remote_path)
                
                for root, dirs, files in os.walk(self.source_dir):
                    for dirname in dirs:
                        remote_dir = os.path.join(root, dirname).replace(str(self.source_dir), '')
                        ftp.mkd(remote_dir)
                    
                    for filename in files:
                        local_path = os.path.join(root, filename)
                        remote_path = os.path.join(root, filename).replace(str(self.source_dir), '')
                        with open(local_path, 'rb') as f:
                            ftp.storbinary(f'STOR {remote_path}', f)
        except Exception as e:
            raise Exception(f"FTP transfer failed: {str(e)}")
    
    def setup_free_ssl(self, domain, email):
        """
        Set up free SSL certificate using Let's Encrypt via cPanel API.
        
        Args:
            domain (str): Domain name for SSL certificate
            email (str): Email for Let's Encrypt registration
        """
        try:
            # This would typically be done via cPanel API or SSH access
            # The following is a simplified example
            certbot_cmd = [
                "certbot",
                "certonly",
                "--webroot",
                "-w", str(self.source_dir),
                "-d", domain,
                "--email", email,
                "--agree-tos",
                "--non-interactive"
            ]
            
            result = subprocess.run(certbot_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"SSL setup failed: {result.stderr}")
                
            print(f"SSL certificate successfully installed for {domain}")
        except Exception as e:
            raise Exception(f"SSL setup error: {str(e)}")

    def cleanup(self):
        """Clean up temporary files."""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

def main():
    try:
        # Example usage
        migrator = WebsiteMigrator("/path/to/website")
        migrator.validate_source()
        backup_path = migrator.create_backup()
        print(f"Backup created at: {backup_path}")
        
        # Transfer files (replace with actual credentials)
        migrator.transfer_files(
            ftp_host="ftp.yourdomain.com",
            ftp_user="your_username",
            ftp_pass="your_password"
        )
        
        # Setup SSL (replace with actual domain and email)
        migrator.setup_free_ssl(
            domain="yourdomain.com",
            email="your@email.com"
        )
        
    except Exception as e:
        print(f"Migration failed: {str(e)}")
    finally:
        migrator.cleanup()

if __name__ == "__main__":
    main()
```
