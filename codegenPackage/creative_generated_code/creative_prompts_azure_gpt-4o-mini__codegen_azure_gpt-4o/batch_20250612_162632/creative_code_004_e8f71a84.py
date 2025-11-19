"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-zignaly.app
Prompt: Write a Python script that integrates with Cloudflare to monitor and respond to phishing site alerts.
Generated: DETERMINISTIC_e8f71a845202a8eb
Batch ID: 20250612_162632
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
import os
import json

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("cloudflare_phishing_monitor.log"),
        logging.StreamHandler()
    ]
)

# Constants for the Cloudflare API
CLOUDFLARE_API_BASE = "https://api.cloudflare.com/client/v4"
# These values should ideally be stored in environment variables or a secure secrets manager
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")

# Verify that API token and account ID are set
if not CLOUDFLARE_API_TOKEN or not CLOUDFLARE_ACCOUNT_ID:
    logging.error("Cloudflare API token or account ID not configured.")
    raise ValueError("Cloudflare API token and account ID must be set.")

# Headers for authenticated API requests
HEADERS = {
    "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
    "Content-Type": "application/json"
}

def get_phishing_alerts():
    """
    Fetch phishing alerts from Cloudflare.
    
    Returns:
        list: List of phishing alerts.
    """
    url = f"{CLOUDFLARE_API_BASE}/accounts/{CLOUDFLARE_ACCOUNT_ID}/security/events"
    params = {"filter[event_type]": "phishing"}
    
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return data.get("result", [])
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch phishing alerts: {e}")
        return []

def handle_phishing_site(alert):
    """
    Respond to a phishing site alert by blocking the reported domain.

    Args:
        alert (dict): Dictionary containing alert details.
    """
    domain = alert.get("source_domain")
    if not domain:
        logging.warning("No domain found in phishing alert.")
        return
    
    url = f"{CLOUDFLARE_API_BASE}/accounts/{CLOUDFLARE_ACCOUNT_ID}/firewall/access_rules/rules"
    payload = {
        "mode": "block",
        "configuration": {"target": "domain", "value": domain},
        "notes": "Automatically blocked due to phishing alert."
    }

    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        logging.info(f"Successfully blocked domain {domain}.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to block domain {domain}: {e}")

def main():
    """
    Main function to monitor and respond to phishing alerts.
    """
    logging.info("Starting phishing site monitor...")
    
    alerts = get_phishing_alerts()
    if not alerts:
        logging.info("No new phishing alerts found.")
        return
    
    for alert in alerts:
        logging.info(f"Processing phishing alert: {alert}")
        handle_phishing_site(alert)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Unhandled exception occurred: {e}")
```

### Notes:
- This script uses environment variables (`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`) to securely manage sensitive information. Use a `.env` file or a secrets manager to set them up.
- Logs are written to both the console and a log file (`cloudflare_phishing_monitor.log`).
- Error handling ensures graceful failure in case of API errors or missing data.
