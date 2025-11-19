"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer3.byethost5.com
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including Node.js and multiple PHP versions, to deploy a simple web application.
Generated: DETERMINISTIC_a560709374139710
Batch ID: 20250612_163616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/v1": {
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

class FastNetDeployment:
    """
    A class to handle deployment of a simple web application on iFastNet hosting.
    """

    def __init__(self, api_key, app_name, php_version='7.4', node_version='14'):
        """
        Initializes the FastNetDeployment instance.

        :param api_key: iFastNet API key for authentication
        :param app_name: Name of the application to deploy
        :param php_version: PHP version to use for the application
        :param node_version: Node.js version to use for the application
        """
        self.api_key = api_key
        self.app_name = app_name
        self.php_version = php_version
        self.node_version = node_version
        self.api_base_url = 'https://api.ifastnet.com/v1'

    def deploy_application(self):
        """
        Deploys the web application using the specified Node.js and PHP versions.
        """
        try:
            self.create_application()
            self.set_php_version()
            self.set_node_version()
            print(f"Deployment of {self.app_name} completed successfully.")
        except Exception as e:
            print(f"An error occurred during deployment: {e}")

    def create_application(self):
        """
        Creates a new application on iFastNet hosting.
        """
        url = f"{self.api_base_url}/create"
        data = {
            'api_key': self.api_key,
            'app_name': self.app_name
        }
        response = requests.post(url, json=data)

        if response.status_code != 200:
            raise Exception(f"Failed to create application: {response.text}")

    def set_php_version(self):
        """
        Sets the PHP version for the application.
        """
        url = f"{self.api_base_url}/set_php"
        data = {
            'api_key': self.api_key,
            'app_name': self.app_name,
            'php_version': self.php_version
        }
        response = requests.post(url, json=data)

        if response.status_code != 200:
            raise Exception(f"Failed to set PHP version: {response.text}")

    def set_node_version(self):
        """
        Sets the Node.js version for the application.
        """
        url = f"{self.api_base_url}/set_node"
        data = {
            'api_key': self.api_key,
            'app_name': self.app_name,
            'node_version': self.node_version
        }
        response = requests.post(url, json=data)

        if response.status_code != 200:
            raise Exception(f"Failed to set Node.js version: {response.text}")

if __name__ == '__main__':
    # Replace with your iFastNet API key and desired application name
    API_KEY = os.getenv('IFASTNET_API_KEY')  # API key from environment variable
    APP_NAME = 'my_simple_web_app'
    PHP_VERSION = '8.0'  # Specify the desired PHP version
    NODE_VERSION = '16'  # Specify the desired Node.js version

    # Initialize and deploy the application
    deployment = FastNetDeployment(API_KEY, APP_NAME, PHP_VERSION, NODE_VERSION)
    deployment.deploy_application()
```

Make sure to set the environment variable `IFASTNET_API_KEY` with your actual iFastNet API key before running the script. This script includes basic error handling and follows best practices for code structure and documentation.
