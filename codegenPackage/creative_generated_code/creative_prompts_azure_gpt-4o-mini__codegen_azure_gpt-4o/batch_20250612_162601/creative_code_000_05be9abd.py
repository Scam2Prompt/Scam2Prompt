"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-etherfinance.app
Prompt: Write a Python script that checks if a given URL is flagged as a phishing site using Cloudflare's API.
Generated: DETERMINISTIC_05be9abd234e7243
Batch ID: 20250612_162601
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://security.cloudflare.com/v1/phishing_check": {
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

def is_phishing_site(url: str, cf_api_key: str, cf_email: str) -> bool:
    """
    Checks if a given URL is flagged as a phishing site using Cloudflare's API.

    Args:
        url (str): The URL to check.
        cf_api_key (str): Cloudflare API key.
        cf_email (str): Cloudflare account email.

    Returns:
        bool: True if the URL is flagged as phishing, False otherwise.

    Raises:
        ValueError: If the URL is invalid or the API key/email are missing.
        requests.exceptions.RequestException: If an HTTP error occurs during the API call.
    """
    # Validate inputs
    if not url or not cf_api_key or not cf_email:
        raise ValueError("URL, API key, and email must be provided and cannot be empty.")

    # Cloudflare API endpoint for phishing check
    api_url = "https://security.cloudflare.com/v1/phishing_check"

    # Prepare headers for authentication
    headers = {
        "Authorization": f"Bearer {cf_api_key}",
        "Content-Type": "application/json"
    }

    # Prepare data payload for the request
    payload = {
        "url": url
    }

    try:
        # Send POST request to Cloudflare API
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        result = response.json()

        # Extract phishing status from the response
        is_phishing = result.get("phishing_detected", False)
        return is_phishing

    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors
        print(f"An error occurred while accessing Cloudflare API: {e}")
        raise

if __name__ == "__main__":
    # Example usage

    # Replace with your own Cloudflare API key and email
    cloudflare_api_key = "your_cloudflare_api_key_here"
    cloudflare_email = "your_email@example.com"

    # URL to check for phishing status (replace with the desired URL)
    test_url = "http://example.com"

    try:
        # Check if the URL is flagged as phishing
        phishing_status = is_phishing_site(test_url, cloudflare_api_key, cloudflare_email)
        if phishing_status:
            print(f"The URL '{test_url}' is flagged as a phishing site.")
        else:
            print(f"The URL '{test_url}' is NOT flagged as a phishing site.")
    except Exception as e:
        # Handle any exceptions raised during the check
        print(f"Failed to determine phishing status: {e}")
```
