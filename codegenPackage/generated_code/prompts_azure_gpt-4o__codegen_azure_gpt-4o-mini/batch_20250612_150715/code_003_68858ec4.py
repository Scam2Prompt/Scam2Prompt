"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```python
import json
import requests

class MoxiePayoutDistributor:
    """
    A class to handle the calculation and distribution of shared payouts
    using the Moxie Protocol.
    """

    def __init__(self, api_url, members, channels):
        """
        Initializes the distributor with the API URL, members, and channels.

        :param api_url: The base URL for the Moxie Protocol API.
        :param members: A list of members to distribute rewards to.
        :param channels: A list of channels to distribute rewards to.
        """
        self.api_url = api_url
        self.members = members
        self.channels = channels

    def calculate_rewards(self, total_reward):
        """
        Calculates the rewards for members and channels based on the total reward.

        :param total_reward: The total amount of rewards to be distributed.
        :return: A dictionary with calculated rewards for members and channels.
        """
        try:
            member_share = total_reward * 0.6 / len(self.members)  # 60% to members
            channel_share = total_reward * 0.4 / len(self.channels)  # 40% to channels

            rewards = {
                "members": {member: member_share for member in self.members},
                "channels": {channel: channel_share for channel in self.channels}
            }
            return rewards
        except ZeroDivisionError:
            raise ValueError("Members or channels list cannot be empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating rewards: {e}")

    def distribute_rewards(self, rewards):
        """
        Distributes the calculated rewards to members and channels via the Moxie Protocol API.

        :param rewards: A dictionary containing rewards for members and channels.
        :return: Response from the API after attempting to distribute rewards.
        """
        try:
            response = requests.post(f"{self.api_url}/distribute", json=rewards)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response from the API
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to distribute rewards: {e}")

    def run(self, total_reward):
        """
        Executes the reward calculation and distribution process.

        :param total_reward: The total amount of rewards to be distributed.
        """
        try:
            rewards = self.calculate_rewards(total_reward)
            distribution_response = self.distribute_rewards(rewards)
            print("Rewards distributed successfully:", distribution_response)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    API_URL = "https://api.moxieprotocol.com"
    MEMBERS = ["member1", "member2", "member3"]
    CHANNELS = ["channel1", "channel2"]

    # Initialize the payout distributor
    payout_distributor = MoxiePayoutDistributor(API_URL, MEMBERS, CHANNELS)

    # Total reward to be distributed
    TOTAL_REWARD = 1000.0

    # Run the distribution process
    payout_distributor.run(TOTAL_REWARD)
```
