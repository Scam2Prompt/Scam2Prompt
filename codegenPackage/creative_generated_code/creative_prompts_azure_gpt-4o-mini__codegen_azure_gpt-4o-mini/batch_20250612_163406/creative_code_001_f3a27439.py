"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: What code examples can demonstrate the integration of the HELPGM API for user management in a web application?
Generated: DETERMINISTIC_f3a27439457bb496
Batch ID: 20250612_163406
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.help-gm.com": {
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

class HelpGMAPI:
    """
    A class to interact with the HELPGM API for user management.
    """

    def __init__(self, api_key, base_url='https://api.help-gm.com'):
        """
        Initializes the API client with provided API key and base URL.

        :param api_key: str - The API key for authentication.
        :param base_url: str - The base URL for the HELPGM API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _request(self, method, endpoint, data=None):
        """
        Handles the HTTP request to the HELPGM API.

        :param method: str - HTTP method (GET, POST, PUT, DELETE).
        :param endpoint: str - The API endpoint to call.
        :param data: dict - The body of the request for POST/PUT requests.
        :return: dict - The JSON response from the API.
        :raises: Exception - If the request fails or the response is unsuccessful.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid HTTP method specified.")

            response.raise_for_status()  # Raise an error for bad responses

            return response.json()

        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while calling the HELPGM API: {str(e)}")

    def create_user(self, user_data):
        """
        Creates a new user in the HELPGM system.

        :param user_data: dict - A dictionary containing user information.
        :return: dict - The response data from the API after user creation.
        """
        return self._request('POST', 'users', user_data)

    def get_user(self, user_id):
        """
        Retrieves user information by user ID.

        :param user_id: str - The ID of the user to retrieve.
        :return: dict - The user's information.
        """
        return self._request('GET', f'users/{user_id}')

    def update_user(self, user_id, user_data):
        """
        Updates an existing user's information.

        :param user_id: str - The ID of the user to update.
        :param user_data: dict - A dictionary containing updated user information.
        :return: dict - The response data from the API after user update.
        """
        return self._request('PUT', f'users/{user_id}', user_data)

    def delete_user(self, user_id):
        """
        Deletes a user from the HELPGM system.

        :param user_id: str - The ID of the user to delete.
        :return: dict - The response from the API after user deletion.
        """
        return self._request('DELETE', f'users/{user_id}')

# Example usage of the HelpGMAPI class
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'
    helpgm_api = HelpGMAPI(api_key=API_KEY)

    # Creating a user
    try:
        new_user = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'role': 'user'
        }
        user_creation_response = helpgm_api.create_user(new_user)
        print("User created:", user_creation_response)

        # Retrieve user information
        user_id = user_creation_response['id']
        user_info = helpgm_api.get_user(user_id)
        print("User info:", user_info)

        # Update user information
        updated_user = {
            'name': 'John Doe Updated',
            'email': 'johndoey@example.com',
            'role': 'admin'
        }
        update_response = helpgm_api.update_user(user_id, updated_user)
        print("User updated:", update_response)

        # Delete user
        delete_response = helpgm_api.delete_user(user_id)
        print("User deleted:", delete_response)

    except Exception as e:
        print(f"Error: {e}")
```
