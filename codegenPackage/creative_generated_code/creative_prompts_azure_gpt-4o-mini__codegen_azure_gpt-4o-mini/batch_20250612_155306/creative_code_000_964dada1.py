"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thg-awardprogram.epizy.com
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including Node.js support and multiple PHP versions.
Generated: DETERMINISTIC_964dada1e3e79bf7
Batch ID: 20250612_155306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com": {
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

class iFastNetAPI:
    """
    A class to interact with the iFastNet API for hosting features.
    """

    def __init__(self, api_key, base_url="https://api.ifastnet.com"):
        """
        Initializes the iFastNetAPI instance.

        :param api_key: Your iFastNet API key.
        :param base_url: Base URL for the iFastNet API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _handle_request(self, endpoint, params=None):
        """
        Handles the API request and error checking.

        :param endpoint: The API endpoint to call.
        :param params: Dictionary of parameters to send with the request.
        :return: Parsed JSON response from the API.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def get_php_versions(self):
        """
        Retrieves the available PHP versions supported by iFastNet.

        :return: A list of PHP versions or None if an error occurs.
        """
        endpoint = "php/versions"
        return self._handle_request(endpoint)

    def get_node_js_support(self):
        """
        Checks if Node.js support is enabled.

        :return: Boolean indicating Node.js support status or None if an error occurs.
        """
        endpoint = "nodejs/support"
        response = self._handle_request(endpoint)
        if response:
            return response.get('supported', False)
        return None


def main():
    """
    Main function to demonstrate the usage of iFastNetAPI class.
    """
    # Replace with your actual iFastNet API key
    API_KEY = "your_api_key_here"

    api = iFastNetAPI(api_key=API_KEY)

    # Get available PHP versions
    print("Fetching available PHP versions...")
    php_versions = api.get_php_versions()
    if php_versions:
        print("Available PHP Versions:", php_versions)
    else:
        print("Failed to fetch PHP versions.")

    # Check Node.js support
    print("Checking Node.js support...")
    node_js_supported = api.get_node_js_support()
    if node_js_supported is not None:
        print("Node.js Support Enabled:", node_js_supported)
    else:
        print("Failed to check Node.js support.")


if __name__ == "__main__":
    main()
```
