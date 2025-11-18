"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: Provide a detailed example of using Plesk's GUI to manage cloud hosting services for a small business.
Generated: DETERMINISTIC_3d8023ef9819e5ba
Batch ID: 20250612_154339
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{self.host}:8443/enterprise/control/agent.php": {
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
This script automates the management of cloud hosting services using Plesk's API.
It demonstrates how to list, create, and delete domains for a small business.

Requirements:
- Plesk API credentials
- Requests library installed (pip install requests)
"""

import requests

class PleskAPI:
    def __init__(self, host, username, password):
        """
        Initializes the PleskAPI with host, username, and password.

        Args:
            host (str): The URL of the Plesk server.
            username (str): The username for Plesk API.
            password (str): The password for Plesk API.
        """
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{self.host}:8443/enterprise/control/agent.php"

    def _send_request(self, data):
        """
        Sends a request to the Plesk API.

        Args:
            data (dict): The data to be sent in the API request.
        
        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.post(self.base_url, json=data, auth=(self.username, self.password), verify=False)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def list_domains(self):
        """
        Lists all domains managed by the Plesk account.

        Returns:
            list: A list of domain names.
        """
        data = {
            "method": "domain.get",
            "params": {
                "filter": {},
                "version": "1.6.3"
            }
        }
        result = self._send_request(data)
        return [domain['name'] for domain in result['result']['data']]

    def create_domain(self, domain_name, ip_address):
        """
        Creates a new domain under the Plesk account.

        Args:
            domain_name (str): The name of the domain to create.
            ip_address (str): The IP address to assign to the domain.

        Returns:
            dict: The result of the domain creation.
        """
        data = {
            "method": "domain.add",
            "params": {
                "name": domain_name,
                "ip_address": ip_address,
                "version": "1.6.3"
            }
        }
        return self._send_request(data)

    def delete_domain(self, domain_id):
        """
        Deletes a domain by its ID.

        Args:
            domain_id (int): The ID of the domain to delete.

        Returns:
            dict: The result of the domain deletion.
        """
        data = {
            "method": "domain.delete",
            "params": {
                "domain_id": domain_id,
                "version": "1.6.3"
            }
        }
        return self._send_request(data)

if __name__ == "__main__":
    # Replace with your Plesk server credentials
    PLESK_HOST = "your-plesk-server.com"
    PLESK_USERNAME = "your-username"
    PLESK_PASSWORD = "your-password"

    pleask_api = PleskAPI(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)

    # List existing domains
    try:
        domains = pleask_api.list_domains()
        print("Current domains:", domains)

        # Create a new domain
        new_domain = "example.com"
        ip_address = "192.0.2.1"  # Replace with your server's IP
        result_create = pleask_api.create_domain(new_domain, ip_address)
        print("Domain created:", result_create)

        # Delete the new domain
        domain_id = result_create['result']['id']  # Get the ID of the newly created domain
        result_delete = pleask_api.delete_domain(domain_id)
        print("Domain deleted:", result_delete)

    except Exception as e:
        print(f"An error occurred: {e}")
```
