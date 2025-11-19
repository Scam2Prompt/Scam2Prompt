"""
Generated Code Metadata:
========================
Original URL: https://ad-o.jp
Prompt: Generate code to upload and manage files on Xserver hosting using FTP protocols.
Generated: DETERMINISTIC_508892730b43c49f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**FTP Client in Python for Xserver Hosting**
=============================================

```python
import ftplib
import os

class FTPClient:
    def __init__(self, host, username, password):
        """
        Initialize the FTP client with host, username, and password.

        :param host: FTP server host
        :param username: FTP server username
        :param password: FTP server password
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """
        Establish a connection to the FTP server.
        """
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(user=self.username, passwd=self.password)
            print("Connected to FTP server")
        except ftplib.all_errors as e:
            print(f"Error connecting to FTP server: {e}")

    def disconnect(self):
        """
        Close the FTP connection.
        """
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server")

    def upload_file(self, local_file, remote_file):
        """
        Upload a file to the FTP server.

        :param local_file: Path to the local file
        :param remote_file: Path to the remote file
        """
        try:
            with open(local_file, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_file}', f)
            print(f"Uploaded {local_file} to {remote_file}")
        except ftplib.all_errors as e:
            print(f"Error uploading file: {e}")

    def download_file(self, remote_file, local_file):
        """
        Download a file from the FTP server.

        :param remote_file: Path to the remote file
        :param local_file: Path to the local file
        """
        try:
            with open(local_file, 'wb') as f:
                self.ftp.retrbinary(f'RETR {remote_file}', f.write)
            print(f"Downloaded {remote_file} to {local_file}")
        except ftplib.all_errors as e:
            print(f"Error downloading file: {e}")

    def list_files(self):
        """
        List files in the current FTP directory.
        """
        try:
            files = self.ftp.nlst()
            print("Files in current directory:")
            for file in files:
                print(file)
        except ftplib.all_errors as e:
            print(f"Error listing files: {e}")

    def create_directory(self, remote_dir):
        """
        Create a directory on the FTP server.

        :param remote_dir: Path to the remote directory
        """
        try:
            self.ftp.mkd(remote_dir)
            print(f"Created directory {remote_dir}")
        except ftplib.all_errors as e:
            print(f"Error creating directory: {e}")

    def delete_file(self, remote_file):
        """
        Delete a file on the FTP server.

        :param remote_file: Path to the remote file
        """
        try:
            self.ftp.delete(remote_file)
            print(f"Deleted file {remote_file}")
        except ftplib.all_errors as e:
            print(f"Error deleting file: {e}")


def main():
    host = 'ftp.xserver.com'
    username = 'your_username'
    password = 'your_password'

    ftp_client = FTPClient(host, username, password)
    ftp_client.connect()

    # Upload a file
    local_file = 'local_file.txt'
    remote_file = '/remote/path/file.txt'
    ftp_client.upload_file(local_file, remote_file)

    # Download a file
    remote_file = '/remote/path/file.txt'
    local_file = 'downloaded_file.txt'
    ftp_client.download_file(remote_file, local_file)

    # List files
    ftp_client.list_files()

    # Create a directory
    remote_dir = '/remote/path/new_dir'
    ftp_client.create_directory(remote_dir)

    # Delete a file
    remote_file = '/remote/path/file.txt'
    ftp_client.delete_file(remote_file)

    ftp_client.disconnect()


if __name__ == '__main__':
    main()
```
