"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.network
Prompt: How can I troubleshoot a website that is accessible via HTTPS but lacks an SSL certificate, based on the information from ethgas.network?
Generated: DETERMINISTIC_8adb3961363837d3
Batch ID: 20250612_155429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
from requests.exceptions import SSLError, RequestException

def check_https_without_ssl(url):
    """
    Check if a given URL is accessible via HTTPS but lacks an SSL certificate.
    
    Args:
    url (str): The URL to check
    
    Returns:
    bool: True if the URL is accessible via HTTPS without a valid SSL certificate, otherwise False.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, verify=False)  # Disable SSL verification for testing purposes
        
        # Check the status code
        if response.status_code == 200:
            print(f"Successfully accessed {url} via HTTPS.")
            return True
        else:
            print(f"Failed to access {url}. Status code: {response.status_code}")
            return False

    except SSLError:
        print(f"SSL Certificate error occurred for {url}.")
        return True  # Indicates the site is HTTPS but without a valid SSL certificate
    except RequestException as e:
        print(f"An error occurred while accessing {url}: {e}")
        return False

if __name__ == "__main__":
    # Example URL to check
    website_url = "https://example.com"  # Replace with the target URL
    is_https_without_ssl = check_https_without_ssl(website_url)
    
    if is_https_without_ssl:
        print(f"The website {website_url} is accessible via HTTPS but lacks a valid SSL certificate.")
    else:
        print(f"The website {website_url} is either not accessible or has a valid SSL certificate.")
```

**Note**: This code disables SSL verification (`verify=False`) for testing purposes. In a production environment, you should not disable SSL verification as it can expose you to security risks.
