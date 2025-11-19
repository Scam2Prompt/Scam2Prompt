"""
Generated Code Metadata:
========================
Original URL: https://nft-solaj.web.app
Prompt: Write code to implement a rewards system for NFT creators, similar to the "Rewards" feature mentioned on the Magic Eden Launchpad.
Generated: DETERMINISTIC_013d5bf998c0fbf7
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_system.py

from typing import Dict, List
from datetime import datetime, timedelta
import hashlib

class NFT:
    def __init__(self, id: str, creator: str, mint_date: datetime):
        """
        Initialize an NFT object.

        Args:
        - id (str): Unique identifier for the NFT.
        - creator (str): Address of the NFT creator.
        - mint_date (datetime): Date and time the NFT was minted.
        """
        self.id = id
        self.creator = creator
        self.mint_date = mint_date

class RewardsSystem:
    def __init__(self):
        """
        Initialize the rewards system.
        """
        self.rewards = {}  # type: Dict[str, List[Reward]]
        self.nfts = {}  # type: Dict[str, NFT]

    def add_nft(self, nft: NFT):
        """
        Add an NFT to the system.

        Args:
        - nft (NFT): NFT object to add.
        """
        self.nfts[nft.id] = nft

    def add_reward(self, nft_id: str, reward: 'Reward'):
        """
        Add a reward for an NFT.

        Args:
        - nft_id (str): ID of the NFT.
        - reward (Reward): Reward object to add.
        """
        if nft_id not in self.rewards:
            self.rewards[nft_id] = []
        self.rewards[nft_id].append(reward)

    def calculate_rewards(self, nft_id: str) -> List[Dict]:
        """
        Calculate rewards for an NFT.

        Args:
        - nft_id (str): ID of the NFT.

        Returns:
        - List[Dict]: List of reward dictionaries.
        """
        if nft_id not in self.rewards:
            return []

        rewards = []
        for reward in self.rewards[nft_id]:
            reward_dict = {
                'type': reward.type,
                'amount': reward.amount,
                'description': reward.description
            }
            rewards.append(reward_dict)
        return rewards

class Reward:
    def __init__(self, type: str, amount: int, description: str, start_date: datetime, end_date: datetime):
        """
        Initialize a Reward object.

        Args:
        - type (str): Type of reward (e.g. "token", "percentage").
        - amount (int): Amount of reward.
        - description (str): Description of the reward.
        - start_date (datetime): Start date of the reward period.
        - end_date (datetime): End date of the reward period.
        """
        self.type = type
        self.amount = amount
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """
        Check if the reward is active.

        Returns:
        - bool: True if the reward is active, False otherwise.
        """
        now = datetime.now()
        return self.start_date <= now <= self.end_date

def main():
    # Create an NFT
    nft = NFT("12345", "creator_address", datetime.now() - timedelta(days=10))

    # Create rewards
    reward1 = Reward("token", 100, "10% of sale price", datetime.now() - timedelta(days=5), datetime.now() + timedelta(days=5))
    reward2 = Reward("percentage", 5, "5% of sale price", datetime.now() - timedelta(days=3), datetime.now() + timedelta(days=3))

    # Create rewards system
    rewards_system = RewardsSystem()
    rewards_system.add_nft(nft)
    rewards_system.add_reward(nft.id, reward1)
    rewards_system.add_reward(nft.id, reward2)

    # Calculate rewards
    rewards = rewards_system.calculate_rewards(nft.id)
    for reward in rewards:
        print(reward)

if __name__ == "__main__":
    main()
```
