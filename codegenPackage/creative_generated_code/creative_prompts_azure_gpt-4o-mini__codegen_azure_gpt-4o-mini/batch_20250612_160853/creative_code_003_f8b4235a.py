"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreibgcum43j7d4mubge4izowokrtbcswc6llh62jjklhh7g5bzrfd6e.ipfs.dweb.link
Prompt: Generate an API call example for accessing OpenGPU features related to staking and bonuses.
Generated: DETERMINISTIC_f8b4235abfaefe12
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opengpu.com/v1": {
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

class OpenGPUAPIClient:
    """
    A client for interacting with the OpenGPU API, specifically for accessing
    staking and bonus features.
    """

    BASE_URL = "https://api.opengpu.com/v1"  # Base URL for the OpenGPU API

    def __init__(self, api_key):
        """
        Initializes the OpenGPU API client with the provided API key.

        :param api_key: The API key for authenticating with the OpenGPU API.
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Returns the headers for the API requests, including the authorization.

        :return: A dictionary containing the headers.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_staking_info(self, user_id):
        """
        Retrieves staking information for a given user.

        :param user_id: The ID of the user whose staking information is to be retrieved.
        :return: A dictionary containing the staking information.
        :raises ValueError: If user_id is invalid.
        :raises Exception: If the API request fails.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")

        url = f"{self.BASE_URL}/staking/{user_id}"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the response as JSON

        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            raise Exception(f"API request failed: {e}")

    def get_bonus_info(self, user_id):
        """
        Retrieves bonus information for a given user.

        :param user_id: The ID of the user whose bonus information is to be retrieved.
        :return: A dictionary containing the bonus information.
        :raises ValueError: If user_id is invalid.
        :raises Exception: If the API request fails.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")

        url = f"{self.BASE_URL}/bonuses/{user_id}"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the response as JSON

        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            raise Exception(f"API request failed: {e}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    user_id = "example_user_id"  # Replace with the actual user ID

    client = OpenGPUAPIClient(API_KEY)

    try:
        staking_info = client.get_staking_info(user_id)
        print("Staking Information:", staking_info)

        bonus_info = client.get_bonus_info(user_id)
        print("Bonus Information:", bonus_info)

    except Exception as e:
        print("Error:", e)
```
