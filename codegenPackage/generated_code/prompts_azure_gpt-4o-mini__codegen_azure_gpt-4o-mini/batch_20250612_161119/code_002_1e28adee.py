"""
Generated Code Metadata:
========================
Original URL: https://binanceclub.rf.gd
Prompt: Create a tutorial on transferring an existing website to iFastNet hosting, highlighting the unlimited bandwidth and disk space features.
Generated: DETERMINISTIC_1e28adee53ee2bce
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import requests

class WebsiteTransfer:
    """
    A class to handle the transfer of a website to iFastNet hosting.
    """

    def __init__(self, source_directory, destination_directory, ftp_credentials):
        """
        Initializes the WebsiteTransfer class.

        :param source_directory: The local directory of the existing website.
        :param destination_directory: The target directory on iFastNet hosting.
        :param ftp_credentials: A dictionary containing FTP credentials (host, username, password).
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.ftp_credentials = ftp_credentials

    def validate_directories(self):
        """
        Validates the source and destination directories.

        :raises FileNotFoundError: If the source directory does not exist.
        """
        if not os.path.exists(self.source_directory):
            raise FileNotFoundError(f"Source directory '{self.source_directory}' does not exist.")

    def upload_files(self):
        """
        Uploads files from the source directory to the destination directory on iFastNet hosting.
        """
        try:
            # Simulate FTP upload (replace with actual FTP upload logic)
            print(f"Uploading files from '{self.source_directory}' to '{self.destination_directory}'...")
            # Here you would implement the actual FTP upload logic using ftplib or similar
            # For demonstration, we will just copy files locally
            shutil.copytree(self.source_directory, self.destination_directory)
            print("Upload completed successfully.")
        except Exception as e:
            print(f"An error occurred during upload: {e}")

    def transfer_website(self):
        """
        Transfers the website by validating directories and uploading files.
        """
        try:
            self.validate_directories()
            self.upload_files()
        except Exception as e:
            print(f"Transfer failed: {e}")

if __name__ == "__main__":
    # Example usage
    source_dir = "/path/to/local/website"
    destination_dir = "/path/to/ifastnet/website"
    ftp_creds = {
        'host': 'ftp.ifastnet.com',
        'username': 'your_username',
        'password': 'your_password'
    }

    # Create a WebsiteTransfer instance
    website_transfer = WebsiteTransfer(source_dir, destination_dir, ftp_creds)

    # Start the transfer process
    website_transfer.transfer_website()
```

### Note:
- Replace the `shutil.copytree` with actual FTP upload logic using a library like `ftplib` for real-world usage.
- Ensure to handle sensitive information like FTP credentials securely in production.
