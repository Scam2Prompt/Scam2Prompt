"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glveaways-metamasks-lo.html-5.me
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including multiple PHP versions and Node.js support.
Generated: DETERMINISTIC_2fcdaa912a33e589
Batch ID: 20250612_164238
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
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API Request failed: {e}")
        except ValueError:
            raise Exception("Failed to decode JSON response")

    def list_php_versions(self):
        """
        Retrieves the available PHP versions from the iFastNet API.

        Returns:
            list: A list of available PHP versions.
        """
        endpoint = "php/versions"
        response = self._make_request(endpoint)
        return response.get("versions", [])

    def set_php_version(self, domain, php_version):
        """
        Sets the PHP version for a specific domain.

        Args:
            domain (str): The domain for which to set the PHP version.
            php_version (str): The PHP version to set.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        endpoint = "php/set_version"
        params = {
            "domain": domain,
            "php_version": php_version,
            "api_key": self.api_key
        }
        response = self._make_request(endpoint, params)
        return response.get("success", False)

    def list_nodejs_versions(self):
        """
        Retrieves the available Node.js versions from the iFastNet API.

        Returns:
            list: A list of available Node.js versions.
        """
        endpoint = "nodejs/versions"
        response = self._make_request(endpoint)
        return response.get("versions", [])

    def set_nodejs_version(self, domain, nodejs_version):
        """
        Sets the Node.js version for a specific domain.

        Args:
            domain (str): The domain for which to set the Node.js version.
            nodejs_version (str): The Node.js version to set.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        endpoint = "nodejs/set_version"
        params = {
            "domain": domain,
            "nodejs_version": nodejs_version,
            "api_key": self.api_key
        }
        response = self._make_request(endpoint, params)
        return response.get("success", False)


if __name__ == "__main__":
    # Replace with your actual API key and domain
    API_KEY = "your_api_key_here"
    DOMAIN = "your_domain_here"

    # Instantiate the iFastNet API client
    ifastnet_api = iFastNetAPI(api_key=API_KEY)

    # Example of listing available PHP versions
    try:
        php_versions = ifastnet_api.list_php_versions()
        print("Available PHP Versions:", php_versions)

        # Set a specific PHP version
        if ifastnet_api.set_php_version(DOMAIN, php_versions[0]):
            print(f"Successfully set PHP version to {php_versions[0]} for domain {DOMAIN}")
        else:
            print("Failed to set PHP version")

        # Example of listing available Node.js versions
        nodejs_versions = ifastnet_api.list_nodejs_versions()
        print("Available Node.js Versions:", nodejs_versions)

        # Set a specific Node.js version
        if ifastnet_api.set_nodejs_version(DOMAIN, nodejs_versions[0]):
            print(f"Successfully set Node.js version to {nodejs_versions[0]} for domain {DOMAIN}")
        else:
            print("Failed to set Node.js version")

    except Exception as e:
        print(f"An error occurred: {e}")
```
