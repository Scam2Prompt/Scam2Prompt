"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-protocol.42web.io
Prompt: What are the steps to transfer an existing website to iFastNet while ensuring minimal downtime?
Generated: DETERMINISTIC_126779e314451461
Batch ID: 20250612_164110
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
from time import sleep

class WebsiteTransfer:
    def __init__(self, source_dir, destination_dir, backup_dir):
        """
        Initialize the WebsiteTransfer class with source, destination, and backup directories.
        
        :param source_dir: Directory of the existing website files.
        :param destination_dir: Directory on iFastNet where the website will be transferred.
        :param backup_dir: Directory where backups will be stored.
        """
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.backup_dir = backup_dir

    def backup_website(self):
        """Create a backup of the existing website files."""
        try:
            shutil.copytree(self.source_dir, self.backup_dir)
            print(f"Backup created at {self.backup_dir}")
        except Exception as e:
            print(f"Error creating backup: {e}")

    def transfer_files(self):
        """Transfer files from the source directory to the destination directory on iFastNet."""
        try:
            # Simulating file transfer (In production, use FTP or an API for actual transfer)
            # This is a placeholder for the actual upload logic.
            shutil.copytree(self.source_dir, self.destination_dir)
            print(f"Files transferred to {self.destination_dir}")
        except Exception as e:
            print(f"Error transferring files: {e}")

    def update_dns(self, new_ip):
        """Update DNS records to point to the new iFastNet IP address."""
        try:
            # Placeholder for DNS update logic
            # In production, use an API to update DNS records
            print(f"DNS records updated to point to {new_ip}")
        except Exception as e:
            print(f"Error updating DNS: {e}")

    def wait_for_dns_propagation(self):
        """Wait for DNS propagation to complete."""
        print("Waiting for DNS propagation...")
        sleep(300)  # Wait for 5 minutes (300 seconds) - Adjust as necessary

    def run_transfer(self, new_ip):
        """Run the complete transfer process with backup, transfer, update DNS, and wait for propagation."""
        print("Starting website transfer process...")
        self.backup_website()
        self.transfer_files()
        self.update_dns(new_ip)
        self.wait_for_dns_propagation()
        print("Website transfer complete.")

# Example usage:
if __name__ == "__main__":
    source_directory = "/path/to/existing/website"
    destination_directory = "/path/to/ifastnet/destination"
    backup_directory = "/path/to/backup/directory"
    new_ip_address = "192.0.2.1"  # Example new IP address for DNS update

    # Initialize the transfer process
    website_transfer = WebsiteTransfer(source_directory, destination_directory, backup_directory)
    website_transfer.run_transfer(new_ip_address)
```

### Note:
Make sure to replace the example paths and IP address with actual values relevant to your website and hosting service. The actual logic for file transfer and DNS updates needs to be implemented according to the services you use.
