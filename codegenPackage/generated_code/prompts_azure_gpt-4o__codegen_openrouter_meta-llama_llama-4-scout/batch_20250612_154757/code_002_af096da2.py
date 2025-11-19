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
# nft_collection.py

import json
import uuid
from typing import Dict, List

class NFT:
    def __init__(self, name: str, description: str, attributes: Dict[str, str]):
        """
        Initialize an NFT object.

        Args:
        - name (str): The name of the NFT.
        - description (str): A brief description of the NFT.
        - attributes (Dict[str, str]): A dictionary of unique attributes for the NFT.
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the NFT
        self.name = name
        self.description = description
        self.attributes = attributes

    def to_dict(self) -> Dict:
        """
        Convert the NFT object to a dictionary.

        Returns:
        - Dict: A dictionary representation of the NFT object.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "attributes": self.attributes
        }

class NFTCollection:
    def __init__(self, name: str, description: str):
        """
        Initialize an NFTCollection object.

        Args:
        - name (str): The name of the NFT collection.
        - description (str): A brief description of the NFT collection.
        """
        self.name = name
        self.description = description
        self.nfts = []  # List to store NFT objects

    def add_nft(self, nft: NFT):
        """
        Add an NFT to the collection.

        Args:
        - nft (NFT): The NFT object to add.
        """
        self.nfts.append(nft)

    def to_dict(self) -> Dict:
        """
        Convert the NFTCollection object to a dictionary.

        Returns:
        - Dict: A dictionary representation of the NFTCollection object.
        """
        return {
            "name": self.name,
            "description": self.description,
            "nfts": [nft.to_dict() for nft in self.nfts]
        }

def create_nft_collection(name: str, description: str, nft_data: List[Dict]) -> NFTCollection:
    """
    Create a personalized NFT collection with unique attributes.

    Args:
    - name (str): The name of the NFT collection.
    - description (str): A brief description of the NFT collection.
    - nft_data (List[Dict]): A list of dictionaries containing NFT data.

    Returns:
    - NFTCollection: An NFTCollection object.

    Raises:
    - ValueError: If nft_data is empty or not a list.
    """
    if not isinstance(nft_data, list) or len(nft_data) == 0:
        raise ValueError("NFT data must be a non-empty list")

    collection = NFTCollection(name, description)

    for data in nft_data:
        try:
            nft = NFT(data["name"], data["description"], data["attributes"])
            collection.add_nft(nft)
        except KeyError as e:
            print(f"Error creating NFT: {e}")

    return collection

def main():
    nft_data = [
        {
            "name": "NFT 1",
            "description": "This is NFT 1",
            "attributes": {
                "color": "red",
                "shape": "circle"
            }
        },
        {
            "name": "NFT 2",
            "description": "This is NFT 2",
            "attributes": {
                "color": "blue",
                "shape": "square"
            }
        }
    ]

    collection = create_nft_collection("My NFT Collection", "A personalized NFT collection", nft_data)

    # Save the collection to a JSON file
    with open("nft_collection.json", "w") as f:
        json.dump(collection.to_dict(), f, indent=4)

if __name__ == "__main__":
    main()
```
