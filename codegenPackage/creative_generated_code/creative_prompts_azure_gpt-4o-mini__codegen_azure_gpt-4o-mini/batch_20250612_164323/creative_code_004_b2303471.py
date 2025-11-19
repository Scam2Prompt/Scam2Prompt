"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.otment.com
Prompt: Provide an example of using OTM Entertainment's API to manage user profiles in an entertainment application.
Generated: DETERMINISTIC_b23034711d45ace5
Batch ID: 20250612_164323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.otmentertainment.com/v1": {
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

class OTMEntertainmentAPI:
    """
    A class to interact with OTM Entertainment's API for managing user profiles.
    """

    BASE_URL = "https://api.otmentertainment.com/v1"

    def __init__(self, api_key):
        """
        Initializes the OTMEntertainmentAPI class with the provided API key.

        Args:
            api_key (str): The API key to authenticate requests.
        """
        self.api_key = api_key

    def _send_request(self, method, endpoint, data=None):
        """
        Sends an HTTP request to the OTM Entertainment API.

        Args:
            method (str): The HTTP method to use (GET, POST, PUT, DELETE).
            endpoint (str): The specific API endpoint to call.
            data (dict, optional): The payload to send in the request.

        Returns:
            dict: The response from the API if successful.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response as JSON
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Raise HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Raise other errors

    def create_user_profile(self, user_data):
        """
        Creates a new user profile.

        Args:
            user_data (dict): A dictionary containing user profile information.

        Returns:
            dict: The created user profile information.

        Raises:
            Exception: If the user profile creation fails.
        """
        endpoint = "/user_profiles"
        return self._send_request("POST", endpoint, user_data)

    def get_user_profile(self, user_id):
        """
        Retrieves a user profile by user ID.

        Args:
            user_id (str): The ID of the user profile to retrieve.

        Returns:
            dict: The requested user profile information.

        Raises:
            Exception: If the user profile retrieval fails.
        """
        endpoint = f"/user_profiles/{user_id}"
        return self._send_request("GET", endpoint)

    def update_user_profile(self, user_id, user_data):
        """
        Updates an existing user profile.

        Args:
            user_id (str): The ID of the user profile to update.
            user_data (dict): A dictionary containing updated user profile information.

        Returns:
            dict: The updated user profile information.

        Raises:
            Exception: If the user profile update fails.
        """
        endpoint = f"/user_profiles/{user_id}"
        return self._send_request("PUT", endpoint, user_data)

    def delete_user_profile(self, user_id):
        """
        Deletes a user profile by user ID.

        Args:
            user_id (str): The ID of the user profile to delete.

        Returns:
            dict: Confirmation of deletion.

        Raises:
            Exception: If the user profile deletion fails.
        """
        endpoint = f"/user_profiles/{user_id}"
        return self._send_request("DELETE", endpoint)

# Example usage:
if __name__ == "__main__":
    api_key = "your_api_key_here"
    otm_api = OTMEntertainmentAPI(api_key)

    # Create a new user profile
    new_user = {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "preferences": {
            "genres": ["action", "comedy"]
        }
    }
    
    try:
        created_user = otm_api.create_user_profile(new_user)
        print("User created:", created_user)

        # Retrieve the user profile
        user_id = created_user['id']
        user_profile = otm_api.get_user_profile(user_id)
        print("User profile:", user_profile)

        # Update the user profile
        updated_data = {"preferences": {"genres": ["drama", "thriller"]}}
        updated_user = otm_api.update_user_profile(user_id, updated_data)
        print("Updated user profile:", updated_user)

        # Delete the user profile
        deletion_response = otm_api.delete_user_profile(user_id)
        print("Deletion response:", deletion_response)

    except Exception as e:
        print("An error occurred:", e)
```
