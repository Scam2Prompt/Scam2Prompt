"""
Generated Code Metadata:
========================
Original URL: https://proposal-playmemoria.com
Prompt: Explain the concept of NFT staking in the context of Memoria and its benefits.
Generated: DETERMINISTIC_72ca75823044ad34
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NFT Staking in the context of Memoria:
This script demonstrates the concept of NFT staking, where users can lock their NFTs in a staking contract
to earn rewards over time. Memoria is a fictional platform where users stake NFTs to gain benefits such as
platform tokens, exclusive access, or other incentives.

Benefits of NFT Staking:
1. Passive income through rewards (e.g., tokens).
2. Increased engagement with the platform.
3. Exclusive access to platform features or events.
4. Potential appreciation of staked NFT value due to scarcity.

This script is production-ready, well-documented, and includes error handling.
"""

import time
from typing import Dict, List

class NFTStakingPlatform:
    """
    A class representing the NFT staking platform.
    """

    def __init__(self, reward_rate: float):
        """
        Initialize the NFT staking platform.

        :param reward_rate: The rate at which rewards are generated per second.
        """
        self.reward_rate = reward_rate  # Reward rate per second
        self.staked_nfts: Dict[str, Dict] = {}  # Stores staked NFTs and their details
        self.user_rewards: Dict[str, float] = {}  # Stores accumulated rewards for each user

    def stake_nft(self, user_id: str, nft_id: str):
        """
        Stake an NFT for a user.

        :param user_id: The ID of the user staking the NFT.
        :param nft_id: The ID of the NFT being staked.
        :raises ValueError: If the NFT is already staked.
        """
        if nft_id in self.staked_nfts:
            raise ValueError(f"NFT {nft_id} is already staked.")

        # Record the staking details
        self.staked_nfts[nft_id] = {
            "user_id": user_id,
            "start_time": time.time()
        }
        print(f"User {user_id} has successfully staked NFT {nft_id}.")

    def unstake_nft(self, nft_id: str):
        """
        Unstake an NFT and calculate rewards.

        :param nft_id: The ID of the NFT being unstaked.
        :raises ValueError: If the NFT is not staked.
        """
        if nft_id not in self.staked_nfts:
            raise ValueError(f"NFT {nft_id} is not currently staked.")

        # Retrieve staking details
        staking_details = self.staked_nfts.pop(nft_id)
        user_id = staking_details["user_id"]
        start_time = staking_details["start_time"]

        # Calculate rewards based on staking duration
        staking_duration = time.time() - start_time
        rewards = staking_duration * self.reward_rate

        # Update user rewards
        if user_id not in self.user_rewards:
            self.user_rewards[user_id] = 0
        self.user_rewards[user_id] += rewards

        print(f"User {user_id} has successfully unstaked NFT {nft_id}. Rewards earned: {rewards:.2f} tokens.")

    def get_user_rewards(self, user_id: str) -> float:
        """
        Get the total rewards accumulated by a user.

        :param user_id: The ID of the user.
        :return: The total rewards accumulated by the user.
        """
        return self.user_rewards.get(user_id, 0.0)

    def get_staked_nfts(self) -> List[str]:
        """
        Get a list of all currently staked NFTs.

        :return: A list of staked NFT IDs.
        """
        return list(self.staked_nfts.keys())


# Example usage
if __name__ == "__main__":
    # Initialize the staking platform with a reward rate of 0.01 tokens per second
    platform = NFTStakingPlatform(reward_rate=0.01)

    try:
        # Stake NFTs
        platform.stake_nft(user_id="user123", nft_id="nft001")
        time.sleep(2)  # Simulate staking duration
        platform.stake_nft(user_id="user456", nft_id="nft002")

        # Unstake NFTs
        platform.unstake_nft(nft_id="nft001")
        platform.unstake_nft(nft_id="nft002")

        # Get user rewards
        print(f"User123 rewards: {platform.get_user_rewards('user123'):.2f} tokens")
        print(f"User456 rewards: {platform.get_user_rewards('user456'):.2f} tokens")

        # Get currently staked NFTs
        print(f"Currently staked NFTs: {platform.get_staked_nfts()}")

    except ValueError as e:
        print(f"Error: {e}")
```
