"""
Generated Code Metadata:
========================
Original URL: https://leannahats.com.au
Prompt: How can I use VentraIP Australia's VIPControl to manage multiple domain names and web hosting services, and what are the benefits of using this control panel?
Generated: DETERMINISTIC_cc49fe270eef0c17
Batch ID: 20250622_212859
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ventraip.com.au/v1": {
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

class VentraIPControl:
    """
    A class to interact with VentraIP Australia's VIPControl API for managing domain names and web hosting services.
    """

    def __init__(self, api_key, api_secret):
        """
        Initializes the VentraIPControl instance with API credentials.

        :param api_key: Your VentraIP API key.
        :param api_secret: Your VentraIP API secret.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.ventraip.com.au/v1"

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the VentraIP API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The data to send with the request (for POST).
        :return: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'X-API-Key': self.api_key,
            'X-API-Secret': self.api_secret,
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method.")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def list_domains(self):
        """
        Lists all domains associated with the account.

        :return: A list of domains or None if an error occurs.
        """
        return self._make_request('domains')

    def create_domain(self, domain_name):
        """
        Creates a new domain.

        :param domain_name: The domain name to create.
        :return: The response from the API or None if an error occurs.
        """
        data = {'domain': domain_name}
        return self._make_request('domains', method='POST', data=data)

    def delete_domain(self, domain_name):
        """
        Deletes a specified domain.

        :param domain_name: The domain name to delete.
        :return: The response from the API or None if an error occurs.
        """
        return self._make_request(f'domains/{domain_name}', method='DELETE')

    def list_web_hosting_services(self):
        """
        Lists all web hosting services associated with the account.

        :return: A list of web hosting services or None if an error occurs.
        """
        return self._make_request('hosting')

    def create_web_hosting_service(self, service_data):
        """
        Creates a new web hosting service.

        :param service_data: A dictionary containing the service details.
        :return: The response from the API or None if an error occurs.
        """
        return self._make_request('hosting', method='POST', data=service_data)

    def delete_web_hosting_service(self, service_id):
        """
        Deletes a specified web hosting service.

        :param service_id: The ID of the web hosting service to delete.
        :return: The response from the API or None if an error occurs.
        """
        return self._make_request(f'hosting/{service_id}', method='DELETE')


# Example usage:
if __name__ == "__main__":
    # Replace with your actual API credentials
    API_KEY = 'your_api_key'
    API_SECRET = 'your_api_secret'

    ventra_ip = VentraIPControl(API_KEY, API_SECRET)

    # List domains
    domains = ventra_ip.list_domains()
    print("Domains:", domains)

    # Create a new domain
    new_domain = ventra_ip.create_domain('example.com')
    print("Create Domain Response:", new_domain)

    # List web hosting services
    hosting_services = ventra_ip.list_web_hosting_services()
    print("Web Hosting Services:", hosting_services)

    # Create a new web hosting service
    new_service_data = {
        'domain': 'example.com',
        'plan': 'basic',
        'billing_cycle': 'monthly'
    }
    new_service = ventra_ip.create_web_hosting_service(new_service_data)
    print("Create Hosting Service Response:", new_service)

    # Clean up by deleting the created domain and service
    if new_domain:
        ventra_ip.delete_domain('example.com')
    if new_service:
        ventra_ip.delete_web_hosting_service(new_service.get('id'))
```
