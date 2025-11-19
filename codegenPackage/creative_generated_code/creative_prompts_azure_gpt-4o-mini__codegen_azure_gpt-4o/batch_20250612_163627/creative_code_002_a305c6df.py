"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notgiveaway.com
Prompt: What are the best practices for configuring Cloudflare to prevent DDoS attacks on my site?
Generated: DETERMINISTIC_a305c6df2caae8e0
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the use of Cloudflare's API to configure basic settings to help mitigate DDoS attacks.
It utilizes the Cloudflare Python API library ('cloudflare') for interacting with Cloudflare's API.
Before running this script, you must have a Cloudflare account and an API key.
"""

import os
import CloudFlare  # Install via `pip install cloudflare`

def configure_ddos_protection(zone_name, api_key, email):
    """
    Configures Cloudflare settings to help prevent DDoS attacks on the specified zone.
    
    :param zone_name: The domain name (zone) to configure protection for.
    :param api_key: The Cloudflare API key.
    :param email: The Cloudflare account email.
    """
    try:
        # Initialize the Cloudflare API client with the provided credentials
        cf = CloudFlare.CloudFlare(email=email, token=api_key)

        # Get the zone ID for the given domain name
        zones = cf.zones.get(params={"name": zone_name})
        if not zones:
            raise ValueError(f"Zone '{zone_name}' not found.")
        zone_id = zones[0]["id"]

        # Enable "I'm under attack" mode
        security_settings = {"security_level": "under_attack"}
        cf.zones.settings.patch(zone_id, data=security_settings)
        print(f"'I'm under attack' mode enabled for zone '{zone_name}'.")

        # Set rate limiting rules (example: block IPs making >100 requests in 10 seconds)
        rate_limit_rule = {
            "match": {
                "request": {
                    "url": "*",  # Apply to all URLs
                }
            },
            "threshold": 100,  # Max requests allowed
            "period": 10,  # Time window in seconds
            "action": "challenge",  # CAPTCHA challenge
            "enabled": True,
            "description": "Rate limiting rule to prevent DDoS attacks",
        }
        cf.zones.rate_limits.post(zone_id, data=rate_limit_rule)
        print(f"Rate limiting rule applied for zone '{zone_name}'.")

        # Enable Web Application Firewall (WAF)
        waf_settings = {"waf_mode": "on"}
        cf.zones.settings.patch(zone_id, data=waf_settings)
        print(f"Web Application Firewall enabled for zone '{zone_name}'.")

        # Success message
        print("DDoS protection configuration complete.")

    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"Cloudflare API Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace the following placeholders with your actual credentials and zone name
    CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_KEY")  # Set this as an environment variable
    CLOUDFLARE_EMAIL = os.getenv("CLOUDFLARE_EMAIL")      # Set this as an environment variable
    ZONE_NAME = "example.com"  # Replace with your domain name

    if not CLOUDFLARE_API_KEY or not CLOUDFLARE_EMAIL:
        print("Please set CLOUDFLARE_API_KEY and CLOUDFLARE_EMAIL environment variables.")
    else:
        configure_ddos_protection(ZONE_NAME, CLOUDFLARE_API_KEY, CLOUDFLARE_EMAIL)
```

**Note:** This script assumes you have installed the `cloudflare` Python library via `pip install cloudflare`. Replace `example.com` with your domain and ensure that your Cloudflare account email and API key are correctly set in environment variables. Always follow Cloudflare's API documentation for updates and additional configuration options.
