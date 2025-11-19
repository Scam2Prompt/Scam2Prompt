"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowtownsmaterials.com
Prompt: Can you provide a code snippet for managing domain nameservers using the Hostinger API based on the information from Cowtowns Materials?
Generated: DETERMINISTIC_d7e9a702e48586ba
Batch ID: 20250612_160553
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
import json

class HostingerAPI:
    """
    A class to interact with the Hostinger API for managing domain nameservers.
    """

    def __init__(self, api_token: str):
        """
        Initialize the HostingerAPI class.

        :param api_token: API token for authentication with Hostinger API.
        """
        self.base_url = "https://api.hostinger.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def update_nameservers(self, domain: str, nameservers: list) -> dict:
        """
        Update nameservers for a domain.

        :param domain: The domain name to update.
        :param nameservers: A list of nameservers to set for the domain.
        :return: API response as a dictionary.
        """
        try:
            # Endpoint for updating nameservers
            url = f"{self.base_url}/domains/{domain}/nameservers"
            
            # Payload for the request
            payload = {
                "nameservers": nameservers
            }

            # Make the PUT request to update nameservers
            response = requests.put(url, headers=self.headers, json=payload)

            # Check for HTTP errors
            response.raise_for_status()

            # Return the JSON response
            return response.json()

        except requests.exceptions.RequestException as e:
            # Handle HTTP errors or connection issues
            return {"error": str(e)}

    def get_nameservers(self, domain: str) -> dict:
        """
        Retrieve current nameservers for a domain.

        :param domain: The domain name to retrieve nameservers for.
        :return: API response as a dictionary.
        """
        try:
            # Endpoint for retrieving nameservers
            url = f"{self.base_url}/domains/{domain}/nameservers"

            # Make the GET request to fetch nameservers
            response = requests.get(url, headers=self.headers)

            # Check for HTTP errors
            response.raise_for_status()

            # Return the JSON response
            return response.json()

        except requests.exceptions.RequestException as e:
            # Handle HTTP errors or connection issues
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Replace with your Hostinger API token
    API_TOKEN = "your_api_token_here"

    # Initialize the HostingerAPI class
    hostinger_api = HostingerAPI(API_TOKEN)

    # Domain and nameservers to manage
    domain_name = "example.com"
    new_nameservers = ["ns1.example.com", "ns2.example.com"]

    # Update nameservers
    update_response = hostinger_api.update_nameservers(domain_name, new_nameservers)
    print("Update Response:", update_response)

    # Get current nameservers
    get_response = hostinger_api.get_nameservers(domain_name)
    print("Current Nameservers:", get_response)
```
