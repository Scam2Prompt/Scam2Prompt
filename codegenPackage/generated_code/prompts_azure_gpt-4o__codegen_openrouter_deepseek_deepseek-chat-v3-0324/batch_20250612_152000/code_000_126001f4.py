"""
Generated Code Metadata:
========================
Original URL: https://drutnet.in
Prompt: Write code to automate the migration of a website to Hostinger, referencing steps outlined in the "How can I migrate a website to Hostinger?" guide.
Generated: DETERMINISTIC_126001f4b530e2e6
Batch ID: 20250612_152000
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
import paramiko
import requests
import tarfile
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import subprocess
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='website_migration.log'
)
logger = logging.getLogger(__name__)

class WebsiteMigrator:
    def __init__(self, config):
        """
        Initialize the migrator with configuration settings.
        
        Args:
            config (dict): Configuration dictionary containing:
                - source_ftp: FTP source details
                - source_ssh: SSH source details
                - source_db: Database source details
                - hostinger_ftp: Hostinger FTP details
                - hostinger_db: Hostinger database details
                - temp_dir: Temporary directory for files
                - website_url: Website URL for verification
        """
        self.config = config
        self.validate_config()
        
    def validate_config(self):
        """Validate the configuration dictionary."""
        required_keys = [
            'source_ftp', 'source_ssh', 'source_db',
            'hostinger_ftp', 'hostinger_db',
            'temp_dir', 'website_url'
        ]
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")
                
        # Create temp directory if it doesn't exist
        os.makedirs(self.config['temp_dir'], exist_ok=True)
        
    def download_files_via_ftp(self):
        """Download website files via FTP from source."""
        try:
            ftp = ftplib.FTP(
                self.config['source_ftp']['host'],
                self.config['source_ftp']['user'],
                self.config['source_ftp']['password']
            )
            
            ftp.cwd(self.config['source_ftp']['remote_path'])
            
            local_path = os.path.join(self.config['temp_dir'], 'website_files')
            os.makedirs(local_path, exist_ok=True)
            
            files = ftp.nlst()
            for file in files:
                local_file = os.path.join(local_path, file)
                with open(local_file, 'wb') as f:
                    ftp.retrbinary(f'RETR {file}', f.write)
                logger.info(f"Downloaded file: {file}")
                
            ftp.quit()
            return local_path
            
        except Exception as e:
            logger.error(f"FTP download failed: {str(e)}")
            raise
            
    def download_files_via_ssh(self):
        """Download website files via SSH/SFTP from source."""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                self.config['source_ssh']['host'],
                username=self.config['source_ssh']['user'],
                password=self.config['source_ssh']['password'],
                port=self.config['source_ssh'].get('port', 22)
            )
            
            sftp = ssh.open_sftp()
            remote_path = self.config['source_ssh']['remote_path']
            local_path = os.path.join(self.config['temp_dir'], 'website_files')
            os.makedirs(local_path, exist_ok=True)
            
            for item in sftp.listdir(remote_path):
                remote_file = os.path.join(remote_path, item)
                local_file = os.path.join(local_path, item)
                sftp.get(remote_file, local_file)
                logger.info(f"Downloaded file via SSH: {item}")
                
            sftp.close()
            ssh.close()
            return local_path
            
        except Exception as e:
            logger.error(f"SSH download failed: {str(e)}")
            raise
            
    def export_database(self):
        """Export database from source."""
        try:
            connection = mysql.connector.connect(
                host=self.config['source_db']['host'],
                user=self.config['source_db']['user'],
                password=self.config['source_db']['password'],
                database=self.config['source_db']['name']
            )
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            dump_file = os.path.join(
                self.config['temp_dir'],
                f'database_dump_{timestamp}.sql'
            )
            
            with open(dump_file, 'w') as f:
                subprocess.run(
                    ['mysqldump',
                     f"--host={self.config['source_db']['host']}",
                     f"--user={self.config['source_db']['user']}",
                     f"--password={self.config['source_db']['password']}",
                     self.config['source_db']['name']],
                    stdout=f,
                    check=True
                )
                
            logger.info(f"Database exported to: {dump_file}")
            return dump_file
            
        except Error as e:
            logger.error(f"Database export failed: {str(e)}")
            raise
            
    def upload_files_to_hostinger(self, local_path):
        """Upload website files to Hostinger via FTP."""
        try:
            ftp = ftplib.FTP(
                self.config['hostinger_ftp']['host'],
                self.config['hostinger_ftp']['user'],
                self.config['hostinger_ftp']['password']
            )
            
            remote_path = self.config['hostinger_ftp']['remote_path']
            ftp.cwd(remote_path)
            
            for root, dirs, files in os.walk(local_path):
                for dir_name in dirs:
                    remote_dir = os.path.join(
                        remote_path,
                        os.path.relpath(os.path.join(root, dir_name), local_path)
                    )
                    try:
                        ftp.mkd(remote_dir)
                    except ftplib.error_perm:
                        pass  # Directory already exists
                        
                for file_name in files:
                    local_file = os.path.join(root, file_name)
                    remote_file = os.path.join(
                        remote_path,
                        os.path.relpath(local_file, local_path)
                    )
                    with open(local_file, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_file}', f)
                    logger.info(f"Uploaded file: {remote_file}")
                    
            ftp.quit()
            
        except Exception as e:
            logger.error(f"FTP upload to Hostinger failed: {str(e)}")
            raise
            
    def import_database_to_hostinger(self, dump_file):
        """Import database to Hostinger."""
        try:
            connection = mysql.connector.connect(
                host=self.config['hostinger_db']['host'],
                user=self.config['hostinger_db']['user'],
                password=self.config['hostinger_db']['password'],
                database=self.config['hostinger_db']['name']
            )
            
            cursor = connection.cursor()
            
            with open(dump_file, 'r') as f:
                sql_commands = f.read().split(';')
                
                for command in sql_commands:
                    if command.strip():
                        cursor.execute(command)
                        
            connection.commit()
            cursor.close()
            connection.close()
            logger.info("Database imported to Hostinger successfully")
            
        except Error as e:
            logger.error(f"Database import failed: {str(e)}")
            raise
            
    def verify_website(self):
        """Verify the website is accessible after migration."""
        try:
            response = requests.get(
                self.config['website_url'],
                timeout=10
            )
            if response.status_code == 200:
                logger.info("Website verification successful")
                return True
            else:
                logger.error(
                    f"Website verification failed. Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            logger.error(f"Website verification error: {str(e)}")
            return False
            
    def cleanup(self):
        """Clean up temporary files."""
        try:
            shutil.rmtree(self.config['temp_dir'])
            logger.info("Temporary files cleaned up")
        except Exception as e:
            logger.error(f"Cleanup failed: {str(e)}")
            
    def migrate(self):
        """Execute the full migration process."""
        try:
            logger.info("Starting website migration to Hostinger")
            
            # Step 1: Download website files
            if 'source_ftp' in self.config and self.config['source_ftp']:
                files_path = self.download_files_via_ftp()
            elif 'source_ssh' in self.config and self.config['source_ssh']:
                files_path = self.download_files_via_ssh()
            else:
                raise ValueError("No valid file transfer method configured")
                
            # Step 2: Export database
            dump_file = self.export_database()
            
            # Step 3: Upload files to Hostinger
            self.upload_files_to_hostinger(files_path)
            
            # Step 4: Import database to Hostinger
            self.import_database_to_hostinger(dump_file)
            
            # Step 5: Verify website
            if not self.verify_website():
                raise Exception("Website verification failed after migration")
                
            logger.info("Website migration completed successfully")
            
        except Exception as e:
            logger.error(f"Migration failed: {str(e)}")
            raise
        finally:
            self.cleanup()

# Example usage
if __name__ == "__main__":
    config =
