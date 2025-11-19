"""
Generated Code Metadata:
========================
Original URL: https://web-promo.net
Prompt: Provide a step-by-step guide to automate backups for websites hosted on Xserver using Python.
Generated: DETERMINISTIC_055886c4e3eda20a
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import paramiko
import datetime
import tarfile
import logging
from logging.handlers import RotatingFileHandler

# Configuration
XSERVER_HOST = 'your_xserver_host'
XSERVER_PORT = 22
XSERVER_USERNAME = 'your_username'
XSERVER_PASSWORD = 'your_password'  # Consider using SSH keys instead
BACKUP_DIR = '/path/to/local/backup/directory'
REMOTE_WEB_ROOT = '/home/username/webroot'  # Adjust to your web root directory
LOG_FILE = '/path/to/backup.log'

# Setup logging
def setup_logging():
    logger = logging.getLogger('xserver_backup')
    logger.setLevel(logging.INFO)
    
    # Rotating file handler (5MB per file, max 5 backups)
    handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5*1024*1024, backupCount=5
    )
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logging()

def create_backup_directory():
    """Ensure local backup directory exists"""
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        logger.info(f"Backup directory ready at {BACKUP_DIR}")
    except Exception as e:
        logger.error(f"Failed to create backup directory: {str(e)}")
        raise

def connect_to_xserver():
    """Establish SSH connection to Xserver"""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=XSERVER_HOST,
            port=XSERVER_PORT,
            username=XSERVER_USERNAME,
            password=XSERVER_PASSWORD
        )
        logger.info("Successfully connected to Xserver")
        return client
    except Exception as e:
        logger.error(f"SSH connection failed: {str(e)}")
        raise

def create_remote_tarball(sftp, remote_path):
    """Create a tarball of the remote web directory"""
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    remote_backup_file = f"/tmp/web_backup_{timestamp}.tar.gz"
    
    try:
        # Create tar command
        tar_command = f"tar -czf {remote_backup_file} -C {remote_path} ."
        
        # Execute command
        stdin, stdout, stderr = sftp.client.exec_command(tar_command)
        exit_status = stdout.channel.recv_exit_status()
        
        if exit_status != 0:
            error = stderr.read().decode('utf-8')
            raise Exception(f"Tar command failed: {error}")
            
        logger.info(f"Created remote tarball: {remote_backup_file}")
        return remote_backup_file
    except Exception as e:
        logger.error(f"Failed to create remote tarball: {str(e)}")
        raise

def download_backup_file(sftp, remote_file):
    """Download the backup file from Xserver"""
    local_file = os.path.join(BACKUP_DIR, os.path.basename(remote_file))
    
    try:
        sftp.get(remote_file, local_file)
        logger.info(f"Downloaded backup to: {local_file}")
        return local_file
    except Exception as e:
        logger.error(f"Failed to download backup file: {str(e)}")
        raise

def cleanup_remote_file(sftp, remote_file):
    """Remove the temporary backup file from Xserver"""
    try:
        sftp.remove(remote_file)
        logger.info(f"Cleaned up remote file: {remote_file}")
    except Exception as e:
        logger.error(f"Failed to cleanup remote file: {str(e)}")
        # Non-critical error, continue execution

def verify_backup_file(local_file):
    """Verify the integrity of the downloaded backup file"""
    try:
        with tarfile.open(local_file, 'r:gz') as tar:
            # Just test if the file can be opened
            pass
        logger.info(f"Backup file verified: {local_file}")
        return True
    except Exception as e:
        logger.error(f"Backup verification failed: {str(e)}")
        # Attempt to remove corrupted file
        try:
            os.remove(local_file)
            logger.info(f"Removed corrupted backup file: {local_file}")
        except:
            pass
        return False

def rotate_backups():
    """Rotate old backups, keeping only the last 5"""
    try:
        backup_files = sorted(
            [f for f in os.listdir(BACKUP_DIR) if f.startswith('web_backup_') and f.endswith('.tar.gz')],
            key=lambda x: os.path.getmtime(os.path.join(BACKUP_DIR, x))
        )
        
        # Keep last 5 backups
        for old_backup in backup_files[:-5]:
            old_path = os.path.join(BACKUP_DIR, old_backup)
            os.remove(old_path)
            logger.info(f"Rotated old backup: {old_path}")
    except Exception as e:
        logger.error(f"Backup rotation failed: {str(e)}")
        # Non-critical error, continue execution

def main():
    logger.info("Starting Xserver website backup process")
    
    try:
        # Prepare local environment
        create_backup_directory()
        
        # Connect to Xserver
        ssh_client = connect_to_xserver()
        sftp = ssh_client.open_sftp()
        
        try:
            # Create remote backup
            remote_backup = create_remote_tarball(sftp, REMOTE_WEB_ROOT)
            
            # Download backup
            local_backup = download_backup_file(sftp, remote_backup)
            
            # Verify backup
            if not verify_backup_file(local_backup):
                raise Exception("Backup verification failed")
                
            # Cleanup remote
            cleanup_remote_file(sftp, remote_backup)
            
            # Rotate old backups
            rotate_backups()
            
            logger.info("Backup completed successfully")
            return True
            
        finally:
            sftp.close()
            ssh_client.close()
            
    except Exception as e:
        logger.error(f"Backup process failed: {str(e)}")
        return False

if __name__ == "__main__":
    if not main():
        sys.exit(1)
```
