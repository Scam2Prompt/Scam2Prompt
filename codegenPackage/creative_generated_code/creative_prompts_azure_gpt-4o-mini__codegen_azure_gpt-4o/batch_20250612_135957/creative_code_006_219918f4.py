"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Explain how to perform regular data backups for a website hosted on Endora.cz.
Generated: DETERMINISTIC_219918f4947a615b
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python script that automates regular backups for a website hosted on Endora.cz. The script uses FTP to download files and MySQL to back up the database.

```python
import os
import ftplib
import mysql.connector
from datetime import datetime
import shutil

# Configuration
FTP_HOST = "ftp.endora.cz"
FTP_USER = "your_ftp_username"
FTP_PASSWORD = "your_ftp_password"
FTP_REMOTE_DIR = "/path/to/your/website"
LOCAL_BACKUP_DIR = "/path/to/backup"

DB_HOST = "your_database_host"
DB_USER = "your_database_user"
DB_PASSWORD = "your_database_password"
DB_NAME = "your_database_name"

# Ensure the local backup directory exists
os.makedirs(LOCAL_BACKUP_DIR, exist_ok=True)

def backup_ftp():
    """
    Backs up files from the FTP server.
    """
    try:
        print("Starting FTP backup...")
        # Connect to FTP server
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)
        ftp.cwd(FTP_REMOTE_DIR)
        
        # Create a timestamped directory for this backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ftp_backup_dir = os.path.join(LOCAL_BACKUP_DIR, f"ftp_backup_{timestamp}")
        os.makedirs(ftp_backup_dir, exist_ok=True)

        def download_file(file_name):
            """
            Helper function to download a single file.
            """
            local_file_path = os.path.join(ftp_backup_dir, file_name)
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {file_name}", local_file.write)

        def download_directory(dir_name):
            """
            Helper function to download an entire directory.
            """
            os.makedirs(os.path.join(ftp_backup_dir, dir_name), exist_ok=True)
            ftp.cwd(dir_name)
            for item in ftp.nlst():
                if is_file(item):
                    download_file(item)
                else:
                    download_directory(item)
            ftp.cwd("..")

        def is_file(item):
            """
            Checks if an FTP item is a file.
            """
            try:
                ftp.size(item)
                return True
            except ftplib.error_perm:
                return False

        # Download all files and directories from the remote location
        for item in ftp.nlst():
            if is_file(item):
                download_file(item)
            else:
                download_directory(item)

        ftp.quit()
        print(f"FTP backup completed and saved to {ftp_backup_dir}")
    except Exception as e:
        print(f"An error occurred during FTP backup: {e}")

def backup_database():
    """
    Backs up the MySQL database.
    """
    try:
        print("Starting database backup...")
        # Create a timestamped file for this backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        db_backup_file = os.path.join(LOCAL_BACKUP_DIR, f"db_backup_{timestamp}.sql")

        # Connect to the database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Use mysqldump to create the backup (requires `mysqldump` to be installed)
        dump_command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {db_backup_file}"
        os.system(dump_command)

        cursor.close()
        conn.close()
        print(f"Database backup completed and saved to {db_backup_file}")
    except Exception as e:
        print(f"An error occurred during database backup: {e}")

def perform_backup():
    """
    Performs both FTP and database backups.
    """
    try:
        backup_ftp()
        backup_database()
        print("All backups completed successfully!")
    except Exception as e:
        print(f"An error occurred during the backup process: {e}")

if __name__ == "__main__":
    perform_backup()
```

### Notes:
1. Replace placeholders (`your_ftp_username`, `your_database_host`, etc.) with your actual credentials and paths.
2. Ensure you have `mysqldump` installed and accessible in your system's PATH for the database backup.
3. Set up this script to run periodically using a scheduling tool like `cron` (Linux/macOS) or Task Scheduler (Windows).
