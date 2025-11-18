"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Recommend tools or libraries for automating regular backups of FTP accounts on Endora.cz hosting services.
Generated: DETERMINISTIC_a2175add073ea2b9
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import os
import datetime
import logging
from pathlib import Path

# Configure logging for the backup process
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('ftp_backup.log'),
                              logging.StreamHandler()])

def create_backup_directory(base_path: str) -> str:
    """
    Create a backup directory with a timestamp.
    
    Args:
        base_path (str): The base path where backups will be stored.
    
    Returns:
        str: The path of the created backup directory.
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = os.path.join(base_path, f'ftp_backup_{timestamp}')
    os.makedirs(backup_dir, exist_ok=True)
    logging.info(f"Created backup directory: {backup_dir}")
    return backup_dir

def ftp_connect(host: str, username: str, password: str) -> ftplib.FTP:
    """
    Establish a connection to the FTP server.
    
    Args:
        host (str): The FTP server address.
        username (str): The FTP account username.
        password (str): The FTP account password.
    
    Returns:
        ftplib.FTP: The connected FTP object.
    
    Raises:
        ftplib.error_perm: If the login fails.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        logging.info(f"Connected to FTP server: {host}")
        return ftp
    except ftplib.error_perm as e:
        logging.error(f"FTP login failed: {e}")
        raise

def download_files(ftp: ftplib.FTP, remote_path: str, local_path: str):
    """
    Download files from the FTP server.

    Args:
        ftp (ftplib.FTP): The connected FTP object.
        remote_path (str): The path on the FTP server to download files from.
        local_path (str): The local path to save downloaded files.
    
    Raises:
        Exception: If an error occurs during file download.
    """
    try:
        # List files in the remote directory
        files = ftp.nlst(remote_path)
        for filename in files:
            local_file = os.path.join(local_path, os.path.basename(filename))
            with open(local_file, 'wb') as f:
                ftp.retrbinary(f'RETR {filename}', f.write)
                logging.info(f"Downloaded: {filename} to {local_file}")
    except Exception as e:
        logging.error(f"Failed to download files from {remote_path}: {e}")
        raise

def backup_ftp_account(host: str, username: str, password: str, remote_path: str, local_backup_dir: str):
    """
    Automate the backup of FTP account files.
    
    Args:
        host (str): The FTP server address.
        username (str): The FTP account username.
        password (str): The FTP account password.
        remote_path (str): The path on the FTP server to backup.
        local_backup_dir (str): The local directory to store backups.
    """
    backup_dir = create_backup_directory(local_backup_dir)
    
    with ftp_connect(host, username, password) as ftp:
        download_files(ftp, remote_path, backup_dir)

if __name__ == '__main__':
    # Define user credentials and paths
    HOST = 'ftp.endora.cz'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    REMOTE_PATH = '/path/to/ftp/files'
    LOCAL_BACKUP_DIR = '/path/to/local/backup/directory'
    
    try:
        backup_ftp_account(HOST, USERNAME, PASSWORD, REMOTE_PATH, LOCAL_BACKUP_DIR)
        logging.info("Backup completed successfully.")
    except Exception as e:
        logging.critical(f"Backup failed: {e}")
```

**Note:** Make sure to replace `'your_username'`, `'your_password'`, and the paths with your actual FTP credentials and desired paths.
