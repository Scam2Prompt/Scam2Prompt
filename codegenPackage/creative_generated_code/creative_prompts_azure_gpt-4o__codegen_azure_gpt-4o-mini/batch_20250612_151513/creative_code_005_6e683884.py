"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-community.42web.io
Prompt: Create a Python script to automate the setup of SSL certificates on a hosting platform that offers free and simple SSL, such as iFastNet.
Generated: DETERMINISTIC_6e6838849fd56731
Batch ID: 20250612_151513
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
import json

class SSLSetupError(Exception):
    """Custom exception for SSL setup errors."""
    pass

def get_api_key():
    """Fetch the API key from environment variables or configuration."""
    import os
    api_key = os.getenv('IFASTNET_API_KEY')
    if not api_key:
        raise SSLSetupError("API key not found. Please set the IFASTNET_API_KEY environment variable.")
    return api_key

def setup_ssl(domain, api_key):
    """Set up SSL certificate for the specified domain using iFastNet API.

    Args:
        domain (str): The domain name to set up SSL for.
        api_key (str): The API key for authentication with the iFastNet API.

    Raises:
        SSLSetupError: If there is an error during the SSL setup process.
    """
    url = "https://api.ifastnet.com/ssl/setup"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'domain': domain,
        'ssl_type': 'free'  # Specify the type of SSL
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        if result.get('success'):
            print(f"SSL setup successfully for domain: {domain}")
        else:
            raise SSLSetupError(f"SSL setup failed: {result.get('message')}")
    except requests.exceptions.RequestException as e:
        raise SSLSetupError(f"Request failed: {e}")

def main():
    """Main function to set up SSL for a given domain."""
    try:
        domain = input("Enter the domain name (e.g., example.com): ").strip()
        api_key = get_api_key()
        setup_ssl(domain, api_key)
    except SSLSetupError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Make sure to set your IFASTNET_API_KEY in your environment before running the script.
