"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-swap.org
Prompt: How can Plesk be used to manage SSL certificates for hosted websites? Provide code examples for automating this process.
Generated: DETERMINISTIC_c1df49ea5778fef0
Batch ID: 20250612_152000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{plesk_host}:8443/": {
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

class PleskSSLManager:
    def __init__(self, plesk_host, username, password):
        """Initialize PleskSSLManager with Plesk host and credentials."""
        self.plesk_host = plesk_host
        self.username = username
        self.password = password
        self.api_url = f'https://{plesk_host}:8443/'
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({
            'Content-Type': 'application/json',
            'HTTP_Accept': 'application/json'
        })
        self._check_connection()

    def _check_connection(self):
        """Check if the connection to the Plesk server is successful."""
        response = self.session.get(self.api_url + 'api/v2.0/')
        if response.status_code != 200:
            raise ConnectionError(f"Failed to connect to Plesk API: {response.text}")

    def list_ssl_certificates(self):
        """List all SSL certificates managed by Plesk."""
        response = self.session.get(self.api_url + 'ssl-certificates')
        if response.status_code != 200:
            raise RuntimeError(f"Error fetching SSL certificates: {response.text}")
        return response.json()

    def add_ssl_certificate(self, domain, cert_data, key_data):
        """Add a new SSL certificate for a specified domain."""
        payload = {
            "certificate": {
                "name": f"{domain} SSL Certificate",
                "data": cert_data,
                "key": key_data
            },
            "domain": {
                "name": domain
            }
        }
        response = self.session.post(self.api_url + 'ssl-certificates', json=payload)
        if response.status_code != 201:
            raise RuntimeError(f"Error adding SSL certificate: {response.text}")
        return response.json()

    def remove_ssl_certificate(self, cert_id):
        """Remove an SSL certificate by its ID."""
        response = self.session.delete(self.api_url + f'ssl-certificates/{cert_id}')
        if response.status_code != 204:
            raise RuntimeError(f"Error removing SSL certificate: {response.text}")
        return f"SSL certificate with ID {cert_id} removed successfully."

    def update_ssl_certificate(self, cert_id, cert_data, key_data):
        """Update an existing SSL certificate."""
        payload = {
            "certificate": {
                "data": cert_data,
                "key": key_data
            }
        }
        response = self.session.put(self.api_url + f'ssl-certificates/{cert_id}', json=payload)
        if response.status_code != 200:
            raise RuntimeError(f"Error updating SSL certificate: {response.text}")
        return response.json()

# Usage example (you should replace these with actual values):
if __name__ == "__main__":
    try:
        plesk_host = 'your-plesk-host'
        username = 'admin'
        password = 'your-password'
        
        ssl_manager = PleskSSLManager(plesk_host, username, password)

        # List SSL certificates
        certs = ssl_manager.list_ssl_certificates()
        print("Existing SSL Certificates:", certs)

        # Add a new SSL certificate
        domain = 'example.com'
        cert_data = '-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----'
        key_data = '-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----'
        new_cert = ssl_manager.add_ssl_certificate(domain, cert_data, key_data)
        print("New SSL Certificate Added:", new_cert)

        # Update an SSL certificate
        cert_id = new_cert['id']  # Use the ID from the creation response
        updated_cert = ssl_manager.update_ssl_certificate(cert_id, cert_data, key_data)
        print("Updated SSL Certificate:", updated_cert)

        # Remove an SSL certificate
        removal_status = ssl_manager.remove_ssl_certificate(cert_id)
        print(removal_status)

    except Exception as e:
        print(f"An error occurred: {e}")
```
