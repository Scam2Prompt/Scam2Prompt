"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-cftc-us10-23b.pages.dev
Prompt: Generate a code example that demonstrates how to configure Cloudflare settings for improved performance and security.
Generated: DETERMINISTIC_40e5bcc1730e64f4
Batch ID: 20250612_161134
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/accounts/{self.account_id": {
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

class CloudflareAPI:
    """
    A class to interact with the Cloudflare API for configuring settings
    to improve performance and security.
    """

    def __init__(self, api_token, account_id):
        """
        Initializes the CloudflareAPI with the given API token and account ID.

        :param api_token: Cloudflare API token for authentication
        :param account_id: Cloudflare account ID
        """
        self.api_token = api_token
        self.account_id = account_id
        self.base_url = f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}"

    def update_performance_settings(self, zone_id, settings):
        """
        Updates performance settings for the specified zone.

        :param zone_id: The ID of the zone to update
        :param settings: A dictionary of performance settings to apply
        :return: Response from the Cloudflare API
        """
        url = f"{self.base_url}/zones/{zone_id}/settings"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.patch(url, json=settings, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def enable_security_features(self, zone_id):
        """
        Enables security features for the specified zone.

        :param zone_id: The ID of the zone to update
        :return: Response from the Cloudflare API
        """
        settings = {
            "default_security_level": "high",
            "browser_check": True,
            "js_challenge": True,
            "attack_mode": "on"
        }
        return self.update_performance_settings(zone_id, settings)

    def configure_cloudflare(self, zone_id):
        """
        Configures Cloudflare settings for a specified zone.

        :param zone_id: The ID of the zone to configure
        """
        print("Enabling security features...")
        security_response = self.enable_security_features(zone_id)
        if security_response:
            print("Security features updated:", security_response)

        performance_settings = {
            "auto_minify": {
                "css": True,
                "html": True,
                "js": True
            },
            "rocket_loader": "on",
            "http2": "on",
            "image_resizing": "on"
        }
        print("Updating performance settings...")
        performance_response = self.update_performance_settings(zone_id, performance_settings)
        if performance_response:
            print("Performance settings updated:", performance_response)

if __name__ == "__main__":
    # Example usage of the CloudflareAPI class

    # Replace these values with your actual Cloudflare API token and account ID
    API_TOKEN = 'your_api_token_here'
    ACCOUNT_ID = 'your_account_id_here'
    ZONE_ID = 'your_zone_id_here'

    # Create an instance of the CloudflareAPI
    cloudflare_api = CloudflareAPI(api_token=API_TOKEN, account_id=ACCOUNT_ID)

    # Configure the Cloudflare settings for the specified zone
    cloudflare_api.configure_cloudflare(ZONE_ID)
```
