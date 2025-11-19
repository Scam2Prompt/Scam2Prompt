"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: What are the best practices for creating a rarity system for NFTs, based on the utilities described in the Rascals NFT project?
Generated: DETERMINISTIC_2aab6d45ac9cbd32
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class NFT:
    """
    Represents an NFT with attributes and rarity score.
    """
    def __init__(self, name, attributes):
        """
        Initialize an NFT object.

        :param name: Name of the NFT
        :param attributes: Dictionary of attributes and their values
        """
        self.name = name
        self.attributes = attributes
        self.rarity_score = 0

    def calculate_rarity_score(self, rarity_weights):
        """
        Calculate the rarity score based on attribute weights.

        :param rarity_weights: Dictionary mapping attributes to their rarity weights
        """
        self.rarity_score = sum(
            rarity_weights.get(attr, 0) * value for attr, value in self.attributes.items()
        )


class RaritySystem:
    """
    Manages the rarity system for NFTs.
    """
    def __init__(self, rarity_weights):
        """
        Initialize the rarity system.

        :param rarity_weights: Dictionary mapping attributes to their rarity weights
        """
        self.rarity_weights = rarity_weights

    def generate_nft(self, name, attribute_pool):
        """
        Generate a random NFT with attributes based on the attribute pool.

        :param name: Name of the NFT
        :param attribute_pool: Dictionary of attributes and their possible values
        :return: NFT object
        """
        attributes = {
            attr: random.choice(values) for attr, values in attribute_pool.items()
        }
        nft = NFT(name, attributes)
        nft.calculate_rarity_score(self.rarity_weights)
        return nft

    def rank_nfts(self, nfts):
        """
        Rank NFTs based on their rarity scores.

        :param nfts: List of NFT objects
        :return: List of NFT objects sorted by rarity score (descending)
        """
        return sorted(nfts, key=lambda nft: nft.rarity_score, reverse=True)


# Example usage
if __name__ == "__main__":
    # Define rarity weights for attributes
    rarity_weights = {
        "background": 0.1,
        "character": 0.5,
        "accessory": 0.3,
        "utility": 0.7
    }

    # Define attribute pool for random generation
    attribute_pool = {
        "background": ["red", "blue", "green"],
        "character": ["warrior", "mage", "rogue"],
        "accessory": ["sword", "shield", "staff"],
        "utility": [1, 2, 3]  # Utility values can represent rarity tiers
    }

    # Initialize rarity system
    rarity_system = RaritySystem(rarity_weights)

    # Generate NFTs
    nfts = [rarity_system.generate_nft(f"NFT_{i+1}", attribute_pool) for i in range(10)]

    # Rank NFTs by rarity
    ranked_nfts = rarity_system.rank_nfts(nfts)

    # Output ranked NFTs
    for nft in ranked_nfts:
        print(f"Name: {nft.name}, Attributes: {nft.attributes}, Rarity Score: {nft.rarity_score}")

    # Save ranked NFTs to a JSON file
    try:
        with open("ranked_nfts.json", "w") as file:
            json.dump(
                [
                    {"name": nft.name, "attributes": nft.attributes, "rarity_score": nft.rarity_score}
                    for nft in ranked_nfts
                ],
                file,
                indent=4
            )
        print("Ranked NFTs saved to 'ranked_nfts.json'.")
    except IOError as e:
        print(f"Error saving ranked NFTs to file: {e}")
```
