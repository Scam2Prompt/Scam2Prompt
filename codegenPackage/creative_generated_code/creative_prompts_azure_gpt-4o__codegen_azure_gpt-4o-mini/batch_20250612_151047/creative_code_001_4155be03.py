"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallet.ro
Prompt: Generate code to perform a bulk domain name search using the EUReg API and return the results in JSON format.
Generated: DETERMINISTIC_4155be031b9bf2f6
Batch ID: 20250612_151047
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.eurid.eu/v1/domains": {
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

class DomainSearchError(Exception):
    """Custom exception for domain search errors."""
    pass

class EURegAPI:
    BASE_URL = "https://api.eurid.eu/v1/domains"

    def __init__(self, api_key: str):
        """
        Initialize the EURegAPI client with an API key.
        
        :param api_key: API key for authenticating requests.
        """
        self.api_key = api_key

    def search_domains(self, domain_list: list) -> dict:
        """
        Perform a bulk domain name search.

        :param domain_list: A list of domain names to search for.
        :return: A dictionary containing the search results.
        :raises DomainSearchError: If an error occurs during the API request.
        """
        try:
            # Prepare the request payload
            payload = {
                "domains": domain_list
            }
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Make the API request
            response = requests.post(self.BASE_URL, headers=headers, data=json.dumps(payload))

            # Check if the request was successful
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            raise DomainSearchError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise DomainSearchError(f"Request error occurred: {req_err}")
        except json.JSONDecodeError as json_err:
            raise DomainSearchError(f"JSON decoding error: {json_err}")

def main():
    # Sample usage of the EURegAPI class
    API_KEY = 'YOUR_API_KEY'  # Replace with your EUReg API key
    domains_to_search = [
        "example.eu",
        "test.eu",
        "sample.eu"
    ]

    try:
        api_client = EURegAPI(API_KEY)
        results = api_client.search_domains(domains_to_search)
        print(json.dumps(results, indent=4))  # Print the results in pretty JSON format

    except DomainSearchError as e:
        print(f"An error occurred during the domain search: {e}")

if __name__ == "__main__":
    main()
```
