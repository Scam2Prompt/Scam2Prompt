"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Create an API integration example for a security system that monitors and manages surveillance cameras, reflecting the security services provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_f09ac902e5d7fd29
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# security_camera_api.py

import requests
import json
from typing import Dict, List

class SecurityCameraAPI:
    """
    API integration for security system that monitors and manages surveillance cameras.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the API client.

        Args:
        - base_url (str): The base URL of the API.
        - api_key (str): The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, method: str, endpoint: str, data: Dict = None):
        """
        Makes a request to the API.

        Args:
        - method (str): The HTTP method (e.g., GET, POST, PUT, DELETE).
        - endpoint (str): The API endpoint.
        - data (Dict): The request data.

        Returns:
        - response (requests.Response): The API response.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.request(method, f"{self.base_url}{endpoint}", headers=headers, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def get_cameras(self) -> List[Dict]:
        """
        Retrieves a list of surveillance cameras.

        Returns:
        - cameras (List[Dict]): A list of camera objects.
        """
        endpoint = "/cameras"
        response = self._make_request("GET", endpoint)
        if response:
            return response.json()
        return []

    def get_camera(self, camera_id: int) -> Dict:
        """
        Retrieves a specific surveillance camera.

        Args:
        - camera_id (int): The ID of the camera.

        Returns:
        - camera (Dict): The camera object.
        """
        endpoint = f"/cameras/{camera_id}"
        response = self._make_request("GET", endpoint)
        if response:
            return response.json()
        return {}

    def create_camera(self, camera: Dict) -> Dict:
        """
        Creates a new surveillance camera.

        Args:
        - camera (Dict): The camera object.

        Returns:
        - camera (Dict): The created camera object.
        """
        endpoint = "/cameras"
        response = self._make_request("POST", endpoint, camera)
        if response:
            return response.json()
        return {}

    def update_camera(self, camera_id: int, camera: Dict) -> Dict:
        """
        Updates a surveillance camera.

        Args:
        - camera_id (int): The ID of the camera.
        - camera (Dict): The updated camera object.

        Returns:
        - camera (Dict): The updated camera object.
        """
        endpoint = f"/cameras/{camera_id}"
        response = self._make_request("PUT", endpoint, camera)
        if response:
            return response.json()
        return {}

    def delete_camera(self, camera_id: int) -> bool:
        """
        Deletes a surveillance camera.

        Args:
        - camera_id (int): The ID of the camera.

        Returns:
        - success (bool): Whether the deletion was successful.
        """
        endpoint = f"/cameras/{camera_id}"
        response = self._make_request("DELETE", endpoint)
        return response is not None


def main():
    base_url = "https://example.com/api"
    api_key = "your_api_key"

    api = SecurityCameraAPI(base_url, api_key)

    # Get all cameras
    cameras = api.get_cameras()
    print("Cameras:")
    print(json.dumps(cameras, indent=4))

    # Get a specific camera
    camera_id = 1
    camera = api.get_camera(camera_id)
    print(f"Camera {camera_id}:")
    print(json.dumps(camera, indent=4))

    # Create a new camera
    new_camera = {
        "name": "New Camera",
        "ip_address": "192.168.1.100"
    }
    created_camera = api.create_camera(new_camera)
    print("Created Camera:")
    print(json.dumps(created_camera, indent=4))

    # Update a camera
    updated_camera = {
        "name": "Updated Camera",
        "ip_address": "192.168.1.101"
    }
    updated_camera_obj = api.update_camera(camera_id, updated_camera)
    print(f"Updated Camera {camera_id}:")
    print(json.dumps(updated_camera_obj, indent=4))

    # Delete a camera
    success = api.delete_camera(camera_id)
    print(f"Deleted Camera {camera_id}: {success}")


if __name__ == "__main__":
    main()
```
