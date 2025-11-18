"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://365cash.us
Prompt: Provide code examples for connecting to Hostinger's hosting server via FTP to upload website files programmatically.
Generated: DETERMINISTIC_576199b157e8f5f6
Batch ID: 20250612_154215
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

class FTPUploader:
    def __init__(self, host, username, password):
        """
        Initializes the FTPUploader with necessary credentials.

        :param host: The FTP server address
        :param username: The FTP account username
        :param password: The FTP account password
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """Establishes a connection to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(user=self.username, passwd=self.password)
            print("Connected to FTP server.")
        except ftplib.all_errors as e:
            print(f"Failed to connect to FTP server: {e}")
            raise

    def upload_file(self, local_file_path, remote_file_path):
        """
        Uploads a single file to the FTP server.

        :param local_file_path: Path to the local file to upload
        :param remote_file_path: Path on the FTP server where the file will be uploaded
        """
        try:
            with open(local_file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_file_path}', file)
                print(f"Uploaded file: {local_file_path} to {remote_file_path}")
        except Exception as e:
            print(f"Failed to upload file {local_file_path}: {e}")
            raise

    def upload_directory(self, local_dir, remote_dir):
        """
        Uploads all files in a directory to the FTP server.

        :param local_dir: Path to the local directory
        :param remote_dir: Path on the FTP server where files will be uploaded
        """
        try:
            # Change to the remote directory
            self.ftp.cwd(remote_dir)
            for filename in os.listdir(local_dir):
                local_file_path = os.path.join(local_dir, filename)
                if os.path.isfile(local_file_path):
                    self.upload_file(local_file_path, filename)
            print(f"All files uploaded from {local_dir} to {remote_dir}")
        except Exception as e:
            print(f"Failed to upload directory {local_dir}: {e}")
            raise

    def disconnect(self):
        """Closes the connection to the FTP server."""
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server.")

# Example usage:
if __name__ == "__main__":
    host = "ftp.example.com"  # Replace with your Hostinger FTP host
    username = "your_username"  # Replace with your FTP username
    password = "your_password"  # Replace with your FTP password

    uploader = FTPUploader(host, username, password)
    
    try:
        uploader.connect()
        uploader.upload_directory("path/to/local/directory", "path/to/remote/directory")
    finally:
        uploader.disconnect()
```
