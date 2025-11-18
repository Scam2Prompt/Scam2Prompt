"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupocapernaum.com
Prompt: Create a Python script to check if a hosting account is active by detecting the presence of a default confirmation page.
Generated: DETERMINISTIC_9cf9216d5a32572f
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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

def is_hosting_account_active(url):
    """
    Check if a hosting account is active by verifying the presence of a default confirmation page.

    Parameters:
    url (str): The URL of the hosting account to check.

    Returns:
    bool: True if the hosting account is active (default page is found), False otherwise.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Check for specific content that signifies an active account
            # This can vary based on hosting providers; adjust the keywords as needed
            if "Default Page" in response.text or "Welcome" in response.text:
                return True
            else:
                return False
        else:
            # Log unexpected status codes
            print(f"Unexpected status code: {response.status_code}")
            return False

    except RequestException as e:
        # Handle requests-related exceptions
        print(f"An error occurred while trying to reach {url}: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    hosting_url = "http://example.com"  # Replace with the actual URL to check
    if is_hosting_account_active(hosting_url):
        print(f"The hosting account at {hosting_url} is active.")
    else:
        print(f"The hosting account at {hosting_url} is not active.")
```
