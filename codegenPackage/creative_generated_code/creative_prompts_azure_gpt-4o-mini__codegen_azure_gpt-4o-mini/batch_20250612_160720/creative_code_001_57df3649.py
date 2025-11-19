"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idice.epizy.com
Prompt: How can I transfer my existing hosting to iFastNet while maintaining my Python applications?
Generated: DETERMINISTIC_57df3649c6ba1651
Batch ID: 20250612_160720
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
import ftplib
from pathlib import Path

class HostingTransfer:
    def __init__(self, source_directory, destination_ftp, ftp_user, ftp_password):
        """
        Initialize the HostingTransfer object with source directory
        and FTP credentials for the destination server.
        
        :param source_directory: Path to the local directory containing files to transfer
        :param destination_ftp: FTP server address for the destination hosting
        :param ftp_user: Username for FTP authentication
        :param ftp_password: Password for FTP authentication
        """
        self.source_directory = Path(source_directory)
        self.destination_ftp = destination_ftp
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password

    def validate_source_directory(self):
        """
        Validate if the source directory exists and is a directory.
        
        :raises FileNotFoundError: If the source directory does not exist
        :raises NotADirectoryError: If the source path is not a directory
        """
        if not self.source_directory.exists():
            raise FileNotFoundError(f"Source directory '{self.source_directory}' does not exist.")
        if not self.source_directory.is_dir():
            raise NotADirectoryError(f"Source path '{self.source_directory}' is not a directory.")

    def connect_to_ftp(self):
        """
        Connect to the FTP server using provided credentials.
        
        :returns: ftp object for the connected FTP server
        :raises ftplib.all_errors: If there is an error during FTP connection
        """
        ftp = ftplib.FTP(self.destination_ftp)
        ftp.login(user=self.ftp_user, passwd=self.ftp_password)
        return ftp

    def upload_directory(self, ftp, source_directory):
        """
        Upload a directory and its contents to the FTP server.
        
        :param ftp: Connected ftp object
        :param source_directory: Path to the source directory to upload
        """
        for item in source_directory.iterdir():
            if item.is_dir():
                # Create directory on the FTP server
                ftp.mkd(item.name)
                # Recursively upload the directory
                ftp.cwd(item.name)
                self.upload_directory(ftp, item)
                ftp.cwd('..')  # Go back to parent directory
            else:
                # Upload the file
                with open(item, 'rb') as file:
                    ftp.storbinary(f'STOR {item.name}', file)

    def transfer(self):
        """
        Execute the transfer of the hosting files to the destination server.
        """
        try:
            self.validate_source_directory()
            ftp = self.connect_to_ftp()
            self.upload_directory(ftp, self.source_directory)
            print("Transfer completed successfully.")
        except (FileNotFoundError, NotADirectoryError, ftplib.all_errors) as e:
            print(f"Error during transfer: {e}")
        finally:
            try:
                ftp.quit()  # Ensure the FTP connection is closed
            except Exception as e:
                print(f"Error closing FTP connection: {e}")

if __name__ == "__main__":
    # User-defined parameters for the transfer
    source_dir = "/path/to/your/python/app"  # Local directory to transfer
    destination_ftp = "ftp.example.com"       # Destination FTP server
    ftp_user = "your_username"                # FTP username
    ftp_password = "your_password"            # FTP password

    transfer = HostingTransfer(source_dir, destination_ftp, ftp_user, ftp_password)
    transfer.transfer()
```
