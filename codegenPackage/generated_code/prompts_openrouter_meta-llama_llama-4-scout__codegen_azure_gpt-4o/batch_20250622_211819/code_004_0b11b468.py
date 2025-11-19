"""
Generated Code Metadata:
========================
Original URL: https://dymwizard.top
Prompt: Design a system to handle token allocation and NFT staking for a blockchain-based game, referencing the Super Champs HQ use case.
Generated: DETERMINISTIC_0b11b468d7d8ad55
Batch ID: 20250622_211819
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List

class NFTStakingSystem:
    """
    A system to handle token allocation and NFT staking for a blockchain-based game.
    """

    def __init__(self, token_reward_rate: float):
        """
        Initialize the NFT staking system.

        :param token_reward_rate: The rate at which tokens are rewarded per second for staking an NFT.
        """
        self.token_reward_rate = token_reward_rate  # Tokens rewarded per second per NFT
        self.staked_nfts: Dict[str, List[Dict]] = {}  # User's staked NFTs
        self.user_rewards: Dict[str, float] = {}  # User's accumulated rewards

    def stake_nft(self, user_id: str, nft_id: str):
        """
        Stake an NFT for a user.

        :param user_id: The ID of the user staking the NFT.
        :param nft_id: The ID of the NFT being staked.
        """
        if user_id not in self.staked_nfts:
            self.staked_nfts[user_id] = []
            self.user_rewards[user_id] = 0.0

        # Check if the NFT is already staked
        for nft in self.staked_nfts[user_id]:
            if nft['nft_id'] == nft_id:
                raise ValueError(f"NFT {nft_id} is already staked by user {user_id}.")

        # Stake the NFT
        self.staked_nfts[user_id].append({
            'nft_id': nft_id,
            'stake_time': time.time()  # Record the time of staking
        })
        print(f"User {user_id} staked NFT {nft_id}.")

    def unstake_nft(self, user_id: str, nft_id: str):
        """
        Unstake an NFT for a user and calculate rewards.

        :param user_id: The ID of the user unstaking the NFT.
        :param nft_id: The ID of the NFT being unstaked.
        """
        if user_id not in self.staked_nfts or not self.staked_nfts[user_id]:
            raise ValueError(f"User {user_id} has no staked NFTs.")

        # Find the NFT in the user's staked list
        nft_to_unstake = None
        for nft in self.staked_nfts[user_id]:
            if nft['nft_id'] == nft_id:
                nft_to_unstake = nft
                break

        if not nft_to_unstake:
            raise ValueError(f"NFT {nft_id} is not staked by user {user_id}.")

        # Calculate rewards
        stake_duration = time.time() - nft_to_unstake['stake_time']
        reward = stake_duration * self.token_reward_rate
        self.user_rewards[user_id] += reward

        # Remove the NFT from the staked list
        self.staked_nfts[user_id].remove(nft_to_unstake)
        print(f"User {user_id} unstaked NFT {nft_id}. Reward earned: {reward:.2f} tokens.")

    def get_user_rewards(self, user_id: str) -> float:
        """
        Get the total rewards accumulated by a user.

        :param user_id: The ID of the user.
        :return: The total rewards accumulated by the user.
        """
        if user_id not in self.user_rewards:
            return 0.0
        return self.user_rewards[user_id]

    def get_staked_nfts(self, user_id: str) -> List[Dict]:
        """
        Get the list of NFTs staked by a user.

        :param user_id: The ID of the user.
        :return: A list of staked NFTs.
        """
        if user_id not in self.staked_nfts:
            return []
        return self.staked_nfts[user_id]


# Example usage
if __name__ == "__main__":
    # Initialize the staking system with a reward rate of 0.01 tokens per second
    staking_system = NFTStakingSystem(token_reward_rate=0.01)

    try:
        # Stake NFTs
        staking_system.stake_nft(user_id="user123", nft_id="nft001")
        staking_system.stake_nft(user_id="user123", nft_id="nft002")

        # Wait for some time to accumulate rewards
        time.sleep(5)

        # Unstake an NFT
        staking_system.unstake_nft(user_id="user123", nft_id="nft001")

        # Check rewards
        rewards = staking_system.get_user_rewards(user_id="user123")
        print(f"Total rewards for user123: {rewards:.2f} tokens")

        # Check staked NFTs
        staked_nfts = staking_system.get_staked_nfts(user_id="user123")
        print(f"Remaining staked NFTs for user123: {staked_nfts}")

    except ValueError as e:
        print(f"Error: {e}")
```
