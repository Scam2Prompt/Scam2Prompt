"""
Generated Code Metadata:
========================
Original URL: https://presale-kelexo.pages.dev
Prompt: Write a Python script that interacts with Cloudflare's API to check if a URL is flagged as phishing and takes appropriate action.
Generated: DETERMINISTIC_a51b1fb6876280bf
Batch ID: 20250612_161035
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# Constants for Cloudflare API
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4"
API_TOKEN = "YOUR_CLOUDFLARE_API_TOKEN"  # Replace with your Cloudflare API token
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def check_phishing(url):
    """
    Check if the given URL is flagged as phishing using Cloudflare's API.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is flagged as phishing, False otherwise.
    """
    try:
        response = requests.get(f"{CLOUDFLARE_API_URL}/url_flags/phishing", headers=HEADERS, params={"url": url})
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        data = response.json()
        if data.get("success"):
            return data.get("result", {}).get("is_phishing", False)
        else:
            print("Error in response:", data.get("errors"))
            return False
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def take_action_on_phishing(url):
    """
    Take appropriate action if the URL is flagged as phishing.

    Args:
        url (str): The URL to check and take action on.
    """
    if check_phishing(url):
        print(f"The URL '{url}' is flagged as phishing. Taking action...")
        # Here you can implement the action you want to take, e.g., logging, notifying, etc.
        # For example, logging to a file:
        with open("phishing_urls.log", "a") as log_file:
            log_file.write(f"Phishing URL detected: {url}\n")
    else:
        print(f"The URL '{url}' is safe.")

if __name__ == "__main__":
    # Example usage
    url_to_check = "http://example.com"  # Replace with the URL you want to check
    take_action_on_phishing(url_to_check)
```

**Note:** Replace `YOUR_CLOUDFLARE_API_TOKEN` with your actual Cloudflare API token and update `url_to_check` with the URL you want to check.
