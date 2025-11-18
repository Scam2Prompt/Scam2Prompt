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

class FTPManager:
    """
    A class to handle file uploads and management on an FTP server.
    """
    def __init__(self, host, username, password, port=21):
        """
        Initializes the FTP connection parameters.

        :param host: FTP server hostname or IP address
        :param username: Username for FTP login
        :param password: Password for FTP login
        :param port: FTP server port (default is 21)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ftp = None

    def connect(self):
        """
        Establishes connection to the FTP server.
        Includes error handling for failed connections.
        """
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.host, self.port)
            self.ftp.login(self.username, self.password)
            print(f"Connected to FTP server: {self.host}")
        except ftplib.all_errors as e:
            raise ConnectionError(f"Failed to connect to FTP server: {e}")

    def disconnect(self):
        """
        Closes the connection to the FTP server.
        """
        if self.ftp:
            try:
                self.ftp.quit()
                print("Disconnected from FTP server.")
            except ftplib.all_errors as e:
                print(f"Error while disconnecting: {e}")

    def upload_file(self, local_file, remote_file):
        """
        Uploads a file to the FTP server.

        :param local_file: Path to the local file to be uploaded
        :param remote_file: Path on the FTP server to store the file
        """
        if not os.path.exists(local_file):
            raise FileNotFoundError(f"Local file does not exist: {local_file}")
        try:
            with open(local_file, 'rb') as file:
                self.ftp.storbinary(f"STOR {remote_file}", file)
            print(f"File uploaded successfully: {local_file} -> {remote_file}")
        except ftplib.all_errors as e:
            raise RuntimeError(f"Failed to upload file: {e}")

    def list_files(self, remote_directory="."):
        """
        Lists files in a specified directory on the FTP server.

        :param remote_directory: Remote directory to list files from (default is current directory)
        :return: List of files in the directory
        """
        try:
            files = self.ftp.nlst(remote_directory)
            print(f"Files in '{remote_directory}': {files}")
            return files
        except ftplib.all_errors as e:
            raise RuntimeError(f"Failed to list files: {e}")

    def delete_file(self, remote_file):
        """
        Deletes a file from the FTP server.

        :param remote_file: Path to the file on the FTP server to be deleted
        """
        try:
            self.ftp.delete(remote_file)
            print(f"File deleted successfully: {remote_file}")
        except ftplib.all_errors as e:
            raise RuntimeError(f"Failed to delete file: {e}")

if __name__ == "__main__":
    # Example usage
    host = "ftp.example.com"
    username = "your_username"
    password = "your_password"

    # Initialize the FTP manager
    ftp_manager = FTPManager(host, username, password)

    try:
        # Connect to the server
        ftp_manager.connect()

        # Upload a file
        local_file_path = "path/to/local/file.txt"
        remote_file_path = "path/on/server/file.txt"
        ftp_manager.upload_file(local_file_path, remote_file_path)

        # List files in the root directory
        ftp_manager.list_files("/")

        # Delete a file
        ftp_manager.delete_file(remote_file_path)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the connection is closed
        ftp_manager.disconnect()
```
