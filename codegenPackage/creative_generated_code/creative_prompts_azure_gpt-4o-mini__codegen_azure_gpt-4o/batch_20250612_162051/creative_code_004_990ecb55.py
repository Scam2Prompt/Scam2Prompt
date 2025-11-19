"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahlrentacar.com.tr
Prompt: How do I configure cURL to bypass SSL verification for testing purposes, and what are the risks involved?
Generated: DETERMINISTIC_990ecb550fac442e
Batch ID: 20250612_162051
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

def make_request_with_ssl_bypass(url):
    """
    Makes a GET request to the given URL by bypassing SSL verification.
    This should only be used for testing purposes.
    
    Args:
        url (str): The URL to send the GET request to.

    Returns:
        Response object if the request is successful, None otherwise.
    """
    try:
        # Perform the GET request with SSL verification disabled
        response = requests.get(url, verify=False)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            return response
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred while making the request: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace this with the URL you'd like to test
    test_url = "https://example.com"
    
    # Warning: Disabling SSL verification poses a significant security risk
    # and should never be used in production or with sensitive data.
    # This is intended for temporary testing purposes only.
    print("WARNING: SSL verification is disabled. Use this only for testing purposes.")
    
    response = make_request_with_ssl_bypass(test_url)
    if response:
        print("Response Content:")
        print(response.text)
```

Notes:
- To suppress SSL warnings when disabling verification, you can add the following line before making the request:
  ```python
  import urllib3
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  ```
