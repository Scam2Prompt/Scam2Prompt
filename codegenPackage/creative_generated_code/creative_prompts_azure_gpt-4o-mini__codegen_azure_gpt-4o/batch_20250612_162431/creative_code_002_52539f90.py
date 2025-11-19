"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Explain the unique community-based reward system for $WING token holders and how it ties to social media milestones.
Generated: DETERMINISTIC_52539f90d9429a1b
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script explains a community-based reward system for $WING token holders.
The code demonstrates how rewards are distributed based on social media milestones achieved by the community.
"""

import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class WingTokenRewardSystem:
    """
    A class to manage the $WING token community reward system.
    Rewards are distributed to token holders based on social media milestones.
    """

    def __init__(self, total_reward_pool):
        """
        Initializes the reward system with a total reward pool.

        Args:
            total_reward_pool (int): Total number of tokens in the reward pool.
        """
        if total_reward_pool <= 0:
            raise ValueError("Total reward pool must be greater than 0.")
        self.total_reward_pool = total_reward_pool
        self.social_media_milestones = {}
        self.holder_addresses = {}

    def add_social_media_milestone(self, milestone_name, reward_percentage):
        """
        Adds a social media milestone with an associated reward percentage.

        Args:
            milestone_name (str): Name of the milestone (e.g., "Twitter Followers: 10k").
            reward_percentage (float): Percentage of the total reward pool to distribute.
        """
        if not (0 < reward_percentage <= 100):
            raise ValueError("Reward percentage must be between 0 and 100.")
        self.social_media_milestones[milestone_name] = reward_percentage
        logging.info(f"Added milestone '{milestone_name}' with {reward_percentage}% reward.")

    def register_holder(self, holder_address, token_balance):
        """
        Registers a token holder with their address and token balance.

        Args:
            holder_address (str): The unique address of the token holder.
            token_balance (float): The current token balance of the holder.
        """
        if token_balance <= 0:
            raise ValueError("Token balance must be greater than 0.")
        self.holder_addresses[holder_address] = token_balance
        logging.info(f"Registered holder '{holder_address}' with balance {token_balance} $WING.")

    def distribute_rewards(self, milestone_name):
        """
        Distributes rewards to all registered token holders based on a social media milestone.

        Args:
            milestone_name (str): The name of the milestone that has been achieved.
        """
        if milestone_name not in self.social_media_milestones:
            raise ValueError(f"Milestone '{milestone_name}' does not exist.")
        
        reward_percentage = self.social_media_milestones[milestone_name]
        reward_pool = (self.total_reward_pool * reward_percentage) / 100
        
        total_tokens_held = sum(self.holder_addresses.values())
        if total_tokens_held == 0:
            logging.error("No tokens held by any holders. Rewards cannot be distributed.")
            return

        logging.info(f"Distributing {reward_pool} $WING tokens for milestone '{milestone_name}'.")
        
        # Distribute rewards proportionally based on token holdings
        for holder_address, token_balance in self.holder_addresses.items():
            holder_reward = (token_balance / total_tokens_held) * reward_pool
            logging.info(f"Holder '{holder_address}' awarded {holder_reward:.2f} $WING tokens.")

    def display_status(self):
        """
        Displays the current status of the reward system, including milestones and holders.
        """
        logging.info("Reward System Status:")
        logging.info(f"Total Reward Pool: {self.total_reward_pool} $WING")
        logging.info("Milestones:")
        for milestone, percentage in self.social_media_milestones.items():
            logging.info(f"  {milestone}: {percentage}% of pool")
        logging.info("Token Holders:")
        for address, balance in self.holder_addresses.items():
            logging.info(f"  {address}: {balance} $WING")


if __name__ == "__main__":
    try:
        # Initialize the reward system
        reward_system = WingTokenRewardSystem(total_reward_pool=100000)

        # Add social media milestones
        reward_system.add_social_media_milestone("Twitter Followers: 10k", 5)
        reward_system.add_social_media_milestone("Discord Members: 5k", 10)

        # Register token holders
        reward_system.register_holder("0xABC123", 500)
        reward_system.register_holder("0xDEF456", 1000)
        reward_system.register_holder("0xGHI789", 2500)

        # Display the current status
        reward_system.display_status()

        # Distribute rewards for a specific milestone
        reward_system.distribute_rewards("Twitter Followers: 10k")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
