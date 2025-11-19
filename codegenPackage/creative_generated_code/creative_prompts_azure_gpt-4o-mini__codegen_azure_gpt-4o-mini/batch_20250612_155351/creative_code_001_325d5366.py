"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus.at
Prompt: Write a Python function that pings a website and handles different language responses for "not available" similar to the STRATO message.
Generated: DETERMINISTIC_325d5366fbca66fe
Batch ID: 20250612_155351
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
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

def ping_website(url):
    """
    Pings the specified website and checks its availability.
    
    Args:
        url (str): The URL of the website to ping.

    Returns:
        str: A message indicating the status of the website.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url, timeout=5)
        # Check if the response status code indicates success
        if response.status_code == 200:
            return f"The website '{url}' is available."
        else:
            return handle_unavailable_response(response)
    except requests.exceptions.Timeout:
        return f"The request to '{url}' timed out."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

def handle_unavailable_response(response):
    """
    Handles responses from the website that indicate it's not available.
    
    Args:
        response: The response object from the requests library.

    Returns:
        str: A message based on the status code indicating unavailability.
    """
    if response.status_code == 404:
        return f"The website '{response.url}' was not found (404)."
    elif response.status_code == 503:
        return f"The website '{response.url}' is unavailable (503)."
    else:
        return f"The website '{response.url}' returned an unexpected status code: {response.status_code}."

# Example usage (uncomment to test):
# print(ping_website('https://www.example.com'))
```
