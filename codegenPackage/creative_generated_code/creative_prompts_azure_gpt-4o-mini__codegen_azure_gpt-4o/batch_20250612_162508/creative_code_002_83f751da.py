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

class RaritySystem:
    """
    A class to handle the creation of rarity systems for NFTs.
    """

    def __init__(self):
        """
        Initialize the RaritySystem with predefined rarity tiers and their probabilities.
        """
        # Define rarity tiers and their probabilities (percentages)
        self.rarity_tiers = {
            "Common": 50.0,       # 50% chance
            "Uncommon": 30.0,    # 30% chance
            "Rare": 15.0,        # 15% chance
            "Epic": 4.0,         # 4% chance
            "Legendary": 1.0     # 1% chance
        }
        self.validate_probabilities()

    def validate_probabilities(self):
        """
        Validates that the sum of the probabilities is 100% to ensure the rarity system is properly configured.
        """
        total_probability = sum(self.rarity_tiers.values())
        if not abs(total_probability - 100.0) < 1e-6:
            raise ValueError("Total probabilities must equal 100%. Current sum: {}".format(total_probability))

    def assign_rarity(self):
        """
        Assigns a rarity tier to an NFT instance based on the configured probabilities.

        Returns:
            str: The assigned rarity tier.
        """
        # Create a weighted choice based on the rarity tiers
        tiers = list(self.rarity_tiers.keys())
        weights = list(self.rarity_tiers.values())
        return random.choices(tiers, weights=weights, k=1)[0]

    def generate_nfts(self, count):
        """
        Generates a specified number of NFTs with assigned rarity tiers.

        Args:
            count (int): The number of NFTs to generate.

        Returns:
            list: A list of dictionaries with NFT rarity data.
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        
        nft_collection = []
        for _ in range(count):
            nft_id = len(nft_collection) + 1  # Simple sequential ID
            rarity = self.assign_rarity()
            nft_collection.append({"id": nft_id, "rarity": rarity})
        return nft_collection


if __name__ == "__main__":
    # Example usage of the RaritySystem class
    try:
        rarity_system = RaritySystem()

        # Generate a collection of 10 NFTs
        nft_collection = rarity_system.generate_nfts(10)

        # Print the generated NFTs and their assigned rarities
        for nft in nft_collection:
            print(f"NFT ID: {nft['id']}, Rarity: {nft['rarity']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
