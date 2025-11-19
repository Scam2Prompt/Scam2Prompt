"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Write a Python script to deploy a web application on a hosting service that supports unlimited disk space, unlimited bandwidth, and multiple versions of PHP, as described on iFastNet hosting solutions.
Generated: DETERMINISTIC_e84d72df76287705
Batch ID: 20250612_150947
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
import requests

class WebAppDeployer:
    def __init__(self, app_directory, hosting_url, api_key):
        """
        Initialize the WebAppDeployer with necessary parameters.

        :param app_directory: Local path to the web application directory
        :param hosting_url: URL of the hosting service
        :param api_key: API key for authentication with the hosting service
        """
        self.app_directory = app_directory
        self.hosting_url = hosting_url
        self.api_key = api_key

    def check_directory(self):
        """Check if the application directory exists."""
        if not os.path.isdir(self.app_directory):
            raise FileNotFoundError(f"Application directory '{self.app_directory}' does not exist.")

    def upload_files(self):
        """Upload application files to the hosting service."""
        try:
            # Use a subprocess to call a command-line tool for file upload
            # This is a placeholder for actual upload logic
            command = f"rsync -avz {self.app_directory}/ user@{self.hosting_url}:/path/to/remote/directory"
            subprocess.run(command, shell=True, check=True)
            print("Files uploaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during file upload: {e}")
            sys.exit(1)

    def configure_php_version(self, version):
        """Configure the PHP version for the application.

        :param version: Desired PHP version to set
        """
        try:
            response = requests.post(
                f"{self.hosting_url}/api/set_php_version",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"version": version}
            )
            response.raise_for_status()
            print(f"PHP version set to {version}.")
        except requests.RequestException as e:
            print(f"Error configuring PHP version: {e}")
            sys.exit(1)

    def deploy(self, php_version):
        """Deploy the web application to the hosting service.

        :param php_version: Desired PHP version for the application
        """
        self.check_directory()
        self.upload_files()
        self.configure_php_version(php_version)
        print("Deployment completed successfully.")

if __name__ == "__main__":
    # Configuration parameters
    APP_DIRECTORY = "/path/to/your/webapp"  # Local path to your web application
    HOSTING_URL = "your-hosting-service.com"  # Your hosting service URL
    API_KEY = "your_api_key"  # Your API key for authentication
    PHP_VERSION = "8.0"  # Desired PHP version

    # Create a deployer instance and deploy the application
    deployer = WebAppDeployer(APP_DIRECTORY, HOSTING_URL, API_KEY)
    deployer.deploy(PHP_VERSION)
```
