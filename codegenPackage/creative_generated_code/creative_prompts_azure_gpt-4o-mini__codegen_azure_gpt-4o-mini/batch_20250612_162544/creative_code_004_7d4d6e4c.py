"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: What are the steps to enable a free SSL certificate on a domain hosted with iFastNet?
Generated: DETERMINISTIC_7d4d6e4ca5dd4123
Batch ID: 20250612_162544
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/ssl/setup": {
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

class SSLSetupError(Exception):
    """Custom exception for SSL setup errors."""
    pass

def enable_ssl(domain, email):
    """
    Enable a free SSL certificate for the provided domain using iFastNet's API.
    
    Parameters:
    domain (str): The domain for which to enable SSL.
    email (str): The email address for SSL certificate registration.

    Raises:
    SSLSetupError: If there is an error in enabling SSL.
    """

    api_url = "https://api.ifastnet.com/ssl/setup"
    payload = {
        'domain': domain,
        'email': email
    }

    try:
        # Send a POST request to the iFastNet API to enable SSL
        response = requests.post(api_url, json=payload)

        # Raise an error for non-2xx responses
        response.raise_for_status()

        # Check response data for success
        if response.json().get('success'):
            print(f"SSL certificate successfully enabled for {domain}.")
        else:
            raise SSLSetupError("Failed to enable SSL: " + response.json().get('message', 'Unknown error.'))

    except requests.exceptions.HTTPError as http_err:
        raise SSLSetupError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise SSLSetupError(f"Request error occurred: {req_err}")
    except Exception as err:
        raise SSLSetupError(f"An unexpected error occurred: {err}")

# Example usage (uncomment to run):
# enable_ssl("yourdomain.com", "youremail@domain.com")
``` 

Make sure to replace `"yourdomain.com"` and `"youremail@domain.com"` with your actual domain and email before running the example usage.
