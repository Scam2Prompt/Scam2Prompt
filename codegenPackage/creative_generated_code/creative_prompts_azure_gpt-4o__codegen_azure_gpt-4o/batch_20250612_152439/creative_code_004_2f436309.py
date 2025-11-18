"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bouncebit.site
Prompt: Write a function to retrieve and update nameserver settings for a domain hosted on Hostinger, using relevant API endpoints or tools.
Generated: DETERMINISTIC_2f436309c0622d09
Batch ID: 20250612_152439
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com": {
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

def update_nameserver_settings(api_token, domain, nameservers):
    """
    Retrieve and update nameserver settings for a domain hosted on Hostinger.

    Parameters:
        api_token (str): Hostinger API Token for authentication.
        domain (str): The domain name to update nameserver settings for.
        nameservers (list): A list of nameservers to set for the domain.

    Returns:
        dict: Response data indicating success or failure of the operation.
    """
    # Base URL for Hostinger API
    base_url = "https://api.hostinger.com"

    # Headers for authorization
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    try:
        # Fetch current nameserver settings
        get_url = f"{base_url}/domains/{domain}/nameservers"
        response = requests.get(get_url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        current_settings = response.json()

        print(f"Current Nameservers: {current_settings}")

        # Update nameserver settings
        update_url = f"{base_url}/domains/{domain}/nameservers"
        payload = {"nameservers": nameservers}
        update_response = requests.put(update_url, json=payload, headers=headers)
        update_response.raise_for_status()  # Raise exception for HTTP errors

        return update_response.json()

    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        return {"error": str(e)}

    except Exception as e:
        # Handle generic errors
        return {"error": str(e)}

# Example usage:
api_token = "your_api_token_here"
domain = "example.com"
nameservers = ["ns1.example.com", "ns2.example.com"]
result = update_nameserver_settings(api_token, domain, nameservers)
print(result)
```
