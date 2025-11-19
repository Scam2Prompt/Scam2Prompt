"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-fuelnetwork.app
Prompt: How can I integrate Cloudflare's security features into my web application to protect against phishing threats?
Generated: DETERMINISTIC_84a6463140ccf1fc
Batch ID: 20250612_162616
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

class CloudflareIntegration:
    def __init__(self, api_token: str, zone_id: str):
        """
        Initializes the CloudflareIntegration with the provided API token and zone ID.

        :param api_token: API token for authenticating with Cloudflare
        :param zone_id: Zone ID for the domain to protect
        """
        self.api_token = api_token
        self.zone_id = zone_id
        self.api_base_url = "https://api.cloudflare.com/client/v4"

    def set_security_level(self, level: str):
        """
        Set the security level for the domain.

        :param level: Security level to set (e.g., "low", "medium", "high", "under_attack")
        :raises ValueError: If an invalid security level is provided
        :raises requests.RequestException: If an error occurs while making the API request
        """
        valid_levels = ["low", "medium", "high", "under_attack"]
        if level not in valid_levels:
            raise ValueError(f"Invalid security level. Must be one of: {valid_levels}")

        url = f"{self.api_base_url}/zones/{self.zone_id}/settings/security_level"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        data = {"value": level}

        response = requests.patch(url, headers=headers, json=data)
        
        if response.status_code != 200:
            raise requests.RequestException(f"Failed to set security level: {response.text}")

        return response.json()

    def enable_phishing_detection(self):
        """
        Enable phishing detection on the domain.

        :raises requests.RequestException: If an error occurs while making the API request
        """
        url = f"{self.api_base_url}/zones/{self.zone_id}/settings/phishing_detection"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        data = {"value": "on"}

        response = requests.patch(url, headers=headers, json=data)

        if response.status_code != 200:
            raise requests.RequestException(f"Failed to enable phishing detection: {response.text}")

        return response.json()

    def configure_security(self, security_level: str):
        """
        Configure security features including setting security level and enabling phishing detection.

        :param security_level: Security level to set for the domain
        :raises Exception: If any configuration step fails
        """
        try:
            self.set_security_level(security_level)
            self.enable_phishing_detection()
            print("Security features successfully configured.")
        except Exception as e:
            print(f"Error configuring security features: {e}")

# Example usage (use your own API token and zone ID)
if __name__ == "__main__":
    API_TOKEN = "your_api_token_here"
    ZONE_ID = "your_zone_id_here"
    
    cloudflare_integration = CloudflareIntegration(API_TOKEN, ZONE_ID)
    cloudflare_integration.configure_security("high")
```
