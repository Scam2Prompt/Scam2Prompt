"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-daomaker.app
Prompt: Provide a code example for integrating Cloudflare's API to monitor and manage website security against phishing threats.
Generated: DETERMINISTIC_d3662808c4b452ce
Batch ID: 20250612_162538
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
import requests
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cloudflare API Configuration
API_BASE_URL = "https://api.cloudflare.com/client/v4"
API_EMAIL = "your_email@example.com"  # Replace with your Cloudflare account email
API_KEY = "your_api_key"  # Replace with your Cloudflare API key
ZONE_ID = "your_zone_id"  # Replace with your Cloudflare Zone ID

# Headers for authentication
HEADERS = {
    "X-Auth-Email": API_EMAIL,
    "X-Auth-Key": API_KEY,
    "Content-Type": "application/json"
}

def list_security_events(zone_id: str) -> Dict[str, Any]:
    """
    Fetch the security events for the given zone.

    :param zone_id: The Cloudflare Zone ID.
    :return: JSON response containing the security events.
    """
    url = f"{API_BASE_URL}/zones/{zone_id}/security/events"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching security events: {e}")
        return {"error": str(e)}

def block_phishing_ip(zone_id: str, ip_address: str) -> Dict[str, Any]:
    """
    Block an IP address identified as a phishing threat.

    :param zone_id: The Cloudflare Zone ID.
    :param ip_address: The IP address to block.
    :return: JSON response from the Cloudflare API.
    """
    url = f"{API_BASE_URL}/zones/{zone_id}/firewall/access_rules/rules"
    payload = {
        "mode": "block",
        "configuration": {
            "target": "ip",
            "value": ip_address
        },
        "notes": "Blocked due to phishing activity"
    }
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error blocking IP address {ip_address}: {e}")
        return {"error": str(e)}

def main():
    """
    Main function to monitor and manage security against phishing threats.
    Fetches security events and blocks identified phishing IPs.
    """
    logging.info("Fetching security events...")
    events = list_security_events(ZONE_ID)

    if "error" in events:
        logging.error("Failed to fetch security events.")
        return

    # Example of processing the events (simplification for demonstration)
    for event in events.get("result", []):
        # Check if the event is related to phishing (example condition)
        if event.get("action") == "block" and event.get("rule_name") == "phishing-detection":
            ip_to_block = event.get("source", {}).get("ip")
            if ip_to_block:
                logging.info(f"Blocking IP: {ip_to_block} due to phishing activity...")
                block_response = block_phishing_ip(ZONE_ID, ip_to_block)
                if "error" in block_response:
                    logging.error(f"Failed to block IP: {ip_to_block}")
                else:
                    logging.info(f"Successfully blocked IP: {ip_to_block}")

if __name__ == "__main__":
    main()
```
