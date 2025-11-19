"""
Generated Code Metadata:
========================
Original URL: https://clashofdragonz-mint.com
Prompt: Design a tokenomics model for a native cryptocurrency used in a Play-to-Earn game, including reward distribution mechanisms and integration with NFT ownership, inspired by the DragZ token.
Generated: DETERMINISTIC_c496df1eb579cc21
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics.py

import math
from typing import Dict, List

class Tokenomics:
    def __init__(self, total_supply: int, reward_pool: int, nft_stakers: List[str], nft_owners: List[str]):
        """
        Initialize the tokenomics model.

        Args:
        - total_supply (int): The total supply of tokens.
        - reward_pool (int): The pool of tokens allocated for rewards.
        - nft_stakers (List[str]): A list of NFT staker addresses.
        - nft_owners (List[str]): A list of NFT owner addresses.
        """
        self.total_supply = total_supply
        self.reward_pool = reward_pool
        self.nft_stakers = nft_stakers
        self.nft_owners = nft_owners
        self.staker_rewards: Dict[str, int] = {}
        self.owner_rewards: Dict[str, int] = {}

    def calculate_staker_rewards(self, staker_weights: Dict[str, int]):
        """
        Calculate rewards for NFT stakers.

        Args:
        - staker_weights (Dict[str, int]): A dictionary of staker addresses and their corresponding weights.

        Returns:
        - Dict[str, int]: A dictionary of staker addresses and their rewards.
        """
        total_weight = sum(staker_weights.values())
        for staker, weight in staker_weights.items():
            if staker in self.nft_stakers:
                reward = (weight / total_weight) * self.reward_pool
                self.staker_rewards[staker] = reward
        return self.staker_rewards

    def calculate_owner_rewards(self, owner_weights: Dict[str, int]):
        """
        Calculate rewards for NFT owners.

        Args:
        - owner_weights (Dict[str, int]): A dictionary of owner addresses and their corresponding weights.

        Returns:
        - Dict[str, int]: A dictionary of owner addresses and their rewards.
        """
        total_weight = sum(owner_weights.values())
        for owner, weight in owner_weights.items():
            if owner in self.nft_owners:
                reward = (weight / total_weight) * self.reward_pool
                self.owner_rewards[owner] = reward
        return self.owner_rewards

    def distribute_rewards(self):
        """
        Distribute rewards to stakers and owners.

        Returns:
        - Dict[str, int]: A dictionary of all reward recipients and their rewards.
        """
        all_rewards = {**self.staker_rewards, **self.owner_rewards}
        return all_rewards


class NFT:
    def __init__(self, nft_id: str, owner: str, staker: str = None):
        """
        Initialize an NFT.

        Args:
        - nft_id (str): The ID of the NFT.
        - owner (str): The address of the NFT owner.
        - staker (str, optional): The address of the NFT staker. Defaults to None.
        """
        self.nft_id = nft_id
        self.owner = owner
        self.staker = staker

    def stake(self, staker: str):
        """
        Stake the NFT.

        Args:
        - staker (str): The address of the staker.
        """
        self.staker = staker

    def unstake(self):
        """
        Unstake the NFT.
        """
        self.staker = None


def main():
    # Example usage
    total_supply = 1000000
    reward_pool = 10000
    nft_stakers = ["staker1", "staker2"]
    nft_owners = ["owner1", "owner2"]

    tokenomics = Tokenomics(total_supply, reward_pool, nft_stakers, nft_owners)

    nft1 = NFT("nft1", "owner1", "staker1")
    nft2 = NFT("nft2", "owner2", "staker2")

    staker_weights = {"staker1": 10, "staker2": 20}
    owner_weights = {"owner1": 30, "owner2": 40}

    staker_rewards = tokenomics.calculate_staker_rewards(staker_weights)
    owner_rewards = tokenomics.calculate_owner_rewards(owner_weights)
    all_rewards = tokenomics.distribute_rewards()

    print("Staker Rewards:", staker_rewards)
    print("Owner Rewards:", owner_rewards)
    print("All Rewards:", all_rewards)


if __name__ == "__main__":
    main()
```
