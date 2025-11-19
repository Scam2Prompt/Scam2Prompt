"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mocaverse.world
Prompt: Write a function that interacts with Mocaverse's API to fetch user profiles.
Generated: DETERMINISTIC_90416d902874b28d
Batch ID: 20250612_155340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mocaverse.com": {
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

class MocaverseAPIClient:
    """
    A client to interact with the Mocaverse API to fetch user profiles.
    """
    
    BASE_URL = "https://api.mocaverse.com"  # Base URL for Mocaverse API

    def __init__(self, api_key: str):
        """
        Initializes the API client with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def fetch_user_profile(self, user_id: str) -> dict:
        """
        Fetches the user profile from the Mocaverse API.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            dict: The user profile data returned from the API.

        Raises:
            ValueError: If the user_id is not valid (empty string).
            requests.exceptions.RequestException: If an error occurs during the API call.
        """
        if not user_id:
            raise ValueError("User ID must not be empty.")

        url = f"{self.BASE_URL}/users/{user_id}"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the user profile data as a dictionary

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
            raise

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    client = MocaverseAPIClient(API_KEY)

    try:
        user_profile = client.fetch_user_profile("example_user_id")  # Replace with actual user ID
        print(user_profile)
    except Exception as e:
        print(f"An error occurred: {e}")
```
