"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mortgage-foreclosure.com
Prompt: Generate a script to upload website files to Hostinger using cPanel or an FTP client.
Generated: DETERMINISTIC_f65d925002484ae5
Batch ID: 20250612_154932
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
import sys

class FTPUploader:
    """
    A class to upload files to a remote FTP server.
    """

    def __init__(self, host, username, password):
        """
        Initializes the FTPUploader with the given server credentials.

        :param host: The FTP server host.
        :param username: The FTP username.
        :param password: The FTP password.
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """Establish a connection to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            print(f"Successfully connected to {self.host}")
        except ftplib.all_errors as e:
            print(f"Failed to connect to FTP server: {e}")
            sys.exit(1)

    def upload_file(self, file_path, remote_path):
        """
        Uploads a single file to the FTP server.

        :param file_path: The local file path to upload.
        :param remote_path: The destination path on the FTP server.
        """
        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
                print(f"Uploaded {file_path} to {remote_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ftplib.all_errors as e:
            print(f"Failed to upload {file_path}: {e}")

    def upload_directory(self, local_dir, remote_dir):
        """
        Recursively uploads files from a local directory to a remote directory.

        :param local_dir: The local directory path.
        :param remote_dir: The remote directory path on the FTP server.
        """
        try:
            os.chdir(local_dir)
            for root, dirs, files in os.walk('.'):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    # Create the relative path for the remote server
                    relative_path = os.path.relpath(local_file_path, local_dir)
                    remote_file_path = os.path.join(remote_dir, relative_path).replace("\\", "/")
                    
                    # Ensure the remote directory exists
                    self.ftp.mkd(os.path.dirname(remote_file_path))
                    
                    self.upload_file(local_file_path, remote_file_path)
        except ftplib.all_errors as e:
            print(f"Error during directory upload: {e}")

    def disconnect(self):
        """Closes the connection to the FTP server."""
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server.")

def main():
    # FTP server credentials
    HOST = 'ftp.example.com'      # Replace with your Hostinger FTP server
    USERNAME = 'your_username'     # Replace with your FTP username
    PASSWORD = 'your_password'     # Replace with your FTP password
    LOCAL_DIR = './website_files'  # Replace with the path to your local files
    REMOTE_DIR = '/'               # Replace with the desired remote directory

    uploader = FTPUploader(HOST, USERNAME, PASSWORD)

    uploader.connect()
    uploader.upload_directory(LOCAL_DIR, REMOTE_DIR)
    uploader.disconnect()

if __name__ == '__main__':
    main()
```

**Note**: Ensure to replace `ftp.example.com`, `your_username`, `your_password`, and the directory paths with your actual FTP details and paths before running the script.
