"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo3.cloudwp.dev
Prompt: Generate code to check the status of a WordPress Playground environment and handle inactive locations using the InMotion Central API.
Generated: DETERMINISTIC_60966573565ad62b
Batch ID: 20250612_145130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.inmotionhosting.com": {
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

class InMotionAPI:
    """
    A class to interact with the InMotion Central API for checking the status of 
    WordPress Playground environments and handling inactive locations.
    """

    def __init__(self, api_key, api_url):
        """
        Initialize the API client with the provided API key and URL.

        :param api_key: str - The API key for authentication.
        :param api_url: str - The base URL for the InMotion Central API.
        """
        self.api_key = api_key
        self.api_url = api_url

    def check_playground_status(self):
        """
        Check the status of the WordPress Playground environment.

        :return: dict - A dictionary containing the status of each location.
        :raises Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(
                f"{self.api_url}/playgrounds/status",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def handle_inactive_locations(self, status_data):
        """
        Handle inactive locations from the status data.

        :param status_data: dict - The status data containing playground locations.
        :return: None
        """
        for location in status_data.get('locations', []):
            if not location['active']:
                self.deactivate_location(location['id'])

    def deactivate_location(self, location_id):
        """
        Deactivate a given location.

        :param location_id: str - The ID of the location to deactivate.
        :raises Exception: If the deactivation request fails or returns an error.
        """
        try:
            response = requests.post(
                f"{self.api_url}/playgrounds/{location_id}/deactivate",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Successfully deactivated location: {location_id}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while deactivating location {location_id}: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred while deactivating location {location_id}: {err}")
            raise

if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your InMotion API key
    API_URL = "https://api.inmotionhosting.com"  # Replace with the actual API URL

    api_client = InMotionAPI(API_KEY, API_URL)

    try:
        playground_status = api_client.check_playground_status()
        api_client.handle_inactive_locations(playground_status)
    except Exception as e:
        print(f"Failed to process playground status: {e}")
```
