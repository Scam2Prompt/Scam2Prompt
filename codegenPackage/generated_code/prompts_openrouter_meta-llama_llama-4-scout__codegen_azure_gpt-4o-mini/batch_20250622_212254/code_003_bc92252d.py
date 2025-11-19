"""
Generated Code Metadata:
========================
Original URL: https://mrspongy.com
Prompt: Generate an API request to Cloudflare's Registrar to register a new domain name with a custom configuration.
Generated: DETERMINISTIC_bc92252df1e9180c
Batch ID: 20250622_212254
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
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

class CloudflareRegistrar:
    def __init__(self, api_token):
        """
        Initialize the CloudflareRegistrar with the provided API token.

        :param api_token: str - The API token for authenticating with Cloudflare's API.
        """
        self.api_token = api_token
        self.base_url = "https://api.cloudflare.com/client/v4"

    def register_domain(self, domain_name, email, nameservers):
        """
        Register a new domain with Cloudflare's Registrar.

        :param domain_name: str - The domain name to register.
        :param email: str - The email address associated with the domain registration.
        :param nameservers: list - A list of nameservers to set for the domain.
        :return: dict - The response from the API.
        """
        url = f"{self.base_url}/registrar/domains"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": domain_name,
            "email": email,
            "nameservers": nameservers
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            return {"error": str(err)}

# Example usage
if __name__ == "__main__":
    # Replace with your actual API token
    api_token = "YOUR_CLOUDFLARE_API_TOKEN"
    registrar = CloudflareRegistrar(api_token)

    # Domain registration details
    domain_name = "example.com"
    email = "admin@example.com"
    nameservers = ["ns1.example.com", "ns2.example.com"]

    # Register the domain
    result = registrar.register_domain(domain_name, email, nameservers)
    print(result)  # Output the result of the domain registration
```
