"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leannahats.com.au
Prompt: How can I implement SSL certificate management through the VentraIP API in a web application?
Generated: DETERMINISTIC_fb812fa5267a6657
Batch ID: 20250612_163423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ventraip.com.au/v3": {
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

class VentraIPAPI:
    """
    A class to interact with the VentraIP API for SSL certificate management.
    """

    def __init__(self, api_key, api_secret):
        """
        Initializes the VentraIPAPI with the provided API key and secret.

        :param api_key: API key for authenticating with the VentraIP API.
        :param api_secret: API secret for authenticating with the VentraIP API.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.ventraip.com.au/v3"

    def _request(self, endpoint, method="GET", data=None):
        """
        Internal method to handle API requests.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The payload for POST requests.
        :return: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
            "X-Api-Secret": self.api_secret
        }
        
        try:
            if method == "POST":
                response = requests.post(url, json=data, headers=headers)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response JSON
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def list_ssl_certificates(self):
        """
        Lists all SSL certificates associated with your account.

        :return: A list of SSL certificates or None if an error occurred.
        """
        return self._request("ssl-certificate")

    def create_ssl_certificate(self, domain, csr):
        """
        Creates a new SSL certificate for the specified domain.

        :param domain: The domain name for the SSL certificate.
        :param csr: The Certificate Signing Request (CSR) for the SSL certificate.
        :return: The response of the SSL certificate creation or None if an error occurred.
        """
        data = {
            "domain": domain,
            "csr": csr
        }
        return self._request("ssl-certificate", method="POST", data=data)

    def renew_ssl_certificate(self, certificate_id):
        """
        Renews an existing SSL certificate.

        :param certificate_id: The ID of the SSL certificate to renew.
        :return: The response of the SSL certificate renewal or None if an error occurred.
        """
        return self._request(f"ssl-certificate/{certificate_id}/renew", method="POST")

# Example usage (replace with actual credentials and data)
if __name__ == "__main__":
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    
    ventra_api = VentraIPAPI(api_key, api_secret)

    # List SSL certificates
    certificates = ventra_api.list_ssl_certificates()
    print(certificates)

    # Create a new SSL certificate
    new_certificate_response = ventra_api.create_ssl_certificate("example.com", "your_csr_here")
    print(new_certificate_response)

    # Renew an SSL certificate
    renewal_response = ventra_api.renew_ssl_certificate("your_certificate_id")
    print(renewal_response)
```
