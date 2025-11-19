"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leannahats.com.au
Prompt: Generate a code snippet to integrate domain name registration with VentraIP's API for managing domain names.
Generated: DETERMINISTIC_86846e0d6038bba5
Batch ID: 20250612_163423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ventraip.com.au": {
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
    A class to interact with the VentraIP API for domain name registration and management.
    """

    def __init__(self, api_key, username):
        """
        Initialize the VentraIPAPI instance with the provided API key and username.

        :param api_key: API key for authenticating with the VentraIP API
        :param username: Username for the VentraIP account
        """
        self.api_key = api_key
        self.username = username
        self.base_url = 'https://api.ventraip.com.au'

    def register_domain(self, domain_name, years=1):
        """
        Registers a new domain name for the specified number of years.

        :param domain_name: The domain name to register
        :param years: Number of years to register the domain for (default is 1)
        :return: Response from the API
        """
        url = f"{self.base_url}/domain/register"
        payload = {
            'domain': domain_name,
            'years': years
        }
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key,
            'X-Username': self.username
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response if the request was successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

        return None  # Return None if there was an error

    def check_domain_availability(self, domain_name):
        """
        Checks the availability of a domain name.

        :param domain_name: The domain name to check
        :return: Availability status and response from the API
        """
        url = f"{self.base_url}/domain/check"
        payload = {
            'domain': domain_name
        }
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key,
            'X-Username': self.username
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None

# Example usage (this should be removed or commented out in production)
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    username = "YOUR_USERNAME"
    ventra_api = VentraIPAPI(api_key, username)

    # Check domain availability
    domain_name = "example.com"
    availability = ventra_api.check_domain_availability(domain_name)
    print(f"Domain Availability: {availability}")

    # Register a domain
    registration_response = ventra_api.register_domain(domain_name, years=2)
    print(f"Registration Response: {registration_response}")
```
