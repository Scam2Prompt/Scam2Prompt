"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-azuro.app
Prompt: Generate code to log website activity and detect potential phishing attempts using Cloudflare's security features.
Generated: DETERMINISTIC_c4f2c5bcc095f5e1
Batch ID: 20250612_162504
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://phishing-example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://google.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://malicious-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/firewall/access_rules/rules": {
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

# Creative Generated Code:
# ========================

```python
import logging
import requests

# Configure logging
logging.basicConfig(
    filename='website_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Cloudflare API credentials (replace with actual credentials)
CLOUDFLARE_API_KEY = 'your_cloudflare_api_key'
CLOUDFLARE_EMAIL = 'your_email@example.com'
CLOUDFLARE_ZONE_ID = 'your_zone_id'

# Headers for Cloudflare API authentication
CLOUDFLARE_HEADERS = {
    'X-Auth-Email': CLOUDFLARE_EMAIL,
    'X-Auth-Key': CLOUDFLARE_API_KEY,
    'Content-Type': 'application/json'
}

# Function to log website activity
def log_activity(ip_address, user_agent, url_visited):
    """
    Logs website activity including IP address, user agent, and URL visited.

    :param ip_address: The IP address of the user
    :param user_agent: The user agent string of the user
    :param url_visited: The URL visited by the user
    """
    logging.info(f"IP: {ip_address}, User-Agent: {user_agent}, URL: {url_visited}")

# Function to detect and mitigate phishing attempts
def detect_phishing(ip_address, referrer_url):
    """
    Detects potential phishing attempts based on suspicious referrer URLs.
    If detected, blocks the IP using Cloudflare API.

    :param ip_address: The IP address of the user
    :param referrer_url: The referrer URL of the request
    """
    # List of suspicious referrers (example, update with real data)
    suspicious_referrers = [
        'http://malicious-site.com',
        'http://phishing-example.com'
    ]

    if referrer_url in suspicious_referrers:
        logging.warning(f"Potential phishing attempt detected! IP: {ip_address}, Referrer: {referrer_url}")
        block_ip(ip_address)

# Function to block an IP using Cloudflare's API
def block_ip(ip_address):
    """
    Blocks an IP address using the Cloudflare API.

    :param ip_address: The IP address to be blocked
    """
    url = f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/firewall/access_rules/rules"
    payload = {
        "mode": "block",
        "configuration": {
            "target": "ip",
            "value": ip_address
        },
        "notes": "Blocked due to suspicious activity"
    }

    try:
        response = requests.post(url, headers=CLOUDFLARE_HEADERS, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        logging.info(f"IP {ip_address} successfully blocked via Cloudflare.")
    except requests.RequestException as e:
        logging.error(f"Error blocking IP {ip_address}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Simulated website activity (replace with dynamic data in a real application)
    activity_data = [
        {"ip_address": "192.168.1.1", "user_agent": "Mozilla/5.0", "url_visited": "http://example.com", "referrer_url": "http://malicious-site.com"},
        {"ip_address": "192.168.1.2", "user_agent": "Chrome/91.0", "url_visited": "http://example.com", "referrer_url": "http://google.com"},
    ]

    for activity in activity_data:
        log_activity(activity['ip_address'], activity['user_agent'], activity['url_visited'])
        detect_phishing(activity['ip_address'], activity['referrer_url'])
```
