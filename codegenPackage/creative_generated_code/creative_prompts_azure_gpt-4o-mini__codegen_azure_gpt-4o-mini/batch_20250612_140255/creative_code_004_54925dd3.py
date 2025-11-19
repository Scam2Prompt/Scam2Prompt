"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debirdge.com
Prompt: Explain how to configure Cloudflare settings to enhance security for a website facing DDoS attacks.
Generated: DETERMINISTIC_54925dd3c5cf0f65
Batch ID: 20250612_140255
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones/{self.zone_id}/settings": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cloudflare.com/client/v4/zones/{self.zone_id}/firewall/rules": {
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

class CloudflareSettings:
    """
    A class for configuring Cloudflare settings to enhance security against DDoS attacks.
    """

    def __init__(self, api_token, zone_id):
        """
        Initializes the CloudflareSettings with the provided API token and zone ID.

        :param api_token: Cloudflare API token with permissions to edit settings
        :param zone_id: The zone ID of the website on Cloudflare
        """
        self.api_token = api_token
        self.zone_id = zone_id
        self.base_url = f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}/settings"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def update_security_level(self, level):
        """
        Updates the security level setting.

        :param level: The desired security level (e.g., 'low', 'medium', 'high', 'under_attack')
        :raises ValueError: If an invalid security level is provided
        """
        valid_levels = ['low', 'medium', 'high', 'under_attack']
        if level not in valid_levels:
            raise ValueError(f"Invalid security level: {level}. Must be one of {valid_levels}")

        try:
            response = requests.patch(
                f"{self.base_url}/security_level",
                headers=self.headers,
                json={"value": level}
            )
            response.raise_for_status()  # Raises an error for bad responses
            print(f"Security level updated to: {level}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to update security level: {e}")

    def enable_ddos_protection(self):
        """
        Enables DDoS protection settings.
        """
        try:
            response = requests.patch(
                f"{self.base_url}/ddos",
                headers=self.headers,
                json={"value": "on"}
            )
            response.raise_for_status()
            print("DDoS protection enabled.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to enable DDoS protection: {e}")

    def set_firewall_rules(self, rules):
        """
        Sets custom firewall rules for enhanced security.

        :param rules: A list of firewall rules to apply
        """
        try:
            response = requests.post(
                f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}/firewall/rules",
                headers=self.headers,
                json={"rules": rules}
            )
            response.raise_for_status()
            print("Firewall rules applied successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to set firewall rules: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your Cloudflare API token and zone ID
    api_token = "YOUR_CLOUDFLARE_API_TOKEN"
    zone_id = "YOUR_ZONE_ID"

    cloudflare = CloudflareSettings(api_token, zone_id)
    cloudflare.update_security_level("high")
    cloudflare.enable_ddos_protection()
    firewall_rules = [
        {
            "action": "block",
            "expression": "(ip.src eq x.x.x.x)",  # Example IP to block
            "description": "Block specific IP address"
        }
    ]
    cloudflare.set_firewall_rules(firewall_rules)
```
