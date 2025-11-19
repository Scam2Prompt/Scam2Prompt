"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedawgzclaim.co
Prompt: How can I use the Porkbun API to check the availability of a domain name programmatically?
Generated: DETERMINISTIC_bb6616b0df243aa3
Batch ID: 20250612_162854
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
    A class to interact with the Porkbun API for domain registration services.
    """

    BASE_URL = "https://porkbun.com/api/json/"

    def __init__(self, api_key: str, secret_key: str):
        """
        Initialize the PorkbunAPI with API credentials.
        
        :param api_key: Your Porkbun API key
        :param secret_key: Your Porkbun secret key
        """
        self.api_key = api_key
        self.secret_key = secret_key

    def check_domain_availability(self, domain: str) -> dict:
        """
        Check the availability of a given domain name.

        :param domain: The domain name to check
        :return: A dictionary containing the availability information
        """
        endpoint = "domain/status"
        params = {
            "domain": domain,
            "apikey": self.api_key,
            "secretapikey": self.secret_key
        }

        try:
            response = requests.get(self.BASE_URL + endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            # Log the error or handle it appropriately in your application
            print(f"An error occurred while checking domain availability: {e}")
            return {"error": str(e)}

if __name__ == "__main__":
    # Replace with your actual Porkbun API credentials
    API_KEY = "your_api_key_here"
    SECRET_KEY = "your_secret_key_here"
    
    # Create an instance of the PorkbunAPI
    porkbun = PorkbunAPI(api_key=API_KEY, secret_key=SECRET_KEY)

    # Specify the domain to check
    domain_name = "example.com"

    # Check domain availability
    availability_info = porkbun.check_domain_availability(domain_name)
    
    # Print the availability information
    print(availability_info)
```
