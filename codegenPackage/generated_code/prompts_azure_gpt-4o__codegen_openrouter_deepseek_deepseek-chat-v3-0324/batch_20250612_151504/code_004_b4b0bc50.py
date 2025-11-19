"""
Generated Code Metadata:
========================
Original URL: https://hodlit.rf.gd
Prompt: Write code to automate the transfer of a website from an existing hosting provider to a new hosting service, referencing the free transfer feature mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_b4b0bc5057d09733
Batch ID: 20250612_151504
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
import paramiko
import requests
from datetime import datetime
import logging
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('website_transfer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WebsiteTransfer:
    def __init__(self, source_host: str, source_user: str, source_password: str,
                 dest_host: str, dest_user: str, dest_password: str,
                 website_name: str, temp_dir: str = '/tmp/website_transfer'):
        """
        Initialize website transfer parameters.
        
        Args:
            source_host: Source hosting server address
            source_user: Source hosting SSH username
            source_password: Source hosting SSH password
            dest_host: Destination hosting server address
            dest_user: Destination hosting SSH username
            dest_password: Destination hosting SSH password
            website_name: Name of website to transfer
            temp_dir: Temporary directory for storing files during transfer
        """
        self.source_host = source_host
        self.source_user = source_user
        self.source_password = source_password
        self.dest_host = dest_host
        self.dest_user = dest_user
        self.dest_password = dest_password
        self.website_name = website_name
        self.temp_dir = temp_dir
        self.ssh_timeout = 30
        self.db_backup_file = f"{self.temp_dir}/{website_name}_db_backup.sql"
        
        # Create temp directory if it doesn't exist
        os.makedirs(self.temp_dir, exist_ok=True)

    def _execute_ssh_command(self, host: str, user: str, password: str, command: str) -> Tuple[bool, str]:
        """
        Execute a command over SSH.
        
        Args:
            host: Host to connect to
            user: SSH username
            password: SSH password
            command: Command to execute
            
        Returns:
            Tuple of (success, output)
        """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=user, password=password, timeout=self.ssh_timeout)
            
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            
            client.close()
            
            if error:
                return False, error
            return True, output
        except Exception as e:
            return False, str(e)

    def _transfer_files_via_sftp(self, src_host: str, src_user: str, src_password: str,
                                dest_host: str, dest_user: str, dest_password: str,
                                src_path: str, dest_path: str) -> bool:
        """
        Transfer files between hosts using SFTP.
        
        Args:
            src_host: Source host
            src_user: Source SSH username
            src_password: Source SSH password
            dest_host: Destination host
            dest_user: Destination SSH username
            dest_password: Destination SSH password
            src_path: Source path
            dest_path: Destination path
            
        Returns:
            True if transfer succeeded, False otherwise
        """
        try:
            # Download from source to local
            with paramiko.SSHClient() as ssh:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(src_host, username=src_user, password=src_password, timeout=self.ssh_timeout)
                sftp = ssh.open_sftp()
                
                # Check if source is file or directory
                try:
                    sftp.stat(src_path)
                    is_dir = False
                except IOError:
                    is_dir = True
                
                if is_dir:
                    self._download_directory(sftp, src_path, self.temp_dir)
                else:
                    local_path = os.path.join(self.temp_dir, os.path.basename(src_path))
                    sftp.get(src_path, local_path)
                sftp.close()
            
            # Upload from local to destination
            with paramiko.SSHClient() as ssh:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(dest_host, username=dest_user, password=dest_password, timeout=self.ssh_timeout)
                sftp = ssh.open_sftp()
                
                if is_dir:
                    self._upload_directory(sftp, os.path.join(self.temp_dir, os.path.basename(src_path)), dest_path)
                else:
                    local_path = os.path.join(self.temp_dir, os.path.basename(src_path))
                    sftp.put(local_path, os.path.join(dest_path, os.path.basename(src_path)))
                sftp.close()
            
            return True
        except Exception as e:
            logger.error(f"File transfer failed: {str(e)}")
            return False

    def _download_directory(self, sftp: paramiko.SFTPClient, remote_path: str, local_path: str):
        """Recursively download directory via SFTP."""
        os.makedirs(local_path, exist_ok=True)
        
        for item in sftp.listdir(remote_path):
            remote_item = os.path.join(remote_path, item)
            local_item = os.path.join(local_path, item)
            
            try:
                sftp.stat(remote_item)
                # It's a file
                sftp.get(remote_item, local_item)
            except IOError:
                # It's a directory
                self._download_directory(sftp, remote_item, local_item)

    def _upload_directory(self, sftp: paramiko.SFTPClient, local_path: str, remote_path: str):
        """Recursively upload directory via SFTP."""
        try:
            sftp.stat(remote_path)
        except IOError:
            sftp.mkdir(remote_path)
        
        for item in os.listdir(local_path):
            local_item = os.path.join(local_path, item)
            remote_item = os.path.join(remote_path, item)
            
            if os.path.isdir(local_item):
                self._upload_directory(sftp, local_item, remote_item)
            else:
                sftp.put(local_item, remote_item)

    def backup_database(self, db_name: str, db_user: str, db_password: str) -> bool:
        """
        Backup database from source host.
        
        Args:
            db_name: Database name
            db_user: Database username
            db_password: Database password
            
        Returns:
            True if backup succeeded, False otherwise
        """
        try:
            command = f"mysqldump -u {db_user} -p'{db_password}' {db_name} > {self.db_backup_file}"
            success, output = self._execute_ssh_command(
                self.source_host, self.source_user, self.source_password, command
            )
            
            if not success:
                logger.error(f"Database backup failed: {output}")
                return False
                
            return True
        except Exception as e:
            logger.error(f"Database backup failed: {str(e)}")
            return False

    def restore_database(self, db_name: str, db_user: str, db_password: str) -> bool:
        """
        Restore database to destination host.
        
        Args:
            db_name: Database name
            db_user: Database username
            db_password: Database password
            
        Returns:
            True if restore succeeded, False otherwise
        """
        try:
            # Transfer backup file to destination
            if not self._transfer_files_via_sftp(
                self.source_host, self.source_user, self.source_password,
                self.dest_host, self.dest_user, self.dest_password,
                self.db_backup_file, "/tmp"
            ):
                return False
                
            # Execute restore command
            remote_path = f"/tmp/{os.path.basename(self.db_backup_file)}"
            command = f"mysql -u {db_user} -p'{db_password}' {db_name} < {remote_path}"
            success, output = self._execute_ssh_command(
                self.dest_host, self.dest_user, self.dest_password, command
            )
            
            if not success:
                logger.error(f"Database restore failed: {output}")
                return False
                
            return True
        except Exception as e:
            logger.error(f"Database restore failed: {str(e)}")
            return False

    def transfer_website_files(self, source_path: str, dest_path: str) -> bool:
        """
        Transfer website files from source to destination.
        
        Args:
            source_path: Path to website files on source
            dest_path: Path to website files on destination
            
        Returns:
            True if transfer succeeded, False otherwise
        """
        try:
            return self._transfer_files_via_sftp(
                self.source_host, self.source_user, self.source_password,
                self.dest_host, self.dest_user, self.dest_password,
                source_path, dest_path
            )
        except Exception as e:
            logger.error(f"Website files transfer failed: {str(e)}")
            return False

    def request_free_transfer(self) -> bool:
        """
        Request
