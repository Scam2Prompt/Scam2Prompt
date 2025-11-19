"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfiul.epizy.com
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including multiple PHP versions and Node.js support.
Generated: DETERMINISTIC_2fcdaa912a33e589
Batch ID: 20250612_163251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/": {
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
    A class to interact with iFastNet's hosting features such as PHP versions and Node.js support.
    """

    def __init__(self, api_key, api_url="https://api.ifastnet.com/"):
        """
        Initializes the API client with the provided API key and base URL.

        Args:
            api_key (str): The API key for authentication.
            api_url (str): The base URL for the API. Defaults to iFastNet's API URL.
        """
        self.api_key = api_key
        self.api_url = api_url

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the specified API endpoint.

        Args:
            endpoint (str): The API endpoint to call.
            params (dict, optional): Any parameters to include in the API call.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the request fails or if the response is not a valid JSON.
        """
        try:
            response = requests.get(f"{self.api_url}{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except ValueError:
            raise Exception("Invalid JSON response from the API")

    def get_php_versions(self):
        """
        Retrieves available PHP versions from iFastNet.

        Returns:
            list: A list of available PHP versions.
        """
        endpoint = "php/versions"
        response = self._make_request(endpoint)
        return response.get("versions", [])

    def switch_php_version(self, domain, php_version):
        """
        Switches the PHP version for a given domain.

        Args:
            domain (str): The domain for which to switch the PHP version.
            php_version (str): The PHP version to switch to.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the operation fails.
        """
        endpoint = "php/switch"
        params = {"domain": domain, "version": php_version}
        response = self._make_request(endpoint, params)
        return response

    def get_node_versions(self):
        """
        Retrieves available Node.js versions from iFastNet.

        Returns:
            list: A list of available Node.js versions.
        """
        endpoint = "node/versions"
        response = self._make_request(endpoint)
        return response.get("versions", [])

    def switch_node_version(self, domain, node_version):
        """
        Switches the Node.js version for a given domain.

        Args:
            domain (str): The domain for which to switch the Node.js version.
            node_version (str): The Node.js version to switch to.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the operation fails.
        """
        endpoint = "node/switch"
        params = {"domain": domain, "version": node_version}
        response = self._make_request(endpoint, params)
        return response

# Example usage of the iFastNetAPI class
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    DOMAIN = "example.com"  # Replace with your actual domain

    try:
        # Initialize the API client
        ifastnet = iFastNetAPI(API_KEY)

        # Get and print available PHP versions
        php_versions = ifastnet.get_php_versions()
        print("Available PHP Versions:", php_versions)

        # Switch to a specific PHP version
        if php_versions:
            response = ifastnet.switch_php_version(DOMAIN, php_versions[0])
            print("Switched PHP Version Response:", response)

        # Get and print available Node.js versions
        node_versions = ifastnet.get_node_versions()
        print("Available Node.js Versions:", node_versions)

        # Switch to a specific Node.js version
        if node_versions:
            response = ifastnet.switch_node_version(DOMAIN, node_versions[0])
            print("Switched Node.js Version Response:", response)

    except Exception as e:
        print(f"Error: {str(e)}")
```
