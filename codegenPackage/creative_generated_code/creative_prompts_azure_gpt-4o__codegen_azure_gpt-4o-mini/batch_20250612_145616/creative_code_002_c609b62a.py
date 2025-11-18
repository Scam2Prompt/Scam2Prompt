"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: Generate a Python script to interact with Nginx Proxy Manager's API to list all configured hosts and their SSL statuses.
Generated: DETERMINISTIC_c609b62a6c65a474
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-nginx-proxy-manager.example.com": {
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

class NginxProxyManagerAPI:
    def __init__(self, base_url, api_key):
        """
        Initialize the Nginx Proxy Manager API client.

        :param base_url: The base URL of the Nginx Proxy Manager API.
        :param api_key: The API key for authenticating requests.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _headers(self):
        """
        Construct the headers for the API request.

        :return: Dictionary containing the headers.
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def list_hosts(self):
        """
        Fetch and list all configured hosts from the Nginx Proxy Manager.

        :return: List of hosts with their SSL statuses or None if an error occurred.
        """
        try:
            response = requests.get(f'{self.base_url}/api/nginx/hosts', headers=self._headers())
            response.raise_for_status()
            return response.json().get('data', [])
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Log the HTTP error
        except Exception as err:
            print(f'An error occurred: {err}')  # Log any other error
        return None

    def display_hosts(self):
        """
        Display the list of hosts and their SSL statuses.

        This method retrieves the hosts and prints their names and SSL statuses.
        """
        hosts = self.list_hosts()
        if hosts is None:
            print("Failed to retrieve hosts.")
            return
        
        print(f"{'Host Name':<40} {'SSL Status':<20}")
        print("=" * 60)
        for host in hosts:
            host_name = host.get('domainNames', ['N/A'])[0]  # Get the first domain name
            ssl_status = "Enabled" if host.get('ssl') else "Disabled"
            print(f"{host_name:<40} {ssl_status:<20}")

if __name__ == '__main__':
    # Configuration - replace with your Nginx Proxy Manager API details
    BASE_URL = 'http://your-nginx-proxy-manager.example.com'
    API_KEY = 'your_api_key_here'

    # Create an instance of the Nginx Proxy Manager API client
    nginx_api = NginxProxyManagerAPI(BASE_URL, API_KEY)

    # Display the configured hosts and their SSL statuses
    nginx_api.display_hosts()
```
