"""
Generated Code Metadata:
========================
Original URL: https://ejelly.web.app
Prompt: What are the best practices for creating a rarity system for NFTs like the 1/1 Jelly Drop mentioned on ejelly.web.app?
Generated: DETERMINISTIC_83f751daeeab28cf
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class NFT:
    """
    A class to represent a Non-Fungible Token (NFT) with rarity attributes.
    """

    def __init__(self, name: str, rarity: str):
        """
        Initializes an NFT instance.

        :param name: The name of the NFT.
        :param rarity: The rarity level of the NFT (e.g., 'common', 'rare', 'epic', 'legendary').
        """
        self.name = name
        self.rarity = rarity

    def __repr__(self) -> str:
        return f"{self.name} ({self.rarity})"


class RaritySystem:
    """
    A class to manage the rarity system for NFTs.
    """

    def __init__(self):
        """
        Initializes the RaritySystem with predefined rarity levels and their probabilities.
        """
        self.rarity_levels: Dict[str, float] = {
            'common': 0.5,
            'rare': 0.3,
            'epic': 0.15,
            'legendary': 0.05
        }

    def generate_nft(self, name: str) -> NFT:
        """
        Generates an NFT with a random rarity based on predefined probabilities.

        :param name: The name of the NFT to be created.
        :return: An NFT instance with a randomly assigned rarity.
        """
        rarity = self._assign_rarity()
        return NFT(name, rarity)

    def _assign_rarity(self) -> str:
        """
        Assigns a rarity level to an NFT based on predefined probabilities.

        :return: A string representing the rarity level.
        """
        rand_value = random.random()
        cumulative_probability = 0.0

        for rarity, probability in self.rarity_levels.items():
            cumulative_probability += probability
            if rand_value < cumulative_probability:
                return rarity

        # Fallback in case of unexpected behavior
        return 'common'

    def create_nfts(self, names: List[str]) -> List[NFT]:
        """
        Creates a list of NFTs with random rarities.

        :param names: A list of names for the NFTs to be created.
        :return: A list of NFT instances.
        """
        nfts = []
        for name in names:
            try:
                nft = self.generate_nft(name)
                nfts.append(nft)
            except Exception as e:
                print(f"Error creating NFT '{name}': {e}")
        return nfts


# Example usage
if __name__ == "__main__":
    rarity_system = RaritySystem()
    nft_names = ["Jelly Drop 1", "Jelly Drop 2", "Jelly Drop 3"]
    nfts = rarity_system.create_nfts(nft_names)

    for nft in nfts:
        print(nft)
```
