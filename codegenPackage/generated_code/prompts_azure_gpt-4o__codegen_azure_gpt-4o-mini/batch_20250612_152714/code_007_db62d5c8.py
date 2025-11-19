"""
Generated Code Metadata:
========================
Original URL: https://smartprotocolcoin.pages.dev
Prompt: Write code to enable NFT collection management and viewing, as described in the "My NFTs" section of the SmartProtocolCoin website.
Generated: DETERMINISTIC_db62d5c82f18dee4
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_manager.py

import json
import os

class NFT:
    """Class representing a Non-Fungible Token (NFT)."""
    
    def __init__(self, token_id, name, owner, metadata):
        self.token_id = token_id
        self.name = name
        self.owner = owner
        self.metadata = metadata

    def __repr__(self):
        return f"NFT(token_id={self.token_id}, name={self.name}, owner={self.owner})"


class NFTCollection:
    """Class to manage a collection of NFTs."""
    
    def __init__(self):
        self.nfts = {}
        self.load_nfts()

    def load_nfts(self):
        """Load NFTs from a JSON file."""
        if os.path.exists('nfts.json'):
            with open('nfts.json', 'r') as file:
                data = json.load(file)
                for nft_data in data:
                    nft = NFT(**nft_data)
                    self.nfts[nft.token_id] = nft

    def save_nfts(self):
        """Save NFTs to a JSON file."""
        with open('nfts.json', 'w') as file:
            json.dump([nft.__dict__ for nft in self.nfts.values()], file)

    def add_nft(self, token_id, name, owner, metadata):
        """Add a new NFT to the collection."""
        if token_id in self.nfts:
            raise ValueError(f"NFT with token_id {token_id} already exists.")
        nft = NFT(token_id, name, owner, metadata)
        self.nfts[token_id] = nft
        self.save_nfts()

    def remove_nft(self, token_id):
        """Remove an NFT from the collection."""
        if token_id not in self.nfts:
            raise ValueError(f"NFT with token_id {token_id} does not exist.")
        del self.nfts[token_id]
        self.save_nfts()

    def view_nft(self, token_id):
        """View details of a specific NFT."""
        nft = self.nfts.get(token_id)
        if nft is None:
            raise ValueError(f"NFT with token_id {token_id} not found.")
        return nft

    def list_nfts(self):
        """List all NFTs in the collection."""
        return list(self.nfts.values())


# Example usage
if __name__ == "__main__":
    try:
        collection = NFTCollection()
        
        # Adding an NFT
        collection.add_nft("1", "CryptoArt", "Alice", {"description": "A unique piece of digital art."})
        
        # Listing all NFTs
        print("All NFTs:", collection.list_nfts())
        
        # Viewing a specific NFT
        print("View NFT:", collection.view_nft("1"))
        
        # Removing an NFT
        collection.remove_nft("1")
        print("All NFTs after removal:", collection.list_nfts())
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
