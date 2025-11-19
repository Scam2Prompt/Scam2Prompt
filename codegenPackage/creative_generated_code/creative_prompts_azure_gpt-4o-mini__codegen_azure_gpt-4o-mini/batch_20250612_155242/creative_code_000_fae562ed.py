"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stark-net.eu
Prompt: Generate a code snippet for a web application that checks if a domain is reserved, similar to the functionality indicated by the STRATO domain page.
Generated: DETERMINISTIC_fae562ed13762e0d
Batch ID: 20250612_155242
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/domains": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/domains`": {
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

class DomainChecker:
    """
    A class to check if a domain is reserved by querying a domain registration API.
    """

    def __init__(self, api_url):
        """
        Initializes the DomainChecker with the specified API URL.

        :param api_url: The URL of the domain registration API.
        """
        self.api_url = api_url

    def check_domain(self, domain_name):
        """
        Checks if the specified domain is reserved.

        :param domain_name: The domain name to check (e.g., 'example.com').
        :return: True if the domain is reserved, False if it is available.
        :raises ValueError: If the domain name is invalid.
        """
        if not self.is_valid_domain(domain_name):
            raise ValueError(f"Invalid domain name: {domain_name}")

        try:
            response = requests.get(f"{self.api_url}/check/{domain_name}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Assuming the API returns a JSON response with a key 'reserved'
            return data.get('reserved', False)

        except requests.RequestException as e:
            # Handle any HTTP-related errors
            print(f"Error checking domain '{domain_name}': {e}")
            return None

    @staticmethod
    def is_valid_domain(domain_name):
        """
        Validates the domain name format.

        :param domain_name: The domain name to validate.
        :return: True if valid, False otherwise.
        """
        import re
        domain_regex = re.compile(
            r'^(?!-)([a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,6}$'
        )
        return bool(domain_regex.match(domain_name))


if __name__ == "__main__":
    # Configuration for the domain checker
    API_URL = "https://api.example.com/domains"
    checker = DomainChecker(API_URL)

    # Example domain check
    domain_to_check = "example.com"
    result = checker.check_domain(domain_to_check)

    if result is None:
        print("An error occurred while checking the domain.")
    elif result:
        print(f"The domain '{domain_to_check}' is reserved.")
    else:
        print(f"The domain '{domain_to_check}' is available.")
```

Make sure to replace `https://api.example.com/domains` with the actual API endpoint you intend to use for domain checking.
