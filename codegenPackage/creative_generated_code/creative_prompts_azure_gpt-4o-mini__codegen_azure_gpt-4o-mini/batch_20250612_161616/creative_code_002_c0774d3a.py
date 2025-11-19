"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danushi.com
Prompt: Can you provide a code snippet for uploading website files to Hostinger based on the guidelines from danushi.com?
Generated: DETERMINISTIC_c0774d3a53069b9d
Batch ID: 20250612_161616
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
    def __init__(self, host, username, password):
        """
        Initializes the HostingerUploader with FTP connection parameters.

        :param host: FTP host address
        :param username: FTP username
        :param password: FTP password
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
            print("Connected to the FTP server.")
        except ftplib.all_errors as e:
            print(f"Failed to connect to the FTP server: {e}")
            raise

    def upload_directory(self, local_directory):
        """
        Uploads all files from the local directory to the FTP server.

        :param local_directory: Path to the local directory containing files
        """
        try:
            for root, _, files in os.walk(local_directory):
                for file in files:
                    local_path = Path(root) / file
                    remote_path = str(local_path.relative_to(local_directory))
                    self.upload_file(local_path, remote_path)
        except Exception as e:
            print(f"Error while uploading directory: {e}")
            raise

    def upload_file(self, local_file, remote_file):
        """
        Uploads a single file to the FTP server.

        :param local_file: Path to the local file
        :param remote_file: Path on the FTP server where the file should be uploaded
        """
        try:
            with open(local_file, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_file}', file)
                print(f"Uploaded {local_file} to {remote_file}.")
        except FileNotFoundError:
            print(f"File not found: {local_file}")
        except ftplib.error_perm as e:
            print(f"Permission error while uploading {remote_file}: {e}")
        except Exception as e:
            print(f"Failed to upload {local_file}: {e}")

    def close(self):
        """Closes the FTP connection."""
        if self.ftp:
            self.ftp.quit()
            print("FTP connection closed.")

# Example Usage
if __name__ == "__main__":
    uploader = HostingerUploader(host='ftp.yourhostinger.com', username='your_username', password='your_password')
    try:
        uploader.connect()
        uploader.upload_directory('path/to/your/local/website/files')
    finally:
        uploader.close()
```

Make sure to replace `'ftp.yourhostinger.com'`, `'your_username'`, and `'your_password'` with your actual Hostinger FTP details and specify the path to your local website files.
