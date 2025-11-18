"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connext.site
Prompt: Write a script to programmatically change domain nameservers using Hostinger's API, referencing the domain management features described on the Hostinger platform.
Generated: DETERMINISTIC_8764031ae7469e9a
Batch ID: 20250612_150052
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
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

class HostingerAPI:
    """
    A class to interact with Hostinger's API for domain management.
    """

    BASE_URL = "https://api.hostinger.com/v1"
    
    def __init__(self, api_key):
        """
        Initializes the HostingerAPI with the provided API key.
        
        :param api_key: Your Hostinger API key for authentication
        """
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def change_nameservers(self, domain, nameservers):
        """
        Change the nameservers for a given domain.

        :param domain: The domain name for which to change nameservers
        :param nameservers: A list of nameservers to set for the domain
        :return: Response from the API
        """
        url = f"{self.BASE_URL}/domains/{domain}/nameservers"
        payload = {
            'nameservers': nameservers
        }

        try:
            response = requests.put(url, headers=self.headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response from the API
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")

# Example Usage
if __name__ == "__main__":
    # Replace with your actual API key and domain details
    API_KEY = "your_api_key_here"
    DOMAIN = "example.com"
    NAMESERVERS = ["ns1.exampledns.com", "ns2.exampledns.com"]

    hostinger_api = HostingerAPI(API_KEY)
    result = hostinger_api.change_nameservers(DOMAIN, NAMESERVERS)

    if result:
        print("Nameservers changed successfully:", result)
    else:
        print("Failed to change nameservers.")
```
