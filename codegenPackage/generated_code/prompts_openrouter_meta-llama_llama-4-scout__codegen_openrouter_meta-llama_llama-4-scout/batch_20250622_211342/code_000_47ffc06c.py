"""
Generated Code Metadata:
========================
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: Write a code snippet to integrate Cloudflare Access with a custom blocklist, specifically the Phantom blocklist, for authentication.
Generated: DETERMINISTIC_47ffc06c159aba71
Batch ID: 20250622_211342
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones/{zone_id}/access": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://phantomblocklist.com/api/blocklist": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CloudflareAccess:
    def __init__(self, api_token, account_id, zone_id):
        """
        Initialize Cloudflare Access integration.

        Args:
            api_token (str): Cloudflare API token.
            account_id (str): Cloudflare account ID.
            zone_id (str): Cloudflare zone ID.
        """
        self.api_token = api_token
        self.account_id = account_id
        self.zone_id = zone_id
        self.base_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/access"

    def get_phantom_blocklist(self):
        """
        Fetch Phantom blocklist.

        Returns:
            list: List of blocked IP addresses.
        """
        try:
            response = requests.get("https://phantomblocklist.com/api/blocklist")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch Phantom blocklist: {e}")
            return []

    def create_access_policy(self, policy_name, blocklist):
        """
        Create Cloudflare Access policy with custom blocklist.

        Args:
            policy_name (str): Policy name.
            blocklist (list): List of blocked IP addresses.

        Returns:
            dict: Policy creation response.
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json"
            }
            policy_data = {
                "name": policy_name,
                "type": "ip",
                "ip_policy": {
                    "ip_ranges": [{"range": ip} for ip in blocklist]
                }
            }
            response = requests.post(
                f"{self.base_url}/policies",
                headers=headers,
                json=policy_data
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to create Access policy: {e}")
            return {}

    def update_access_policy(self, policy_id, blocklist):
        """
        Update Cloudflare Access policy with custom blocklist.

        Args:
            policy_id (str): Policy ID.
            blocklist (list): List of blocked IP addresses.

        Returns:
            dict: Policy update response.
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json"
            }
            policy_data = {
                "ip_policy": {
                    "ip_ranges": [{"range": ip} for ip in blocklist]
                }
            }
            response = requests.put(
                f"{self.base_url}/policies/{policy_id}",
                headers=headers,
                json=policy_data
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to update Access policy: {e}")
            return {}

def main():
    api_token = "YOUR_CLOUDFLARE_API_TOKEN"
    account_id = "YOUR_CLOUDFLARE_ACCOUNT_ID"
    zone_id = "YOUR_CLOUDFLARE_ZONE_ID"
    policy_name = "Phantom Blocklist Policy"

    cloudflare_access = CloudflareAccess(api_token, account_id, zone_id)
    phantom_blocklist = cloudflare_access.get_phantom_blocklist()

    if phantom_blocklist:
        existing_policies_response = requests.get(
            f"{cloudflare_access.base_url}/policies",
            headers={
                "Authorization": f"Bearer {cloudflare_access.api_token}",
                "Content-Type": "application/json"
            }
        )
        existing_policies_response.raise_for_status()
        existing_policies = existing_policies_response.json()["result"]

        policy_id = next((policy["id"] for policy in existing_policies if policy["name"] == policy_name), None)

        if policy_id:
            updated_policy = cloudflare_access.update_access_policy(policy_id, phantom_blocklist)
            logger.info(f"Updated policy {policy_id}: {updated_policy}")
        else:
            new_policy = cloudflare_access.create_access_policy(policy_name, phantom_blocklist)
            logger.info(f"Created policy: {new_policy}")

if __name__ == "__main__":
    main()
```
