"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: How can I use the Moxie Protocol to create Fan Tokens for my Farcaster channel and implement programmatic rewards?
Generated: DETERMINISTIC_b6353ae88a6473fc
Batch ID: 20250612_162854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.moxieprotocol.com/v1": {
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

class MoxieProtocol:
    BASE_URL = "https://api.moxieprotocol.com/v1"  # Base URL for Moxie Protocol API

    def __init__(self, api_key):
        """
        Initializes the MoxieProtocol class with the provided API key.

        :param api_key: Your Moxie Protocol API key
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_fan_token(self, channel_id, token_details):
        """
        Creates a fan token for the specified Farcaster channel.

        :param channel_id: The ID of the Farcaster channel
        :param token_details: A dictionary containing the details of the token
        :return: The response from the Moxie API
        """
        url = f"{self.BASE_URL}/channels/{channel_id}/tokens"
        try:
            response = requests.post(url, headers=self.headers, json=token_details)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response in JSON format
        except requests.RequestException as e:
            print(f"Error creating fan token: {e}")
            return None

    def issue_rewards(self, channel_id, reward_details):
        """
        Issues rewards for the specified channel.

        :param channel_id: The ID of the Farcaster channel
        :param reward_details: A dictionary containing the details of the rewards
        :return: The response from the Moxie API
        """
        url = f"{self.BASE_URL}/channels/{channel_id}/rewards"
        try:
            response = requests.post(url, headers=self.headers, json=reward_details)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response in JSON format
        except requests.RequestException as e:
            print(f"Error issuing rewards: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your API key and channel ID
    API_KEY = "your_api_key_here"
    CHANNEL_ID = "your_channel_id_here"

    # Instantiate the Moxie Protocol class
    moxie = MoxieProtocol(API_KEY)

    # Define token details
    token_details = {
        "name": "Fan Token",
        "symbol": "FT",
        "total_supply": 10000,
        "description": "Exclusive token for channel fans"
    }

    # Create fan token
    fan_token_response = moxie.create_fan_token(CHANNEL_ID, token_details)
    if fan_token_response:
        print("Fan token created successfully:", fan_token_response)

    # Define reward details
    reward_details = {
        "name": "Loyalty Reward",
        "amount": 50,
        "description": "Reward for loyal fans"
    }

    # Issue rewards
    reward_response = moxie.issue_rewards(CHANNEL_ID, reward_details)
    if reward_response:
        print("Rewards issued successfully:", reward_response)
```

Note: Don't forget to replace `your_api_key_here` and `your_channel_id_here` with actual credentials and IDs when executing the code.
