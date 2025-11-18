"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namestajnovidom.com
Prompt: Write a Python script to check if a given online betting platform has SSL encryption and supports 2FA authentication, referencing the security criteria mentioned on the 토토플레이 site.
Generated: DETERMINISTIC_86ce79decfec923b
Batch ID: 20250612_151334
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example-betting-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{parsed_url.netloc": {
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
from requests.exceptions import RequestException
from urllib.parse import urlparse

def check_ssl_encryption(url):
    """
    Check if the given URL has an SSL certificate.
    
    Args:
        url (str): The URL of the betting platform to check.
    
    Returns:
        bool: True if SSL is enabled, otherwise False.
    """
    parsed_url = urlparse(url)
    ssl_url = f"https://{parsed_url.netloc}"
    
    try:
        response = requests.get(ssl_url, timeout=5)
        return response.status_code == 200
    except RequestException:
        return False

def check_2fa_support(url):
    """
    Check if the given URL supports two-factor authentication.

    This is a simple check that looks for common 2FA keywords in the
    response content or headers. This approach may need to be 
    refined based on specific implementations of the betting platform.
    
    Args:
        url (str): The URL of the betting platform to check.
    
    Returns:
        bool: True if 2FA is supported, otherwise False.
    """
    try:
        response = requests.get(url, timeout=5)
        # Checking for presence of common 2FA keywords
        return "two-factor" in response.text.lower() or "2fa" in response.text.lower()
    except RequestException:
        return False

def main():
    """
    Main function to check SSL encryption and 2FA support for a given betting platform.
    """
    # Example betting platform URL (change as necessary)
    betting_platform_url = "https://example-betting-site.com"
    
    print(f"Checking security features for: {betting_platform_url}")
    
    # Check for SSL encryption
    ssl_status = check_ssl_encryption(betting_platform_url)
    if ssl_status:
        print("SSL encryption is enabled.")
    else:
        print("SSL encryption is NOT enabled.")
    
    # Check for 2FA support
    two_fa_status = check_2fa_support(betting_platform_url)
    if two_fa_status:
        print("Two-factor authentication is supported.")
    else:
        print("Two-factor authentication is NOT supported.")

if __name__ == "__main__":
    main()
```
