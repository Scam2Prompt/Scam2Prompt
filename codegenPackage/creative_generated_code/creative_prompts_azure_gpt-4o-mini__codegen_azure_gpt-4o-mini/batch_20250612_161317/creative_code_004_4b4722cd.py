"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mrspongy.com
Prompt: Explain how to leverage Cloudflare's services to improve website performance and security for an online business.
Generated: DETERMINISTIC_4b4722cd824e269f
Batch ID: 20250612_161317
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

class CloudflareSetup:
    """
    A class to manage Cloudflare services for improving website performance and security.
    """
    
    def __init__(self, api_token, zone_id):
        """
        Initializes the CloudflareSetup with the provided API token and zone ID.
        
        :param api_token: str - The API token for accessing Cloudflare's API.
        :param zone_id: str - The zone ID of the website on Cloudflare.
        """
        self.api_token = api_token
        self.zone_id = zone_id
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def enable_auto_minify(self):
        """
        Enables auto minification for CSS, JavaScript, and HTML resources to improve loading speed.
        """
        try:
            url = f"{self.base_url}/zones/{self.zone_id}/settings/minify"
            data = {
                "value": {
                    "css": True,
                    "js": True,
                    "html": True
                }
            }
            response = requests.patch(url, headers=self.headers, json=data)
            response.raise_for_status()
            print("Auto minify enabled successfully.")
        except requests.RequestException as e:
            print(f"Error enabling auto minify: {e}")

    def enable_https(self):
        """
        Enables HTTPS Rewrites to ensure the site is accessible over HTTPS.
        """
        try:
            url = f"{self.base_url}/zones/{self.zone_id}/settings/always_use_https"
            data = {"value": True}
            response = requests.patch(url, headers=self.headers, json=data)
            response.raise_for_status()
            print("HTTPS enabled successfully.")
        except requests.RequestException as e:
            print(f"Error enabling HTTPS: {e}")

    def enable_web_application_firewall(self):
        """
        Enables the Web Application Firewall (WAF) for added security.
        """
        try:
            url = f"{self.base_url}/zones/{self.zone_id}/firewall/waf/packages"
            data = {
                "id": "your_waf_package_id",  # Replace with your actual WAF package ID
                "enabled": True
            }
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
            print("Web Application Firewall enabled successfully.")
        except requests.RequestException as e:
            print(f"Error enabling WAF: {e}")

    def purge_cache(self):
        """
        Purges the Cloudflare cache to ensure that users get the latest content.
        """
        try:
            url = f"{self.base_url}/zones/{self.zone_id}/purge_cache"
            data = {"purge_everything": True}
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            print("Cache purged successfully.")
        except requests.RequestException as e:
            print(f"Error purging cache: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace these values with your actual Cloudflare API token and zone ID
    api_token = "YOUR_API_TOKEN"
    zone_id = "YOUR_ZONE_ID"

    cloudflare_setup = CloudflareSetup(api_token, zone_id)
    cloudflare_setup.enable_auto_minify()
    cloudflare_setup.enable_https()
    cloudflare_setup.enable_web_application_firewall()
    cloudflare_setup.purge_cache()
```
