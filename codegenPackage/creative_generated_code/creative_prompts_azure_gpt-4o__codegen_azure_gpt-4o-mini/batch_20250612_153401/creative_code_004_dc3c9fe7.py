"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-648--sage-chimera-b7dc72.netlify.app
Prompt: Create a function to publish unique NFT collections and showcase them for others to view, based on the Foster Marketplace's NFT creation process.
Generated: DETERMINISTIC_dc3c9fe7a96f7995
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class NFTCollection:
    """Class to represent a unique NFT collection."""

    def __init__(self, name: str, creator: str, description: str, items: List[str]):
        """
        Initialize a new NFT collection.

        :param name: Name of the NFT collection
        :param creator: Creator of the NFT collection
        :param description: Description of the NFT collection
        :param items: List of NFTs in this collection
        """
        self.name = name
        self.creator = creator
        self.description = description
        self.items = items

    def to_dict(self) -> Dict[str, Any]:
        """Convert the NFT collection to a dictionary format for serialization."""
        return {
            "name": self.name,
            "creator": self.creator,
            "description": self.description,
            "items": self.items
        }


class NFTMarketplace:
    """Class to represent an NFT marketplace."""

    def __init__(self):
        """Initialize the NFT marketplace with an empty collection list."""
        self.collections = []

    def publish_collection(self, collection: NFTCollection) -> None:
        """
        Publish a new NFT collection to the marketplace.

        :param collection: NFTCollection instance to be published
        :raises ValueError: If collection name is empty or already exists
        """
        if not collection.name:
            raise ValueError("Collection name cannot be empty.")
        
        if any(c.name == collection.name for c in self.collections):
            raise ValueError(f"Collection with name '{collection.name}' already exists.")

        self.collections.append(collection)

    def showcase_collections(self) -> str:
        """Showcase all NFT collections in the marketplace."""
        return json.dumps([collection.to_dict() for collection in self.collections], indent=2)


def main():
    """Main function to demonstrate the NFT marketplace functionality."""
    marketplace = NFTMarketplace()

    # Create a sample NFT collection
    try:
        collection1 = NFTCollection(
            name="Artistic Wonders",
            creator="Jane Doe",
            description="A collection of stunning digital art pieces.",
            items=["art1.png", "art2.png", "art3.png"]
        )
        
        # Publish the collection
        marketplace.publish_collection(collection1)

        # Showcase the collections
        print(marketplace.showcase_collections())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
