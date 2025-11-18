"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: Generate a step-by-step guide for adding a domain to a Hostinger hosting plan programmatically using available APIs or libraries.
Generated: DETERMINISTIC_769dc2aba2c738d7
Batch ID: 20250612_145306
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
    def __init__(self, api_key):
        """
        Initialize the Hostinger API client with the provided API key.
        
        :param api_key: Your Hostinger API key for authentication.
        """
        self.base_url = "https://api.hostinger.com/v1"
        self.api_key = api_key

    def add_domain(self, domain_name, plan_id):
        """
        Adds a domain to a Hostinger hosting plan.
        
        :param domain_name: The domain name to be added (e.g., 'example.com').
        :param plan_id: The ID of the hosting plan to which the domain will be added.
        :return: Response from the Hostinger API.
        """
        endpoint = f"{self.base_url}/domains"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "domain": domain_name,
            "plan_id": plan_id
        }
        
        try:
            response = requests.post(endpoint, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
    
if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    domain_to_add = "example.com"  # Domain you want to add
    hosting_plan_id = "123456"  # The hosting plan ID to which domain is added

    hostinger_api = HostingerAPI(API_KEY)
    response = hostinger_api.add_domain(domain_to_add, hosting_plan_id)
    
    if response:  # Check if the response is not None
        print("Domain added successfully:", response)
    else:
        print("Failed to add domain.")
```
