"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: How can I implement DDoS protection in my web application using Cloudflare's API?
Generated: DETERMINISTIC_70518d9c0c0c58ae
Batch ID: 20250612_163231
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
import os

# Cloudflare API Base URL
CLOUDFLARE_API_BASE = "https://api.cloudflare.com/client/v4"

# Cloudflare API credentials (Environment variables for security)
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_KEY")  # Your API Key
CLOUDFLARE_EMAIL = os.getenv("CLOUDFLARE_EMAIL")  # Your Cloudflare account email
ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")  # Your Zone ID for the domain

if not CLOUDFLARE_API_KEY or not CLOUDFLARE_EMAIL or not ZONE_ID:
    raise ValueError(
        "Environment variables CLOUDFLARE_API_KEY, CLOUDFLARE_EMAIL, and ZONE_ID are required."
    )

# Headers for the Cloudflare API
HEADERS = {
    "X-Auth-Email": CLOUDFLARE_EMAIL,
    "X-Auth-Key": CLOUDFLARE_API_KEY,
    "Content-Type": "application/json",
}


def enable_ddos_protection(zone_id):
    """
    Enables DDoS protection by configuring the security level to 'under_attack'.
    This level activates the "I'm Under Attack Mode" on Cloudflare.

    :param zone_id: The Zone ID of the domain where protection should be enabled.
    :return: Response from the Cloudflare API.
    """
    url = f"{CLOUDFLARE_API_BASE}/zones/{zone_id}/settings/security_level"
    data = {"value": "under_attack"}  # Set to "under_attack" for DDoS protection.

    try:
        # Make the API request
        response = requests.patch(url, headers=HEADERS, json=data)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        result = response.json()

        if result["success"]:
            print("DDoS protection successfully enabled.")
            return result
        else:
            print("Failed to enable DDoS protection:", result["errors"])
            return None

    except requests.exceptions.RequestException as e:
        print("Error while enabling DDoS protection:", str(e))
        return None


if __name__ == "__main__":
    # Enable DDoS protection for the configured zone
    response = enable_ddos_protection(ZONE_ID)

    # Print the API response (for debugging or logging purposes)
    print("API Response:", response)
```
