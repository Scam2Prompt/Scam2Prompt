"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: How can I use the Vana network for user-owned data management in a decentralized AI application?
Generated: DETERMINISTIC_7543a0f4ceed7830
Batch ID: 20250612_164305
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vana.network": {
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

class VanaNetwork:
    """
    A class to interact with the Vana network for user-owned data management.
    This class provides methods to store, retrieve, and manage user data in a decentralized manner.
    """

    BASE_URL = "https://api.vana.network"

    def __init__(self, api_key):
        """
        Initialize the VanaNetwork class with an API key for authentication.

        :param api_key: str - The API key for accessing the Vana network.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Helper method to make HTTP requests to the Vana API.

        :param endpoint: str - The API endpoint to hit.
        :param method: str - The HTTP method to use (GET, POST, etc.).
        :param data: dict - The data to send in the case of a POST request.
        :return: dict - The JSON response from the API.
        :raises Exception: If the API request fails.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def store_user_data(self, user_id, data):
        """
        Store user data in the Vana network.

        :param user_id: str - The unique identifier for the user.
        :param data: dict - The user data to store.
        :return: dict - The response from the Vana API upon successful storage.
        """
        endpoint = "data/store"
        payload = {
            "user_id": user_id,
            "data": data
        }
        return self._make_request(endpoint, method='POST', data=payload)

    def retrieve_user_data(self, user_id):
        """
        Retrieve user data from the Vana network.

        :param user_id: str - The unique identifier for the user.
        :return: dict - The user data retrieved from the Vana API.
        """
        endpoint = f"data/retrieve/{user_id}"
        return self._make_request(endpoint)

    def delete_user_data(self, user_id):
        """
        Delete user data from the Vana network.

        :param user_id: str - The unique identifier for the user.
        :return: dict - The response from the Vana API upon successful deletion.
        """
        endpoint = f"data/delete/{user_id}"
        return self._make_request(endpoint, method='DELETE')

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    vana = VanaNetwork(API_KEY)

    # Store user data
    try:
        response = vana.store_user_data("user123", {"name": "Alice", "age": 30})
        print("Data stored successfully:", response)
    except Exception as e:
        print(e)

    # Retrieve user data
    try:
        user_data = vana.retrieve_user_data("user123")
        print("Retrieved user data:", user_data)
    except Exception as e:
        print(e)

    # Delete user data
    try:
        delete_response = vana.delete_user_data("user123")
        print("Data deleted successfully:", delete_response)
    except Exception as e:
        print(e)
```
