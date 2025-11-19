"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-oasis.app
Prompt: What libraries can help detect and prevent phishing attempts in web applications, and how do they integrate with Cloudflare?
Generated: DETERMINISTIC_3565c2a827327fa2
Batch ID: 20250612_162601
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://checkurl.phishtank.com/checkurl/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cloudflare.com/client/v4/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the Python code that uses a library to detect phishing attempts, integrates with Cloudflare, and includes error handling. It uses `PhishTank` for phishing detection and Cloudflare's API for integration:

```python
import requests
import json
from cloudflare_api import CloudflareAPI  # Placeholder for Cloudflare API wrapper (you'll need to install or build one)

# Constants
PHISHTANK_API_URL = "https://checkurl.phishtank.com/checkurl/"
PHISHTANK_API_KEY = "your_phishtank_api_key_here"
CLOUDFLARE_API_TOKEN = "your_cloudflare_api_token_here"
CLOUDFLARE_ZONE_ID = "your_cloudflare_zone_id_here"

def check_url_phishing(url):
    """
    Function to check if a URL is a phishing attempt using PhishTank API.
    Args:
        url (str): The URL to check.
    Returns:
        dict: The result from PhishTank indicating whether the URL is a phishing attempt.
    """
    try:
        payload = {
            "url": url,
            "format": "json",
            "app_key": PHISHTANK_API_KEY
        }
        response = requests.post(PHISHTANK_API_URL, data=payload)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error connecting to PhishTank API: {e}")
        return {"error": str(e)}

def block_phishing_url_on_cloudflare(url):
    """
    Function to block a phishing URL using Cloudflare's Firewall API.
    Args:
        url (str): The URL to block.
    Returns:
        dict: The result from Cloudflare API.
    """
    try:
        cf_api = CloudflareAPI(auth_token=CLOUDFLARE_API_TOKEN)  # Initialize Cloudflare API wrapper
        firewall_rule = {
            "action": "block",
            "filter": {
                "expression": f"http.request.full_uri eq \"{url}\"",
                "paused": False,
                "description": "Phishing URL detected and blocked"
            }
        }
        response = cf_api.create_firewall_rule(zone_id=CLOUDFLARE_ZONE_ID, rule_data=firewall_rule)
        return response
    except Exception as e:
        # Handle Cloudflare API errors
        print(f"Error blocking URL on Cloudflare: {e}")
        return {"error": str(e)}

def main():
    """
    Main function to detect and prevent phishing attempts.
    """
    url_to_check = input("Enter the URL to check for phishing: ").strip()
    
    print("Checking URL with PhishTank API...")
    phishing_check_result = check_url_phishing(url_to_check)
    
    if "results" in phishing_check_result and phishing_check_result["results"]["valid"] and phishing_check_result["results"]["in_database"]:
        if phishing_check_result["results"]["phish_detail_page"]:
            print(f"Phishing URL detected: {url_to_check}")
            print("Blocking phishing URL on Cloudflare...")
            cloudflare_response = block_phishing_url_on_cloudflare(url_to_check)
            print("Cloudflare response:", cloudflare_response)
        else:
            print(f"The URL {url_to_check} is not flagged as phishing.")
    else:
        print("Unable to verify the URL or an error occurred:", phishing_check_result)

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace placeholders (`your_phishtank_api_key_here`, `your_cloudflare_api_token_here`, `your_cloudflare_zone_id_here`) with actual values.
2. `cloudflare_api` is assumed to be a wrapper for Cloudflare's API, which you can create or install via existing packages. If unavailable, you can directly use the `requests` library to interact with Cloudflare's API (`https://api.cloudflare.com/client/v4/`).
3. Error handling is added for both API calls to ensure robustness.
