"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drutnet.in
Prompt: Generate a step-by-step Python script for transferring website files to Hostinger, ensuring compatibility with the migration process mentioned.
Generated: DETERMINISTIC_06591273e6b01d81
Batch ID: 20250612_152000
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
import logging
from dotenv import load_dotenv

# Load environment variables from a .env file for security (recommended for production)
load_dotenv()

# Configure logging for debugging and production monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# FTP credentials (stored securely in the .env file)
FTP_HOST = os.getenv('FTP_HOST')  # Hostinger FTP server address
FTP_USER = os.getenv('FTP_USER')  # FTP username
FTP_PASSWORD = os.getenv('FTP_PASSWORD')  # FTP password
LOCAL_DIRECTORY = os.getenv('LOCAL_DIRECTORY')  # Local directory to upload
REMOTE_DIRECTORY = os.getenv('REMOTE_DIRECTORY')  # Remote directory on Hostinger

def upload_file_to_hostinger(ftp_client, local_file_path, remote_file_path):
    """
    Uploads a single file to the Hostinger server.
    
    :param ftp_client: ftplib.FTP object
    :param local_file_path: Path to the local file
    :param remote_file_path: Path to the remote file
    :return: None
    """
    try:
        with open(local_file_path, 'rb') as file:
            ftp_client.storbinary(f"STOR {remote_file_path}", file)
        logging.info(f"File uploaded successfully: {local_file_path} -> {remote_file_path}")
    except Exception as e:
        logging.error(f"Failed to upload {local_file_path} to {remote_file_path}: {e}")

def upload_directory_to_hostinger(ftp_client, local_dir, remote_dir):
    """
    Recursively uploads a directory and its contents to the Hostinger server.
    
    :param ftp_client: ftplib.FTP object
    :param local_dir: Path to the local directory
    :param remote_dir: Path to the remote directory
    :return: None
    """
    try:
        # Ensure the remote directory exists; create if it doesn't
        if remote_dir not in ftp_client.nlst():
            ftp_client.mkd(remote_dir)
            logging.info(f"Created remote directory: {remote_dir}")
    except Exception as e:
        logging.warning(f"Failed to create remote directory {remote_dir}: {e}")

    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = f"{remote_dir}/{item}"

        if os.path.isdir(local_path):
            # Recursively upload subdirectories
            upload_directory_to_hostinger(ftp_client, local_path, remote_path)
        else:
            # Upload individual files
            upload_file_to_hostinger(ftp_client, local_path, remote_path)

def main():
    """
    Main function to handle file transfers to Hostinger FTP server.
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASSWORD)
        logging.info("Connected to Hostinger FTP server.")

        # Begin upload process
        upload_directory_to_hostinger(ftp, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
        
        # Close the connection
        ftp.quit()
        logging.info("FTP connection closed.")
    except Exception as e:
        logging.error(f"Error during FTP operation: {e}")

if __name__ == "__main__":
    # Ensure environment variables are set before running
    if not FTP_HOST or not FTP_USER or not FTP_PASSWORD or not LOCAL_DIRECTORY or not REMOTE_DIRECTORY:
        logging.error("Missing required environment variables. Please check the .env file.")
    else:
        main()
```

**Note:**  
1. Create a `.env` file in the same directory as this script to securely store your FTP credentials and paths:
    ```
    FTP_HOST=ftp.hostinger.com
    FTP_USER=your_username
    FTP_PASSWORD=your_password
    LOCAL_DIRECTORY=/path/to/local/directory
    REMOTE_DIRECTORY=/path/to/remote/directory
    ```
2. Install `python-dotenv` using `pip install python-dotenv` if you want to use the `.env` file for environment variables.
