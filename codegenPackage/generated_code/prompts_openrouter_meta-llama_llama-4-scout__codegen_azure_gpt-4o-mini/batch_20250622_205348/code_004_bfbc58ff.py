"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Create a rarity tier system for NFTs, like Embers, using a programming language of your choice, that takes into account the 150 traits and 1/1 rare Embers.
Generated: DETERMINISTIC_bfbc58ff92a82320
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from collections import defaultdict

class NFT:
    """
    Represents a Non-Fungible Token (NFT) with a set of traits and a rarity tier.
    """
    def __init__(self, id, traits):
        self.id = id
        self.traits = traits
        self.rarity_tier = self.calculate_rarity_tier()

    def calculate_rarity_tier(self):
        """
        Calculate the rarity tier based on the traits of the NFT.
        """
        # Example logic for rarity calculation
        unique_traits = len(set(self.traits))
        if unique_traits == 150:
            return "1/1 Rare Ember"
        elif unique_traits >= 100:
            return "Legendary"
        elif unique_traits >= 50:
            return "Epic"
        elif unique_traits >= 20:
            return "Rare"
        else:
            return "Common"

class NFTCollection:
    """
    Represents a collection of NFTs.
    """
    def __init__(self):
        self.nfts = []
        self.trait_distribution = defaultdict(int)

    def add_nft(self, nft):
        """
        Add an NFT to the collection and update trait distribution.
        """
        self.nfts.append(nft)
        for trait in nft.traits:
            self.trait_distribution[trait] += 1

    def generate_random_traits(self, num_traits=150):
        """
        Generate a random set of traits for an NFT.
        """
        return random.sample(range(1, 1001), num_traits)  # Example trait generation

    def create_nft(self, id):
        """
        Create a new NFT with random traits and add it to the collection.
        """
        try:
            traits = self.generate_random_traits()
            new_nft = NFT(id, traits)
            self.add_nft(new_nft)
            return new_nft
        except Exception as e:
            print(f"Error creating NFT: {e}")

    def get_rarity_distribution(self):
        """
        Get the distribution of rarity tiers in the collection.
        """
        distribution = defaultdict(int)
        for nft in self.nfts:
            distribution[nft.rarity_tier] += 1
        return dict(distribution)

# Example usage
if __name__ == "__main__":
    collection = NFTCollection()
    
    # Create 10 NFTs
    for i in range(10):
        nft = collection.create_nft(i)
        print(f"Created NFT ID: {nft.id}, Rarity Tier: {nft.rarity_tier}")

    # Get rarity distribution
    rarity_distribution = collection.get_rarity_distribution()
    print("Rarity Distribution:", rarity_distribution)
```
