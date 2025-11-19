"""
Generated Code Metadata:
========================
Original URL: https://micropro.co.nz
Prompt: Write a Python script to automate FTP file upload for a website hosted on a server.
Generated: DETERMINISTIC_447eef33a2171a07
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ftplib
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("ftp_upload.log"), logging.StreamHandler()]
)

def upload_file_to_ftp(server, username, password, local_file_path, remote_file_path):
    """
    Uploads a file to an FTP server.

    Args:
        server (str): FTP server address.
        username (str): FTP username.
        password (str): FTP password.
        local_file_path (str): Path to the local file to be uploaded.
        remote_file_path (str): Path on the server where the file will be uploaded.

    Returns:
        None
    """
    try:
        # Check if the local file exists
        if not os.path.isfile(local_file_path):
            logging.error(f"Local file '{local_file_path}' does not exist.")
            return

        # Connect to the FTP server
        logging.info(f"Connecting to FTP server: {server}")
        with ftplib.FTP(server) as ftp:
            ftp.login(user=username, passwd=password)
            logging.info("Successfully logged in to the FTP server.")

            # Open the local file in binary mode
            with open(local_file_path, 'rb') as file:
                # Upload the file to the server
                logging.info(f"Uploading file '{local_file_path}' to '{remote_file_path}'...")
                ftp.storbinary(f"STOR {remote_file_path}", file)
                logging.info("File upload successful.")

    except ftplib.all_errors as e:
        logging.error(f"FTP error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # FTP server details
    FTP_SERVER = "ftp.example.com"
    FTP_USERNAME = "your_username"
    FTP_PASSWORD = "your_password"

    # File paths
    LOCAL_FILE_PATH = "path/to/your/local/file.txt"
    REMOTE_FILE_PATH = "path/on/server/file.txt"

    # Upload the file
    upload_file_to_ftp(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, LOCAL_FILE_PATH, REMOTE_FILE_PATH)
```
