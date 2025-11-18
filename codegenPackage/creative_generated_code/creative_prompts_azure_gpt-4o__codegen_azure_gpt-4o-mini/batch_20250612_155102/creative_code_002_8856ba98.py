"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergas.biz
Prompt: Provide code to automate the detection of HTTPS configuration issues for a website hosted on FASTPANEL, including missing SSL certificates.
Generated: DETERMINISTIC_8856ba9887cf9fdc
Batch ID: 20250612_155102
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

def check_https_configuration(url):
    """
    Check the HTTPS configuration of a given URL by attempting to access it over HTTPS.
    
    Args:
        url (str): The URL to check. Must start with 'https://'.

    Returns:
        dict: A dictionary containing the results of the check, including status and any errors.
    """
    results = {
        'url': url,
        'is_https': False,
        'ssl_certificate': None,
        'error': None,
    }

    try:
        # Ensure the URL starts with 'https://'
        if not url.startswith('https://'):
            raise ValueError("URL must start with 'https://'")

        # Send a GET request to the HTTPS URL
        response = requests.get(url, verify=True)

        # If the request was successful, we confirm HTTPS is configured correctly
        results['is_https'] = True
        results['ssl_certificate'] = response.cert  # Get the SSL certificate details

    except SSLError as ssl_error:
        # Handle SSL errors specifically
        results['error'] = f"SSL Error: {ssl_error}"
    except RequestException as req_error:
        # Handle general request exceptions (e.g., connection errors, timeouts)
        results['error'] = f"Request Error: {req_error}"
    except ValueError as val_error:
        # Handle value errors (e.g., invalid URL format)
        results['error'] = f"Value Error: {val_error}"
    except Exception as e:
        # Catch-all for any other unexpected exceptions
        results['error'] = f"Unexpected Error: {e}"

    return results

# Example usage
if __name__ == "__main__":
    test_url = "https://example.com"
    check_results = check_https_configuration(test_url)

    if check_results['is_https']:
        print(f"HTTPS is configured correctly for {check_results['url']}.")
        print(f"SSL Certificate: {check_results['ssl_certificate']}")
    else:
        print(f"HTTPS configuration issue detected for {check_results['url']}: {check_results['error']}")
```

Make sure to replace `"https://example.com"` with the specific website you want to check when running the script.
