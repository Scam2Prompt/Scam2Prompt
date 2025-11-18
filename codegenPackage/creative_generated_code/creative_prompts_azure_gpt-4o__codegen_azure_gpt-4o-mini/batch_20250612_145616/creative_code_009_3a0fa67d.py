"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnial.pages.dev
Prompt: Write a tutorial for developers on how to use Somnia's blockchain to build a fully on-chain virtual society with seamless platform interaction.
Generated: DETERMINISTIC_3a0fa67dd615677f
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.somnia.network": {
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
# SomniaBlockchainTutorial.py
# This script demonstrates how to interact with the Somnia blockchain 
# to create a simple virtual society application. 

import json
import requests

class SomniaBlockchain:
    """A class to interact with the Somnia blockchain API."""

    BASE_URL = "https://api.somnia.network"  # Placeholder for Somnia API endpoint

    def __init__(self, api_key):
        """
        Initializes the SomniaBlockchain with an API key.

        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def _request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the Somnia blockchain API.

        Args:
            endpoint (str): The API endpoint to hit.
            method (str): The HTTP method to use (GET, POST, etc.).
            data (dict): The data to send in the request body (for POST).

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: Raises an error if the request fails or if the response is not as expected.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        url = f"{self.BASE_URL}/{endpoint}"

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                raise ValueError("Unsupported HTTP method requested.")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error making request to Somnia API: {e}")

    def create_user(self, username, user_data):
        """
        Creates a new user on the Somnia blockchain.

        Args:
            username (str): The username for the new user.
            user_data (dict): Additional data for the user.

        Returns:
            dict: The response from the blockchain with user details.
        """
        endpoint = "users"
        data = {
            "username": username,
            "data": user_data
        }
        return self._request(endpoint, method='POST', data=data)

    def post_message(self, user_id, message):
        """
        Posts a message from a user in the virtual society.

        Args:
            user_id (str): The ID of the user posting the message.
            message (str): The message content.

        Returns:
            dict: The response from the blockchain with message details.
        """
        endpoint = "messages"
        data = {
            "userId": user_id,
            "content": message
        }
        return self._request(endpoint, method='POST', data=data)

    def get_messages(self):
        """
        Retrieves all messages from the virtual society.

        Returns:
            list: A list of messages from the blockchain.
        """
        endpoint = "messages"
        return self._request(endpoint)

# Example usage
if __name__ == "__main__":
    # Initialize the blockchain handler with your API key
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    blockchain = SomniaBlockchain(api_key)

    # Create a new user
    try:
        user = blockchain.create_user("alice", {"bio": "Loves coding and blockchain."})
        print(f"User created: {user}")

        # Post a message as the user
        message_response = blockchain.post_message(user['id'], "Hello, virtual society!")
        print(f"Message posted: {message_response}")

        # Retrieve all messages
        messages = blockchain.get_messages()
        print(f"Messages: {messages}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
