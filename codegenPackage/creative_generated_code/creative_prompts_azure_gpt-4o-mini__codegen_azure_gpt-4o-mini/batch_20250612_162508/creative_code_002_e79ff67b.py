"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydrop.web.app
Prompt: What are the best practices for developing a rarity system for NFTs, as seen in the Jelly Drop project?
Generated: DETERMINISTIC_e79ff67b3b7be7cb
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class NFT:
    """Class to represent an NFT with a unique ID and its rarity level."""
    
    def __init__(self, nft_id: int, rarity: str) -> None:
        self.nft_id = nft_id
        self.rarity = rarity

    def __repr__(self) -> str:
        return f"NFT(ID: {self.nft_id}, Rarity: {self.rarity})"


class RaritySystem:
    """Class to manage the rarity assignment for NFTs."""

    def __init__(self, rarities: List[str], rarity_weights: List[int]) -> None:
        """
        Initializes the rarity system with defined rarity types and their weights.

        :param rarities: List of rarity types (e.g., 'Common', 'Rare', 'Epic', 'Legendary').
        :param rarity_weights: Corresponding weights for each rarity type.
        """
        if len(rarities) != len(rarity_weights):
            raise ValueError("Rarities and weights must have the same length.")

        self.rarities = rarities
        self.rarity_weights = rarity_weights
        self.total_weight = sum(rarity_weights)

    def _select_rarity(self) -> str:
        """Selects a rarity based on the defined weights."""
        random_value = random.randint(1, self.total_weight)
        cumulative_weight = 0
        
        for rarity, weight in zip(self.rarities, self.rarity_weights):
            cumulative_weight += weight
            if random_value <= cumulative_weight:
                return rarity
        
        raise Exception("Rarity selection failed, check weights configuration.")

    def generate_nfts(self, count: int) -> List[NFT]:
        """
        Generates a specified number of NFTs with randomly assigned rarities.

        :param count: The number of NFTs to generate.
        :return: A list of NFTs with assigned rarities.
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        
        nfts = []
        for nft_id in range(1, count + 1):
            rarity = self._select_rarity()
            nfts.append(NFT(nft_id, rarity))
        
        return nfts


# Example usage
if __name__ == "__main__":
    # Define rarities and their corresponding weights
    rarities = ['Common', 'Rare', 'Epic', 'Legendary']
    rarity_weights = [70, 20, 9, 1]  # Total weight = 100

    try:
        rarity_system = RaritySystem(rarities, rarity_weights)
        generated_nfts = rarity_system.generate_nfts(10)  # Generate 10 NFTs
        print(generated_nfts)
    except Exception as e:
        print(f"Error: {e}")
```
