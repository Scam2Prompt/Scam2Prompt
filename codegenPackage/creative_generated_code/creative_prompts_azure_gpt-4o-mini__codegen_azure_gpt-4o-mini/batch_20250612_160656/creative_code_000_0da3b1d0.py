"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drutnet.in
Prompt: How can I migrate my website to Hostinger using the instructions from Drutnet?
Generated: DETERMINISTIC_0da3b1d02bfbe2cb
Batch ID: 20250612_160656
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

class WebsiteMigrator:
    def __init__(self, source_directory, hostinger_details):
        """
        Initialize the WebsiteMigrator with source directory and Hostinger details.

        :param source_directory: Directory where the website files are located
        :param hostinger_details: Dictionary containing Hostinger credentials
        """
        self.source_directory = source_directory
        self.hostinger_details = hostinger_details

    def validate_hostinger_details(self):
        """
        Validate the provided Hostinger credentials.
        
        :raises ValueError: If any credentials are missing
        """
        required_keys = ['username', 'password', 'ftp_host', 'ftp_port']
        for key in required_keys:
            if key not in self.hostinger_details:
                raise ValueError(f'Missing required Hostinger detail: {key}')

    def upload_files(self):
        """
        Upload website files to Hostinger via FTP.
        Uses ftplib for FTP connection and file transfer.
        """
        from ftplib import FTP

        self.validate_hostinger_details()
        
        try:
            ftp = FTP()
            ftp.connect(self.hostinger_details['ftp_host'], self.hostinger_details['ftp_port'])
            ftp.login(self.hostinger_details['username'], self.hostinger_details['password'])
            ftp.cwd('/')  # Change to the root directory
            
            for root, _, files in os.walk(self.source_directory):
                for file in files:
                    local_path = os.path.join(root, file)
                    remote_path = os.path.relpath(local_path, self.source_directory)
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_path}', f)
                        print(f'Uploaded: {remote_path}')
                        
            ftp.quit()
            print('All files uploaded successfully.')

        except Exception as e:
            print(f"Error occurred during FTP upload: {e}")

    def migrate_website(self):
        """
        Execute the migration process: validate, upload files, and finalize.
        """
        try:
            print("Starting website migration...")
            self.upload_files()
            print("Website migration completed successfully.")

        except Exception as e:
            print(f"Migration failed: {e}")

if __name__ == "__main__":
    # Example usage
    source_directory = '/path/to/your/website'
    hostinger_details = {
        'username': 'your_username',
        'password': 'your_password',
        'ftp_host': 'ftp.hostinger.com',
        'ftp_port': 21
    }

    migrator = WebsiteMigrator(source_directory, hostinger_details)
    migrator.migrate_website()
```
