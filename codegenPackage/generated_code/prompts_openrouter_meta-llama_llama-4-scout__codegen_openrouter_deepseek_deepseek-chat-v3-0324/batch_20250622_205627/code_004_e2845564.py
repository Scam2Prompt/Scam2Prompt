"""
Generated Code Metadata:
========================
Original URL: https://panz-3cy.pages.dev
Prompt: Design a data structure to store and manage a large collection of NFTs, such as the 8,880 lil pandas in Lil Z's Adventure, and provide an example implementation in a programming language.
Generated: DETERMINISTIC_e2845564e29b40f1
Batch ID: 20250622_205627
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/panda2.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/panda1.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import os

@dataclass
class NFT:
    """
    Represents an NFT with its metadata.
    """
    token_id: int
    name: str
    description: str
    image_url: str
    attributes: Dict[str, str]
    owner: str

class NFTCollection:
    """
    A data structure to store and manage a large collection of NFTs.
    """
    def __init__(self, name: str):
        self.name = name
        self.nfts: Dict[int, NFT] = {}
        self.next_token_id = 1

    def add_nft(self, name: str, description: str, image_url: str, attributes: Dict[str, str], owner: str) -> NFT:
        """
        Adds a new NFT to the collection.
        """
        nft = NFT(
            token_id=self.next_token_id,
            name=name,
            description=description,
            image_url=image_url,
            attributes=attributes,
            owner=owner
        )
        self.nfts[self.next_token_id] = nft
        self.next_token_id += 1
        return nft

    def get_nft(self, token_id: int) -> Optional[NFT]:
        """
        Retrieves an NFT by its token ID.
        """
        return self.nfts.get(token_id)

    def get_nfts_by_owner(self, owner: str) -> List[NFT]:
        """
        Retrieves all NFTs owned by a specific address.
        """
        return [nft for nft in self.nfts.values() if nft.owner == owner]

    def get_nfts_by_attribute(self, attribute: str, value: str) -> List[NFT]:
        """
        Retrieves all NFTs with a specific attribute value.
        """
        return [nft for nft in self.nfts.values() if nft.attributes.get(attribute) == value]

    def transfer_nft(self, token_id: int, new_owner: str) -> bool:
        """
        Transfers ownership of an NFT.
        """
        nft = self.get_nft(token_id)
        if not nft:
            return False
        nft.owner = new_owner
        return True

    def save_to_file(self, file_path: str) -> bool:
        """
        Saves the NFT collection to a JSON file.
        """
        try:
            data = {
                "name": self.name,
                "nfts": [
                    {
                        "token_id": nft.token_id,
                        "name": nft.name,
                        "description": nft.description,
                        "image_url": nft.image_url,
                        "attributes": nft.attributes,
                        "owner": nft.owner
                    }
                    for nft in self.nfts.values()
                ],
                "next_token_id": self.next_token_id
            }
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving collection: {e}")
            return False

    @classmethod
    def load_from_file(cls, file_path: str) -> Optional['NFTCollection']:
        """
        Loads an NFT collection from a JSON file.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            collection = cls(data["name"])
            collection.next_token_id = data["next_token_id"]
            
            for nft_data in data["nfts"]:
                collection.nfts[nft_data["token_id"]] = NFT(
                    token_id=nft_data["token_id"],
                    name=nft_data["name"],
                    description=nft_data["description"],
                    image_url=nft_data["image_url"],
                    attributes=nft_data["attributes"],
                    owner=nft_data["owner"]
                )
            
            return collection
        except Exception as e:
            print(f"Error loading collection: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create a new collection
    collection = NFTCollection("Lil Z's Adventure Pandas")
    
    # Add some NFTs
    collection.add_nft(
        name="Lil Panda #1",
        description="The first panda in the adventure",
        image_url="https://example.com/panda1.png",
        attributes={"background": "forest", "hat": "none"},
        owner="0x123..."
    )
    
    collection.add_nft(
        name="Lil Panda #2",
        description="The second panda in the adventure",
        image_url="https://example.com/panda2.png",
        attributes={"background": "mountain", "hat": "cowboy"},
        owner="0x456..."
    )
    
    # Save collection to file
    collection.save_to_file("lil_pandas_collection.json")
    
    # Load collection from file
    loaded_collection = NFTCollection.load_from_file("lil_pandas_collection.json")
    if loaded_collection:
        print(f"Loaded collection: {loaded_collection.name}")
        print(f"Total NFTs: {len(loaded_collection.nfts)}")
```
