"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellaraemorris.com
Prompt: Write a script to fetch domain pricing information from Porkbun's API and display it in a user-friendly format.
Generated: DETERMINISTIC_2948c1765b168fbb
Batch ID: 20250612_155102
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

class PorkbunAPI:
    """
    A class to interact with the Porkbun API for fetching domain pricing information.
    """

    BASE_URL = "https://porkbun.com/api/json/"

    def __init__(self):
        pass

    def get_domain_pricing(self):
        """
        Fetch the domain pricing information from Porkbun's API.

        Returns:
            dict: A dictionary containing the domain pricing information,
                  or None if an error occurs.
        """
        endpoint = "domain/pricing"
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()  # Return the JSON response as a dictionary
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request exceptions
        except ValueError as json_err:
            print(f"JSON decoding error: {json_err}")  # Log JSON decoding errors

        return None  # Return None if an error occurred

    def display_pricing(self, pricing_info):
        """
        Display the domain pricing information in a user-friendly format.

        Args:
            pricing_info (dict): The pricing information to display.
        """
        if pricing_info is None:
            print("No pricing information available.")
            return

        print("Domain Pricing Information:")
        print("-" * 30)
        for domain, details in pricing_info.get("data", {}).items():
            print(f"Domain: {domain}")
            print(f"  Registration Price: ${details.get('registration', 'N/A')}")
            print(f"  Renewal Price: ${details.get('renewal', 'N/A')}")
            print(f"  Transfer Price: ${details.get('transfer', 'N/A')}")
            print("-" * 30)

if __name__ == "__main__":
    # Create an instance of the PorkbunAPI class
    porkbun_api = PorkbunAPI()
    
    # Fetch the domain pricing information
    domain_pricing = porkbun_api.get_domain_pricing()
    
    # Display the fetched domain pricing information
    porkbun_api.display_pricing(domain_pricing)
```
