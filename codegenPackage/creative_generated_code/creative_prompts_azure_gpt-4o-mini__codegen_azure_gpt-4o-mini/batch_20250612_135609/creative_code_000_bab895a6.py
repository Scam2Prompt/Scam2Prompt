"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ad-o.jp
Prompt: Generate a code snippet to integrate with the Xserver Hosting Service API for managing hosting configurations.
Generated: DETERMINISTIC_bab895a6352f197a
Batch ID: 20250612_135609
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.xserver.com/v1/": {
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

class XserverAPI:
    """
    A class to interact with the Xserver Hosting Service API for managing hosting configurations.
    """

    def __init__(self, api_key, base_url='https://api.xserver.com/v1/'):
        """
        Initializes the XserverAPI with the API key and base URL.

        :param api_key: str: The API key for authentication with the Xserver API.
        :param base_url: str: The base URL for the Xserver API (default is set to the official API URL).
        """
        self.api_key = api_key
        self.base_url = base_url

    def _request(self, method, endpoint, data=None):
        """
        Private method to handle API requests.

        :param method: str: The HTTP method to use (GET, POST, PUT, DELETE).
        :param endpoint: str: The API endpoint to hit.
        :param data: dict: The data to send with the request (for POST/PUT).
        :return: dict: The JSON response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Parse and return JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle HTTP error
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred: {req_err}")  # Handle any other request error

        return None  # Return None if an error occurred

    def get_hosting_configurations(self):
        """
        Fetches the current hosting configurations.

        :return: dict: The current hosting configurations or None on error.
        """
        return self._request('GET', 'hosting/configurations')

    def update_hosting_configuration(self, config_id, configuration_data):
        """
        Updates a specific hosting configuration.

        :param config_id: str: The ID of the configuration to update.
        :param configuration_data: dict: The new configuration data.
        :return: dict: The updated configuration or None on error.
        """
        endpoint = f'hosting/configurations/{config_id}'
        return self._request('PUT', endpoint, configuration_data)

    def delete_hosting_configuration(self, config_id):
        """
        Deletes a specific hosting configuration.

        :param config_id: str: The ID of the configuration to delete.
        :return: bool: True if deletion was successful, False otherwise.
        """
        endpoint = f'hosting/configurations/{config_id}'
        response = self._request('DELETE', endpoint)
        return response is not None  # Return True if response exists, indicating success


# Example usage:
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY_HERE'
    xserver_api = XserverAPI(api_key)

    # Get hosting configurations
    configurations = xserver_api.get_hosting_configurations()
    if configurations:
        print("Hosting Configurations:", configurations)

    # Update a configuration
    config_id = '123456'
    new_config_data = {
        'setting1': 'value1',
        'setting2': 'value2'
    }
    updated_config = xserver_api.update_hosting_configuration(config_id, new_config_data)
    if updated_config:
        print("Updated Configuration:", updated_config)

    # Delete a configuration
    deletion_successful = xserver_api.delete_hosting_configuration(config_id)
    if deletion_successful:
        print(f"Configuration {config_id} deleted successfully.")
```
