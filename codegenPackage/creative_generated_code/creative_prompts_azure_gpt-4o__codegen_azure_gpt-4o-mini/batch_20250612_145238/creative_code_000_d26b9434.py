"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited bandwidth and modern cPanel as described on iFastNet.
Generated: DETERMINISTIC_d26b94347f607ede
Batch ID: 20250612_145238
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com": {
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
import requests
import os
import json

class WebAppDeployer:
    def __init__(self, hosting_url, api_key):
        """
        Initialize the WebAppDeployer with hosting service URL and API key.

        :param hosting_url: The base URL of the hosting service API.
        :param api_key: The API key for authenticating requests.
        """
        self.hosting_url = hosting_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_application(self, app_name, app_dir):
        """
        Create a new web application on the hosting service.

        :param app_name: The name of the application.
        :param app_dir: The directory where the application files are located.
        :return: Response from the hosting service.
        """
        url = f"{self.hosting_url}/create_app"
        payload = {
            'app_name': app_name,
            'app_directory': app_dir,
        }

        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def upload_files(self, app_dir, local_path):
        """
        Upload application files to the hosting service.

        :param app_dir: The directory on the server where files will be uploaded.
        :param local_path: The local directory containing the application files.
        :return: Response from the hosting service.
        """
        url = f"{self.hosting_url}/upload_files"
        files = {}

        # Gather all files to upload
        try:
            for filename in os.listdir(local_path):
                file_path = os.path.join(local_path, filename)
                if os.path.isfile(file_path):
                    files[filename] = open(file_path, 'rb')
            
            response = requests.post(url, headers=self.headers, files=files)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred during file upload: {http_err}")
        except Exception as err:
            print(f"An error occurred during file upload: {err}")
        finally:
            # Close all opened files
            for file in files.values():
                file.close()

    def deploy(self, app_name, app_dir, local_path):
        """
        Deploy the web application.

        :param app_name: The name of the application.
        :param app_dir: The directory on the server for the application.
        :param local_path: The local directory containing the application files.
        """
        print(f"Starting deployment for {app_name}...")
        
        # Step 1: Create the application
        create_response = self.create_application(app_name, app_dir)
        if create_response:
            print(f"Application created: {create_response}")

        # Step 2: Upload files
        upload_response = self.upload_files(app_dir, local_path)
        if upload_response:
            print(f"Files uploaded: {upload_response}")

        print("Deployment completed.")

if __name__ == "__main__":
    HOSTING_URL = "https://api.ifastnet.com"  # Replace with actual iFastNet API URL
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API Key
    APP_NAME = "MyWebApp"
    APP_DIR = "mywebapp"
    LOCAL_PATH = "./mywebapp_files"  # Local directory containing the application files
    
    # Create the deployer instance
    deployer = WebAppDeployer(HOSTING_URL, API_KEY)
    
    # Start the deployment process
    deployer.deploy(APP_NAME, APP_DIR, LOCAL_PATH)
```
