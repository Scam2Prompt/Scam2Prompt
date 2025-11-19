"""
Generated Code Metadata:
========================
Original URL: https://suilbwei.rf.gd
Prompt: Generate code to transfer a website from an existing hosting provider to a new hosting service that offers free domain names and modern cPanel, as outlined on iFastNet's webpage.
Generated: DETERMINISTIC_4e24787ea4b7b073
Batch ID: 20250612_154938
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
import tarfile
import ftplib
import paramiko
import requests
from datetime import datetime
import logging

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
    def __init__(self, old_host_config, new_host_config):
        """
        Initialize with old and new hosting configurations.
        
        Args:
            old_host_config (dict): Configuration for old hosting provider
            new_host_config (dict): Configuration for new hosting provider (iFastNet)
        """
        self.old_host = old_host_config
        self.new_host = new_host_config
        self.backup_dir = "website_backup"
        self.temp_dir = "temp_transfer"
        
        # Validate configurations
        self._validate_configs()
        
    def _validate_configs(self):
        """Validate required configuration parameters."""
        required_old = ['host', 'username', 'password', 'type']
        required_new = ['host', 'username', 'password', 'cpanel_url']
        
        for param in required_old:
            if param not in self.old_host:
                raise ValueError(f"Missing required old host parameter: {param}")
                
        for param in required_new:
            if param not in self.new_host:
                raise ValueError(f"Missing required new host parameter: {param}")
    
    def _create_backup_dir(self):
        """Create backup directory if it doesn't exist."""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
            logging.info(f"Created backup directory: {self.backup_dir}")
    
    def _create_temp_dir(self):
        """Create temporary directory for transfer."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)
        logging.info(f"Created temporary directory: {self.temp_dir}")
    
    def _cleanup_temp_dir(self):
        """Clean up temporary directory."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            logging.info(f"Cleaned up temporary directory: {self.temp_dir}")
    
    def _download_via_ftp(self):
        """Download website files via FTP."""
        try:
            ftp = ftplib.FTP(self.old_host['host'])
            ftp.login(user=self.old_host['username'], passwd=self.old_host['password'])
            
            # Change to website root directory
            if 'remote_path' in self.old_host:
                ftp.cwd(self.old_host['remote_path'])
            
            # List and download files
            files = ftp.nlst()
            for file in files:
                local_path = os.path.join(self.temp_dir, file)
                with open(local_path, 'wb') as f:
                    ftp.retrbinary(f'RETR {file}', f.write)
                logging.info(f"Downloaded: {file}")
            
            ftp.quit()
            return True
        except Exception as e:
            logging.error(f"FTP download failed: {str(e)}")
            return False
    
    def _download_via_ssh(self):
        """Download website files via SSH/SFTP."""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                self.old_host['host'],
                username=self.old_host['username'],
                password=self.old_host['password']
            )
            
            sftp = ssh.open_sftp()
            
            # Change to website root directory
            remote_path = self.old_host.get('remote_path', '.')
            
            # Recursively download files
            for item in sftp.listdir(remote_path):
                remote_item = f"{remote_path}/{item}"
                local_item = os.path.join(self.temp_dir, item)
                
                try:
                    sftp.get(remote_item, local_item)
                    logging.info(f"Downloaded: {item}")
                except IOError:
                    # This is a directory, create it locally
                    os.makedirs(local_item, exist_ok=True)
                    self._download_sftp_dir(sftp, remote_item, local_item)
            
            sftp.close()
            ssh.close()
            return True
        except Exception as e:
            logging.error(f"SSH download failed: {str(e)}")
            return False
    
    def _download_sftp_dir(self, sftp, remote_path, local_path):
        """Recursively download directory via SFTP."""
        os.makedirs(local_path, exist_ok=True)
        for item in sftp.listdir(remote_path):
            remote_item = f"{remote_path}/{item}"
            local_item = os.path.join(local_path, item)
            
            try:
                sftp.get(remote_item, local_item)
                logging.info(f"Downloaded: {remote_item}")
            except IOError:
                # This is a directory, recurse
                os.makedirs(local_item, exist_ok=True)
                self._download_sftp_dir(sftp, remote_item, local_item)
    
    def _download_database(self):
        """Download database dump if configured."""
        if 'database' not in self.old_host:
            logging.info("No database configured for backup")
            return True
            
        db_config = self.old_host['database']
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dump_file = os.path.join(self.backup_dir, f"db_backup_{timestamp}.sql")
        
        try:
            command = [
                'mysqldump',
                '-h', db_config.get('host', 'localhost'),
                '-u', db_config['username'],
                f"-p{db_config['password']}",
                db_config['name'],
                '--result-file', dump_file
            ]
            
            if 'port' in db_config:
                command.extend(['-P', str(db_config['port'])])
            
            subprocess.run(command, check=True)
            logging.info(f"Database backup created: {dump_file}")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Database backup failed: {str(e)}")
            return False
    
    def _create_backup_archive(self):
        """Create compressed backup archive."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = os.path.join(self.backup_dir, f"website_backup_{timestamp}.tar.gz")
        
        try:
            with tarfile.open(archive_name, "w:gz") as tar:
                tar.add(self.temp_dir, arcname=os.path.basename(self.temp_dir))
            logging.info(f"Created backup archive: {archive_name}")
            return archive_name
        except Exception as e:
            logging.error(f"Archive creation failed: {str(e)}")
            return None
    
    def _upload_to_new_host(self, archive_path):
        """Upload files to new hosting provider."""
        try:
            # For iFastNet with cPanel, we'll use FTP upload
            ftp = ftplib.FTP(self.new_host['host'])
            ftp.login(user=self.new_host['username'], passwd=self.new_host['password'])
            
            # Change to website root directory
            if 'remote_path' in self.new_host:
                ftp.cwd(self.new_host['remote_path'])
            
            # Upload files recursively from temp directory
            for root, dirs, files in os.walk(self.temp_dir):
                for dir_name in dirs:
                    remote_dir = os.path.relpath(os.path.join(root, dir_name), self.temp_dir)
                    try:
                        ftp.mkd(remote_dir.replace('\\', '/'))
                    except ftplib.error_perm:
                        pass  # Directory likely already exists
                
                for file_name in files:
                    local_path = os.path.join(root, file_name)
                    remote_path = os.path.relpath(local_path, self.temp_dir).replace('\\', '/')
                    
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_path}', f)
                    logging.info(f"Uploaded: {remote_path}")
            
            ftp.quit()
            return True
        except Exception as e:
            logging.error(f"FTP upload failed: {str(e)}")
            return False
    
    def _import_database(self):
        """Import database to new hosting provider."""
        if 'database' not in self.new_host:
            logging.info("No database configured for import")
            return True
            
        db_config = self.new_host['database']
        dump_file = None
        
        # Find the latest database backup
        for file in os.listdir(self.backup_dir):
            if file.startswith("db_backup_") and file.endswith(".sql"):
                dump_file = os.path.join(self.backup_dir, file)
                break
        
        if not dump_file:
            logging.warning("No database dump found for import")
            return False
        
        try:
            command = [
                'mysql',
                '-h', db_config.get('host', 'localhost'),
                '-u',
