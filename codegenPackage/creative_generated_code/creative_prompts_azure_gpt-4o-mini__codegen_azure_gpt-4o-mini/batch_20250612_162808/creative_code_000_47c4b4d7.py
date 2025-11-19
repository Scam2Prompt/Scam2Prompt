"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galanetwork.net
Prompt: Generate a Python script to register a new domain using the .CN or .中国 TLDs as outlined by the China Internet Network Information Center.
Generated: DETERMINISTIC_47c4b4d781c0f920
Batch ID: 20250612_162808
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/domain": {
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

class DomainRegistrationError(Exception):
    """Custom exception for domain registration errors."""
    pass

class DomainRegistrar:
    """Class to handle the domain registration process."""

    def __init__(self, api_url, api_key):
        """Initialize the registrar with API URL and authentication key."""
        self.api_url = api_url
        self.api_key = api_key

    def register_domain(self, domain_name, registrant_info):
        """
        Register a new domain.

        :param domain_name: str, the domain name to register (must end with .CN or .中国)
        :param registrant_info: dict, information about the registrant (should contain required fields)
        :raises DomainRegistrationError: if the registration fails
        :return: dict, response from the registration API
        """
        if not self._is_valid_domain(domain_name):
            raise ValueError("Domain name must end with .CN or .中国")

        # Prepare the request payload
        payload = {
            'api_key': self.api_key,
            'domain_name': domain_name,
            'registrant_info': registrant_info
        }

        try:
            # Send the registration request
            response = requests.post(f"{self.api_url}/register", json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            # Return the response JSON
            return response.json()

        except requests.HTTPError as http_err:
            raise DomainRegistrationError(f"HTTP error occurred: {http_err}") from http_err
        except requests.RequestException as req_err:
            raise DomainRegistrationError(f"Request error occurred: {req_err}") from req_err

    def _is_valid_domain(self, domain_name):
        """Validate the domain name against allowed TLDs."""
        return domain_name.endswith('.CN') or domain_name.endswith('.中国')


if __name__ == "__main__":
    # Example usage
    API_URL = "https://api.example.com/domain"
    API_KEY = "your_api_key_here"

    registrar = DomainRegistrar(API_URL, API_KEY)

    domain = "example.cn"
    registrant = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+8613800138000",
        "organization": "Example Org",
        "address": "123 Example St, Beijing, China",
    }

    try:
        registration_response = registrar.register_domain(domain, registrant)
        print("Domain registered successfully:", registration_response)
    except DomainRegistrationError as e:
        print("Failed to register domain:", e)
    except ValueError as ve:
        print("Validation error:", ve)
```
