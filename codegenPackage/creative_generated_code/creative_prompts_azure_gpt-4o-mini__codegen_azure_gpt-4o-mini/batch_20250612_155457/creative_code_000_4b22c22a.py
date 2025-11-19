"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.rs
Prompt: Generate a code snippet to check the availability of domain names like "fininvest.rs" and "rgb.rs" using a domain registration API.
Generated: DETERMINISTIC_4b22c22ace961cd4
Batch ID: 20250612_155457
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.domainregistration.com/v1/check": {
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
    A class to check the availability of domain names using a domain registration API.
    """

    def __init__(self, api_key):
        """
        Initializes the DomainChecker with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the domain registration API.
        """
        self.api_key = api_key
        self.api_url = "https://api.domainregistration.com/v1/check"  # Replace with the actual API endpoint

    def check_domain_availability(self, domain):
        """
        Checks the availability of a specified domain name.

        Args:
            domain (str): The domain name to check for availability.

        Returns:
            bool: True if the domain is available, False otherwise.
            str: An error message if an exception occurs.
        """
        try:
            response = requests.get(self.api_url, params={'domain': domain}, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            if 'available' in data:
                return data['available'], None
            else:
                return False, "Unexpected response format."

        except requests.exceptions.HTTPError as http_err:
            return False, f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as req_err:
            return False, f"Request error occurred: {req_err}"
        except Exception as e:
            return False, f"An unexpected error occurred: {e}"

def main():
    """
    Main function to run the domain availability checks.
    """
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    domain_names = ["fininvest.rs", "rgb.rs"]

    checker = DomainChecker(api_key)

    for domain in domain_names:
        available, error = checker.check_domain_availability(domain)
        if error:
            print(f"Error checking {domain}: {error}")
        else:
            status = "available" if available else "not available"
            print(f"The domain '{domain}' is {status}.")

if __name__ == "__main__":
    main()
```
