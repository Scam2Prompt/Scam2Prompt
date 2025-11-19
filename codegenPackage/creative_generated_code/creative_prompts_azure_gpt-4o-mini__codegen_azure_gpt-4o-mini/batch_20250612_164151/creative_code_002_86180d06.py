"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: Write a Python script that utilizes the features of iFastNet Web Hosting, focusing on multiple PHP versions and SSL setup.
Generated: DETERMINISTIC_86180d06981a2855
Batch ID: 20250612_164151
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
    A class to interact with the iFastNet API for managing web hosting features
    such as PHP version management and SSL setup.
    """

    def __init__(self, api_key):
        """
        Initializes the iFastNetAPI with the provided API key.

        :param api_key: str - The API key for authenticating requests to the iFastNet API.
        """
        self.base_url = "https://api.ifastnet.com"
        self.api_key = api_key

    def _make_api_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the iFastNet API.

        :param endpoint: str - The API endpoint to call.
        :param method: str - The HTTP method to use ('GET' or 'POST').
        :param data: dict - The data to send with the request (for POST).
        :return: dict - The parsed JSON response from the API.
        :raises Exception: If the API request fails or returns an error.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def get_php_versions(self):
        """
        Retrieves the available PHP versions for the hosting account.

        :return: list - A list of available PHP versions.
        """
        endpoint = "php/versions"
        response = self._make_api_request(endpoint)
        return response.get('data', [])

    def set_php_version(self, domain, php_version):
        """
        Sets the specified PHP version for the given domain.

        :param domain: str - The domain for which to set the PHP version.
        :param php_version: str - The PHP version to set (e.g., '7.4', '8.0').
        :raises Exception: If setting the PHP version fails.
        """
        endpoint = "php/set"
        data = {
            'domain': domain,
            'version': php_version
        }
        response = self._make_api_request(endpoint, method='POST', data=data)
        if not response.get('success'):
            raise Exception("Failed to set PHP version.")

    def setup_ssl(self, domain):
        """
        Sets up SSL for the specified domain.

        :param domain: str - The domain for which to set up SSL.
        :raises Exception: If SSL setup fails.
        """
        endpoint = "ssl/setup"
        data = {
            'domain': domain
        }
        response = self._make_api_request(endpoint, method='POST', data=data)
        if not response.get('success'):
            raise Exception("Failed to set up SSL.")

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual iFastNet API key
    api_key = "YOUR_API_KEY"
    domain = "example.com"

    try:
        ifastnet = iFastNetAPI(api_key)

        # Fetch available PHP versions
        php_versions = ifastnet.get_php_versions()
        print(f"Available PHP Versions: {php_versions}")

        # Set PHP version for the domain
        selected_php_version = '8.0'  # Example version
        ifastnet.set_php_version(domain, selected_php_version)
        print(f"PHP version for {domain} set to {selected_php_version}.")

        # Setup SSL for the domain
        ifastnet.setup_ssl(domain)
        print(f"SSL successfully set up for {domain}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
