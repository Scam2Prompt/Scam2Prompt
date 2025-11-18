"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitriunm.cloud
Prompt: Write code to automate the migration of a website to Hostinger using FTP and provide steps for uploading files as described on the Hostinger platform.
Generated: DETERMINISTIC_6c477977e5b9d16f
Batch ID: 20250612_150323
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

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FTPSiteMigrator:
    def __init__(self, host, username, password):
        """
        Initialize the FTPSiteMigrator with FTP server details.
        
        :param host: FTP server address
        :param username: FTP username
        :param password: FTP password
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """Connect to the FTP server using provided credentials."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            logging.info("Connected to the FTP server successfully.")
        except ftplib.all_errors as e:
            logging.error(f"FTP error: {e}")
            raise

    def upload_file(self, file_path, remote_path):
        """
        Upload a single file to the FTP server.
        
        :param file_path: Local file path to be uploaded
        :param remote_path: Destination path on the FTP server
        """
        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
                logging.info(f"Uploaded '{file_path}' to '{remote_path}'.")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
        except ftplib.all_errors as e:
            logging.error(f"FTP upload error: {e}")

    def upload_directory(self, local_directory, remote_directory):
        """
        Recursively upload a directory to the FTP server.
        
        :param local_directory: Local directory to be uploaded
        :param remote_directory: Destination directory on the FTP server
        """
        try:
            os.makedirs(remote_directory, exist_ok=True)
            for item in os.listdir(local_directory):
                local_path = os.path.join(local_directory, item)
                remote_path = f"{remote_directory}/{item}"

                if os.path.isfile(local_path):
                    self.upload_file(local_path, remote_path)
                elif os.path.isdir(local_path):
                    self.upload_directory(local_path, remote_path)
        except Exception as e:
            logging.error(f"Error uploading directory: {e}")

    def close(self):
        """Close the FTP connection."""
        if self.ftp:
            self.ftp.quit()
            logging.info("Disconnected from the FTP server.")

def main():
    # FTP server credentials
    host = "your-hostinger-ftp-server.com"
    username = "your-ftp-username"
    password = "your-ftp-password"
    
    # Local and remote paths
    local_directory = "path/to/your/local/website/files"
    remote_directory = "/public_html"  # Example: Hostinger's default web root

    # Create a site migrator instance and perform migration
    migrator = FTPSiteMigrator(host, username, password)

    try:
        migrator.connect()
        migrator.upload_directory(local_directory, remote_directory)
    finally:
        migrator.close()

if __name__ == "__main__":
    main()
``` 

### Steps for uploading files to Hostinger using FTP:
1. Gather your Hostinger FTP credentials (FTP server address, username, and password).
2. Ensure the local website files are organized in a directory.
3. Update the `host`, `username`, and `password` variables in the code with your Hostinger FTP details.
4. Specify the local directory containing your website files in the `local_directory` variable.
5. Run the Python script to initiate the migration process.
6. Monitor the logging output for the status of the upload process.
