"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellaraemorris.com
Prompt: What are the steps to set up DNS records for a domain purchased from Porkbun?
Generated: DETERMINISTIC_1a59f038c94c6a52
Batch ID: 20250612_162554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/": {
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

class PorkbunDNSManager:
    """
    A class to manage DNS records for a domain purchased from Porkbun.
    """

    def __init__(self, api_key, secret_key):
        """
        Initializes the PorkbunDNSManager with API credentials.

        :param api_key: Your Porkbun API key.
        :param secret_key: Your Porkbun secret key.
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = 'https://porkbun.com/api/json/'

    def _send_request(self, endpoint, data):
        """
        Sends a request to the Porkbun API.

        :param endpoint: The API endpoint to call.
        :param data: The data to send in the request.
        :return: The JSON response from the API.
        """
        try:
            response = requests.post(f'{self.base_url}{endpoint}', json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error communicating with Porkbun API: {e}")
            return None

    def get_domain_info(self, domain):
        """
        Retrieves information about the specified domain.

        :param domain: The domain to fetch information for.
        :return: Dictionary containing domain information or None on failure.
        """
        data = {
            'apikey': self.api_key,
            'secret': self.secret_key,
            'domain': domain
        }
        return self._send_request('domain/retrieve', data)

    def add_dns_record(self, domain, record_type, name, content, ttl=3600):
        """
        Adds a DNS record for the specified domain.

        :param domain: The domain to add the record for.
        :param record_type: The type of the DNS record (e.g., A, CNAME).
        :param name: The name of the DNS record.
        :param content: The content of the DNS record.
        :param ttl: Time to live for the DNS record in seconds (default is 3600).
        :return: Response from the API or None on failure.
        """
        data = {
            'apikey': self.api_key,
            'secret': self.secret_key,
            'domain': domain,
            'type': record_type,
            'name': name,
            'content': content,
            'ttl': ttl
        }
        return self._send_request('dns/create', data)

    def delete_dns_record(self, domain, record_id):
        """
        Deletes a DNS record for the specified domain.

        :param domain: The domain to delete the record from.
        :param record_id: The ID of the DNS record to delete.
        :return: Response from the API or None on failure.
        """
        data = {
            'apikey': self.api_key,
            'secret': self.secret_key,
            'domain': domain,
            'id': record_id
        }
        return self._send_request('dns/delete', data)

# Example usage (uncomment and replace with actual keys and domain):
# api_key = 'your_api_key'
# secret_key = 'your_secret_key'
# dns_manager = PorkbunDNSManager(api_key, secret_key)
# domain_info = dns_manager.get_domain_info('example.com')
# print(domain_info)
# dns_manager.add_dns_record('example.com', 'A', 'www', '192.0.2.1')
# dns_manager.delete_dns_record('example.com', 'record_id_here')
```
