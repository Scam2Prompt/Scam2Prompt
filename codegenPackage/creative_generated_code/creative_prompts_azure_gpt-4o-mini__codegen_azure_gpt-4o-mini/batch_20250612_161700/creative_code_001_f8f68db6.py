"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zestcommute.com
Prompt: What steps should I take to resolve the cURL error indicating 'no alternative certificate subject name matches target host'?
Generated: DETERMINISTIC_f8f68db6bade100a
Batch ID: 20250612_161700
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
from requests.exceptions import SSLError

def fetch_data(url):
    """
    Fetches data from the specified URL using HTTPS.
    
    Parameters:
    url (str): The URL to fetch data from.

    Returns:
    response (requests.Response): The HTTP response object if the request is successful.

    Raises:
    ValueError: If the URL is not valid.
    SSLError: If there is a cURL SSL error.
    """
    # Validate the URL
    if not isinstance(url, str) or not url.startswith("https://"):
        raise ValueError("URL must be a valid HTTPS URL.")

    try:
        # Make a GET request to the specified URL
        response = requests.get(url, verify=True)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response
    except SSLError as ssl_error:
        # Handle SSL errors, such as certificate mismatches
        print("SSL Error: Unable to verify the certificate. Ensure the hostname matches the certificate.")
        print("Error details:", ssl_error)
        raise
    except requests.RequestException as req_error:
        # Handle other request exceptions
        print("Request failed:", req_error)
        raise

# Example usage
if __name__ == "__main__":
    try:
        url = "https://example.com"  # Replace with your target URL
        response = fetch_data(url)
        print("Data fetched successfully:", response.text)
    except Exception as e:
        print("An error occurred:", e)
```
