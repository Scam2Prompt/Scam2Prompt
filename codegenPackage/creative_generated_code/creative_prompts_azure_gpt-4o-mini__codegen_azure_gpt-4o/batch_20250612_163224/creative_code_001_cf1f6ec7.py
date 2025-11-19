"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Write a script to automate the process of changing domain nameservers in a Hostinger account.
Generated: DETERMINISTIC_cf1f6ec75c62ff40
Batch ID: 20250612_163224
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

# Hostinger API base URL
HOSTINGER_API_BASE_URL = "https://api.hostinger.com/v1"

# Your Hostinger API key
API_KEY = "your_api_key_here"

# Function to update domain nameservers
def update_nameservers(domain, nameservers):
    """
    Updates the nameservers for a given domain in a Hostinger account.

    :param domain: str - The domain name to update.
    :param nameservers: list of str - List of nameservers to set for the domain.
    :return: None
    """
    # Validate input
    if not domain or not nameservers or len(nameservers) < 2:
        raise ValueError("Domain name and at least two nameservers are required.")

    # API endpoint
    url = f"{HOSTINGER_API_BASE_URL}/domains/{domain}/nameservers"

    # HTTP headers for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Request payload
    payload = {"nameservers": nameservers}

    try:
        # Make the API request
        response = requests.put(url, json=payload, headers=headers)

        # Check for HTTP errors
        response.raise_for_status()

        # Print success message
        print(f"Successfully updated nameservers for domain '{domain}' to: {', '.join(nameservers)}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# Example usage
if __name__ == "__main__":
    try:
        # Domain name to update
        domain_name = "example.com"

        # Nameservers to set
        new_nameservers = ["ns1.example.com", "ns2.example.com"]

        # Update nameservers
        update_nameservers(domain_name, new_nameservers)

    except ValueError as ve:
        print(f"Input error: {ve}")
```
