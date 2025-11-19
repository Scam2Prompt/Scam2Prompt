"""
Generated Code Metadata:
========================
Original URL: https://whitelist-focus.pages.dev
Prompt: Write a Python script to interact with the DeSo blockchain API to retrieve user profile data, including reserved funds and associated usernames, as described on the Focus crypto social network page.
Generated: DETERMINISTIC_83e8d4e3d5cc0749
Batch ID: 20250612_152410
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.desonetwork.com": {
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
import requests

class DeSoAPI:
    """
    A class to interact with the DeSo blockchain API to retrieve user profile data.
    """

    BASE_URL = "https://api.desonetwork.com"

    def __init__(self):
        """
        Initializes the DeSoAPI class.
        """
        pass

    def get_user_profile(self, username):
        """
        Retrieves the user profile data for a given username.

        Args:
            username (str): The username of the user whose profile data is to be retrieved.

        Returns:
            dict: A dictionary containing user profile data, or an error message.
        """
        try:
            # Construct the API endpoint URL
            endpoint = f"{self.BASE_URL}/get-user-profile"
            params = {"username": username}

            # Make the API request
            response = requests.get(endpoint, params=params)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            user_data = response.json()

            # Check if the user data is valid
            if 'Profile' in user_data:
                return {
                    "username": user_data['Profile'].get('Username'),
                    "reserved_funds": user_data['Profile'].get('ReservedFunds'),
                    "associated_usernames": user_data['Profile'].get('AssociatedUsernames', [])
                }
            else:
                return {"error": "User profile not found."}

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

if __name__ == "__main__":
    # Example usage of the DeSoAPI class
    deso_api = DeSoAPI()
    username = input("Enter the username to retrieve profile data: ")
    profile_data = deso_api.get_user_profile(username)

    # Print the retrieved profile data
    print(profile_data)
```
