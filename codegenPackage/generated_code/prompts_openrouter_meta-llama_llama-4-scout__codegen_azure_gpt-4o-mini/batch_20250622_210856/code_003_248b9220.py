"""
Generated Code Metadata:
========================
Original URL: https://e-mainnet.pages.dev
Prompt: Design a blockchain-based system for minting and distributing digital assets, incorporating a quick start guide and recovery mechanisms.
Generated: DETERMINISTIC_248b9220ef2b155a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from hashlib import sha256
import json
import time
from typing import List, Dict, Any

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self) -> Dict[str, Any]:
        """Convert block to dictionary format."""
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        }

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data: Any, previous_hash: str = None) -> Block:
        """Create a new block and add it to the chain."""
        index = len(self.chain) + 1
        timestamp = time.time()
        hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash or '0', timestamp, data, hash)
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """Create a SHA-256 hash of a block."""
        block_string = f"{index}{previous_hash}{timestamp}{json.dumps(data)}"
        return sha256(block_string.encode()).hexdigest()

    def get_chain(self) -> List[Dict[str, Any]]:
        """Return the blockchain as a list of dictionaries."""
        return [block.to_dict() for block in self.chain]

class DigitalAsset:
    """Class representing a digital asset."""
    
    def __init__(self, name: str, owner: str):
        self.name = name
        self.owner = owner

    def to_dict(self) -> Dict[str, Any]:
        """Convert digital asset to dictionary format."""
        return {
            "name": self.name,
            "owner": self.owner
        }

class AssetManager:
    """Class for managing digital assets on the blockchain."""
    
    def __init__(self):
        self.blockchain = Blockchain()
        self.assets: Dict[str, DigitalAsset] = {}

    def mint_asset(self, name: str, owner: str) -> str:
        """Mint a new digital asset and add it to the blockchain."""
        if name in self.assets:
            raise ValueError("Asset already exists.")
        
        asset = DigitalAsset(name, owner)
        self.assets[name] = asset
        self.blockchain.create_block(data=asset.to_dict())
        return f"Asset '{name}' minted successfully."

    def transfer_asset(self, name: str, new_owner: str) -> str:
        """Transfer ownership of a digital asset."""
        if name not in self.assets:
            raise ValueError("Asset does not exist.")
        
        asset = self.assets[name]
        asset.owner = new_owner
        self.blockchain.create_block(data=asset.to_dict())
        return f"Asset '{name}' transferred to '{new_owner}' successfully."

    def get_asset_info(self, name: str) -> Dict[str, Any]:
        """Retrieve information about a digital asset."""
        if name not in self.assets:
            raise ValueError("Asset does not exist.")
        
        return self.assets[name].to_dict()

# Quick Start Guide
if __name__ == "__main__":
    try:
        # Initialize Asset Manager
        asset_manager = AssetManager()

        # Mint a new digital asset
        print(asset_manager.mint_asset("ArtPiece1", "Alice"))

        # Transfer ownership of the asset
        print(asset_manager.transfer_asset("ArtPiece1", "Bob"))

        # Retrieve asset information
        print(asset_manager.get_asset_info("ArtPiece1"))

        # Print the blockchain
        print(json.dumps(asset_manager.blockchain.get_chain(), indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
