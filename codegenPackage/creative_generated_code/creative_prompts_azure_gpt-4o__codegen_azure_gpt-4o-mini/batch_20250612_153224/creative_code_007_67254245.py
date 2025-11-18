"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Recommend APIs or libraries for configuring IP-based telephone systems and provide sample code for setting up a small business telephony network, inspired by the plantas telefónicas services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_67254245d0f48bda
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests

class TelephonyNetwork:
    """A class to manage a small business telephony network using APIs."""

    def __init__(self, api_url, api_key):
        """
        Initialize the TelephonyNetwork with API URL and key.

        Args:
            api_url (str): The base URL of the telephony API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _make_api_request(self, endpoint, method='GET', data=None):
        """
        Make a request to the telephony API.

        Args:
            endpoint (str): The API endpoint to hit.
            method (str): The HTTP method ('GET', 'POST', etc.).
            data (dict): Data to send in the request body.

        Returns:
            dict: The JSON response from the API.
        """
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        
        try:
            if method == 'POST':
                response = requests.post(f"{self.api_url}/{endpoint}", headers=headers, json=data)
            else:
                response = requests.get(f"{self.api_url}/{endpoint}", headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            return None

    def create_extension(self, extension_number, user_name):
        """
        Create a new extension for a user.

        Args:
            extension_number (str): The extension number to create.
            user_name (str): The name of the user.

        Returns:
            dict: Response from the API upon creating the extension.
        """
        endpoint = 'extensions'
        data = {
            'extension': extension_number,
            'user': user_name,
        }
        return self._make_api_request(endpoint, method='POST', data=data)

    def configure_call_forwarding(self, extension_number, forward_to):
        """
        Configure call forwarding for a specific extension.

        Args:
            extension_number (str): The extension number to configure.
            forward_to (str): The number to forward calls to.

        Returns:
            dict: Response from the API upon configuring call forwarding.
        """
        endpoint = f'extensions/{extension_number}/forwarding'
        data = {
            'forward_to': forward_to,
        }
        return self._make_api_request(endpoint, method='POST', data=data)

    def list_extensions(self):
        """
        List all configured extensions in the network.

        Returns:
            list: A list of extensions.
        """
        endpoint = 'extensions'
        return self._make_api_request(endpoint)

# Example usage
if __name__ == '__main__':
    API_URL = os.getenv('TELEPHONY_API_URL')  # Set your API URL in the environment
    API_KEY = os.getenv('TELEPHONY_API_KEY')  # Set your API key in the environment

    telephony_network = TelephonyNetwork(API_URL, API_KEY)

    # Create a new extension
    new_extension = telephony_network.create_extension('1001', 'John Doe')
    print(f"Created Extension: {new_extension}")

    # Configure call forwarding
    forwarding_response = telephony_network.configure_call_forwarding('1001', '+1234567890')
    print(f"Forwarding Response: {forwarding_response}")

    # List all extensions
    extensions = telephony_network.list_extensions()
    print(f"Configured Extensions: {extensions}")
```
