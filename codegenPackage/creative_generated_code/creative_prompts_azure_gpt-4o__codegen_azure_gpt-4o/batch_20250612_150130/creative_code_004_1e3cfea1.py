"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masknet.top
Prompt: Provide code examples for integrating CyberPanel's API with a custom web application to automate hosting tasks.
Generated: DETERMINISTIC_1e3cfea170c964ed
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-cyberpanel-domain:8090": {
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

class CyberPanelAPI:
    """
    A class to interact with the CyberPanel API to automate hosting tasks.
    """
    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the CyberPanelAPI client with base URL and API key.
        
        :param base_url: The base URL of your CyberPanel instance, e.g., "https://your-cyberpanel-domain:8090".
        :param api_key: API key for authenticating with CyberPanel.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json'
        }

    def _request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        Private helper function to send API requests to CyberPanel.

        :param endpoint: API endpoint to hit (e.g., "/api/v2/listWebsites").
        :param method: HTTP method to use (GET or POST).
        :param data: Data payload for POST requests.
        :return: JSON response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        params = {'apiKey': self.api_key}
        try:
            if method.upper() == 'POST':
                response = requests.post(url, headers=self.headers, params=params, json=data, timeout=10)
            else:  # Default to GET
                response = requests.get(url, headers=self.headers, params=params, timeout=10)

            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def list_websites(self):
        """
        Fetches a list of websites hosted on the CyberPanel instance.

        :return: List of websites as JSON data.
        """
        endpoint = '/api/v2/listWebsites'
        return self._request(endpoint)

    def create_website(self, domain: str, email: str, package: str, php_version: str = '7.4'):
        """
        Creates a new website on the CyberPanel instance.

        :param domain: The domain name for the new website.
        :param email: Admin email for the domain.
        :param package: Hosting package name to assign to the website.
        :param php_version: PHP version to use (default is 7.4).
        :return: Response JSON from the API.
        """
        endpoint = '/api/v2/createWebsite'
        data = {
            'domainName': domain,
            'email': email,
            'packageName': package,
            'php': php_version
        }
        return self._request(endpoint, method='POST', data=data)

    def delete_website(self, domain: str):
        """
        Deletes an existing website from the CyberPanel instance.

        :param domain: The domain name of the website to delete.
        :return: Response JSON from the API.
        """
        endpoint = '/api/v2/deleteWebsite'
        data = {'domainName': domain}
        return self._request(endpoint, method='POST', data=data)


# Example usage:
if __name__ == '__main__':
    # Replace with your CyberPanel instance details
    CYBERPANEL_URL = "https://your-cyberpanel-domain:8090"
    CYBERPANEL_API_KEY = "your_api_key"

    # Initialize the API client
    client = CyberPanelAPI(CYBERPANEL_URL, CYBERPANEL_API_KEY)

    # List all websites
    try:
        websites = client.list_websites()
        print("Websites:", websites)
    except Exception as e:
        print(f"Error fetching websites: {e}")

    # Create a new website
    try:
        new_website_response = client.create_website(
            domain="example.com",
            email="admin@example.com",
            package="default",
            php_version="8.1"
        )
        print("Create Website Response:", new_website_response)
    except Exception as e:
        print(f"Error creating website: {e}")

    # Delete a website
    try:
        delete_response = client.delete_website(domain="example.com")
        print("Delete Website Response:", delete_response)
    except Exception as e:
        print(f"Error deleting website: {e}")
```
