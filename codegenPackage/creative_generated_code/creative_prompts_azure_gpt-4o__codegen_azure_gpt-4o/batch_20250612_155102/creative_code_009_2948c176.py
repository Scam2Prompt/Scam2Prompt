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
  "https://api.porkbun.com/v3/pricing/get": {
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
import sys

# Constants for the API
API_BASE_URL = "https://api.porkbun.com/v3/pricing/get"
API_KEY = "<YOUR_API_KEY>"  # Replace with your actual API key
API_SECRET = "<YOUR_API_SECRET>"  # Replace with your actual API secret

def fetch_domain_pricing():
    """
    Fetch domain pricing information from Porkbun's API.

    Returns:
        dict: The parsed JSON response containing domain pricing information.
    """
    # Prepare the payload for authentication
    payload = {
        "apikey": API_KEY,
        "apisecret": API_SECRET
    }

    try:
        # Make the POST request to the API
        response = requests.post(API_BASE_URL, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors
        print(f"Error fetching domain pricing information: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error parsing response: {e}", file=sys.stderr)
        sys.exit(1)

def display_pricing(pricing_data):
    """
    Display domain pricing information in a user-friendly format.

    Args:
        pricing_data (dict): The domain pricing data returned by the API.
    """
    # Check if the response contains pricing information
    if "pricing" not in pricing_data:
        print("No pricing information found in the API response.", file=sys.stderr)
        sys.exit(1)

    print("Domain Pricing Information")
    print("--------------------------")
    for tld, prices in pricing_data["pricing"].items():
        print(f"TLD: {tld}")
        print(f"  Registration: ${prices.get('registration', 'N/A')}")
        print(f"  Renewal: ${prices.get('renewal', 'N/A')}")
        print(f"  Transfer: ${prices.get('transfer', 'N/A')}")
        print()

def main():
    """
    Main function to fetch and display domain pricing information.
    """
    print("Fetching domain pricing information...")
    pricing_data = fetch_domain_pricing()
    display_pricing(pricing_data)

if __name__ == "__main__":
    main()
```
