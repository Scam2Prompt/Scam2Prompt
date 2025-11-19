"""
Generated Code Metadata:
========================
Original URL: https://maindapps.42web.io
Prompt: Write a Python script that utilizes the features of iFastNet Web Hosting, including multiple PHP versions and SSL support.
Generated: DETERMINISTIC_ec94e4dc5ab2bcbb
Batch ID: 20250612_164134
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

# Generated Code:
# ===============

```python
import requests

class iFastNetAPI:
    """
    A class to interact with the iFastNet Web Hosting API.
    """

    def __init__(self, api_key, base_url='https://api.ifastnet.com'):
        """
        Initializes the iFastNetAPI with the provided API key and base URL.

        :param api_key: The API key for authentication.
        :param base_url: The base URL for the iFastNet API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the iFastNet API.

        :param endpoint: The API endpoint to call.
        :param params: Optional parameters to include in the request.
        :return: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to {url}: {e}")
            return None

    def get_php_versions(self):
        """
        Retrieves the available PHP versions from the iFastNet API.

        :return: A list of available PHP versions or None if an error occurs.
        """
        return self._make_request('php-versions')

    def enable_ssl(self, domain):
        """
        Enables SSL for the specified domain.

        :param domain: The domain for which to enable SSL.
        :return: The response from the API or None if an error occurs.
        """
        params = {'domain': domain}
        return self._make_request('enable-ssl', params)

    def set_php_version(self, domain, php_version):
        """
        Sets the PHP version for the specified domain.

        :param domain: The domain for which to set the PHP version.
        :param php_version: The PHP version to set.
        :return: The response from the API or None if an error occurs.
        """
        params = {'domain': domain, 'php_version': php_version}
        return self._make_request('set-php-version', params)

if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = 'your_api_key_here'
    
    # Create an instance of the iFastNetAPI
    ifastnet_api = iFastNetAPI(API_KEY)

    # Get available PHP versions
    php_versions = ifastnet_api.get_php_versions()
    if php_versions:
        print("Available PHP Versions:", php_versions)

    # Example usage: Enable SSL for a domain
    domain_to_enable_ssl = 'example.com'
    ssl_response = ifastnet_api.enable_ssl(domain_to_enable_ssl)
    if ssl_response:
        print(f"SSL enabled for {domain_to_enable_ssl}: {ssl_response}")

    # Example usage: Set PHP version for a domain
    domain_to_set_php = 'example.com'
    php_version_to_set = '7.4'
    php_response = ifastnet_api.set_php_version(domain_to_set_php, php_version_to_set)
    if php_response:
        print(f"PHP version set for {domain_to_set_php}: {php_response}")
```
