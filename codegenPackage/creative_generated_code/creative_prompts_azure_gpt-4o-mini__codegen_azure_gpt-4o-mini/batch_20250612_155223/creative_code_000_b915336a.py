"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myamlcheckbot.com
Prompt: Write a code snippet to check the availability of a domain using a VPS and cPanel API.
Generated: DETERMINISTIC_b915336aac84fc41
Batch ID: 20250612_155223
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-cpanel-url:2083": {
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
import json

class DomainAvailabilityChecker:
    """
    A class to check the availability of a domain using the cPanel API.
    """

    def __init__(self, cpanel_url, username, password):
        """
        Initializes the DomainAvailabilityChecker with cPanel credentials.

        :param cpanel_url: The URL of the cPanel API.
        :param username: The cPanel username.
        :param password: The cPanel password.
        """
        self.cpanel_url = cpanel_url
        self.username = username
        self.password = password

    def check_domain_availability(self, domain_name):
        """
        Checks if the specified domain is available.

        :param domain_name: The domain name to check.
        :return: True if the domain is available, False otherwise.
        """
        api_endpoint = f"{self.cpanel_url}/json-api/cpanel"
        params = {
            'cpanel_jsonapi_user': self.username,
            'cpanel_jsonapi_apiversion': '2',
            'cpanel_jsonapi_module': 'DomainInfo',
            'cpanel_jsonapi_func': 'domaininfo',
            'domain': domain_name
        }

        try:
            response = requests.get(api_endpoint, params=params, auth=(self.username, self.password))

            # Check for HTTP request errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Check if the domain is available
            if 'data' in data and isinstance(data['data'], list):
                # If there are no records for the domain, it is available
                return len(data['data']) == 0
            else:
                # Handle unexpected response format
                print("Unexpected response format:", data)
                return False

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return False
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")
            return False
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")
            return False

# Example usage:
if __name__ == "__main__":
    # Replace with your actual cPanel credentials and domain to check
    cpanel_url = "https://your-cpanel-url:2083"
    username = "your_username"
    password = "your_password"
    
    domain_checker = DomainAvailabilityChecker(cpanel_url, username, password)
    
    domain_name_to_check = "exampledomain.com"
    is_available = domain_checker.check_domain_availability(domain_name_to_check)

    if is_available:
        print(f"The domain '{domain_name_to_check}' is available!")
    else:
        print(f"The domain '{domain_name_to_check}' is not available.")
```
