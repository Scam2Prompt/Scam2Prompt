"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeiand.app
Prompt: What are the best practices for securing a website against phishing attacks, and how can I implement them using Cloudflare?
Generated: DETERMINISTIC_bd9acda0dfd022e6
Batch ID: 20250612_162646
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones/{self.zone_id}/": {
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

class PhishingProtection:
    def __init__(self, api_token, zone_id):
        """
        Initializes the PhishingProtection class with Cloudflare API token and zone ID.

        Parameters:
            api_token (str): The Cloudflare API Token for authentication.
            zone_id (str): The Zone ID of the domain to protect.
        """
        self.api_token = api_token
        self.zone_id = zone_id
        self.base_url = f"https://api.cloudflare.com/client/v4/zones/{self.zone_id}/"

    def set_firewall_rule(self, action="block"):
        """
        Set a firewall rule to block known phishing attempts.

        Parameters:
            action (str): The action to take ("block" or "challenge").
        """
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        # Firewall rule to block requests with known phishing characteristics
        rule_data = {
            "rules": [
                {
                    "action": action,
                    "expression": "(http.request.uri.path contains 'phishing' or http.request.headers['User-Agent'] contains 'phishing')",
                    "description": "Block known phishing attempts",
                    "enabled": True
                }
            ]
        }

        try:
            response = requests.post(f"{self.base_url}firewall/rules", json=rule_data, headers=headers)
            response.raise_for_status()  # Raise error for bad responses
            print("Firewall rule set successfully.")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")  # Print HTTP error
        except Exception as e:
            print(f"An error occurred: {e}")  # Print any other errors

    def enable_bot_management(self):
        """
        Enable bot management features to mitigate automated phishing attempts.
        """
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        bot_management_data = {
            "enabled": True
        }

        try:
            response = requests.patch(f"{self.base_url}bot_management", json=bot_management_data, headers=headers)
            response.raise_for_status()  # Raise error for bad responses
            print("Bot management enabled successfully.")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")  # Print HTTP error
        except Exception as e:
            print(f"An error occurred: {e}")  # Print any other errors

if __name__ == "__main__":
    # Usage example
    API_TOKEN = "your_cloudflare_api_token"
    ZONE_ID = "your_cloudflare_zone_id"

    # Initialize the phishing protection instance
    phishing_protection = PhishingProtection(API_TOKEN, ZONE_ID)

    # Set a firewall rule to block phishing attempts
    phishing_protection.set_firewall_rule()

    # Enable bot management
    phishing_protection.enable_bot_management()
```
