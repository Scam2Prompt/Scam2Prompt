"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbtrum.net
Prompt: What are the best practices for configuring Cloudflare settings to prevent DDoS attacks on my website?
Generated: DETERMINISTIC_c72357b785cd3896
Batch ID: 20250612_164035
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
  "https://api.cloudflare.com/client/v4/zones/{self.zone_id}/firewall/access_rules/rules": {
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

class CloudflareDDoSProtection:
    def __init__(self, api_token, zone_id):
        """
        Initializes the CloudflareDDoSProtection instance.
        
        :param api_token: Cloudflare API token with necessary permissions
        :param zone_id: Cloudflare zone ID for the website
        """
        self.api_token = api_token
        self.zone_id = zone_id
        self.base_url = f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}/settings"

    def update_security_level(self, level):
        """
        Updates the security level to help mitigate DDoS attacks.
        
        :param level: Security level can be 'essentially_off', 'low', 'medium', 'high', or 'under_attack'
        :raises ValueError: If an invalid security level is provided
        :return: Response from Cloudflare API
        """
        valid_levels = ['essentially_off', 'low', 'medium', 'high', 'under_attack']
        if level not in valid_levels:
            raise ValueError(f"Invalid security level: {level}. Must be one of {valid_levels}.")

        url = f"{self.base_url}/security_level"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        data = {"value": level}

        try:
            response = requests.patch(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response as JSON
        except requests.exceptions.RequestException as e:
            print(f"Error updating security level: {e}")
            return None

    def enable_bot_fight_mode(self):
        """
        Enables bot fight mode to help mitigate bot attacks.
        
        :return: Response from Cloudflare API
        """
        url = f"{self.base_url}/bot_management"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        data = {"value": "on"}

        try:
            response = requests.patch(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response as JSON
        except requests.exceptions.RequestException as e:
            print(f"Error enabling bot fight mode: {e}")
            return None

    def set_ip_access_rules(self, action, ip_address):
        """
        Sets access rules for specific IP addresses.
        
        :param action: Action to perform ('allow', 'block', 'challenge')
        :param ip_address: The IP address to set the access rule for
        :raises ValueError: If an invalid action is provided
        :return: Response from Cloudflare API
        """
        valid_actions = ['allow', 'block', 'challenge']
        if action not in valid_actions:
            raise ValueError(f"Invalid action: {action}. Must be one of {valid_actions}.")

        url = f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}/firewall/access_rules/rules"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        data = {
            "mode": action,
            "configuration": {
                "target": "ip",
                "value": ip_address
            },
            "notes": f"{action.capitalize()} access rule for {ip_address}"
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response as JSON
        except requests.exceptions.RequestException as e:
            print(f"Error setting IP access rule: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Provide your Cloudflare API token and zone ID here
    api_token = "YOUR_API_TOKEN"
    zone_id = "YOUR_ZONE_ID"

    ddos_protection = CloudflareDDoSProtection(api_token, zone_id)
    print(ddos_protection.update_security_level("high"))
    print(ddos_protection.enable_bot_fight_mode())
    print(ddos_protection.set_ip_access_rules("block", "192.0.2.1"))
```
