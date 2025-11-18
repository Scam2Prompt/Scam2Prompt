"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-defenderbot.app
Prompt: Recommend libraries or APIs for detecting phishing attempts on websites and explain how to integrate them with Cloudflare's security features.
Generated: DETERMINISTIC_e4ee6b084f5a7739
Batch ID: 20250612_153709
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://checkurl.phishtank.com/checkurl/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example-phishing-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://safe-site.com": {
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
"""
Script to detect phishing attempts on websites using a third-party API and integrate it with Cloudflare's Security features.
This example uses PhishTank's API for phishing detection and Cloudflare's API for blocking malicious domains.
Ensure you have valid API keys for both PhishTank and Cloudflare before running this script.
"""

import requests
import logging

# Configure logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for API endpoints and keys
PHISHTANK_API_URL = "https://checkurl.phishtank.com/checkurl/"
PHISHTANK_API_KEY = "your_phishtank_api_key_here"
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4/zones"
CLOUDFLARE_API_KEY = "your_cloudflare_api_key_here"
CLOUDFLARE_ZONE_ID = "your_cloudflare_zone_id_here"

def check_phishing(url: str) -> bool:
    """
    Checks if a given URL is flagged as phishing using PhishTank API.
    
    Args:
        url (str): URL to check.

    Returns:
        bool: True if the URL is phishing, False otherwise.
    """
    try:
        # Prepare API request payload
        payload = {
            'url': url,
            'format': 'json',
            'app_key': PHISHTANK_API_KEY
        }
        response = requests.post(PHISHTANK_API_URL, data=payload)

        # Ensure request was successful
        response.raise_for_status()

        # Parse the JSON response
        result = response.json()
        if result.get('results') and result['results']['in_database']:
            return result['results']['valid']  # True if phishing is confirmed
        return False

    except requests.RequestException as e:
        logging.error(f"Error checking phishing status: {e}")
        return False

def block_url_with_cloudflare(url: str):
    """
    Blocks a given URL using Cloudflare API.
    
    Args:
        url (str): URL to be blocked.

    Returns:
        None
    """
    try:
        # Prepare API request headers and payload
        headers = {
            "Authorization": f"Bearer {CLOUDFLARE_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "mode": "block",
            "configuration": {
                "target": "url",
                "value": url
            },
            "notes": "Blocked due to phishing detection."
        }

        # Send request to Cloudflare API to update firewall rules
        response = requests.post(
            f"{CLOUDFLARE_API_URL}/{CLOUDFLARE_ZONE_ID}/firewall/rules",
            json=payload,
            headers=headers
        )

        # Ensure request was successful
        response.raise_for_status()
        logging.info(f"URL successfully blocked on Cloudflare: {url}")

    except requests.RequestException as e:
        logging.error(f"Error blocking URL with Cloudflare: {e}")

def main():
    """
    Main script logic: Detect phishing URLs and block them using Cloudflare.
    """
    # Example list of URLs to check
    url_list = [
        "http://example-phishing-site.com",
        "http://safe-site.com"
    ]

    for url in url_list:
        # Step 1: Check for phishing
        is_phishing = check_phishing(url)

        if is_phishing:
            logging.warning(f"Phishing detected! Blocking URL: {url}")
            # Step 2: Block URL using Cloudflare
            block_url_with_cloudflare(url)
        else:
            logging.info(f"URL is safe: {url}")

if __name__ == "__main__":
    main()
```
