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

Certainly! Below is Python code that you can use to automate FTP backups from an Endora.cz hosting service. It uses `ftplib` for FTP operations and `zipfile` to compress the backup files. It also includes error handling and logging.

```python
import ftplib
import os
import zipfile
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='ftp_backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def connect_to_ftp(host, username, password):
    """
    Connects to the FTP server and returns the FTP connection object.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        logging.info("Successfully connected to FTP server.")
        return ftp
    except ftplib.all_errors as e:
        logging.error(f"Failed to connect to FTP server: {e}")
        raise

def download_files(ftp, remote_dir, local_dir):
    """
    Downloads files from the FTP server.
    """
    try:
        ftp.cwd(remote_dir)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        for filename in ftp.nlst():  # List files in the directory
            local_file = os.path.join(local_dir, filename)
            with open(local_file, 'wb') as f:
                ftp.retrbinary(f"RETR {filename}", f.write)
            logging.info(f"Downloaded: {filename}")
    except ftplib.all_errors as e:
        logging.error(f"Failed to download files from remote directory '{remote_dir}': {e}")
        raise

def zip_backup(source_dir, zip_file_name):
    """
    Compresses files into a zip archive.
    """
    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)  # Relative path for the zip archive
                    zipf.write(file_path, arcname)
        logging.info(f"Created backup archive: {zip_file_name}")
    except Exception as e:
        logging.error(f"Failed to create backup archive: {e}")
        raise

def main():
    # FTP server credentials
    FTP_HOST = 'ftp.endora.cz'
    FTP_USERNAME = 'your_username'
    FTP_PASSWORD = 'your_password'
    REMOTE_DIR = '/path/to/remote/directory'  # Remote directory to back up
    LOCAL_BACKUP_DIR = './ftp_backup'        # Local directory to store backups

    # Generate a zip file name with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_file_name = f'ftp_backup_{timestamp}.zip'

    try:
        # Step 1: Connect to FTP server
        ftp = connect_to_ftp(FTP_HOST, FTP_USERNAME, FTP_PASSWORD)

        # Step 2: Download files from the FTP server
        download_files(ftp, REMOTE_DIR, LOCAL_BACKUP_DIR)

        # Step 3: Zip the downloaded files
        zip_backup(LOCAL_BACKUP_DIR, zip_file_name)

        # Step 4: Close the FTP connection
        ftp.quit()
        logging.info("Backup process completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during the backup process: {e}")

if __name__ == "__main__":
    main()
```

### Key Notes:
- Replace placeholders like `your_username`, `your_password`, and `/path/to/remote/directory` with actual values for your FTP server.
- Ensure the `local_backup_dir` path is writable.
- Install Python and any dependencies before running the script.

This script is production-ready, adheres to best practices, and includes logging and error handling for easier debugging and monitoring.
