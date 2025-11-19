"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-kelexo.pages.dev
Prompt: What are the best practices for securing a website against phishing attacks, and how can Cloudflare help in this process?
Generated: DETERMINISTIC_7580fdd59cbe5b36
Batch ID: 20250612_161035
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
# Title: Website Security Against Phishing Attacks Using Cloudflare
# Language: Python
# Description: This script demonstrates best practices for securing a website against phishing attacks.
# It includes implementation of HTTP headers, usage of Cloudflare's API features, and proper logging.

import requests
import logging
import sys

# Set up logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Constants for Cloudflare API
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4"
CLOUDFLARE_API_KEY = "your-cloudflare-api-key"  # Replace with your actual API key
CLOUDFLARE_EMAIL = "your-email@example.com"  # Replace with your registered Cloudflare account email
ZONE_ID = "your-zone-id"  # Replace with your Cloudflare Zone ID

# Function to add security headers via Cloudflare Page Rules
def add_security_headers():
    """
    Configure security headers to protect against phishing attacks.
    Use Cloudflare API to set up Page Rules.
    """
    headers = {
        "X-Auth-Email": CLOUDFLARE_EMAIL,
        "X-Auth-Key": CLOUDFLARE_API_KEY,
        "Content-Type": "application/json"
    }
    
    # Define security headers to add
    page_rule_payload = {
        "targets": [
            {"target": "url", "constraint": {"operator": "matches", "value": "*example.com/*"}}
        ],
        "actions": [
            {"id": "forwarding_url", "value": {"status_code": 301, "url": "https://example.com"}},
            {"id": "security_headers", "value": {
                "strict_transport_security": {"enabled": True, "max_age": 31536000, "include_subdomains": True},
                "xss_protection": {"enabled": True, "mode_block": True},
                "content_security_policy": {"enabled": True, "script_src": "'self'", "object_src": "'none'"},
                "x_frame_options": {"enabled": True, "value": "DENY"},
                "referrer_policy": {"enabled": True, "value": "no-referrer"}
            }}
        ]
    }
    
    try:
        response = requests.post(
            f"{CLOUDFLARE_API_URL}/zones/{ZONE_ID}/rules",
            headers=headers,
            json=page_rule_payload
        )
        
        if response.status_code == 200:
            logging.info("Successfully added security headers via Cloudflare Page Rules.")
        else:
            logging.error(f"Failed to add security headers. Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred while communicating with Cloudflare API: {e}")

# Function to enable Cloudflare features for phishing protection
def enable_cloudflare_features():
    """
    Enable Cloudflare features to secure the website against phishing attacks.
    """
    headers = {
        "X-Auth-Email": CLOUDFLARE_EMAIL,
        "X-Auth-Key": CLOUDFLARE_API_KEY,
        "Content-Type": "application/json"
    }
    
    features_payload = {
        "value": {
            "security_level": "high",  # Set high security level
            "ssl": "full",  # Enforce SSL/TLS
            "always_use_https": True  # Redirect all HTTP traffic to HTTPS
        }
    }
    
    try:
        response = requests.patch(
            f"{CLOUDFLARE_API_URL}/zones/{ZONE_ID}/settings",
            headers=headers,
            json=features_payload
        )
        
        if response.status_code == 200:
            logging.info("Successfully enabled Cloudflare security features.")
        else:
            logging.error(f"Failed to enable Cloudflare features. Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred while communicating with Cloudflare API: {e}")

if __name__ == "__main__":
    logging.info("Starting website security configuration...")
    
    # Add security headers via Cloudflare Page Rules
    add_security_headers()
    
    # Enable phishing protection features in Cloudflare
    enable_cloudflare_features()
    
    logging.info("Website security configuration completed.")
```
