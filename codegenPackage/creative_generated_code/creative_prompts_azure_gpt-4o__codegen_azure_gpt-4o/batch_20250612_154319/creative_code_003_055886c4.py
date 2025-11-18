"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-promo.net
Prompt: Provide a step-by-step guide to automate backups for websites hosted on Xserver using Python.
Generated: DETERMINISTIC_055886c4e3eda20a
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import paramiko
import datetime
import tarfile
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configuration
XSERVER_HOST = "your-xserver-host.com"  # Replace with your Xserver host
USERNAME = "your-username"  # Replace with your Xserver username
PASSWORD = "your-password"  # Replace with your password
REMOTE_DIR = "/home/your-account/public_html/"  # Replace with your site root directory
LOCAL_BACKUP_DIR = "/path/to/local/backup/"  # Replace with your local backup directory
PORT = 22  # Default SSH port

# Ensure local backup directory exists
if not os.path.exists(LOCAL_BACKUP_DIR):
    os.makedirs(LOCAL_BACKUP_DIR)

def create_tarball(source_dir, output_filename):
    """
    Creates a tarball (.tar.gz) archive from the specified source directory.
    """
    try:
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        logging.info(f"Backup archive created: {output_filename}")
    except Exception as e:
        logging.error(f"Failed to create tarball: {e}")
        raise

def download_remote_files(ssh_client, remote_dir, local_dir):
    """
    Downloads all files and directories from a remote server to a local directory via SFTP.
    """
    try:
        sftp = ssh_client.open_sftp()
        for item in sftp.listdir(remote_dir):
            remote_path = os.path.join(remote_dir, item)
            local_path = os.path.join(local_dir, item)
            if is_remote_directory(sftp, remote_path):
                # Create local directory and recursively download contents
                os.makedirs(local_path, exist_ok=True)
                download_remote_files(ssh_client, remote_path, local_path)
            else:
                # Download file
                sftp.get(remote_path, local_path)
                logging.info(f"Downloaded: {remote_path} -> {local_path}")
        sftp.close()
    except Exception as e:
        logging.error(f"Failed to download files: {e}")
        raise

def is_remote_directory(sftp, path):
    """
    Determines if a remote path is a directory using SFTP.
    """
    try:
        return stat.S_ISDIR(sftp.stat(path).st_mode)
    except Exception:
        return False

def perform_backup():
    """
    Orchestrates the backup process for the website hosted on Xserver.
    """
    try:
        # Establish SSH connection
        logging.info("Connecting to Xserver...")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            XSERVER_HOST, port=PORT, username=USERNAME, password=PASSWORD
        )
        logging.info("SSH connection established.")

        # Create temporary local backup directory for downloaded files
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_backup_dir = os.path.join(LOCAL_BACKUP_DIR, f"temp_{timestamp}")
        os.makedirs(temp_backup_dir, exist_ok=True)

        # Download website files from remote server
        logging.info("Downloading website files...")
        download_remote_files(ssh_client, REMOTE_DIR, temp_backup_dir)

        # Create tarball archive of the downloaded files
        final_backup = os.path.join(LOCAL_BACKUP_DIR, f"backup_{timestamp}.tar.gz")
        create_tarball(temp_backup_dir, final_backup)

        # Cleanup temporary directory
        logging.info("Cleaning up temporary files...")
        for root, dirs, files in os.walk(temp_backup_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_backup_dir)

        logging.info("Backup completed successfully.")
    except Exception as e:
        logging.error(f"Backup failed: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()
        logging.info("SSH connection closed.")

if __name__ == "__main__":
    perform_backup()
```
