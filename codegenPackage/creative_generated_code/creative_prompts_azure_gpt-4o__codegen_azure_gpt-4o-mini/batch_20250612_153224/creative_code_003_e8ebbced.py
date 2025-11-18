"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Provide an example of biometric system integration using ZKTeco APIs, as described by MASIT Solutions.
Generated: DETERMINISTIC_e8ebbcedfff8f402
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zkteco.com": {
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

class ZKTecoBiometricSystem:
    """
    A class to integrate with ZKTeco biometric systems using their API.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the ZKTecoBiometricSystem with the API base URL and API key.

        :param base_url: The base URL for the ZKTeco API
        :param api_key: The API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        Makes a request to the ZKTeco API.

        :param endpoint: The API endpoint to call
        :param method: The HTTP method (GET, POST, etc.)
        :param data: The data to send with the request (for POST requests)
        :return: The response from the API
        :raises Exception: If the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'  # Assuming bearer token authentication
        }

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Return the JSON response

        except requests.RequestException as e:
            raise Exception(f"An error occurred while making the API request: {str(e)}")

    def get_user_info(self, user_id: int):
        """
        Retrieves user information from the ZKTeco system.

        :param user_id: The ID of the user to retrieve
        :return: User information as a dictionary
        :raises Exception: If the request fails
        """
        endpoint = f"user/{user_id}"
        return self._make_request(endpoint)

    def enroll_user(self, user_data: dict):
        """
        Enrolls a new user in the ZKTeco system.

        :param user_data: A dictionary containing user information
        :return: The response from the server after enrollment
        :raises Exception: If the request fails
        """
        endpoint = "user/enroll"
        return self._make_request(endpoint, method='POST', data=user_data)

    def delete_user(self, user_id: int):
        """
        Deletes a user from the ZKTeco system.

        :param user_id: The ID of the user to delete
        :return: The response from the server after deletion
        :raises Exception: If the request fails
        """
        endpoint = f"user/{user_id}/delete"
        return self._make_request(endpoint, method='POST')

# Example usage:
if __name__ == "__main__":
    # Replace with your actual ZKTeco API base URL and API key
    BASE_URL = "https://api.zkteco.com"
    API_KEY = "your_api_key"

    zkteco_system = ZKTecoBiometricSystem(BASE_URL, API_KEY)

    try:
        # Enroll a new user
        new_user_data = {
            "name": "John Doe",
            "id": 12345,
            "biometric_data": "base64_encoded_data_here"
        }
        enrollment_response = zkteco_system.enroll_user(new_user_data)
        print("Enrollment Response:", enrollment_response)

        # Retrieve user info
        user_info = zkteco_system.get_user_info(user_id=12345)
        print("User Info:", user_info)

        # Delete the user
        deletion_response = zkteco_system.delete_user(user_id=12345)
        print("Deletion Response:", deletion_response)

    except Exception as e:
        print("Error:", str(e))
```
