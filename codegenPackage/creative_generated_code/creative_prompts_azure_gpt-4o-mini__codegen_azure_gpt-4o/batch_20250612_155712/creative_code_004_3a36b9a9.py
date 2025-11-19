"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://org-morse.claims
Prompt: Provide an example of using the Porkbun API to retrieve information about my hosted domains.
Generated: DETERMINISTIC_3a36b9a95a8fcc51
Batch ID: 20250612_155712
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
API_KEY = "your_api_key_here"  # Replace with your actual API key
API_SECRET = "your_api_secret_here"  # Replace with your actual API secret

def fetch_domains(api_key, api_secret):
    """
    Fetches the list of hosted domains from the Porkbun API.

    Parameters:
        api_key (str): The API key for authentication.
        api_secret (str): The API secret for authentication.

    Returns:
        list: A list of domain names if successful.
        None: If the API request fails.
    """
    # Endpoint for retrieving domain list
    endpoint = f"{API_BASE_URL}/dns/retrieve"

    # Prepare the request payload for authentication
    payload = {
        "apikey": api_key,
        "apisecret": api_secret
    }

    try:
        # Make the POST request to the Porkbun API
        response = requests.post(endpoint, json=payload)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check the API response status
        if data.get("status") == "SUCCESS":
            # Return the list of domains
            return data.get("domains", [])
        else:
            # Log or handle API-level failure
            print(f"API error: {data.get('message')}")
            return None
    except requests.RequestException as e:
        # Handle request-level issues
        print(f"Request error: {e}")
        return None

if __name__ == "__main__":
    # Fetch and print the list of domains
    domains = fetch_domains(API_KEY, API_SECRET)
    if domains is not None:
        print("Hosted Domains:")
        for domain in domains:
            print(f"- {domain}")
    else:
        print("Failed to retrieve domains.")
```

**Note:** Replace `your_api_key_here` and `your_api_secret_here` with your actual Porkbun API credentials. Make sure to handle sensitive information securely and avoid hardcoding credentials in production environments.
