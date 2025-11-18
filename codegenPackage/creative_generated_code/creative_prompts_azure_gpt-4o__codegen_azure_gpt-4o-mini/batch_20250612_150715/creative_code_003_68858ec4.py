"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Create a script to calculate and distribute shared payouts using the Moxie Protocol, splitting rewards between members, channels, and the Farcaster Network.
Generated: DETERMINISTIC_68858ec4b0270fdd
Batch ID: 20250612_150715
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.moxieprotocol.com": {
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
import json
import requests
from decimal import Decimal, InvalidOperation

# Define constants for the Moxie Protocol API
MOXIE_API_URL = "https://api.moxieprotocol.com"
HEADERS = {
    "Content-Type": "application/json",
}

class PayoutDistributor:
    def __init__(self):
        self.members = []
        self.channels = []
        self.total_reward = Decimal('0.0')

    def load_members(self, members_json):
        """Load members from a JSON string."""
        try:
            self.members = json.loads(members_json)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON format for members") from e

    def load_channels(self, channels_json):
        """Load channels from a JSON string."""
        try:
            self.channels = json.loads(channels_json)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON format for channels") from e

    def set_total_reward(self, amount):
        """Set the total reward amount to be distributed."""
        try:
            self.total_reward = Decimal(amount)
        except (InvalidOperation, ValueError) as e:
            raise ValueError("Invalid amount for total reward") from e

    def calculate_payouts(self):
        """Calculate payouts for members and channels."""
        if not self.members or not self.channels:
            raise ValueError("Members and channels must be loaded before calculating payouts")

        member_count = len(self.members)
        channel_count = len(self.channels)

        # Calculate member and channel shares
        member_share = self.total_reward / (member_count + channel_count)
        channel_share = self.total_reward / (member_count + channel_count)

        payouts = {
            "members": {member: str(member_share) for member in self.members},
            "channels": {channel: str(channel_share) for channel in self.channels},
        }

        return payouts

    def send_payouts(self, payouts):
        """Send the calculated payouts to the Moxie Protocol API."""
        try:
            response = requests.post(
                f"{MOXIE_API_URL}/payouts",
                headers=HEADERS,
                data=json.dumps(payouts)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError("Failed to send payouts to Moxie Protocol") from e

def main():
    distributor = PayoutDistributor()

    # Sample JSON input for members and channels
    members_json = '["member1", "member2", "member3"]'
    channels_json = '["channel1", "channel2"]'

    try:
        distributor.load_members(members_json)
        distributor.load_channels(channels_json)
        distributor.set_total_reward(Decimal('100.00'))

        payouts = distributor.calculate_payouts()
        response = distributor.send_payouts(payouts)

        print("Payouts were successfully distributed:", response)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
