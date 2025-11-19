"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://f89badf5.7acd740c665c9b25ec20d877.workers.dev
Prompt: How can I implement a secure connection check in my web application using API calls?
Generated: DETERMINISTIC_ed789083871e8f8c
Batch ID: 20250612_163423
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
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

def check_secure_connection(api_url: str) -> bool:
    """
    Check if the given API URL supports a secure connection (HTTPS).
    
    Parameters:
    api_url (str): The API endpoint to check.
    
    Returns:
    bool: True if the connection is secure, False otherwise.
    
    Raises:
    ValueError: If the provided URL is not valid.
    RequestException: For errors during the request.
    """
    # Validate the URL format
    if not api_url.startswith("http://") and not api_url.startswith("https://"):
        raise ValueError("Invalid URL. It must start with 'http://' or 'https://'.")

    try:
        # Send a HEAD request to the API URL
        response = requests.head(api_url, allow_redirects=True)

        # Check if the response URL starts with 'https://'
        return response.url.startswith("https://")

    except RequestException as e:
        # Log the error for debugging purposes
        print(f"Error during connection check: {e}")
        raise

# Example usage
if __name__ == "__main__":
    api_endpoint = "https://api.example.com"

    try:
        is_secure = check_secure_connection(api_endpoint)
        if is_secure:
            print(f"The connection to {api_endpoint} is secure.")
        else:
            print(f"The connection to {api_endpoint} is not secure.")
    except (ValueError, RequestException) as e:
        print(f"Failed to check secure connection: {e}")
```
