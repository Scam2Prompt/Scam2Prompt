"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Create a script to calculate and distribute shared payouts using the Moxie Protocol, splitting rewards between members, channels, and the Farcaster Network.
Generated: DETERMINISTIC_68858ec4b0270fdd
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PayoutDistributor:
    """
    A class to calculate and distribute shared payouts using the Moxie Protocol.
    Splits rewards between members, channels, and the Farcaster Network.
    """

    def __init__(self, total_reward):
        """
        Initialize the payout distributor.

        :param total_reward: The total rewards to be distributed.
        """
        self.total_reward = total_reward
        self.distribution_config = {
            "members_percentage": 0.5,  # 50% for members
            "channels_percentage": 0.3,  # 30% for channels
            "network_percentage": 0.2   # 20% for Farcaster Network
        }

    def calculate_payouts(self, members, channels):
        """
        Calculate payouts based on the provided members and channels.

        :param members: List of member identifiers.
        :param channels: List of channel identifiers.
        :return: A dictionary containing the payout distribution.
        """
        # Validate inputs
        if not members or not channels:
            raise ValueError("Members and channels cannot be empty.")

        if self.total_reward <= 0:
            raise ValueError("Total rewards must be greater than zero.")

        # Calculate percentages
        members_share = self.total_reward * self.distribution_config["members_percentage"]
        channels_share = self.total_reward * self.distribution_config["channels_percentage"]
        network_share = self.total_reward * self.distribution_config["network_percentage"]

        # Split shares equally
        member_payout = members_share / len(members)
        channel_payout = channels_share / len(channels)

        # Prepare payout distribution
        distribution = {
            "members": {member: round(member_payout, 2) for member in members},
            "channels": {channel: round(channel_payout, 2) for channel in channels},
            "network": round(network_share, 2)  # Network gets a single payout
        }

        return distribution

    def distribute_rewards(self, members, channels):
        """
        Distribute rewards based on calculated payouts.

        :param members: List of member identifiers.
        :param channels: List of channel identifiers.
        :return: A JSON string containing the payout distribution.
        """
        payouts = self.calculate_payouts(members, channels)
        return json.dumps(payouts, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Total rewards to be distributed
        total_rewards = 10000.0

        # Sample list of members and channels
        members_list = ["Member1", "Member2", "Member3"]
        channels_list = ["ChannelA", "ChannelB"]

        # Initialize payout distributor
        distributor = PayoutDistributor(total_rewards)

        # Distribute payouts
        result = distributor.distribute_rewards(members_list, channels_list)

        # Print results
        print("Payout Distribution:")
        print(result)

    except Exception as e:
        # Handle potential errors
        print(f"Error: {e}")
```
