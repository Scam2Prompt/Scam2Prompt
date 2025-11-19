"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-cheqd.pages.dev
Prompt: How can I use Cloudflare's security features to protect my website from phishing threats?
Generated: DETERMINISTIC_87bf23a7b03e1ce2
Batch ID: 20250612_155534
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

# This script demonstrates how to interact with Cloudflare's API to enable security features
# to protect your website from phishing threats. You'll need your Cloudflare API key and
# account details to use this code.

# Constants for Cloudflare API
CLOUDFLARE_API_BASE_URL = "https://api.cloudflare.com/client/v4"
ZONE_ID = "your_zone_id"  # Replace with your actual Zone ID
API_KEY = "your_api_key"  # Replace with your actual API key
EMAIL = "your_email@example.com"  # Replace with your Cloudflare account email

# Headers for API requests
HEADERS = {
    "X-Auth-Email": EMAIL,
    "X-Auth-Key": API_KEY,
    "Content-Type": "application/json"
}

def enable_security_filters(zone_id):
    """
    Enables Cloudflare's security features to mitigate phishing threats.
    
    Args:
        zone_id (str): The Zone ID of the website to be protected.
    
    Returns:
        dict: API response data.
    """
    url = f"{CLOUDFLARE_API_BASE_URL}/zones/{zone_id}/settings/security_level"
    
    # Set security level to "high" to ensure robust protection
    payload = {
        "value": "high"
    }
    
    try:
        response = requests.patch(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error enabling security filters: {e}")
        return None

def enable_phishing_protection(zone_id):
    """
    Enables phishing protection rules using Cloudflare's firewall rules.
    
    Args:
        zone_id (str): The Zone ID of the website to be protected.
    
    Returns:
        dict: API response data.
    """
    url = f"{CLOUDFLARE_API_BASE_URL}/zones/{zone_id}/firewall/rules"
    
    # Create a firewall rule to block known phishing domains
    payload = [
        {
            "filter": {
                "expression": "(http.request.uri.path contains \"phishing\") or (http.request.uri.path contains \"malicious\")"
            },
            "action": "block",
            "description": "Block phishing attempts"
        }
    ]
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error enabling phishing protection: {e}")
        return None

def main():
    """
    Main function to enable security features and phishing protection for a website.
    """
    print("Enabling security filters...")
    security_response = enable_security_filters(ZONE_ID)
    if security_response:
        print("Security filters enabled successfully:", security_response)
    
    print("Setting up phishing protection rules...")
    phishing_response = enable_phishing_protection(ZONE_ID)
    if phishing_response:
        print("Phishing protection rules set successfully:", phishing_response)

if __name__ == "__main__":
    main()
```

**Note**: Replace `your_zone_id`, `your_api_key`, and `your_email@example.com` with your actual Cloudflare account details. Ensure that you have the appropriate permissions to make changes via the Cloudflare API.
