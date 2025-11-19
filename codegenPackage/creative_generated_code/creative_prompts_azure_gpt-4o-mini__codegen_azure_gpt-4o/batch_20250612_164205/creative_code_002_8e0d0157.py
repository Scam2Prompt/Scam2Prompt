"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodlit.rf.gd
Prompt: How can I transfer my existing website to iFastNet hosting while ensuring a free domain name is included?
Generated: DETERMINISTIC_8e0d015710eb50f3
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Transferring a website to iFastNet hosting involves tasks that can't be directly accomplished with code alone. Instead, it involves setting up hosting, updating DNS records, and migrating website files. Below is a Python script that automates part of the process: uploading files via FTP to the iFastNet server. The script assumes you have your iFastNet FTP credentials and domain-related details.

```python
import ftplib
import os
import logging
from dotenv import load_dotenv

# Load credentials from a .env file for security (recommended)
load_dotenv()

# FTP server details (replace with your iFastNet credentials)
FTP_HOST = os.getenv("FTP_HOST")  # e.g., "ftp.ifastnet.com"
FTP_USER = os.getenv("FTP_USER")  # Your FTP username
FTP_PASS = os.getenv("FTP_PASS")  # Your FTP password
FTP_DEST_PATH = os.getenv("FTP_DEST_PATH", "/htdocs/")  # Destination path on the server

# Local folder containing website files
LOCAL_WEBSITE_FOLDER = "path/to/your/website/files"

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def upload_file(ftp, local_file_path, remote_file_path):
    """
    Upload a single file to the FTP server.
    :param ftp: Active FTP connection object
    :param local_file_path: Path to the file on the local system
    :param remote_file_path: Path to the file on the FTP server
    """
    try:
        with open(local_file_path, "rb") as file:
            ftp.storbinary(f"STOR {remote_file_path}", file)
            logging.info(f"Uploaded: {local_file_path} -> {remote_file_path}")
    except Exception as e:
        logging.error(f"Failed to upload {local_file_path}: {e}")

def upload_directory(ftp, local_directory, remote_directory):
    """
    Recursively upload an entire directory to the FTP server.
    :param ftp: Active FTP connection object
    :param local_directory: Path to the local directory
    :param remote_directory: Path to the remote directory on the FTP server
    """
    try:
        # Change to the remote directory or create it
        try:
            ftp.cwd(remote_directory)
        except ftplib.error_perm:
            ftp.mkd(remote_directory)
            ftp.cwd(remote_directory)

        # Iterate over local files and subdirectories
        for item in os.listdir(local_directory):
            local_item_path = os.path.join(local_directory, item)
            remote_item_path = f"{remote_directory}/{item}"

            if os.path.isdir(local_item_path):
                # Recursively upload subdirectories
                upload_directory(ftp, local_item_path, remote_item_path)
            else:
                # Upload individual files
                upload_file(ftp, local_item_path, remote_item_path)

    except Exception as e:
        logging.error(f"Failed to upload directory {local_directory}: {e}")

def main():
    """
    Main function to handle FTP upload and setup.
    """
    try:
        # Connect to FTP server
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        logging.info("Connected to FTP server.")

        # Upload website files
        upload_directory(ftp, LOCAL_WEBSITE_FOLDER, FTP_DEST_PATH)

        # Close FTP connection
        ftp.quit()
        logging.info("FTP upload complete. Connection closed.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Instructions for Use:
1. Install required dependencies: `pip install python-dotenv`.
2. Create a `.env` file in the same directory as the script with the following content:
   ```
   FTP_HOST=ftp.ifastnet.com
   FTP_USER=your_ftp_username
   FTP_PASS=your_ftp_password
   FTP_DEST_PATH=/htdocs/
   ```
3. Update `LOCAL_WEBSITE_FOLDER` to the path containing your website files.
4. Run the script with Python: `python script_name.py`.

### Notes:
- Ensure your DNS settings point to iFastNet's servers for the free domain to work.
- The script only uploads files and directories; database migration (if needed) must be handled separately.
