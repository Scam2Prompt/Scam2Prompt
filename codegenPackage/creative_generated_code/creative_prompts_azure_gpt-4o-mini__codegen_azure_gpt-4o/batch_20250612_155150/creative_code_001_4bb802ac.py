"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.lovestoblog.com
Prompt: How can I transfer my existing website to iFastNet hosting while ensuring minimal downtime?
Generated: DETERMINISTIC_4bb802ac9310ca54
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python script that uses FTP to transfer website files from your local system to iFastNet hosting. This script assumes you have access to your iFastNet FTP credentials and that your local website files are ready for upload.

```python
import ftplib
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def upload_directory(ftp, local_dir, remote_dir):
    """
    Recursively upload files and directories to the FTP server.

    :param ftp: ftplib.FTP object
    :param local_dir: Path to the local directory
    :param remote_dir: Path to the remote directory on the FTP server
    """
    try:
        # Change or create the remote directory
        if remote_dir not in ftp.nlst():
            ftp.mkd(remote_dir)
        ftp.cwd(remote_dir)
        logging.info(f"Switched to remote directory: {remote_dir}")
    except ftplib.error_perm as e:
        logging.error(f"Failed to access or create remote directory {remote_dir}: {e}")
        raise

    # Iterate through local files and directories
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        if os.path.isdir(local_path):  # If the item is a directory
            upload_directory(ftp, local_path, item)
        else:  # If the item is a file
            try:
                with open(local_path, "rb") as file:
                    ftp.storbinary(f"STOR {item}", file)
                logging.info(f"Uploaded: {item}")
            except Exception as e:
                logging.error(f"Failed to upload {item}: {e}")
    
    # Return to the parent directory
    ftp.cwd("..")
    logging.info("Returned to the parent directory.")

def main():
    # FTP server credentials for iFastNet
    FTP_HOST = "ftp.yourdomain.com"  # Replace with your iFastNet FTP hostname
    FTP_USER = "your_username"       # Replace with your FTP username
    FTP_PASS = "your_password"       # Replace with your FTP password
    LOCAL_WEBSITE_DIR = "/path/to/your/local/website/files"  # Replace with the path to your website files
    REMOTE_WEBSITE_DIR = "/public_html"  # Replace with the target directory on iFastNet
    
    try:
        # Connect to FTP server
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        logging.info(f"Connected to FTP server: {FTP_HOST}")
        
        # Start uploading files
        upload_directory(ftp, LOCAL_WEBSITE_DIR, REMOTE_WEBSITE_DIR)
        logging.info("Upload completed successfully.")
        
        # Close the FTP connection
        ftp.quit()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Instructions:
1. Replace the placeholders (`FTP_HOST`, `FTP_USER`, `FTP_PASS`, `LOCAL_WEBSITE_DIR`) with your actual iFastNet FTP credentials and local file paths.
2. Save this script as `upload_to_ifastnet.py`.
3. Ensure Python is installed on your machine, and execute the script using `python upload_to_ifastnet.py`.
4. Double-check permissions and configurations on the iFastNet server to ensure the uploaded files serve properly.

This script assumes you have FTP access to the iFastNet hosting server and a good understanding of your website structure.
