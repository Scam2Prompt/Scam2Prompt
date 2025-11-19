"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxiful.epizy.com
Prompt: Illustrate how to transfer an existing website to iFastNet hosting using a specific programming language.
Generated: DETERMINISTIC_5f8fc2accf19a4d9
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import requests
from ftplib import FTP, error_perm

class WebsiteTransfer:
    def __init__(self, ftp_host, ftp_user, ftp_pass, local_website_path):
        """
        Initialize the WebsiteTransfer instance.

        :param ftp_host: The FTP host address (iFastNet server).
        :param ftp_user: The FTP username for authentication.
        :param ftp_pass: The FTP password for authentication.
        :param local_website_path: The local path of the website files to transfer.
        """
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass
        self.local_website_path = local_website_path
        self.ftp = FTP()

    def connect_ftp(self):
        """Connects to the FTP server and logs in."""
        try:
            self.ftp.connect(self.ftp_host)
            self.ftp.login(self.ftp_user, self.ftp_pass)
            print("Connected to FTP server.")
        except Exception as e:
            print(f"Error connecting to FTP server: {e}")
            raise

    def upload_file(self, local_file_path, remote_file_path):
        """
        Upload a single file to the FTP server.

        :param local_file_path: The path of the local file to upload.
        :param remote_file_path: The destination path on the FTP server.
        """
        try:
            with open(local_file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_file_path}', file)
                print(f"Uploaded: {remote_file_path}")
        except error_perm as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"Error uploading {local_file_path}: {e}")

    def upload_directory(self, local_directory):
        """
        Recursively upload a directory to the FTP server.

        :param local_directory: The local directory to upload.
        """
        for root, dirs, files in os.walk(local_directory):
            remote_path = root.replace(self.local_website_path, "").replace("\\", "/")
            try:
                self.ftp.mkd(remote_path)  # Create remote directory if it doesn't exist
            except error_perm as e:
                if not str(e).startswith('550'):  # Ignore if directory already exists
                    print(f"Error creating directory {remote_path}: {e}")

            for file_name in files:
                local_file_path = os.path.join(root, file_name)
                remote_file_path = f"{remote_path}/{file_name}"
                self.upload_file(local_file_path, remote_file_path)

    def transfer(self):
        """Initiates the transfer of the website to the FTP server."""
        self.connect_ftp()
        self.upload_directory(self.local_website_path)
        self.ftp.quit()
        print("Website transfer completed.")

if __name__ == "__main__":
    # Replace with your actual FTP credentials and local website path
    ftp_host = "ftp.your-ifastnet-domain.com"
    ftp_user = "your_username"
    ftp_pass = "your_password"
    local_website_path = "path/to/your/local/website"

    transfer = WebsiteTransfer(ftp_host, ftp_user, ftp_pass, local_website_path)
    transfer.transfer()
```
