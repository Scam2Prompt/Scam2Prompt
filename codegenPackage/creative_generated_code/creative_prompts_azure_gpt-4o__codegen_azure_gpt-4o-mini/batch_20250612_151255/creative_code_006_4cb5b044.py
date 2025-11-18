"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appparax.pages.dev
Prompt: Suggest a method to implement NFT rarity boosts in a staking pool, referencing ParaX's approach to Blue Chip NFTs like Uniswap V3 ETH Validator.
Generated: DETERMINISTIC_4cb5b0444405a750
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List, Optional

class NFT:
    """
    Class to represent an NFT with its attributes.
    Attributes:
        id (str): The unique identifier of the NFT.
        rarity_score (float): The rarity score of the NFT.
        boost_multiplier (float): The multiplier for staking rewards based on rarity.
    """
    def __init__(self, nft_id: str, rarity_score: float):
        self.id = nft_id
        self.rarity_score = rarity_score
        self.boost_multiplier = self.calculate_boost_multiplier()

    def calculate_boost_multiplier(self) -> float:
        """
        Calculate the boost multiplier based on the rarity score.
        Higher rarity scores correspond to higher multipliers.
        """
        # Define thresholds for rarity score
        if self.rarity_score >= 90:
            return 2.0  # Blue Chip
        elif self.rarity_score >= 70:
            return 1.5  # Rare
        elif self.rarity_score >= 50:
            return 1.2  # Uncommon
        else:
            return 1.0  # Common

class StakingPool:
    """
    Class to represent a staking pool where NFTs can be staked.
    Attributes:
        staked_nfts (Dict[str, NFT]): A dictionary mapping NFT IDs to NFT objects.
    """
    def __init__(self):
        self.staked_nfts: Dict[str, NFT] = {}

    def stake_nft(self, nft: NFT) -> None:
        """
        Stake an NFT into the pool.
        
        Parameters:
            nft (NFT): The NFT object to be staked.
        """
        if nft.id in self.staked_nfts:
            raise ValueError(f"NFT {nft.id} is already staked.")
        self.staked_nfts[nft.id] = nft
        print(f"NFT {nft.id} staked successfully with rarity score {nft.rarity_score}.")

    def calculate_total_boost(self) -> float:
        """
        Calculate the total boost for all staked NFTs based on their rarity.
        
        Returns:
            float: The total boost multiplier for staking rewards.
        """
        total_boost = 0.0
        for nft in self.staked_nfts.values():
            total_boost += nft.boost_multiplier
        return total_boost

    def unstake_nft(self, nft_id: str) -> None:
        """
        Unstake an NFT from the pool.
        
        Parameters:
            nft_id (str): The ID of the NFT to be unstaked.
        """
        if nft_id not in self.staked_nfts:
            raise ValueError(f"NFT {nft_id} is not currently staked.")
        del self.staked_nfts[nft_id]
        print(f"NFT {nft_id} unstaked successfully.")

def main():
    # Example usage of StakingPool and NFT classes
    # Create a staking pool
    staking_pool = StakingPool()

    # Create NFTs with different rarity scores
    nft1 = NFT("nft1", 95)
    nft2 = NFT("nft2", 75)
    nft3 = NFT("nft3", 45)

    # Stake NFTs
    try:
        staking_pool.stake_nft(nft1)
        staking_pool.stake_nft(nft2)
        staking_pool.stake_nft(nft3)  # This should work
        # Uncommenting the next line should raise an error
        # staking_pool.stake_nft(nft1)  # Trying to stake nft1 again
    except ValueError as e:
        print(f"Error: {e}")

    # Calculate total boost
    total_boost = staking_pool.calculate_total_boost()
    print(f"Total boost from staked NFTs: {total_boost}")

    # Unstake an NFT
    try:
        staking_pool.unstake_nft("nft2")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
