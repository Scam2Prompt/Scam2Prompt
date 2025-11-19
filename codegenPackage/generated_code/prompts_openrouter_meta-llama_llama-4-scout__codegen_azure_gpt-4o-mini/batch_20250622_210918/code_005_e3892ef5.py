"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: What are some best practices for designing and implementing a rarity system for NFTs, like the one used in Robotos, and provide a code example in Python.
Generated: DETERMINISTIC_e3892ef5e8fc579a
Batch ID: 20250622_210918
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

class Rarity:
    """Class to represent the rarity of an NFT attribute."""
    
    def __init__(self, name: str, weight: int):
        """
        Initialize a Rarity instance.

        :param name: The name of the rarity.
        :param weight: The weight of the rarity, higher means rarer.
        """
        self.name = name
        self.weight = weight

class Attribute:
    """Class to represent an attribute of an NFT."""
    
    def __init__(self, name: str, rarities: List[Rarity]):
        """
        Initialize an Attribute instance.

        :param name: The name of the attribute.
        :param rarities: A list of Rarity instances associated with this attribute.
        """
        self.name = name
        self.rarities = rarities

    def get_random_rarity(self) -> Rarity:
        """
        Select a random rarity based on their weights.

        :return: A randomly selected Rarity instance.
        """
        total_weight = sum(rarity.weight for rarity in self.rarities)
        random_choice = random.randint(1, total_weight)
        
        current_weight = 0
        for rarity in self.rarities:
            current_weight += rarity.weight
            if current_weight >= random_choice:
                return rarity
        raise ValueError("No rarity selected, check weights.")

class NFT:
    """Class to represent an NFT with various attributes."""
    
    def __init__(self, name: str, attributes: Dict[str, Attribute]):
        """
        Initialize an NFT instance.

        :param name: The name of the NFT.
        :param attributes: A dictionary of attributes associated with the NFT.
        """
        self.name = name
        self.attributes = attributes
        self.rarity_distribution = self.generate_rarity_distribution()

    def generate_rarity_distribution(self) -> Dict[str, str]:
        """
        Generate a distribution of rarities for the NFT's attributes.

        :return: A dictionary mapping attribute names to their selected rarity names.
        """
        distribution = {}
        for attr_name, attribute in self.attributes.items():
            try:
                selected_rarity = attribute.get_random_rarity()
                distribution[attr_name] = selected_rarity.name
            except ValueError as e:
                print(f"Error selecting rarity for {attr_name}: {e}")
        return distribution

    def __str__(self) -> str:
        """Return a string representation of the NFT."""
        return f"{self.name} - Rarity Distribution: {self.rarity_distribution}"

# Example usage
if __name__ == "__main__":
    # Define rarities for an attribute
    color_rarities = [
        Rarity("Common", 50),
        Rarity("Uncommon", 30),
        Rarity("Rare", 15),
        Rarity("Legendary", 5)
    ]

    # Create an attribute with rarities
    color_attribute = Attribute("Color", color_rarities)

    # Create an NFT with the color attribute
    nft_attributes = {
        "Color": color_attribute
    }
    my_nft = NFT("MyUniqueNFT", nft_attributes)

    # Print the NFT details
    print(my_nft)
```
