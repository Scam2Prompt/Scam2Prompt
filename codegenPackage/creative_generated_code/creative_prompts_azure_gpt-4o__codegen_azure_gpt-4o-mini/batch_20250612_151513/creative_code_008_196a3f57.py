"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Write code to integrate DX Link's FTP server options into a file transfer application, ensuring compatibility with their network specifications.
Generated: DETERMINISTIC_196a3f577ceb6c73
Batch ID: 20250612_151513
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
import logging
from typing import List

# Configure logging for better visibility of operations and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FtpClient:
    """A class to interact with an FTP server."""

    def __init__(self, host: str, username: str, password: str):
        """Initialize the FTP client with server credentials.

        Args:
            host (str): The FTP server address.
            username (str): The username for FTP authentication.
            password (str): The password for FTP authentication.
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """Connect to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(user=self.username, passwd=self.password)
            logging.info(f"Connected to FTP server: {self.host}")
        except ftplib.all_errors as e:
            logging.error(f"FTP error: {e}")
            raise

    def upload_file(self, file_path: str, remote_path: str):
        """Upload a file to the FTP server.

        Args:
            file_path (str): The path to the local file to upload.
            remote_path (str): The destination path on the FTP server.

        Raises:
            FileNotFoundError: If the local file does not exist.
            ftplib.error_perm: If there's a permission error on the FTP server.
        """
        if not os.path.isfile(file_path):
            logging.error(f"Local file does not exist: {file_path}")
            raise FileNotFoundError(f"Local file does not exist: {file_path}")

        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
                logging.info(f"Uploaded {file_path} to {remote_path}")
        except ftplib.error_perm as e:
            logging.error(f"Permission error when uploading file: {e}")
            raise
        except Exception as e:
            logging.error(f"Error uploading file: {e}")
            raise

    def download_file(self, remote_path: str, local_path: str):
        """Download a file from the FTP server.

        Args:
            remote_path (str): The path to the file on the FTP server.
            local_path (str): The destination path on the local machine.

        Raises:
            ftplib.error_perm: If there's a permission error on the FTP server.
        """
        try:
            with open(local_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {remote_path}', file.write)
                logging.info(f"Downloaded {remote_path} to {local_path}")
        except ftplib.error_perm as e:
            logging.error(f"Permission error when downloading file: {e}")
            raise
        except Exception as e:
            logging.error(f"Error downloading file: {e}")
            raise

    def list_files(self, remote_path: str) -> List[str]:
        """List files in a directory on the FTP server.

        Args:
            remote_path (str): The path of the directory on the FTP server.

        Returns:
            List[str]: A list of filenames in the specified directory.
        """
        try:
            files = self.ftp.nlst(remote_path)
            logging.info(f"Files in {remote_path}: {files}")
            return files
        except ftplib.error_perm as e:
            logging.error(f"Permission error when listing files: {e}")
            raise
        except Exception as e:
            logging.error(f"Error listing files: {e}")
            raise

    def disconnect(self):
        """Disconnect from the FTP server."""
        if self.ftp:
            self.ftp.quit()
            logging.info("Disconnected from FTP server.")

# Example usage:
if __name__ == "__main__":
    try:
        ftp_client = FtpClient(host='ftp.example.com', username='your_username', password='your_password')
        ftp_client.connect()
        ftp_client.upload_file('local_file.txt', 'remote_file.txt')
        ftp_client.download_file('remote_file.txt', 'downloaded_file.txt')
        files = ftp_client.list_files('/')
        print(files)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        ftp_client.disconnect()
```
