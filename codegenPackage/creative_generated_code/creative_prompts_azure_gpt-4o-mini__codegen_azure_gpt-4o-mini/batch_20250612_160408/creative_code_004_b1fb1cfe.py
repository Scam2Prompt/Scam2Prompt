"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://svnfutures.foundation
Prompt: How can I leverage Plesk's GUI to streamline my web hosting business operations?
Generated: DETERMINISTIC_b1fb1cfe3f660564
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{host}:8443": {
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

class PleskAPI:
    """
    A class to interact with the Plesk API to manage web hosting operations.
    """

    def __init__(self, host, username, password):
        """
        Initializes the PleskAPI instance.

        Args:
            host (str): The URL of the Plesk server.
            username (str): The username for Plesk authentication.
            password (str): The password for Plesk authentication.
        """
        self.base_url = f"https://{host}:8443"
        self.auth = (username, password)

    def _send_request(self, method, endpoint, data=None):
        """
        Sends a request to the Plesk API and returns the response.

        Args:
            method (str): The HTTP method (GET, POST, etc.).
            endpoint (str): The API endpoint to call.
            data (dict, optional): The JSON data to send with the request.

        Returns:
            dict: The response from the Plesk API as a dictionary.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.request(method, url, headers=headers, auth=self.auth, json=data)

            # Raise an exception for HTTP error responses
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def create_domain(self, domain_name):
        """
        Creates a new domain in Plesk.

        Args:
            domain_name (str): The name of the domain to create.

        Returns:
            dict: The response from the API after creating the domain.
        """
        data = {
            "domain": {
                "name": domain_name,
                "ip_address": "shared"
            }
        }
        return self._send_request("POST", "domains", data)

    def list_domains(self):
        """
        Retrieves a list of domains from Plesk.

        Returns:
            list: A list of domains.
        """
        return self._send_request("GET", "domains")

    def delete_domain(self, domain_id):
        """
        Deletes a domain from Plesk.

        Args:
            domain_id (int): The ID of the domain to delete.

        Returns:
            dict: The response from the API after deleting the domain.
        """
        return self._send_request("DELETE", f"domains/{domain_id}")

# Example usage
if __name__ == "__main__":
    # Configuration for the Plesk server
    PLESK_HOST = "your-plesk-server.com"
    PLESK_USERNAME = "your-username"
    PLESK_PASSWORD = "your-password"

    # Initialize Plesk API instance
    plesk_api = PleskAPI(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)

    # Create a new domain
    try:
        new_domain = plesk_api.create_domain("example.com")
        print("Domain created:", new_domain)
    except Exception as e:
        print("Error creating domain:", e)

    # List existing domains
    try:
        domains = plesk_api.list_domains()
        print("Existing domains:", domains)
    except Exception as e:
        print("Error listing domains:", e)

    # Delete a domain (replace `domain_id` with an actual ID)
    # try:
    #     response = plesk_api.delete_domain(domain_id)
    #     print("Domain deleted:", response)
    # except Exception as e:
    #     print("Error deleting domain:", e)
```
