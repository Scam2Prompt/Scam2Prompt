"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Suggest an API that could be used to integrate a secure CCTV monitoring system for educational institutions, similar to the security measures at SMA Rizvi Textile Institute.
Generated: DETERMINISTIC_37b233496203cd1c
Batch ID: 20250612_155259
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cctvmonitor.com/v1": {
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

class CCTVMonitorAPI:
    """
    A class to interact with a CCTV monitoring API for secure surveillance in educational institutions.
    """

    BASE_URL = "https://api.cctvmonitor.com/v1"  # Hypothetical base URL

    def __init__(self, api_key):
        """
        Initializes the CCTVMonitorAPI with an API key for authentication.

        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Returns the headers required for API requests, including authentication.

        :return: dict - The headers with the authorization token.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_camera_status(self, camera_id):
        """
        Retrieves the current status of a specific camera by its ID.

        :param camera_id: str - The unique identifier for the camera.
        :return: dict - The response from the API containing the camera status.
        :raises Exception: If the request fails or returns an error.
        """
        url = f"{self.BASE_URL}/cameras/{camera_id}/status"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

    def get_all_cameras(self):
        """
        Retrieves a list of all cameras registered in the monitoring system.

        :return: list - A list of cameras with their details.
        :raises Exception: If the request fails or returns an error.
        """
        url = f"{self.BASE_URL}/cameras"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

    def set_camera_recording(self, camera_id, recording=True):
        """
        Enables or disables recording for a specific camera.

        :param camera_id: str - The unique identifier for the camera.
        :param recording: bool - True to enable recording, False to disable.
        :return: dict - The response from the API confirming the action.
        :raises Exception: If the request fails or returns an error.
        """
        url = f"{self.BASE_URL}/cameras/{camera_id}/record"
        payload = {"record": recording}

        try:
            response = requests.post(url, headers=self._get_headers(), json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

# Example usage (commented out):
# api_key = "your_api_key_here"
# cctv_api = CCTVMonitorAPI(api_key)
# camera_status = cctv_api.get_camera_status("camera_id_123")
# print(camera_status)
```
