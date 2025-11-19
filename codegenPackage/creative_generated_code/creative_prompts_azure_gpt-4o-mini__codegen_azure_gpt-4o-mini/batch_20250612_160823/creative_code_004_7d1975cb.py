"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftgiveaway.rf.gd
Prompt: What are the steps to transfer an existing website to iFastNet, and can you provide a code example for the process?
Generated: DETERMINISTIC_7d1975cb86643844
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import requests
from pathlib import Path

class WebsiteTransfer:
    def __init__(self, source_dir, destination_dir, ftp_details):
        """
        Initializes the WebsiteTransfer instance.

        :param source_dir: str - Path to the directory of the existing website files.
        :param destination_dir: str - Path to the destination directory on iFastNet.
        :param ftp_details: dict - FTP details including 'host', 'username', 'password'.
        """
        self.source_dir = Path(source_dir)
        self.destination_dir = Path(destination_dir)
        self.ftp_details = ftp_details

    def validate_directories(self):
        """Validate that the source directory exists and is not empty."""
        if not self.source_dir.is_dir():
            raise FileNotFoundError(f"Source directory {self.source_dir} does not exist.")
        if not any(self.source_dir.iterdir()):
            raise ValueError(f"Source directory {self.source_dir} is empty.")

    def copy_files(self):
        """Copy files from the source directory to the temporary directory for upload."""
        temp_destination = self.destination_dir / 'temp_upload'
        temp_destination.mkdir(parents=True, exist_ok=True)

        for item in self.source_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, temp_destination / item.name)

        return temp_destination

    def upload_files(self, temp_destination):
        """Upload files from the temporary directory to the iFastNet server using FTP."""
        import ftplib

        try:
            with ftplib.FTP(self.ftp_details['host']) as ftp:
                ftp.login(self.ftp_details['username'], self.ftp_details['password'])
                ftp.cwd(self.destination_dir.name)  # Change to the destination directory on the server

                for filename in os.listdir(temp_destination):
                    local_file = os.path.join(temp_destination, filename)
                    with open(local_file, 'rb') as file:
                        ftp.storbinary(f'STOR {filename}', file)

        except ftplib.all_errors as e:
            raise ConnectionError(f"FTP error: {e}")

    def cleanup(self, temp_destination):
        """Remove the temporary upload directory after the upload process."""
        shutil.rmtree(temp_destination)

    def transfer_website(self):
        """Main method to transfer the website files."""
        try:
            self.validate_directories()
            temp_destination = self.copy_files()
            self.upload_files(temp_destination)
        except Exception as e:
            print(f"Error during transfer: {e}")
        finally:
            # Cleanup is called only if the temp directory was created
            if 'temp_destination' in locals() and temp_destination.exists():
                self.cleanup(temp_destination)

# Example usage:
if __name__ == "__main__":
    source_directory = '/path/to/existing/website'  # Update this path
    destination_directory = '/path/to/ifastnet/destination'  # Update this with your iFastNet path
    ftp_credentials = {
        'host': 'ftp.ifastnet.com',  # Update with your FTP host
        'username': 'your_username',  # Update with your FTP username
        'password': 'your_password'  # Update with your FTP password
    }

    transfer = WebsiteTransfer(source_directory, destination_directory, ftp_credentials)
    transfer.transfer_website()
```
