"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Create a code snippet that integrates with a diving gear API to retrieve information about underwater drones and their specifications.
Generated: DETERMINISTIC_c94f9e2bd8e7789c
Batch ID: 20250612_135046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.divinggear.com": {
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

class DivingGearAPI:
    """
    A class to interact with the Diving Gear API for retrieving underwater drone information.
    """
    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the DivingGearAPI instance.

        :param base_url: Base URL of the Diving Gear API.
        :param api_key: API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_underwater_drones(self) -> list:
        """
        Retrieves a list of underwater drones and their specifications.

        :return: List of underwater drones with their specifications.
        :raises Exception: If the API request fails or returns an error.
        """
        endpoint = f"{self.base_url}/underwater-drones"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make the GET request to fetch underwater drone data
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            return response.json()  # Parse the JSON response into Python objects
        except requests.exceptions.RequestException as e:
            # Handle any network-related or HTTP errors
            raise Exception(f"Failed to retrieve underwater drones: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Constants for API integration
    BASE_URL = "https://api.divinggear.com"
    API_KEY = "your_api_key_here"

    # Initialize the API client
    diving_gear_api = DivingGearAPI(base_url=BASE_URL, api_key=API_KEY)

    try:
        # Fetch underwater drone data
        drones = diving_gear_api.get_underwater_drones()

        # Print list of drones and their specifications
        print("Underwater Drones:")
        for drone in drones:
            print(f"Name: {drone['name']}, Specifications: {drone['specifications']}")
    except Exception as e:
        # Handle any exceptions during API calls
        print(f"Error: {e}")
```
