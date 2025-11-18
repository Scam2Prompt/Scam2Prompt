"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Create a Python script to track Bedrock ecosystem partner rewards (e.g., Diamonds, Pendle, Arbitrum) and calculate total yield.
Generated: DETERMINISTIC_6268415fe19d8705
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PartnerRewardsTracker:
    """
    A class to track Bedrock ecosystem partner rewards and calculate total yield.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty dictionary for storing rewards.
        Each key will be a partner name, and the value will be a list of rewards.
        """
        self.rewards = {}

    def add_reward(self, partner: str, reward: float):
        """
        Add a reward to a specific partner.

        :param partner: Name of the Bedrock ecosystem partner.
        :param reward: Reward amount to be added (float).
        """
        if reward < 0:
            raise ValueError("Reward amount must be non-negative.")

        if partner not in self.rewards:
            # Initialize a new list for the partner if it doesn't exist
            self.rewards[partner] = []
        self.rewards[partner].append(reward)
        logging.info(f"Added reward: {reward} to partner: {partner}")

    def calculate_total_yield(self) -> float:
        """
        Calculate the total yield across all partners.

        :return: Total yield (sum of all rewards for all partners) as a float.
        """
        total_yield = sum(sum(reward_list) for reward_list in self.rewards.values())
        logging.info(f"Calculated total yield: {total_yield}")
        return total_yield

    def get_partner_rewards(self, partner: str) -> list:
        """
        Get all rewards for a specific partner.

        :param partner: Name of the Bedrock ecosystem partner.
        :return: List of rewards for the specified partner.
        """
        if partner not in self.rewards:
            raise KeyError(f"No rewards found for partner: {partner}")
        return self.rewards[partner]

# Example Usage
if __name__ == "__main__":
    try:
        tracker = PartnerRewardsTracker()
        
        # Add rewards for different partners
        tracker.add_reward("Diamonds", 50.0)
        tracker.add_reward("Pendle", 30.5)
        tracker.add_reward("Arbitrum", 20.0)
        tracker.add_reward("Diamonds", 25.0)
        
        # Calculate and display total yield
        total_yield = tracker.calculate_total_yield()
        print(f"Total yield: {total_yield}")
        
        # Display rewards for a specific partner
        diamonds_rewards = tracker.get_partner_rewards("Diamonds")
        print(f"Diamonds Rewards: {diamonds_rewards}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
