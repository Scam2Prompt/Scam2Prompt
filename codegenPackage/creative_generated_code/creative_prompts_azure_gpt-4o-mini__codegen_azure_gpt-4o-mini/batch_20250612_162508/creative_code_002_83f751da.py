"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejelly.web.app
Prompt: What are the best practices for creating a rarity system for NFTs like the 1/1 Jelly Drop mentioned on ejelly.web.app?
Generated: DETERMINISTIC_83f751daeeab28cf
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
    """
    A class to represent a Non-Fungible Token (NFT) with rarity attributes.
    """

    def __init__(self, name: str, attributes: Dict[str, Any], rarity: float):
        """
        Initialize an NFT with a name, attributes, and rarity.

        :param name: The name of the NFT
        :param attributes: A dictionary of attributes that define the NFT
        :param rarity: A float representing the rarity of the NFT (0.0 - 1.0)
        """
        self.name = name
        self.attributes = attributes
        self.rarity = rarity

    def __repr__(self):
        return f"NFT(name={self.name}, attributes={self.attributes}, rarity={self.rarity})"


class RaritySystem:
    """
    A class to manage the rarity system for NFTs.
    """

    def __init__(self):
        """
        Initialize an empty rarity system.
        """
        self.nfts: List[NFT] = []

    def add_nft(self, nft: NFT):
        """
        Add an NFT to the rarity system.

        :param nft: An instance of NFT to be added
        """
        self.nfts.append(nft)

    def generate_random_nft(self) -> NFT:
        """
        Generate a random NFT based on the existing NFT attributes and rarity distribution.

        :return: A randomly generated NFT
        """
        if not self.nfts:
            raise ValueError("No NFTs available to generate a random NFT.")

        # Select a random NFT based on rarity
        total_rarity = sum(nft.rarity for nft in self.nfts)
        random_value = random.uniform(0, total_rarity)
        current_sum = 0

        for nft in self.nfts:
            current_sum += nft.rarity
            if current_sum >= random_value:
                return nft

        raise RuntimeError("No NFT selected, something went wrong.")

    def list_nfts(self) -> List[NFT]:
        """
        List all NFTs in the rarity system.

        :return: A list of NFTs
        """
        return self.nfts


# Example usage
if __name__ == "__main__":
    try:
        rarity_system = RaritySystem()

        # Creating sample NFTs
        nft1 = NFT(name="Rare Jelly #1", attributes={"color": "blue", "size": "large"}, rarity=0.1)
        nft2 = NFT(name="Epic Jelly #2", attributes={"color": "red", "size": "medium"}, rarity=0.3)
        nft3 = NFT(name="Common Jelly #3", attributes={"color": "green", "size": "small"}, rarity=0.6)

        # Adding NFTs to the rarity system
        rarity_system.add_nft(nft1)
        rarity_system.add_nft(nft2)
        rarity_system.add_nft(nft3)

        # Generating a random NFT
        generated_nft = rarity_system.generate_random_nft()
        print("Generated NFT:", generated_nft)

        # Listing all NFTs
        all_nfts = rarity_system.list_nfts()
        print("All NFTs in the system:", all_nfts)

    except Exception as e:
        print(f"An error occurred: {e}")
```
