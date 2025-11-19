"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Explain how to automate website management tasks using Plesk's API.
Generated: DETERMINISTIC_fb42ef645ee6f7f8
Batch ID: 20250612_161617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server.com": {
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

class PleskAPI:
    """
    A class to interact with the Plesk API for automating website management tasks.
    """

    def __init__(self, host, username, password):
        """
        Initializes the PleskAPI instance with host, username, and password.

        :param host: The URL of the Plesk server.
        :param username: The username for Plesk login.
        :param password: The password for Plesk login.
        """
        self.host = host
        self.username = username
        self.password = password
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.session = requests.Session()

    def _request(self, method, endpoint, data=None):
        """
        Internal method to handle API requests.

        :param method: HTTP method (GET, POST, PUT, DELETE).
        :param endpoint: API endpoint to call.
        :param data: Data to send with the request (for POST/PUT).
        :return: Response from the Plesk API.
        """
        url = f"{self.host}/api/v2{endpoint}"
        try:
            response = self.session.request(method, url, headers=self.headers,
                                             auth=(self.username, self.password),
                                             json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def list_websites(self):
        """
        Lists all websites managed by Plesk.

        :return: A list of websites.
        """
        endpoint = "/websites"
        return self._request("GET", endpoint)

    def create_website(self, domain, ip_address, username, password):
        """
        Creates a new website in Plesk.

        :param domain: The domain name for the new website.
        :param ip_address: The IP address to assign to the website.
        :param username: The username for the new website's subscription.
        :param password: The password for the new website's subscription.
        :return: The response from the API.
        """
        endpoint = "/websites"
        data = {
            "name": domain,
            "ip": ip_address,
            "webspace": {
                "login": username,
                "password": password
            }
        }
        return self._request("POST", endpoint, data)

    def delete_website(self, website_id):
        """
        Deletes a website from Plesk.

        :param website_id: The ID of the website to delete.
        :return: The response from the API.
        """
        endpoint = f"/websites/{website_id}"
        return self._request("DELETE", endpoint)

# Example usage:
if __name__ == "__main__":
    # Initialize connection to Plesk API
    plesk = PleskAPI(host="https://your-plesk-server.com", 
                     username="your-username", 
                     password="your-password")
    
    # List existing websites
    websites = plesk.list_websites()
    print("Websites:", websites)

    # Create a new website
    new_website = plesk.create_website(domain="example.com", 
                                        ip_address="192.0.2.1", 
                                        username="newuser", 
                                        password="securepassword")
    print("New Website Created:", new_website)

    # Delete a website
    if websites and 'id' in websites[0]:  # Ensure there is at least one website
        website_id = websites[0]['id']
        deletion_response = plesk.delete_website(website_id)
        print("Website Deleted:", deletion_response)
```
