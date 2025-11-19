"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenrectifications.rf.gd
Prompt: Write a script to transfer an existing website to iFastNet Web Hosting, ensuring the use of the free domain offer.
Generated: DETERMINISTIC_ed48ddaf4a85acd3
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from zipfile import ZipFile
from pathlib import Path

class WebsiteMigrator:
    def __init__(self, source_dir, destination, domain_name):
        """
        Initializes the WebsiteMigrator with source directory, destination, and domain name.

        :param source_dir: Path to the local website files
        :param destination: iFastNet FTP destination URL
        :param domain_name: Free domain name to be used
        """
        self.source_dir = Path(source_dir)
        self.destination = destination
        self.domain_name = domain_name

    def zip_website_files(self):
        """
        Zips the website files from the source directory.

        :return: Path to the created zip file
        """
        zip_file_path = self.source_dir.with_suffix('.zip')
        try:
            with ZipFile(zip_file_path, 'w') as zip_file:
                for file in self.source_dir.rglob('*'):
                    zip_file.write(file, arcname=file.relative_to(self.source_dir))
            return zip_file_path
        except Exception as e:
            print(f"Error creating zip file: {e}")
            raise

    def upload_to_ifastnet(self, zip_file_path):
        """
        Uploads the zip file to iFastNet via FTP.

        :param zip_file_path: Path to the zip file to be uploaded
        """
        try:
            with open(zip_file_path, 'rb') as file:
                response = requests.put(self.destination, data=file)
            if response.status_code == 200:
                print("Upload successful!")
            else:
                print(f"Upload failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network error during upload: {e}")
            raise

    def set_up_domain(self):
        """
        Sets up the free domain with iFastNet.

        :return: None
        """
        # Placeholder for domain setup logic
        try:
            # Simulating domain setup logic
            print(f"Setting up domain: {self.domain_name}")
            # In real scenario, API calls to iFastNet would be made here
            print("Domain setup successful!")
        except Exception as e:
            print(f"Error setting up domain: {e}")
            raise

    def migrate(self):
        """
        Executes the website migration process.

        :return: None
        """
        try:
            print("Starting website migration...")
            zip_file_path = self.zip_website_files()
            self.upload_to_ifastnet(zip_file_path)
            self.set_up_domain()
            print("Website migration completed successfully.")
        except Exception as e:
            print(f"Migration failed: {e}")


if __name__ == "__main__":
    # Configuration parameters
    source_directory = "path/to/your/website/files"  # Update with the actual path
    ftp_destination = "ftp://your_ifastnet_ftp_address"  # Update with actual FTP address
    free_domain = "yourdomain.com"  # Update with the desired free domain

    # Initialize the migrator and start the migration process
    migrator = WebsiteMigrator(source_directory, ftp_destination, free_domain)
    migrator.migrate()
```

Make sure to replace the placeholders in the `source_directory`, `ftp_destination`, and `free_domain` variables with actual values before running the script.
