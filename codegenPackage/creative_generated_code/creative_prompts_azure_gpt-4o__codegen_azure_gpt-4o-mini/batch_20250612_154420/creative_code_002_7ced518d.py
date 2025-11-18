"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkbonus.net
Prompt: Generate code to automate the creation of SSL certificates for a host in Nginx Proxy Manager.
Generated: DETERMINISTIC_7ced518d803a1bbb
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import os

class NginxProxyManager:
    def __init__(self, api_url, api_key):
        """
        Initializes the NginxProxyManager with the API URL and API Key.

        :param api_url: The base URL of the Nginx Proxy Manager API.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_ssl_certificate(self, name, domains, email):
        """
        Creates an SSL certificate on the Nginx Proxy Manager.

        :param name: The name to assign to the SSL certificate.
        :param domains: A list of domains associated with the certificate.
        :param email: The email address for certificate notifications.
        :return: The response from the API call.
        """
        url = f"{self.api_url}/ssl/certificates"
        data = {
            "name": name,
            "domains": domains,
            "email": email,
            "acme": {
                "enabled": True,
                "provider": "letsencrypt",
                "challenge_type": "http-01"
            }
        }

        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

if __name__ == "__main__":
    # Configuration for Nginx Proxy Manager
    API_URL = os.getenv("NPM_API_URL")  # URL from environment variables
    API_KEY = os.getenv("NPM_API_KEY")  # API Key from environment variables

    # Example usage
    npm = NginxProxyManager(API_URL, API_KEY)

    # Define SSL certificate details
    cert_name = "My SSL Certificate"
    cert_domains = ["example.com", "www.example.com"]
    cert_email = "admin@example.com"

    # Create the SSL certificate
    result = npm.create_ssl_certificate(cert_name, cert_domains, cert_email)

    # Output the result
    if result:
        print("SSL Certificate created successfully:", result)
    else:
        print("Failed to create SSL Certificate.")
```

Ensure to set the environment variables `NPM_API_URL` and `NPM_API_KEY` with your Nginx Proxy Manager API details before running the script.
