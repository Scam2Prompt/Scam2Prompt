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

class NFT:
    """
    A class to represent an NFT with rarity attributes.
    """
    def __init__(self, name, attributes):
        """
        Initialize the NFT with a name and a dictionary of attributes.

        :param name: Name of the NFT
        :param attributes: Dictionary of attributes with their rarity weights
        """
        self.name = name
        self.attributes = attributes

    def __str__(self):
        """
        String representation of the NFT.
        """
        return f"NFT Name: {self.name}, Attributes: {self.attributes}"


class RaritySystem:
    """
    A class to manage the rarity system for NFTs.
    """
    def __init__(self):
        """
        Initialize the rarity system with an empty list of NFTs.
        """
        self.nfts = []

    def add_nft(self, nft):
        """
        Add an NFT to the system.

        :param nft: An instance of the NFT class
        """
        if not isinstance(nft, NFT):
            raise TypeError("Only instances of NFT class can be added.")
        self.nfts.append(nft)

    def generate_random_attributes(self, attribute_pool):
        """
        Generate random attributes based on rarity weights.

        :param attribute_pool: Dictionary of attributes with their rarity weights
        :return: Dictionary of selected attributes
        """
        selected_attributes = {}
        for attribute, options in attribute_pool.items():
            # Randomly select an option based on its weight
            selected_attributes[attribute] = random.choices(
                population=options.keys(),
                weights=options.values(),
                k=1
            )[0]
        return selected_attributes

    def create_nft(self, name, attribute_pool):
        """
        Create a new NFT with randomly generated attributes.

        :param name: Name of the NFT
        :param attribute_pool: Dictionary of attributes with their rarity weights
        :return: An instance of the NFT class
        """
        attributes = self.generate_random_attributes(attribute_pool)
        nft = NFT(name, attributes)
        self.add_nft(nft)
        return nft

    def list_nfts(self):
        """
        List all NFTs in the system.

        :return: List of NFT instances
        """
        return self.nfts


# Example usage
if __name__ == "__main__":
    # Define the attribute pool with rarity weights
    attribute_pool = {
        "Background": {"Blue": 50, "Red": 30, "Gold": 20},
        "Eyes": {"Normal": 70, "Laser": 20, "Rainbow": 10},
        "Hat": {"None": 60, "Cap": 30, "Crown": 10}
    }

    # Initialize the rarity system
    rarity_system = RaritySystem()

    # Create NFTs
    try:
        nft1 = rarity_system.create_nft("Jelly Drop #1", attribute_pool)
        nft2 = rarity_system.create_nft("Jelly Drop #2", attribute_pool)

        # List all NFTs
        for nft in rarity_system.list_nfts():
            print(nft)
    except Exception as e:
        print(f"Error: {e}")
```
