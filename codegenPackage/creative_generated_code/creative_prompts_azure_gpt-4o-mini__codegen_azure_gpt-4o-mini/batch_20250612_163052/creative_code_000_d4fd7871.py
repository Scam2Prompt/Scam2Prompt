"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbasedawgz.xyz
Prompt: What are the steps to register a domain name using Porkbun, and can you provide a code snippet for automating domain registration via their API?
Generated: DETERMINISTIC_d4fd7871a4436807
Batch ID: 20250612_163052
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3/": {
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

class PorkbunAPI:
    """
    A class to interact with the Porkbun API for domain registration.
    """

    API_BASE_URL = 'https://porkbun.com/api/json/v3/'

    def __init__(self, api_key: str, secret: str):
        """
        Initializes the PorkbunAPI with provided API credentials.

        :param api_key: Your Porkbun API key
        :param secret: Your Porkbun secret
        """
        self.api_key = api_key
        self.secret = secret

    def register_domain(self, domain: str, years: int, nick: str, reg_contact: dict) -> dict:
        """
        Registers a domain using the Porkbun API.

        :param domain: The domain name to register
        :param years: Number of years to register the domain for
        :param nick: Nickname for the domain
        :param reg_contact: Registration contact details as a dictionary
        :return: Response from the Porkbun API
        """
        endpoint = 'register'
        payload = {
            'apikey': self.api_key,
            'secret': self.secret,
            'domain': domain,
            'years': years,
            'nick': nick,
            'contact': reg_contact
        }

        try:
            response = requests.post(self.API_BASE_URL + endpoint, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Log the HTTP error
        except Exception as err:
            print(f'An error occurred: {err}')  # Log any other errors

        return {}

# Example usage of the PorkbunAPI class
if __name__ == '__main__':
    # Replace with your actual API credentials
    API_KEY = 'YOUR_API_KEY'
    SECRET = 'YOUR_SECRET'

    porkbun_api = PorkbunAPI(API_KEY, SECRET)

    # Domain details
    domain_name = 'example.com'
    registration_years = 1
    domain_nickname = 'Example Domain'
    
    # Registration contact details
    registration_contact = {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address_1": "123 Example St",
        "city": "Example City",
        "state": "EX",
        "postalCode": "12345",
        "country": "US",
        "organization": "Example Org",
        "private": False
    }

    # Register the domain
    registration_response = porkbun_api.register_domain(domain_name, registration_years, domain_nickname, registration_contact)

    # Print the registration response
    print(registration_response)
```
