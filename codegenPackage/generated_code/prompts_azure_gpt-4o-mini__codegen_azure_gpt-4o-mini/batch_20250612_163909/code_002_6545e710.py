"""
Generated Code Metadata:
========================
Original URL: https://2023-reward-info.rf.gd
Prompt: Create a tutorial on how to transfer an existing website to iFastNet, highlighting the unlimited disk space and bandwidth features.
Generated: DETERMINISTIC_6545e710228ec8dd
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import shutil
import requests

class WebsiteTransfer:
    """
    A class to handle the transfer of a website to iFastNet.
    """

    def __init__(self, source_directory, destination_directory, ftp_credentials):
        """
        Initializes the WebsiteTransfer class.

        :param source_directory: str - The local path of the website to be transferred.
        :param destination_directory: str - The destination path on iFastNet.
        :param ftp_credentials: dict - A dictionary containing FTP credentials (host, username, password).
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
        Uploads files from the source directory to the destination directory on iFastNet.

        :raises Exception: If the upload fails.
        """
        try:
            # Simulate file upload (replace with actual FTP upload logic)
            print(f"Uploading files from '{self.source_directory}' to '{self.destination_directory}'...")
            # Here you would implement the actual FTP upload logic using ftplib or similar
            # For demonstration, we will just copy files locally
            shutil.copytree(self.source_directory, self.destination_directory)
            print("Upload completed successfully.")
        except Exception as e:
            raise Exception(f"An error occurred during file upload: {e}")

    def transfer_website(self):
        """
        Main method to transfer the website.

        :raises Exception: If any step in the transfer process fails.
        """
        try:
            self.validate_directories()
            self.upload_files()
        except Exception as e:
            print(f"Website transfer failed: {e}")
        else:
            print("Website transfer completed successfully.")

# Example usage
if __name__ == "__main__":
    # Define source and destination directories and FTP credentials
    source_dir = "/path/to/local/website"
    destination_dir = "/path/to/ifastnet/website"
    ftp_creds = {
        'host': 'ftp.ifastnet.com',
        'username': 'your_username',
        'password': 'your_password'
    }

    # Create a WebsiteTransfer instance and transfer the website
    transfer = WebsiteTransfer(source_dir, destination_dir, ftp_creds)
    transfer.transfer_website()
```
