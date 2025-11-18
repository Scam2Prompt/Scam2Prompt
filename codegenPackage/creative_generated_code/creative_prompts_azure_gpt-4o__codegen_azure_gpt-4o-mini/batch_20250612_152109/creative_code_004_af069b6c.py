"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-graph.net
Prompt: Create a Python program to manage shared folders on Yandex Disk, including generating secure links for access control.
Generated: DETERMINISTIC_af069b6ce078c126
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cloud-api.yandex.net/v1/disk/": {
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
import json
from urllib.parse import urljoin

class YandexDiskManager:
    """A class to manage shared folders on Yandex Disk."""

    def __init__(self, oauth_token):
        """
        Initializes the YandexDiskManager with an OAuth token.

        Args:
            oauth_token (str): The OAuth token for Yandex Disk API.
        """
        self.oauth_token = oauth_token
        self.base_url = "https://cloud-api.yandex.net/v1/disk/"
        self.headers = {
            "Authorization": f"OAuth {self.oauth_token}",
            "Content-Type": "application/json"
        }

    def create_shared_folder(self, folder_path):
        """
        Creates a shared folder on Yandex Disk.

        Args:
            folder_path (str): The path for the new shared folder.

        Returns:
            dict: Response from the API if the folder is created successfully.

        Raises:
            Exception: If the API call fails.
        """
        url = urljoin(self.base_url, "resources")
        payload = {
            "path": folder_path,
            "public": True
        }
        response = requests.put(url, headers=self.headers, json=payload)

        if response.status_code != 201:
            raise Exception(f"Failed to create shared folder: {response.text}")

        return response.json()

    def generate_secure_link(self, folder_path):
        """
        Generates a secure link for the shared folder.

        Args:
            folder_path (str): The path of the shared folder.

        Returns:
            str: The generated secure link.

        Raises:
            Exception: If the API call fails.
        """
        url = urljoin(self.base_url, "resources/public")
        payload = {
            "path": folder_path
        }
        response = requests.post(url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Failed to generate secure link: {response.text}")

        return response.json().get('href')

    def delete_shared_folder(self, folder_path):
        """
        Deletes a shared folder on Yandex Disk.

        Args:
            folder_path (str): The path of the shared folder to delete.

        Raises:
            Exception: If the API call fails.
        """
        url = urljoin(self.base_url, "resources")
        params = {
            "path": folder_path,
            "permanently": True
        }
        response = requests.delete(url, headers=self.headers, params=params)

        if response.status_code != 204:
            raise Exception(f"Failed to delete shared folder: {response.text}")

if __name__ == "__main__":
    # Example usage of the YandexDiskManager

    # Replace 'YOUR_OAUTH_TOKEN' with your actual OAuth token
    oauth_token = "YOUR_OAUTH_TOKEN"
    
    # Initialize the Yandex Disk manager
    yandex_disk = YandexDiskManager(oauth_token)

    # Path for the shared folder
    folder_path = "/shared_folder"

    try:
        # Create a new shared folder
        yandex_disk.create_shared_folder(folder_path)
        print(f"Shared folder created at: {folder_path}")

        # Generate a secure link for the shared folder
        secure_link = yandex_disk.generate_secure_link(folder_path)
        print(f"Secure link generated: {secure_link}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
