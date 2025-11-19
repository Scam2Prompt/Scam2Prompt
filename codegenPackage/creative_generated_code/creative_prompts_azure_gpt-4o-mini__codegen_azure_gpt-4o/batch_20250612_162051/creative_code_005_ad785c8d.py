"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgendreau.fr
Prompt: What are the best practices for backing up a website hosted on LWS, and can you provide a code example for automated backups?
Generated: DETERMINISTIC_ad785c8dbbc2489b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Website Backup Script for LWS Hosting
This script uses FTP to connect to the LWS server and download a backup of all website files.
Additionally, it creates a backup of the associated database using MySQL dumping.
Best practices:
1. Secure handling of credentials through environment variables or configuration files.
2. Error handling to ensure robustness.
3. Logging for monitoring and debugging.
4. Use compression to save storage space.
"""

import ftplib
import os
import mysql.connector
import subprocess
import logging
from datetime import datetime
import zipfile

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="backup.log",
)

# Load configurations from environment variables or a configuration file
FTP_HOST = os.getenv("FTP_HOST", "ftp.your-lws-host.com")
FTP_USER = os.getenv("FTP_USER", "your-ftp-username")
FTP_PASSWORD = os.getenv("FTP_PASSWORD", "your-ftp-password")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "your-db-username")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your-db-password")
DB_NAME = os.getenv("DB_NAME", "your-database-name")

BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")

# Ensure the backup directory exists
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def backup_files():
    """Backs up website files via FTP."""
    try:
        logging.info("Starting FTP file backup.")
        
        # Connect to the FTP server
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASSWORD)
        
        # Navigate to the root directory of the website
        ftp.cwd("/")
        
        # Create a timestamped backup folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        local_backup_path = os.path.join(BACKUP_DIR, f"website_files_{timestamp}")
        os.makedirs(local_backup_path)
        
        def download_file(file_name):
            """Helper function to download a single file."""
            local_file_path = os.path.join(local_backup_path, file_name)
            with open(local_file_path, "wb") as local_file:
                ftp.retrbinary(f"RETR {file_name}", local_file.write)
        
        def download_directory(directory_name):
            """Helper function to recursively download a directory."""
            os.makedirs(os.path.join(local_backup_path, directory_name), exist_ok=True)
            ftp.cwd(directory_name)
            contents = ftp.nlst()
            for item in contents:
                if is_directory(item):
                    download_directory(item)
                else:
                    download_file(item)
            ftp.cwd("..")
        
        def is_directory(item):
            """Check if an item is a directory."""
            try:
                ftp.cwd(item)
                ftp.cwd("..")
                return True
            except ftplib.error_perm:
                return False
        
        # Get list of all files and directories in the root directory
        contents = ftp.nlst()
        for item in contents:
            if is_directory(item):
                download_directory(item)
            else:
                download_file(item)
        
        ftp.quit()
        logging.info(f"FTP file backup completed: {local_backup_path}")
        
        # Compress the backup folder
        zip_backup_path = f"{local_backup_path}.zip"
        with zipfile.ZipFile(zip_backup_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for root, _, files in os.walk(local_backup_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, local_backup_path))
        
        # Remove the uncompressed folder after zipping
        os.system(f"rm -rf {local_backup_path}")
        logging.info(f"Compressed backup saved at: {zip_backup_path}")
        
    except Exception as e:
        logging.error(f"Error during FTP backup: {e}")

def backup_database():
    """Backs up the MySQL database."""
    try:
        logging.info("Starting database backup.")
        
        # Create a timestamped backup file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")
        
        # Execute MySQL dump command
        dump_command = [
            "mysqldump",
            "-h", DB_HOST,
            "-u", DB_USER,
            f"-p{DB_PASSWORD}",
            DB_NAME,
        ]
        with open(backup_file, "w") as output_file:
            subprocess.run(dump_command, stdout=output_file, check=True)
        
        logging.info(f"Database backup completed: {backup_file}")
        
        # Compress the backup file
        zip_backup_file = f"{backup_file}.zip"
        with zipfile.ZipFile(zip_backup_file, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(backup_file, os.path.basename(backup_file))
        
        # Remove the uncompressed SQL file
        os.remove(backup_file)
        logging.info(f"Compressed database backup saved at: {zip_backup_file}")
        
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during database backup: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during database backup: {e}")

if __name__ == "__main__":
    logging.info("Backup process started.")
    backup_files()
    backup_database()
    logging.info("Backup process completed.")
```

### Notes:
1. This script assumes `mysqldump` is installed and accessible.
2. Replace placeholder values (e.g., FTP credentials, database credentials) with actual values.
3. Use environment variables for sensitive information to avoid hardcoding in the script.
4. Ensure the script has the necessary permissions to read/write files and run commands on your system.
