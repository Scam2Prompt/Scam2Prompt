"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzcf.land
Prompt: Provide a step-by-step guide to interact with a mapping portal API that requires user authentication, including handling errors if no maps are visible.
Generated: DETERMINISTIC_58cb343bf246e76f
Batch ID: 20250612_145727
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mappingportal.com": {
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

class MappingPortalAPI:
    def __init__(self, base_url, api_key):
        """
        Initializes the MappingPortalAPI with the base URL and API key.

        :param base_url: str - The base URL of the mapping portal API.
        :param api_key: str - The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def authenticate(self):
        """
        Authenticates the user with the API.

        :raises Exception: If the authentication fails.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self.base_url}/auth', headers=headers)

        if response.status_code != 200:
            raise Exception(f'Authentication failed: {response.text}')

        print('Authentication successful.')

    def get_maps(self):
        """
        Retrieves the list of maps available to the user.

        :return: list - A list of maps.
        :raises Exception: If no maps are visible or if the request fails.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self.base_url}/maps', headers=headers)

        if response.status_code != 200:
            raise Exception(f'Failed to retrieve maps: {response.text}')

        maps = response.json().get('maps', [])
        if not maps:
            raise Exception('No maps are visible to the user.')

        return maps

    def display_maps(self):
        """
        Displays the maps to the user.
        """
        try:
            self.authenticate()
            maps = self.get_maps()
            for map_info in maps:
                print(f"Map ID: {map_info['id']}, Name: {map_info['name']}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    # Example usage:
    API_BASE_URL = 'https://api.mappingportal.com'
    API_KEY = 'your_api_key_here'  # Replace with your actual API key

    mapping_api = MappingPortalAPI(API_BASE_URL, API_KEY)
    mapping_api.display_maps()
```
