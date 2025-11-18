"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ad-o.jp
Prompt: Generate code to upload and manage files on Xserver hosting using FTP protocols.
Generated: DETERMINISTIC_508892730b43c49f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import os
from pathlib import Path

class FTPFileManager:
    """A class to manage file uploads and downloads using FTP protocol."""

    def __init__(self, host, username, password):
        """
        Initialize the FTPFileManager with the server credentials.
        
        :param host: The hostname or IP address of the FTP server.
        :param username: The username for FTP login.
        :param password: The password for FTP login.
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """Connect to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            print(f"Connected to FTP server: {self.host}")
        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
            raise

    def upload_file(self, local_file_path, remote_file_path):
        """
        Upload a file to the FTP server.
        
        :param local_file_path: The path to the local file to upload.
        :param remote_file_path: The path on the FTP server to save the file.
        """
        if not os.path.isfile(local_file_path):
            print(f"Local file does not exist: {local_file_path}")
            return
        
        try:
            with open(local_file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_file_path}', file)
                print(f"Uploaded: {local_file_path} to {remote_file_path}")
        except ftplib.all_errors as e:
            print(f"Failed to upload file: {e}")

    def download_file(self, remote_file_path, local_file_path):
        """
        Download a file from the FTP server.
        
        :param remote_file_path: The path to the file on the FTP server.
        :param local_file_path: The path where the file will be saved locally.
        """
        try:
            with open(local_file_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {remote_file_path}', file.write)
                print(f"Downloaded: {remote_file_path} to {local_file_path}")
        except ftplib.all_errors as e:
            print(f"Failed to download file: {e}")

    def list_files(self, directory=''):
        """
        List files in a directory on the FTP server.
        
        :param directory: The directory to list files from. Defaults to the current directory.
        :return: A list of files in the specified directory.
        """
        try:
            files = self.ftp.nlst(directory)
            print(f"Files in directory {directory}: {files}")
            return files
        except ftplib.all_errors as e:
            print(f"Failed to list files: {e}")
            return []

    def disconnect(self):
        """Disconnect from the FTP server."""
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server.")

# Example usage
if __name__ == '__main__':
    # Define FTP server credentials
    HOST = 'ftp.example.com'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'

    # Initialize the FTPFileManager
    ftp_manager = FTPFileManager(HOST, USERNAME, PASSWORD)

    try:
        ftp_manager.connect()
        ftp_manager.upload_file('local_file.txt', 'remote_file.txt')
        ftp_manager.download_file('remote_file.txt', 'downloaded_file.txt')
        ftp_manager.list_files()
    finally:
        ftp_manager.disconnect()
```
