"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xn--fixdfloat-23a.com
Prompt: Create a guide on using Plesk's GUI for managing web servers, including code for common tasks like adding domains and managing databases.
Generated: DETERMINISTIC_b4dfaa7dfcbbb532
Batch ID: 20250612_162624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443": {
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
# Import required libraries
import requests
import json

class PleskAPI:
    def __init__(self, host, username, password):
        """
        Initializes the Plesk API client with host, username, and password.

        :param host: The URL of the Plesk server (e.g., 'https://your-plesk-server:8443')
        :param username: The Plesk admin username
        :param password: The Plesk admin password
        """
        self.host = host
        self.username = username
        self.password = password
        self.headers = {
            'Content-Type': 'application/json'
        }

    def _make_request(self, method, endpoint, data=None):
        """
        Makes an HTTP request to the Plesk API.

        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint
        :param data: Data to be sent with the request
        :return: Response from the Plesk API
        """
        url = f"{self.host}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, auth=(self.username, self.password), json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None

    def add_domain(self, domain_name):
        """
        Adds a new domain to the Plesk server.

        :param domain_name: The name of the domain to add
        :return: Response from the Plesk API
        """
        endpoint = "/domains"
        data = {
            "domain": {
                "name": domain_name,
                "suspended": "false"
            }
        }
        return self._make_request("POST", endpoint, data)

    def list_domains(self):
        """
        Lists all domains on the Plesk server.

        :return: List of domains
        """
        endpoint = "/domains"
        return self._make_request("GET", endpoint)

    def add_database(self, db_name, db_type, domain_id):
        """
        Adds a new database to a specified domain.

        :param db_name: The name of the database
        :param db_type: The type of the database (e.g., 'mysql')
        :param domain_id: The ID of the domain to which the database will be added
        :return: Response from the Plesk API
        """
        endpoint = f"/databases"
        data = {
            "database": {
                "name": db_name,
                "type": db_type,
                "domain-id": domain_id
            }
        }
        return self._make_request("POST", endpoint, data)

    def list_databases(self):
        """
        Lists all databases on the Plesk server.

        :return: List of databases
        """
        endpoint = "/databases"
        return self._make_request("GET", endpoint)

# Example usage
if __name__ == "__main__":
    # Replace with your actual Plesk server details
    PLESK_HOST = "https://your-plesk-server:8443"
    PLESK_USERNAME = "admin"
    PLESK_PASSWORD = "your-password"

    # Create an instance of PleskAPI
    plesk_api = PleskAPI(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)

    # Adding a domain
    domain_response = plesk_api.add_domain("example.com")
    print("Add Domain Response:", domain_response)

    # Listing all domains
    domains = plesk_api.list_domains()
    print("List of Domains:", domains)

    # Adding a database
    if domains and 'domains' in domains:
        domain_id = domains['domains'][0]['id']  # Get the ID of the first domain
        db_response = plesk_api.add_database("example_db", "mysql", domain_id)
        print("Add Database Response:", db_response)

    # Listing all databases
    databases = plesk_api.list_databases()
    print("List of Databases:", databases)
```

This script uses the Plesk API to manage domains and databases programmatically. The code includes methods for adding domains, listing domains, adding databases, and listing databases, along with error handling and clear documentation.
