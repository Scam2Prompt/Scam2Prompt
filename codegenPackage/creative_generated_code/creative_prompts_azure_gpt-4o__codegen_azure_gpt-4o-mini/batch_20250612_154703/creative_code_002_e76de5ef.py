"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm9.com
Prompt: Generate a Python script to add a domain to a hosting plan using Hostinger's API or similar hosting service APIs.
Generated: DETERMINISTIC_e76de5ef5f63f555
Batch ID: 20250612_154703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
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

class HostingServiceAPIError(Exception):
    """Custom exception for handling errors from the hosting service API."""
    pass

class HostingerAPI:
    """Class to interact with the Hostinger API for domain management."""

    BASE_URL = "https://api.hostinger.com/v1"  # Base URL for the Hostinger API

    def __init__(self, api_key):
        """Initialize the API client with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating with the Hostinger API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """Internal method to make a request to the Hostinger API.

        Args:
            endpoint (str): The API endpoint to call.
            method (str): The HTTP method to use (GET, POST, etc.).
            data (dict, optional): The data to send with POST requests.

        Returns:
            dict: The JSON response from the API.

        Raises:
            HostingServiceAPIError: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            raise HostingServiceAPIError(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            raise HostingServiceAPIError(f"An error occurred: {err}") from err

    def add_domain_to_hosting_plan(self, domain_name, plan_id):
        """Add a domain to a specified hosting plan.

        Args:
            domain_name (str): The domain name to add.
            plan_id (str): The ID of the hosting plan to which the domain should be added.

        Returns:
            dict: Response from the API after adding the domain.

        Raises:
            HostingServiceAPIError: If the domain cannot be added or any API error occurs.
        """
        endpoint = "/domains/add"
        data = {
            "domain": domain_name,
            "plan_id": plan_id
        }
        return self._make_request(endpoint, method='POST', data=data)

if __name__ == "__main__":
    # Example usage of the HostingerAPI class
    API_KEY = "your_api_key_here"  # Replace with your actual Hostinger API key
    DOMAIN_NAME = "example.com"      # Replace with the domain you want to add
    PLAN_ID = "12345"                 # Replace with your actual plan ID

    try:
        hostinger_api = HostingerAPI(API_KEY)
        response = hostinger_api.add_domain_to_hosting_plan(DOMAIN_NAME, PLAN_ID)
        print("Domain added successfully:", response)
    except HostingServiceAPIError as e:
        print("Error:", e)
```
