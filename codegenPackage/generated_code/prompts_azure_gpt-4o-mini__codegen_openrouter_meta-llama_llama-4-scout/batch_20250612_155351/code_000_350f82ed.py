"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: How can I implement a staking mechanism for NFTs similar to the Jelly Staking feature on the Rascals NFT website?
Generated: DETERMINISTIC_350f82edd24ec790
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_mechanism.py

from datetime import datetime, timedelta
from typing import Dict, List

class NFT:
    def __init__(self, id: int, name: str, owner: str):
        """
        Initialize an NFT object.

        Args:
        id (int): Unique identifier for the NFT.
        name (str): Name of the NFT.
        owner (str): Owner of the NFT.
        """
        self.id = id
        self.name = name
        self.owner = owner

class StakingMechanism:
    def __init__(self):
        """
        Initialize the staking mechanism.
        """
        self.staked_nfts: Dict[int, datetime] = {}  # Map of staked NFTs to their stake dates
        self.unstake_penalty: timedelta = timedelta(days=7)  # Penalty period for unstaking
        self.stake_rewards: Dict[int, int] = {}  # Map of staked NFTs to their rewards

    def stake_nft(self, nft: NFT, stake_duration: timedelta):
        """
        Stake an NFT.

        Args:
        nft (NFT): The NFT to stake.
        stake_duration (timedelta): The duration to stake the NFT for.

        Raises:
        ValueError: If the NFT is already staked.
        """
        if nft.id in self.staked_nfts:
            raise ValueError("NFT is already staked")

        self.staked_nfts[nft.id] = datetime.now() + stake_duration
        self.stake_rewards[nft.id] = 0  # Initialize reward to 0

    def unstake_nft(self, nft_id: int):
        """
        Unstake an NFT.

        Args:
        nft_id (int): The ID of the NFT to unstake.

        Raises:
        ValueError: If the NFT is not staked.
        """
        if nft_id not in self.staked_nfts:
            raise ValueError("NFT is not staked")

        stake_date = self.staked_nfts[nft_id]
        if datetime.now() < stake_date:
            # Apply penalty for unstaking before stake duration
            print(f"Penalty applied for unstaking NFT {nft_id} early")
        else:
            # Reward NFT owner
            reward = self.calculate_reward(nft_id)
            self.stake_rewards[nft_id] = reward
            print(f"NFT {nft_id} owner rewarded with {reward}")

        del self.staked_nfts[nft_id]

    def calculate_reward(self, nft_id: int) -> int:
        """
        Calculate the reward for an NFT.

        Args:
        nft_id (int): The ID of the NFT.

        Returns:
        int: The reward amount.
        """
        # Implement reward calculation logic here
        return 100

    def get_staked_nfts(self) -> List[NFT]:
        """
        Get a list of staked NFTs.

        Returns:
        List[NFT]: A list of staked NFTs.
        """
        # For demonstration purposes, assume NFT objects are stored elsewhere
        nfts = [NFT(1, "NFT 1", "Owner 1"), NFT(2, "NFT 2", "Owner 2")]
        staked_nfts = []
        for nft in nfts:
            if nft.id in self.staked_nfts:
                staked_nfts.append(nft)
        return staked_nfts

def main():
    staking_mechanism = StakingMechanism()
    nft1 = NFT(1, "NFT 1", "Owner 1")
    nft2 = NFT(2, "NFT 2", "Owner 2")

    staking_mechanism.stake_nft(nft1, timedelta(days=30))
    staking_mechanism.stake_nft(nft2, timedelta(days=60))

    print("Staked NFTs:")
    for nft in staking_mechanism.get_staked_nfts():
        print(f"ID: {nft.id}, Name: {nft.name}, Owner: {nft.owner}")

    staking_mechanism.unstake_nft(nft1.id)

if __name__ == "__main__":
    main()
```
