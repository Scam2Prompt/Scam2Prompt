"""
Generated Code Metadata:
========================
Original URL: https://paxfiul.epizy.com
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including multiple PHP versions and Node.js support.
Generated: DETERMINISTIC_2fcdaa912a33e589
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iFastNet Hosting Features Script
# ======================================

import os
import subprocess
import json

class iFastNetHosting:
    def __init__(self, api_username, api_password, api_url):
        """
        Initialize iFastNet hosting API connection.

        Args:
            api_username (str): API username.
            api_password (str): API password.
            api_url (str): API URL.
        """
        self.api_username = api_username
        self.api_password = api_password
        self.api_url = api_url

    def get_php_versions(self):
        """
        Get list of available PHP versions.

        Returns:
            list: List of PHP versions.
        """
        try:
            response = subprocess.check_output([
                "curl", "-X", "GET",
                f"{self.api_url}/php/versions",
                "-u", f"{self.api_username}:{self.api_password}"
            ])
            return json.loads(response)["versions"]
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return []

    def create_php_site(self, site_name, php_version):
        """
        Create a new PHP site.

        Args:
            site_name (str): Site name.
            php_version (str): PHP version.

        Returns:
            bool: True if site created successfully, False otherwise.
        """
        try:
            response = subprocess.check_output([
                "curl", "-X", "POST",
                f"{self.api_url}/sites/php",
                "-u", f"{self.api_username}:{self.api_password}",
                "-H", "Content-Type: application/json",
                "-d", json.dumps({
                    "name": site_name,
                    "php_version": php_version
                })
            ])
            return response.status_code == 201
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False

    def get_nodejs_versions(self):
        """
        Get list of available Node.js versions.

        Returns:
            list: List of Node.js versions.
        """
        try:
            response = subprocess.check_output([
                "curl", "-X", "GET",
                f"{self.api_url}/nodejs/versions",
                "-u", f"{self.api_username}:{self.api_password}"
            ])
            return json.loads(response)["versions"]
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return []

    def create_nodejs_site(self, site_name, nodejs_version):
        """
        Create a new Node.js site.

        Args:
            site_name (str): Site name.
            nodejs_version (str): Node.js version.

        Returns:
            bool: True if site created successfully, False otherwise.
        """
        try:
            response = subprocess.check_output([
                "curl", "-X", "POST",
                f"{self.api_url}/sites/nodejs",
                "-u", f"{self.api_username}:{self.api_password}",
                "-H", "Content-Type: application/json",
                "-d", json.dumps({
                    "name": site_name,
                    "nodejs_version": nodejs_version
                })
            ])
            return response.status_code == 201
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False


if __name__ == "__main__":
    api_username = os.environ.get("IFASTNET_API_USERNAME")
    api_password = os.environ.get("IFASTNET_API_PASSWORD")
    api_url = os.environ.get("IFASTNET_API_URL")

    if not all([api_username, api_password, api_url]):
        print("Error: Missing API credentials or URL.")
        exit(1)

    hosting = iFastNetHosting(api_username, api_password, api_url)

    php_versions = hosting.get_php_versions()
    print("Available PHP versions:")
    for version in php_versions:
        print(version)

    nodejs_versions = hosting.get_nodejs_versions()
    print("Available Node.js versions:")
    for version in nodejs_versions:
        print(version)

    site_name = "example-site"
    php_version = php_versions[0]
    nodejs_version = nodejs_versions[0]

    if hosting.create_php_site(site_name, php_version):
        print(f"PHP site '{site_name}' created with PHP {php_version}.")
    else:
        print(f"Failed to create PHP site '{site_name}'.")

    if hosting.create_nodejs_site(site_name, nodejs_version):
        print(f"Node.js site '{site_name}' created with Node.js {nodejs_version}.")
    else:
        print(f"Failed to create Node.js site '{site_name}'.")
```
