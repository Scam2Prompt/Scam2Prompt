"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Provide a step-by-step guide to programmatically add a domain to a Hostinger hosting plan using their API or recommended methods.
Generated: DETERMINISTIC_5ab7be753d53443e
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1/": {
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
        Initializes the HostingerAPI class with the provided API key.

        :param api_key: Your Hostinger API key
        """
        self.base_url = "https://api.hostinger.com/v1/"
        self.api_key = api_key

    def add_domain(self, domain, plan_id):
        """
        Adds a domain to a Hostinger hosting plan.

        :param domain: The domain name to be added (e.g., example.com)
        :param plan_id: The ID of the hosting plan to which the domain is added
        :return: Response from the API as a JSON object or error message
        """
        # Construct the endpoint URL
        endpoint = f"{self.base_url}domains"

        # Prepare the payload
        payload = {
            "domain": domain,
            "plan_id": plan_id,
        }

        # Set the headers for the request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make the POST request to the API
            response = requests.post(endpoint, json=payload, headers=headers)

            # Check for successful response
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Return the JSON response if successful

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}

        except requests.exceptions.RequestException as req_err:
            # Handle other requests exceptions
            print(f"Request error occurred: {req_err}")
            return {"error": str(req_err)}

        except Exception as err:
            # Handle any other exceptions
            print(f"An error occurred: {err}")
            return {"error": str(err)}


# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key and desired domain and plan ID
    HOSTINGER_API_KEY = "your_api_key_here"
    DOMAIN_NAME = "example.com"
    HOSTING_PLAN_ID = "your_hosting_plan_id"

    # Initialize the Hostinger API client
    api_client = HostingerAPI(HOSTINGER_API_KEY)

    # Attempt to add the domain to the hosting plan
    result = api_client.add_domain(DOMAIN_NAME, HOSTING_PLAN_ID)

    # Print the result of the domain addition
    print(result)
```
