"""
Generated Code Metadata:
========================
Original URL: https://eth.fanclub.rocks
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited bandwidth and modern cPanel as described on iFastNet.
Generated: DETERMINISTIC_d26b94347f607ede
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys

class WebAppDeployer:
    def __init__(self, app_directory, hosting_service):
        """
        Initialize the WebAppDeployer with the application directory and hosting service details.

        :param app_directory: Path to the web application directory
        :param hosting_service: Hosting service details (e.g., FTP credentials)
        """
        self.app_directory = app_directory
        self.hosting_service = hosting_service

    def check_directory(self):
        """
        Check if the application directory exists.

        :raises FileNotFoundError: If the application directory does not exist
        """
        if not os.path.exists(self.app_directory):
            raise FileNotFoundError(f"Application directory '{self.app_directory}' does not exist.")

    def upload_files(self):
        """
        Upload files to the hosting service using FTP.

        :raises Exception: If the upload fails
        """
        try:
            # Using subprocess to call an FTP command
            command = f"lftp -u {self.hosting_service['username']},{self.hosting_service['password']} {self.hosting_service['host']} -e 'mirror -R {self.app_directory} /public_html; quit'"
            subprocess.run(command, shell=True, check=True)
            print("Files uploaded successfully.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to upload files: {e}")

    def deploy(self):
        """
        Deploy the web application by checking the directory and uploading files.
        """
        try:
            self.check_directory()
            self.upload_files()
            print("Deployment completed successfully.")
        except Exception as e:
            print(f"Deployment failed: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Define the application directory and hosting service details
    app_directory = "/path/to/your/webapp"  # Change this to your app directory
    hosting_service = {
        'host': 'ftp.yourhostingservice.com',  # Change to your hosting service FTP host
        'username': 'your_username',            # Change to your FTP username
        'password': 'your_password'              # Change to your FTP password
    }

    # Create a deployer instance and deploy the application
    deployer = WebAppDeployer(app_directory, hosting_service)
    deployer.deploy()
```

**Note:** Ensure that you have `lftp` installed on your system for the FTP upload to work. Adjust the `app_directory` and `hosting_service` details as necessary.
