"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Create a tutorial on using the TON DNS service to register a domain name on the TON network, including code examples.
Generated: DETERMINISTIC_77335e65c975a23d
Batch ID: 20250612_162843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://tonapi.io/v1/dns": {
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
# Import required libraries
import requests
import json

# Define constants for the TON DNS service
TON_DNS_API_URL = "https://tonapi.io/v1/dns"

def register_domain(api_key, domain_name, owner_public_key):
    """
    Register a domain name on the TON network via TON DNS service.

    Parameters:
        api_key (str): API key for authenticating with the TON DNS service.
        domain_name (str): The domain name to register.
        owner_public_key (str): The public key of the domain owner.

    Returns:
        dict: Response from the TON DNS service.
    """
    # Prepare the request payload
    payload = {
        "domain": domain_name,
        "owner": owner_public_key,
        "action": "register"
    }

    # Set up the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Send the POST request to register the domain
        response = requests.post(TON_DNS_API_URL, headers=headers, data=json.dumps(payload))
        
        # Raise an error for bad responses
        response.raise_for_status()

        # Return the response in JSON format
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error occurred: {json_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None

if __name__ == "__main__":
    # Example usage of the register_domain function

    # Replace with your actual API key, domain name, and owner's public key
    API_KEY = "YOUR_API_KEY"
    DOMAIN_NAME = "example.ton"
    OWNER_PUBLIC_KEY = "YOUR_PUBLIC_KEY"

    # Register the domain
    response = register_domain(API_KEY, DOMAIN_NAME, OWNER_PUBLIC_KEY)

    # Check if the registration was successful
    if response:
        print("Domain registration response:", response)
    else:
        print("Domain registration failed.")
```

Make sure to replace `YOUR_API_KEY`, `example.ton`, and `YOUR_PUBLIC_KEY` with your actual API key, desired domain name, and owner's public key respectively before running this code.
