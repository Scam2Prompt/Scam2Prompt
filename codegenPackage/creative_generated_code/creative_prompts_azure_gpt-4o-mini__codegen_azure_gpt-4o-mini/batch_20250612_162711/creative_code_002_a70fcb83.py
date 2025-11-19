"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepnconnectdapp.pages.dev
Prompt: Write a function to handle NFT rewards distribution based on the staking mechanisms outlined in the DeFi Protocol.
Generated: DETERMINISTIC_a70fcb835dcb6da6
Batch ID: 20250612_162711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List, Tuple
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NFTRewardDistributor:
    def __init__(self):
        """Initialize the NFTRewardDistributor with an empty stake record."""
        self.staking_records: Dict[str, float] = {}  # Stores user addresses and their staked amounts

    def stake(self, user_address: str, amount: float) -> None:
        """Stake a specified amount of tokens for a user.

        Args:
            user_address (str): The address of the user staking tokens.
            amount (float): The amount of tokens to stake.

        Raises:
            ValueError: If the staking amount is non-positive or the address is invalid.
        """
        if amount <= 0:
            logging.error("Stake amount must be positive.")
            raise ValueError("Stake amount must be positive.")
        if not self._is_valid_address(user_address):
            logging.error("Invalid user address provided.")
            raise ValueError("Invalid user address.")

        self.staking_records[user_address] = self.staking_records.get(user_address, 0) + amount
        logging.info(f"{user_address} staked {amount}. Total staked: {self.staking_records[user_address]}")

    def distribute_rewards(self, total_rewards: float) -> Dict[str, float]:
        """Distribute NFT rewards based on the staking amounts.

        Args:
            total_rewards (float): The total amount of rewards to distribute.

        Returns:
            Dict[str, float]: A dictionary mapping user addresses to their NFT rewards.

        Raises:
            ValueError: If total rewards are non-positive or there are no staked users.
        """
        if total_rewards <= 0:
            logging.error("Total rewards must be positive.")
            raise ValueError("Total rewards must be positive.")
        if not self.staking_records:
            logging.error("No staked users to distribute rewards to.")
            raise ValueError("No staked users to distribute rewards.")

        total_staked = sum(self.staking_records.values())
        rewards_distribution: Dict[str, float] = {}

        for user_address, staked_amount in self.staking_records.items():
            reward = (staked_amount / total_staked) * total_rewards
            rewards_distribution[user_address] = reward
            logging.info(f"Distributed {reward} rewards to {user_address}")

        return rewards_distribution

    def _is_valid_address(self, address: str) -> bool:
        """Check if a given address is valid (dummy validation).

        Args:
            address (str): The address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return isinstance(address, str) and len(address) == 42  # Example length for Ethereum addresses

# Example Usage
if __name__ == "__main__":
    distributor = NFTRewardDistributor()
    try:
        distributor.stake("0x1234567890abcdef1234567890abcdef12345678", 100)
        distributor.stake("0xabcdef1234567890abcdef1234567890abcdef12", 200)
        rewards = distributor.distribute_rewards(300)
        print("Rewards Distribution:", rewards)
    except ValueError as e:
        logging.error(f"Error during processing: {e}")
```
