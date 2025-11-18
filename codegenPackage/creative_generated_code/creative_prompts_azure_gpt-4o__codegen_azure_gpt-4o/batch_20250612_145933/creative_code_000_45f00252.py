"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arastrum.com
Prompt: Write a Python script to automate the migration of a website to Hostinger, referencing the steps provided on the Arastrum website.
Generated: DETERMINISTIC_45f00252ee8525fd
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import ftplib
import shutil
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_website_files(source_dir: str, backup_dir: str) -> None:
    """
    Backs up the website files to a local backup directory.

    Args:
        source_dir (str): Path to the source directory of the website files.
        backup_dir (str): Path to the backup directory.
    """
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        shutil.copytree(source_dir, backup_dir, dirs_exist_ok=True)
        logging.info(f"Website files backed up successfully to {backup_dir}")
    except Exception as e:
        logging.error(f"Error while backing up website files: {e}")
        raise

def connect_to_ftp(host: str, username: str, password: str) -> ftplib.FTP:
    """
    Establishes an FTP connection.

    Args:
        host (str): FTP host address.
        username (str): FTP username.
        password (str): FTP password.

    Returns:
        ftplib.FTP: An active FTP connection.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        logging.info(f"Connected to FTP server at {host}")
        return ftp
    except ftplib.all_errors as e:
        logging.error(f"FTP connection error: {e}")
        raise

def upload_files_to_hostinger(ftp: ftplib.FTP, local_dir: str, remote_dir: str) -> None:
    """
    Uploads files from a local directory to the Hostinger server.

    Args:
        ftp (ftplib.FTP): Active FTP connection.
        local_dir (str): Path to the local directory containing website files.
        remote_dir (str): Path to the remote directory where files should be uploaded.
    """
    def upload_file(local_path: str, remote_path: str):
        """
        Helper function to upload a single file.
        """
        with open(local_path, 'rb') as file:
            ftp.storbinary(f"STOR {remote_path}", file)
        logging.info(f"Uploaded {local_path} to {remote_path}")

    try:
        ftp.cwd(remote_dir)
    except ftplib.error_perm:
        ftp.mkd(remote_dir)
        ftp.cwd(remote_dir)
        logging.info(f"Created and moved to remote directory {remote_dir}")

    for root, dirs, files in os.walk(local_dir):
        for dir_name in dirs:
            remote_subdir = os.path.join(remote_dir, os.path.relpath(os.path.join(root, dir_name), local_dir))
            try:
                ftp.mkd(remote_subdir)
                logging.info(f"Created remote directory {remote_subdir}")
            except ftplib.error_perm:
                logging.info(f"Remote directory {remote_subdir} already exists.")
        
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            remote_file_path = os.path.join(remote_dir, os.path.relpath(local_file_path, local_dir))
            upload_file(local_file_path, remote_file_path)

def migrate_database(db_dump_file: str, hostinger_db_config: dict) -> None:
    """
    Migrates the database to Hostinger.

    Args:
        db_dump_file (str): Path to the SQL dump file of the database.
        hostinger_db_config (dict): Dictionary containing Hostinger database connection information.
            Keys: 'host', 'username', 'password', 'database'.
    """
    try:
        import mysql.connector

        conn = mysql.connector.connect(
            host=hostinger_db_config['host'],
            user=hostinger_db_config['username'],
            password=hostinger_db_config['password'],
            database=hostinger_db_config['database']
        )
        cursor = conn.cursor()

        with open(db_dump_file, 'r') as file:
            dump_content = file.read()
        
        for command in dump_content.split(';'):
            if command.strip():
                cursor.execute(command)
        
        conn.commit()
        logging.info("Database migrated successfully to Hostinger.")
    except mysql.connector.Error as e:
        logging.error(f"Error during database migration: {e}")
        raise
    finally:
        cursor.close()
        conn.close()

def main():
    """
    Main function to execute the migration.
    """
    try:
        # Configuration
        source_dir = "/path/to/your/website/files"
        backup_dir = "/path/to/your/backup"
        local_db_dump = "/path/to/your/database/dump.sql"

        ftp_host = "ftp.hostinger.com"
        ftp_username = "your_ftp_username"
        ftp_password = "your_ftp_password"
        remote_dir = "/public_html"

        hostinger_db_config = {
            'host': 'your_hostinger_db_host',
            'username': 'your_hostinger_db_user',
            'password': 'your_hostinger_db_password',
            'database': 'your_hostinger_db_name'
        }

        # Perform actions
        backup_website_files(source_dir, backup_dir)

        ftp = connect_to_ftp(ftp_host, ftp_username, ftp_password)
        upload_files_to_hostinger(ftp, source_dir, remote_dir)
        ftp.quit()

        migrate_database(local_db_dump, hostinger_db_config)
    except Exception as e:
        logging.error(f"Migration failed: {e}")

if __name__ == "__main__":
    main()
```
