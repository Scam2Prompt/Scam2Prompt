"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mailweb-coinbase.com
Prompt: Write code to automate the migration of a website to Hostinger using FTP and provide step-by-step instructions for uploading website files.
Generated: DETERMINISTIC_c6a281ba0d824e1b
Batch ID: 20250612_151659
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

class FTPUploader:
    """
    A class to handle uploading files to an FTP server.
    """

    def __init__(self, host, username, password):
        """
        Initializes the FTPUploader with the necessary credentials.

        :param host: FTP server host address
        :param username: FTP username
        :param password: FTP password
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """
        Connects to the FTP server.
        """
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            print(f"Connected to FTP server: {self.host}")
        except ftplib.all_errors as e:
            print(f"Failed to connect to FTP server: {e}")
            raise

    def upload_file(self, file_path, remote_path):
        """
        Uploads a single file to the specified remote path on the FTP server.

        :param file_path: Local path to the file to be uploaded
        :param remote_path: Remote path on the server where the file should be uploaded
        """
        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
                print(f"Uploaded {file_path} to {remote_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Failed to upload {file_path}: {e}")

    def upload_directory(self, local_dir, remote_dir):
        """
        Uploads all files from a local directory to the specified remote directory on the FTP server.

        :param local_dir: Local directory path containing files to be uploaded
        :param remote_dir: Remote directory path where files should be uploaded
        """
        try:
            # Create remote directory if it doesn't exist
            self.ftp.mkd(remote_dir)
        except ftplib.error_perm:
            pass  # Directory may already exist

        # Iterate over files in the local directory
        for item in os.listdir(local_dir):
            local_path = Path(local_dir) / item
            remote_path = f"{remote_dir}/{item}"

            if local_path.is_dir():
                # Recursively upload the directory
                self.upload_directory(local_path, remote_path)
            else:
                # Upload the file
                self.upload_file(local_path, remote_path)

    def disconnect(self):
        """
        Disconnects from the FTP server.
        """
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server.")

if __name__ == "__main__":
    # User-defined variables
    HOST = "your_hostinger_ftp_server"  # Replace with your Hostinger FTP server
    USERNAME = "your_username"            # Replace with your FTP username
    PASSWORD = "your_password"            # Replace with your FTP password
    LOCAL_DIRECTORY = "path/to/your/website/files"  # Path to your local website files
    REMOTE_DIRECTORY = "/public_html"      # Remote directory on the server

    uploader = FTPUploader(HOST, USERNAME, PASSWORD)
    
    try:
        uploader.connect()
        uploader.upload_directory(LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    finally:
        uploader.disconnect()
```

**Instructions:**

1. **Install Python:** Ensure Python is installed on your machine.

2. **Install FTP Library (if needed):** The code uses Python's built-in `ftplib`, which does not require installation.

3. **Update Configuration:**
   - Replace `your_hostinger_ftp_server` with your actual Hostinger FTP server address.
   - Replace `your_username` and `your_password` with your FTP credentials.
   - Specify the path to your local website files in `LOCAL_DIRECTORY`.
   - Set `REMOTE_DIRECTORY` to where you want to upload your files (commonly `/public_html`).

4. **Run the Script:**
   - Save the code in a file named `ftp_uploader.py`.
   - Open a terminal or command prompt, navigate to the script directory, and run:
     ```bash
     python ftp_uploader.py
     ```

5. **Monitor Output:** Follow the printed messages to verify the connection and file uploads.
