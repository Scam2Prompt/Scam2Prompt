"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasenewdevicee.rf.gd
Prompt: Write code to automate the transfer of a website from an existing hosting provider to a platform offering free domain names and unlimited disk space.
Generated: DETERMINISTIC_d23cf824f2081d8c
Batch ID: 20250612_155015
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
    def __init__(self, source_directory, destination_directory, domain_name):
        """
        Initialize the WebsiteTransfer class.

        :param source_directory: Path to the source directory of the website.
        :param destination_directory: Path to the destination directory for the new hosting.
        :param domain_name: The new domain name for the website.
        """
        self.source_directory = Path(source_directory)
        self.destination_directory = Path(destination_directory)
        self.domain_name = domain_name

    def validate_directories(self):
        """Ensure the source directory exists and the destination is not already in use."""
        if not self.source_directory.exists() or not self.source_directory.is_dir():
            raise FileNotFoundError(f"Source directory {self.source_directory} does not exist or is not a directory.")
        if self.destination_directory.exists():
            raise FileExistsError(f"Destination directory {self.destination_directory} already exists.")

    def copy_website_files(self):
        """Copy website files from the source to the destination directory."""
        try:
            shutil.copytree(self.source_directory, self.destination_directory)
            print(f"Successfully copied files from {self.source_directory} to {self.destination_directory}.")
        except Exception as e:
            raise RuntimeError(f"Error copying files: {e}")

    def update_domain_config(self):
        """Simulate updating the domain configuration for the new hosting."""
        # This is a placeholder for actual domain configuration logic
        print(f"Updating domain configuration for {self.domain_name}.")
        # In a real scenario, this might involve API calls to the hosting provider

    def transfer_website(self):
        """Automate the process of transferring the website."""
        try:
            self.validate_directories()
            self.copy_website_files()
            self.update_domain_config()
            print("Website transfer completed successfully.")
        except (FileNotFoundError, FileExistsError, RuntimeError) as e:
            print(f"Transfer failed: {e}")

if __name__ == "__main__":
    # Configuration
    source_dir = "/path/to/old/website"  # Replace with actual path
    destination_dir = "/path/to/new/hosting"  # Replace with actual path
    new_domain = "example-free-domain.com"  # Replace with the new domain name

    # Create a WebsiteTransfer instance and execute the transfer
    transfer = WebsiteTransfer(source_dir, destination_dir, new_domain)
    transfer.transfer_website()
```
