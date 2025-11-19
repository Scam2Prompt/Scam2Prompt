"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbasedawgz.xyz
Prompt: Provide an example of using the Porkbun API to retrieve information about a parked domain and its registration details.
Generated: DETERMINISTIC_c5afbb4708a183c8
Batch ID: 20250612_163052
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.porkbun.com/v3": {
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

# Constants for Porkbun API
API_BASE_URL = "https://api.porkbun.com/v3"
API_KEY = "<your_api_key>"  # Replace with your Porkbun API key
API_SECRET = "<your_api_secret>"  # Replace with your Porkbun API secret

def get_domain_info(domain_name):
    """
    Retrieves information about a parked domain and its registration details using the Porkbun API.

    :param domain_name: The domain name to query (e.g., "example.com").
    :return: Dictionary containing domain information if successful, None otherwise.
    """
    # Define the endpoint for domain info
    endpoint = f"{API_BASE_URL}/ping"  # Note: Adjust endpoint based on actual Porkbun API documentation
    
    # Prepare request payload
    payload = {
        "apikey": API_KEY,
        "secretapikey": API_SECRET,
        "domain": domain_name
    }
    
    try:
        # Make the HTTP POST request
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        domain_info = response.json()

        # Check for a successful response
        if domain_info.get("status") == "SUCCESS":
            return domain_info
        else:
            print(f"Error: {domain_info.get('message')}")
            return None
    except requests.RequestException as e:
        # Handle any request-related errors
        print(f"HTTP Request failed: {e}")
        return None
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Failed to parse JSON response: {e}")
        return None

# Example usage
if __name__ == "__main__":
    domain_name = "example.com"
    domain_info = get_domain_info(domain_name)
    
    if domain_info:
        print(f"Domain Information for {domain_name}:")
        print(domain_info)
    else:
        print(f"Failed to retrieve information for domain {domain_name}.")
```

*Note*: Ensure you replace `<your_api_key>` and `<your_api_secret>` with your actual Porkbun API credentials. Also, verify the correct endpoint (`/ping` here is just a placeholder; use the appropriate endpoint from the Porkbun API documentation for retrieving parked domain and registration details).
