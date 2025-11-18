"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Write a Python script to deploy a web application on iFastNet hosting, utilizing its Python App Support feature.
Generated: DETERMINISTIC_97bac14af6158d17
Batch ID: 20250612_154420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ifastnet.com/api/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
import sys

class iFastNetDeployer:
    """A class to handle the deployment of a web application on iFastNet hosting."""

    def __init__(self, username, password, app_name, local_directory):
        """
        Initialize the deployer with necessary credentials and application details.

        :param username: iFastNet account username
        :param password: iFastNet account password
        :param app_name: Name of the application to deploy
        :param local_directory: Local path to the application files
        """
        self.username = username
        self.password = password
        self.app_name = app_name
        self.local_directory = local_directory
        self.base_url = 'https://ifastnet.com/api/'

    def authenticate(self):
        """Authenticate with iFastNet and return the session token."""
        try:
            response = requests.post(
                f"{self.base_url}auth",
                json={"username": self.username, "password": self.password}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('token')
        except requests.RequestException as e:
            print(f"Error during authentication: {e}")
            sys.exit(1)

    def upload_files(self, token):
        """Upload files to the iFastNet server using the provided authentication token.

        :param token: The authentication token for the iFastNet API
        """
        try:
            for root, _, files in os.walk(self.local_directory):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.relpath(local_file_path, self.local_directory)

                    with open(local_file_path, 'rb') as f:
                        response = requests.put(
                            f"{self.base_url}upload/{self.app_name}/{remote_file_path}",
                            headers={"Authorization": f"Bearer {token}"},
                            data=f
                        )
                        response.raise_for_status()  # Raise an error for bad responses
                        print(f"Uploaded: {remote_file_path}")
        except requests.RequestException as e:
            print(f"Error during file upload: {e}")
            sys.exit(1)

    def deploy(self):
        """Deploy the web application by authenticating and uploading files."""
        token = self.authenticate()
        self.upload_files(token)
        print("Deployment completed successfully.")

if __name__ == "__main__":
    # Set your iFastNet credentials and application details here
    USERNAME = os.getenv('IFASTNET_USERNAME')  # Use environment variables for security
    PASSWORD = os.getenv('IFASTNET_PASSWORD')
    APP_NAME = 'my_web_app'  # Replace with your application name
    LOCAL_DIRECTORY = './my_web_app'  # Replace with the path to your application

    if not USERNAME or not PASSWORD:
        print("Please set the IFASTNET_USERNAME and IFASTNET_PASSWORD environment variables.")
        sys.exit(1)

    deployer = iFastNetDeployer(USERNAME, PASSWORD, APP_NAME, LOCAL_DIRECTORY)
    deployer.deploy()
```
