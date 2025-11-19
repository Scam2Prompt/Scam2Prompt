"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-pryzm.app
Prompt: How can I use Cloudflare's API to monitor and respond to phishing threats on my site?
Generated: DETERMINISTIC_299851f5fe61c962
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
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
Script to monitor and respond to phishing threats on a website using Cloudflare's API.
This script fetches security events related to phishing and blocks the offending IPs.
Requires: Python 3.7+, `requests` library installed.
"""

import requests
import logging

# Define API credentials and base URL
CLOUDFLARE_API_BASE_URL = "https://api.cloudflare.com/client/v4"
API_TOKEN = "your-api-token"  # Replace with your Cloudflare API token
ZONE_ID = "your-zone-id"      # Replace with your Cloudflare Zone ID

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Fetch security events from Cloudflare
def fetch_security_events():
    """
    Fetch recent security events, including phishing threats, from Cloudflare.
    
    Returns:
        list: A list of security events containing phishing threats.
    """
    url = f"{CLOUDFLARE_API_BASE_URL}/zones/{ZONE_ID}/security_events"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        
        # Filter phishing-related events
        phishing_events = [
            event for event in data.get("result", [])
            if event.get("action") == "phishing"
        ]
        return phishing_events
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching security events: {e}")
        return []

# Block IPs involved in phishing
def block_ips(ips):
    """
    Block a list of IPs using Cloudflare's Firewall API.
    
    Args:
        ips (list): List of IP addresses to block.
    """
    url = f"{CLOUDFLARE_API_BASE_URL}/zones/{ZONE_ID}/firewall/access_rules/rules"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    for ip in ips:
        payload = {
            "mode": "block",
            "configuration": {
                "target": "ip",
                "value": ip
            },
            "notes": "Blocked due to phishing activity"
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            logging.info(f"Successfully blocked IP: {ip}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error blocking IP {ip}: {e}")

# Monitor and respond to phishing threats
def monitor_and_respond():
    """
    Main function to monitor phishing threats and respond by blocking offending IPs.
    """
    logging.info("Fetching security events...")
    phishing_events = fetch_security_events()

    if phishing_events:
        # Extract IPs from phishing events
        ips_to_block = {event.get("source", {}).get("ip") for event in phishing_events}
        logging.info(f"Found {len(ips_to_block)} IPs to block.")
        
        if ips_to_block:
            logging.info("Blocking IPs...")
            block_ips(list(ips_to_block))
        else:
            logging.info("No IPs found to block.")
    else:
        logging.info("No phishing threats detected.")

# Entry point of the script
if __name__ == "__main__":
    monitor_and_respond()
```

Make sure to replace `your-api-token` and `your-zone-id` with appropriate values from your Cloudflare account.
