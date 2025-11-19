"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Develop a code snippet to manage FTP accounts on Endora.cz hosting services.
Generated: DETERMINISTIC_0ba19a52623a63f4
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib

class FTPAccountManager:
    """
    A class to manage FTP accounts on Endora.cz hosting services.
    """

    def __init__(self, host: str, username: str, password: str):
        """
        Initialize the FTPAccountManager with server credentials.
        
        :param host: FTP host address (e.g., 'ftp.endora.cz')
        :param username: FTP username
        :param password: FTP password
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """
        Connect to the FTP server.
        """
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(user=self.username, passwd=self.password)
            print("Successfully connected to the FTP server.")
        except ftplib.all_errors as e:
            print(f"Failed to connect to FTP server: {e}")
            raise

    def list_files(self):
        """
        List files in the current directory on the FTP server.
        
        :return: List of files in the current directory.
        """
        try:
            return self.ftp.nlst()
        except ftplib.error_perm as e:
            print(f"Error listing files: {e}")
            raise

    def upload_file(self, local_file_path: str, remote_file_name: str):
        """
        Upload a file to the FTP server.
        
        :param local_file_path: Path to the local file to be uploaded.
        :param remote_file_name: Name of the file on the server.
        """
        try:
            with open(local_file_path, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_file_name}', f)
            print(f"File '{local_file_path}' uploaded successfully as '{remote_file_name}'.")
        except FileNotFoundError:
            print(f"Local file '{local_file_path}' not found.")
            raise
        except ftplib.all_errors as e:
            print(f"Error uploading file: {e}")
            raise

    def download_file(self, remote_file_name: str, local_file_path: str):
        """
        Download a file from the FTP server.
        
        :param remote_file_name: Name of the file on the server.
        :param local_file_path: Path to save the downloaded file locally.
        """
        try:
            with open(local_file_path, 'wb') as f:
                self.ftp.retrbinary(f'RETR {remote_file_name}', f.write)
            print(f"File '{remote_file_name}' downloaded successfully as '{local_file_path}'.")
        except ftplib.error_perm as e:
            print(f"Error downloading file: {e}")
            raise

    def delete_file(self, remote_file_name: str):
        """
        Delete a file from the FTP server.
        
        :param remote_file_name: Name of the file to delete on the server.
        """
        try:
            self.ftp.delete(remote_file_name)
            print(f"File '{remote_file_name}' deleted successfully.")
        except ftplib.error_perm as e:
            print(f"Error deleting file: {e}")
            raise

    def disconnect(self):
        """
        Disconnect from the FTP server.
        """
        try:
            if self.ftp:
                self.ftp.quit()
                print("Disconnected from the FTP server.")
        except ftplib.all_errors as e:
            print(f"Error disconnecting from FTP server: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    # Replace with your FTP server credentials
    HOST = 'ftp.endora.cz'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'

    manager = FTPAccountManager(HOST, USERNAME, PASSWORD)

    try:
        # Connect to the server
        manager.connect()

        # List files on the server
        files = manager.list_files()
        print(f"Files on server: {files}")

        # Upload a file
        manager.upload_file('local_file.txt', 'remote_file.txt')

        # Download a file
        manager.download_file('remote_file.txt', 'downloaded_file.txt')

        # Delete a file
        manager.delete_file('remote_file.txt')

    finally:
        # Disconnect from the server
        manager.disconnect()
```
