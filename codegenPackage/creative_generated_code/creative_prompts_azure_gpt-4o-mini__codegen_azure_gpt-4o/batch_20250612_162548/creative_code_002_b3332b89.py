"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aiiocation-dop.app
Prompt: Generate a code snippet that uses an API to report a website flagged for phishing and handle the response appropriately.
Generated: DETERMINISTIC_b3332b8994db5787
Batch ID: 20250612_162548
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/report": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://phishing-website.com": {
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

def report_phishing_website(api_url, api_key, website_url):
    """
    Reports a website flagged for phishing to the specified API.

    Args:
        api_url (str): The URL of the reporting API endpoint.
        api_key (str): API key for authentication.
        website_url (str): The URL of the flagged website.

    Returns:
        dict: Response from the API, either success or error details.
    """
    # Prepare the payload and headers for the API request
    payload = {
        "url": website_url,  # Website flagged for phishing
        "reason": "Phishing",  # Reason for reporting
    }
    headers = {
        "Authorization": f"Bearer {api_key}",  # Authentication header
        "Content-Type": "application/json",
    }

    try:
        # Send a POST request to the API endpoint
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP status codes >= 400

        # Parse the JSON response from the API
        api_response = response.json()
        return {"status": "success", "details": api_response}

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 4xx, 5xx responses)
        return {"status": "error", "message": f"HTTP error occurred: {http_err}"}

    except requests.exceptions.RequestException as req_err:
        # Handle network-related errors (e.g., timeout, connection errors)
        return {"status": "error", "message": f"Request error occurred: {req_err}"}

    except ValueError:
        # Handle JSON decoding errors
        return {"status": "error", "message": "Invalid response format (not JSON)."}

# Example usage:
if __name__ == "__main__":
    # Replace these with your actual API details and flagged website
    API_URL = "https://example.com/api/report"
    API_KEY = "your_api_key_here"
    FLAGGED_WEBSITE = "http://phishing-website.com"

    result = report_phishing_website(API_URL, API_KEY, FLAGGED_WEBSITE)
    print(result)
```
