"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mrspongy.com
Prompt: Explain how to leverage Cloudflare's services to improve website performance and security for an online business.
Generated: DETERMINISTIC_4b4722cd824e269f
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to leverage Cloudflare's API for managing website performance and security.
This script uses Cloudflare's Python API wrapper (`cloudflare-python`) to:
1. Enable appropriate security settings.
2. Configure caching rules for better performance.
3. Set up rate limiting to prevent abuse.

Prerequisites:
- Install the `cloudflare-python` package via pip: `pip install cloudflare-python`
- Obtain your Cloudflare API credentials (API token or key).
"""

import CloudFlare
import sys

def main():
    """Main function to configure Cloudflare settings for a domain."""
    try:
        # Initialize the Cloudflare API client
        api_token = "your_api_token_here"  # Replace with your Cloudflare API token
        cf = CloudFlare.CloudFlare(token=api_token)

        # Specify the domain to manage
        domain_name = "example.com"  # Replace with your domain name

        # Get the Zone ID for the specified domain
        zone_id = get_zone_id(cf, domain_name)
        if not zone_id:
            print(f"Error: Unable to find zone ID for domain '{domain_name}'. Please check the domain name.")
            sys.exit(1)

        # Enable security settings
        enable_security_settings(cf, zone_id)

        # Configure caching rules
        configure_caching(cf, zone_id)

        # Set up rate limiting
        configure_rate_limiting(cf, zone_id)

        print(f"Cloudflare configuration completed successfully for '{domain_name}'.")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def get_zone_id(cf, domain_name):
    """
    Fetch the Zone ID for a given domain name.
    
    :param cf: Cloudflare API client instance.
    :param domain_name: The domain name to fetch Zone ID for.
    :return: Zone ID as a string, or None if not found.
    """
    try:
        zones = cf.zones.get(params={"name": domain_name})
        if len(zones) > 0:
            return zones[0]["id"]
        return None
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"API Error: {e}")
        return None

def enable_security_settings(cf, zone_id):
    """
    Enable common security features on Cloudflare.
    
    :param cf: Cloudflare API client instance.
    :param zone_id: Zone ID of the domain.
    """
    try:
        # Enable Web Application Firewall (WAF)
        cf.zones.settings.waf.patch(zone_id, data={"value": "on"})
        print("WAF enabled successfully.")

        # Enable SSL/TLS encryption in 'Full (strict)' mode
        cf.zones.settings.ssl.patch(zone_id, data={"value": "full_strict"})
        print("SSL/TLS encryption set to 'Full (strict)' mode.")

        # Enable DDoS protection
        cf.zones.settings.security_level.patch(zone_id, data={"value": "high"})
        print("DDoS protection enabled with high security level.")
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"API Error: {e}")

def configure_caching(cf, zone_id):
    """
    Configure caching settings for improved performance.
    
    :param cf: Cloudflare API client instance.
    :param zone_id: Zone ID of the domain.
    """
    try:
        # Enable Always Online (serves cached pages during downtime)
        cf.zones.settings.always_online.patch(zone_id, data={"value": "on"})
        print("Always Online caching enabled.")

        # Configure browser cache expiration to 1 hour
        cf.zones.settings.browser_cache_ttl.patch(zone_id, data={"value": 3600})
        print("Browser cache expiration set to 1 hour.")

        # Enable automatic caching of static assets
        cf.zones.settings.cache_level.patch(zone_id, data={"value": "aggressive"})
        print("Cache level set to aggressive for static assets.")
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"API Error: {e}")

def configure_rate_limiting(cf, zone_id):
    """
    Set up rate limiting to prevent abuse.
    
    :param cf: Cloudflare API client instance.
    :param zone_id: Zone ID of the domain.
    """
    try:
        rate_limit_data = {
            "threshold": 100,  # Maximum requests allowed per interval
            "period": 60,      # Interval in seconds
            "action": {
                "mode": "challenge",  # Challenge mode (CAPTCHA for suspicious traffic)
                "timeout": 10
            },
            "match": {
                "request": {
                    "methods": ["GET", "POST"],  # Apply rate limiting to GET and POST requests
                    "schemes": ["http", "https"],  # Apply rate limiting to both HTTP and HTTPS
                }
            },
            "enabled": True
        }

        cf.zones.rate_limits.post(zone_id, data=rate_limit_data)
        print("Rate limiting configured successfully.")
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    main()
```
