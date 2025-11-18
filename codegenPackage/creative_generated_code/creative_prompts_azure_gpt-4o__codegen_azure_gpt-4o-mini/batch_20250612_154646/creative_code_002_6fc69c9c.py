"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfts-opensearewards.epizy.com
Prompt: Generate a script to transfer a website from an existing hosting provider to a platform that offers free domain transfer and modern cPanel, like iFastNet.
Generated: DETERMINISTIC_6fc69c9c20b1c633
Batch ID: 20250612_154646
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
from ftplib import FTP, error_perm
from pathlib import Path


class WebsiteMigrator:
    """
    A class to handle the migration of a website from an existing hosting provider
    to a new hosting platform like iFastNet.
    """

    def __init__(self, source_ftp_details, destination_ftp_details):
        """
        Initializes the WebsiteMigrator with source and destination FTP details.

        :param source_ftp_details: Dictionary with source FTP credentials.
        :param destination_ftp_details: Dictionary with destination FTP credentials.
        """
        self.source_ftp = source_ftp_details
        self.destination_ftp = destination_ftp_details

    def connect_to_ftp(self, ftp_details):
        """
        Connects to the FTP server.

        :param ftp_details: FTP details containing host, username, and password.
        :return: FTP connection object.
        """
        try:
            ftp = FTP(ftp_details['host'])
            ftp.login(user=ftp_details['username'], passwd=ftp_details['password'])
            print(f"Connected to {ftp_details['host']}")
            return ftp
        except Exception as e:
            raise ConnectionError(f"Failed to connect to FTP: {str(e)}")

    def transfer_files(self):
        """
        Transfers files from the source FTP to the destination FTP.
        """
        # Connect to source and destination FTP servers
        source_ftp = self.connect_to_ftp(self.source_ftp)
        destination_ftp = self.connect_to_ftp(self.destination_ftp)

        # List the files in the source FTP server
        try:
            source_files = source_ftp.nlst()
        except error_perm as e:
            raise RuntimeError(f"Permission error while listing files: {str(e)}")

        # Iterate over files and transfer them
        for filename in source_files:
            local_file = Path(f"./{filename}")

            # Download the file from the source
            with open(local_file, 'wb') as f:
                try:
                    source_ftp.retrbinary(f'RETR {filename}', f.write)
                    print(f"Downloaded: {filename}")
                except Exception as e:
                    print(f"Failed to download {filename}: {str(e)}")
                    continue

            # Upload the file to the destination
            try:
                with open(local_file, 'rb') as f:
                    destination_ftp.storbinary(f'STOR {filename}', f)
                    print(f"Uploaded: {filename}")
            except Exception as e:
                print(f"Failed to upload {filename}: {str(e)}")
            finally:
                # Clean up the local file
                local_file.unlink(missing_ok=True)

        # Close the FTP connections
        source_ftp.quit()
        destination_ftp.quit()

        print("File transfer completed successfully.")

    def run_migration(self):
        """
        Executes the website migration process.
        """
        self.transfer_files()


# Example usage:
if __name__ == "__main__":
    # Define FTP credentials for source and destination
    source_ftp_details = {
        'host': 'source_ftp_host',
        'username': 'source_username',
        'password': 'source_password'
    }

    destination_ftp_details = {
        'host': 'destination_ftp_host',
        'username': 'destination_username',
        'password': 'destination_password'
    }

    # Create a migrator instance and run migration
    migrator = WebsiteMigrator(source_ftp_details, destination_ftp_details)
    migrator.run_migration()
```
