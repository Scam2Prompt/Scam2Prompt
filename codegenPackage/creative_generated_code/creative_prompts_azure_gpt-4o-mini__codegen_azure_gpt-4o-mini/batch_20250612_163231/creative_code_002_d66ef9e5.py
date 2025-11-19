"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: What are the best practices for configuring Cloudflare settings to prevent DDoS attacks in a web application?
Generated: DETERMINISTIC_d66ef9e5aaf9cfd5
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones/{self.zone_id": {
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
# cloudflare_ddos_protection.py

import requests

class CloudflareDDOSProtection:
    """
    A class to configure Cloudflare settings to mitigate DDoS attacks for a web application.
    """

    def __init__(self, api_token, zone_id):
        """
        Initializes the CloudflareDDOSProtection with API token and zone ID.

        :param api_token: Cloudflare API token for authentication
        :param zone_id: Cloudflare zone ID for your domain
        """
        self.api_token = api_token
        self.zone_id = zone_id
        self.base_url = f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}"

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to Cloudflare API.

        :param endpoint: The API endpoint to call
        :param method: The HTTP method to use (GET, POST, PATCH, DELETE)
        :param data: The data to send with a POST or PATCH request
        :return: The response from the API
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other error
            return None

    def enable_anti_ddos(self):
        """
        Enables Cloudflare's DDoS protection settings.
        """
        data = {
            "value": "on"
        }
        result = self._make_request("firewall/settings/security_level", method='PATCH', data=data)
        if result:
            print("DDoS protection has been enabled.")
        else:
            print("Failed to enable DDoS protection.")

    def configure_rate_limiting(self, threshold=100, interval=60):
        """
        Configures rate limiting to mitigate DDoS attacks.

        :param threshold: Number of requests allowed before triggering the limit
        :param interval: Time window in seconds for the threshold
        """
        data = {
            "enabled": True,
            "threshold": threshold,
            "period": interval,
            "action": "block"
        }
        result = self._make_request("rate_limits", method='POST', data=data)
        if result and result.get("success"):
            print("Rate limiting has been configured.")
        else:
            print("Failed to configure rate limiting.")

    def update_web_application_firewall(self, action="on"):
        """
        Updates the Web Application Firewall (WAF) settings.

        :param action: Turn the WAF on or off
        """
        data = {
            "mode": action
        }
        result = self._make_request("firewall/waf/packages", method='PATCH', data=data)
        if result and result.get("success"):
            print("WAF has been updated.")
        else:
            print("Failed to update WAF settings.")

# Example usage:
if __name__ == "__main__":
    # Replace with your actual Cloudflare API token and zone ID
    API_TOKEN = "your_api_token"
    ZONE_ID = "your_zone_id"

    cloudflare_protection = CloudflareDDOSProtection(API_TOKEN, ZONE_ID)
    cloudflare_protection.enable_anti_ddos()
    cloudflare_protection.configure_rate_limiting(threshold=100, interval=60)
    cloudflare_protection.update_web_application_firewall(action="on")
```
