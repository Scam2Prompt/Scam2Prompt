"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobgridl.top
Prompt: Recommend APIs or libraries compatible with aaPanel for managing server configurations programmatically.
Generated: DETERMINISTIC_f9c84fd3f70a8ffc
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourdomain:8888": {
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
"""
Script to interact with aaPanel using their API for managing server configurations programmatically.
aaPanel provides an API interface for managing server configurations, available in its settings.

This script demonstrates how to authenticate and interact with aaPanel's API.
Dependencies:
- requests library (install using `pip install requests`)

Ensure aaPanel's API is enabled and API key is obtained via the aaPanel settings.
"""

import requests
import json

class AaPanelAPI:
    """
    A class to interact with the aaPanel API.
    """
    def __init__(self, base_url, api_key):
        """
        Initialize the AaPanelAPI class.
        
        Args:
            base_url (str): The base URL of the aaPanel server (e.g., 'https://yourdomain:8888').
            api_key (str): The API key obtained from aaPanel settings.
        """
        self.base_url = base_url.rstrip('/') + '/panel/api'
        self.api_key = api_key

    def make_request(self, endpoint, data=None):
        """
        Make an authenticated request to the aaPanel API.

        Args:
            endpoint (str): The API endpoint to interact with.
            data (dict, optional): The payload to send, if required.

        Returns:
            dict: The JSON response from the API.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            payload = {"request_token": self.api_key}
            
            # Merge additional data with payload, if provided
            if data:
                payload.update(data)

            # Send POST request to the API
            response = requests.post(url, data=payload)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            # Parse and return the JSON response
            return response.json()
        except requests.RequestException as e:
            # Handle network or HTTP errors
            print(f"Error while making request to {endpoint}: {str(e)}")
            return {"status": False, "error": str(e)}
        except json.JSONDecodeError:
            # Handle JSON parsing errors
            print(f"Error parsing response from {endpoint}")
            return {"status": False, "error": "Invalid JSON response"}

    def get_server_status(self):
        """
        Retrieve the current server status from aaPanel.

        Returns:
            dict: The server status information.
        """
        return self.make_request("getSystemTotal")
    
    def restart_service(self, service_name):
        """
        Restart a specific service (e.g., Nginx, Apache, MySQL) on the server.

        Args:
            service_name (str): The name of the service to restart.

        Returns:
            dict: The result of the restart operation.
        """
        return self.make_request("restartServer", data={"server_name": service_name})

    def list_sites(self):
        """
        Retrieve a list of all hosted sites on the server.

        Returns:
            dict: The list of hosted websites.
        """
        return self.make_request("getSiteList")
    
    def create_site(self, domain, port=80, path='/www/wwwroot', php_version='7.4'):
        """
        Create a new site on the server.

        Args:
            domain (str): The domain name for the new site.
            port (int): The port for the site (default is 80).
            path (str): The directory path for the site files.
            php_version (str): PHP version to use for the site.

        Returns:
            dict: The result of the site creation operation.
        """
        data = {
            "webname": domain,
            "port": port,
            "path": path,
            "version": php_version
        }
        return self.make_request("createSite", data=data)


# Example usage
if __name__ == "__main__":
    # Specify your aaPanel server URL and API key
    BASE_URL = "https://yourdomain:8888"  # Replace with your aaPanel URL
    API_KEY = "your_api_key_here"         # Replace with your aaPanel API key

    # Initialize the AaPanelAPI client
    panel_client = AaPanelAPI(BASE_URL, API_KEY)

    # Example: Get server status
    server_status = panel_client.get_server_status()
    print("Server Status:", server_status)

    # Example: Restart Nginx service
    restart_result = panel_client.restart_service("nginx")
    print("Restart Result:", restart_result)

    # Example: List hosted sites
    sites = panel_client.list_sites()
    print("Hosted Sites:", sites)

    # Example: Create a new site
    new_site_result = panel_client.create_site(domain="example.com")
    print("New Site Result:", new_site_result)
```
