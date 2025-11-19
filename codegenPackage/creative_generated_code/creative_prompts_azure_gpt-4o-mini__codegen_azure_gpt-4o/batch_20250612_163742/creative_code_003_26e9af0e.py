"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-two.vercel.app
Prompt: Provide an example of how to create a collection of NFTs with pricing and edition details like those listed on the MetaMask Two site.
Generated: DETERMINISTIC_26e9af0ec073bedc
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NFT:
    """
    Class representing a single NFT.
    """

    def __init__(self, name: str, description: str, price: float, edition: int, total_editions: int):
        """
        Initialize an NFT object.

        :param name: Name of the NFT
        :param description: Description of the NFT
        :param price: Price of the NFT in ETH
        :param edition: Edition number of the NFT
        :param total_editions: Total number of editions for this NFT
        """
        self.name = name
        self.description = description
        self.price = price
        self.edition = edition
        self.total_editions = total_editions

    def to_dict(self) -> dict:
        """
        Convert the NFT instance to a dictionary representation.

        :return: Dictionary containing NFT details
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "edition": self.edition,
            "total_editions": self.total_editions
        }


class NFTCollection:
    """
    Class representing a collection of NFTs.
    """

    def __init__(self, collection_name: str):
        """
        Initialize an NFTCollection object.

        :param collection_name: Name of the NFT collection
        """
        self.collection_name = collection_name
        self.nfts = []

    def add_nft(self, nft: NFT) -> None:
        """
        Add an NFT to the collection.

        :param nft: NFT object to be added
        """
        if not isinstance(nft, NFT):
            raise ValueError("Only instances of NFT can be added to the collection.")
        self.nfts.append(nft)

    def to_json(self) -> str:
        """
        Convert the collection to a JSON string representation.

        :return: JSON string containing the collection details
        """
        collection_data = {
            "collection_name": self.collection_name,
            "nfts": [nft.to_dict() for nft in self.nfts]
        }
        return json.dumps(collection_data, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Create an NFT collection
        collection = NFTCollection("MetaMask Two Collection")

        # Add NFTs to the collection
        collection.add_nft(NFT("NFT #1", "First NFT in the collection", 0.05, 1, 10))
        collection.add_nft(NFT("NFT #2", "Second NFT in the collection", 0.08, 2, 10))
        collection.add_nft(NFT("NFT #3", "Third NFT in the collection", 0.15, 3, 10))

        # Convert collection to JSON for display or storage
        collection_json = collection.to_json()

        # Print the formatted JSON
        print(collection_json)

    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")
```
