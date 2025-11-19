"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-modenetwork.app
Prompt: Write a Python script that checks if a URL is flagged as a phishing site using Cloudflare's API.
Generated: DETERMINISTIC_27c6c8be4c45d381
Batch ID: 20250612_162504
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
  "https://api.cloudflare.com/client/v4/url/firewall/rules": {
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

# Constants for Cloudflare API
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4/url/firewall/rules"
API_TOKEN = "YOUR_CLOUDFLARE_API_TOKEN"  # Replace with your Cloudflare API token

def is_phishing_url(url):
    """
    Checks if the provided URL is flagged as a phishing site using Cloudflare's API.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is flagged as phishing, False otherwise.
    """
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        # Sending GET request to Cloudflare API
        response = requests.get(CLOUDFLARE_API_URL, headers=headers)
        
        # Check for successful request
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Iterate over the rules to check if the URL is flagged
        for rule in data.get('result', []):
            if 'match' in rule and url in rule['match']:
                return True  # URL is flagged as phishing

        return False  # URL is not flagged as phishing

    except requests.exceptions.RequestException as e:
        # Log the error and return False for safety
        print(f"Error checking URL: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    test_url = "http://example.com"  # Replace with the actual URL you want to check
    if is_phishing_url(test_url):
        print(f"The URL {test_url} is flagged as a phishing site.")
    else:
        print(f"The URL {test_url} is safe.")
```

**Note:** Remember to replace `YOUR_CLOUDFLARE_API_TOKEN` with your actual Cloudflare API token before running the code.
