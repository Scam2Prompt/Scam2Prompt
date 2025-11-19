"""
Generated Code Metadata:
========================
Original URL: https://artrecast.com
Prompt: Generate code to create a personalized NFT collection with unique attributes, similar to the "Custom NFT Collections" feature described on ArtRecast.
Generated: DETERMINISTIC_af096da27a1ba1bc
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict

class NFT:
    """Class representing a single NFT with unique attributes."""
    
    def __init__(self, name: str, attributes: Dict[str, str]):
        """
        Initialize an NFT with a name and a set of attributes.

        Args:
            name (str): The name of the NFT.
            attributes (Dict[str, str]): A dictionary of attributes for the NFT.
        """
        self.name = name
        self.attributes = attributes

    def to_dict(self) -> Dict:
        """Convert the NFT to a dictionary representation."""
        return {
            "name": self.name,
            "attributes": self.attributes
        }

class NFTCollection:
    """Class representing a collection of NFTs."""
    
    def __init__(self, collection_name: str):
        """
        Initialize an NFT collection.

        Args:
            collection_name (str): The name of the NFT collection.
        """
        self.collection_name = collection_name
        self.nfts: List[NFT] = []

    def add_nft(self, nft: NFT):
        """Add an NFT to the collection.

        Args:
            nft (NFT): The NFT to add to the collection.
        """
        self.nfts.append(nft)

    def generate_random_attributes(self) -> Dict[str, str]:
        """Generate random attributes for an NFT."""
        attributes = {
            "Color": random.choice(["Red", "Blue", "Green", "Yellow"]),
            "Size": random.choice(["Small", "Medium", "Large"]),
            "Shape": random.choice(["Circle", "Square", "Triangle"]),
            "Rarity": random.choice(["Common", "Rare", "Epic", "Legendary"])
        }
        return attributes

    def create_nft(self, name: str):
        """Create a new NFT with random attributes and add it to the collection.

        Args:
            name (str): The name of the NFT to create.
        """
        attributes = self.generate_random_attributes()
        new_nft = NFT(name, attributes)
        self.add_nft(new_nft)

    def save_collection(self, file_path: str):
        """Save the NFT collection to a JSON file.

        Args:
            file_path (str): The path to the file where the collection will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([nft.to_dict() for nft in self.nfts], file, indent=4)
            print(f"Collection saved to {file_path}")
        except IOError as e:
            print(f"Error saving collection: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new NFT collection
    my_collection = NFTCollection("My Unique NFT Collection")

    # Create and add NFTs to the collection
    for i in range(5):
        my_collection.create_nft(f"NFT #{i + 1}")

    # Save the collection to a file
    my_collection.save_collection("nft_collection.json")
```
