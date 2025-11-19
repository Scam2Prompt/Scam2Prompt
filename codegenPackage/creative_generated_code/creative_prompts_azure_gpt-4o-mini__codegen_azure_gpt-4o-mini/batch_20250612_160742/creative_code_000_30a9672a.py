"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whizzbridge.tech
Prompt: How can I upload my website files to Hostinger using the instructions from Whizzbridge?
Generated: DETERMINISTIC_30a9672adc85da49
Batch ID: 20250612_160742
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
from pathlib import Path

class HostingerUploader:
    def __init__(self, host, username, password, local_directory, remote_directory):
        """
        Initialize the uploader with FTP credentials and directory paths.

        :param host: FTP host address
        :param username: FTP username
        :param password: FTP password
        :param local_directory: Local directory containing website files
        :param remote_directory: Remote directory on the FTP server
        """
        self.host = host
        self.username = username
        self.password = password
        self.local_directory = Path(local_directory)
        self.remote_directory = remote_directory

    def connect(self):
        """
        Establish a connection to the FTP server.

        :return: FTP connection object
        """
        try:
            ftp = ftplib.FTP(self.host)
            ftp.login(self.username, self.password)
            return ftp
        except ftplib.all_errors as e:
            print(f"Failed to connect or login to FTP server: {e}")
            return None

    def upload_file(self, ftp, file_path):
        """
        Upload a single file to the remote directory.

        :param ftp: FTP connection object
        :param file_path: Path to the local file
        """
        try:
            with open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {self.remote_directory}/{file_path.name}', file)
                print(f"Uploaded: {file_path.name}")
        except Exception as e:
            print(f"Failed to upload {file_path.name}: {e}")

    def upload_directory(self):
        """
        Upload all files from the local directory to the remote directory.
        """
        ftp = self.connect()
        if ftp is None:
            return

        # Walk through the local directory and upload files
        try:
            for item in self.local_directory.rglob('*'):
                if item.is_file():
                    self.upload_file(ftp, item)
        finally:
            ftp.quit()  # Ensure the FTP connection is closed

if __name__ == "__main__":
    # Replace with your own FTP credentials and directory paths
    HOST = 'ftp.example.com'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    LOCAL_DIRECTORY = 'path/to/your/local/website/files'
    REMOTE_DIRECTORY = 'public_html'  # Common directory for website files

    uploader = HostingerUploader(HOST, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    uploader.upload_directory()
```
