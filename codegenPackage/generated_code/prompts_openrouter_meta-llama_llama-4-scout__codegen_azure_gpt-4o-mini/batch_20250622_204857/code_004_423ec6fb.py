"""
Generated Code Metadata:
========================
Original URL: https://metazeechain.pages.dev
Prompt: "Design a blockchain-based system for secure digital identity management and asset tokenization with interoperable data exchange."
Generated: DETERMINISTIC_423ec6fb9c741701
Batch ID: 20250622_204857
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
from time import time
from typing import List, Dict, Any

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data: Any, previous_hash: str = None) -> Block:
        """Creates a new block and adds it to the chain."""
        index = len(self.chain) + 1
        timestamp = time()
        hash = self.hash_block(index, previous_hash or self.chain[-1].hash, timestamp, data)
        new_block = Block(index, previous_hash or self.chain[-1].hash, timestamp, data, hash)
        self.chain.append(new_block)
        return new_block

    @staticmethod
    def hash_block(index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """Creates a SHA-256 hash of a block."""
        block_string = f"{index}{previous_hash}{timestamp}{json.dumps(data)}"
        return sha256(block_string.encode()).hexdigest()

    def get_chain(self) -> List[Dict[str, Any]]:
        """Returns the blockchain as a list of dictionaries."""
        return [block.__dict__ for block in self.chain]

class DigitalIdentity:
    """Class representing a digital identity."""
    
    def __init__(self, user_id: str, attributes: Dict[str, Any]):
        self.user_id = user_id
        self.attributes = attributes

class AssetToken:
    """Class representing a tokenized asset."""
    
    def __init__(self, asset_id: str, owner_id: str, metadata: Dict[str, Any]):
        self.asset_id = asset_id
        self.owner_id = owner_id
        self.metadata = metadata

class IdentityManagementSystem:
    """Class for managing digital identities and asset tokenization."""
    
    def __init__(self):
        self.blockchain = Blockchain()
        self.identities: Dict[str, DigitalIdentity] = {}
        self.assets: Dict[str, AssetToken] = {}

    def register_identity(self, user_id: str, attributes: Dict[str, Any]) -> str:
        """Registers a new digital identity and adds it to the blockchain."""
        if user_id in self.identities:
            raise ValueError("Identity already exists.")
        identity = DigitalIdentity(user_id, attributes)
        self.identities[user_id] = identity
        block = self.blockchain.create_block(data={"action": "register_identity", "user_id": user_id, "attributes": attributes})
        return block.hash

    def tokenize_asset(self, asset_id: str, owner_id: str, metadata: Dict[str, Any]) -> str:
        """Tokenizes an asset and adds it to the blockchain."""
        if asset_id in self.assets:
            raise ValueError("Asset already tokenized.")
        if owner_id not in self.identities:
            raise ValueError("Owner identity does not exist.")
        asset = AssetToken(asset_id, owner_id, metadata)
        self.assets[asset_id] = asset
        block = self.blockchain.create_block(data={"action": "tokenize_asset", "asset_id": asset_id, "owner_id": owner_id, "metadata": metadata})
        return block.hash

    def get_identity(self, user_id: str) -> DigitalIdentity:
        """Retrieves a digital identity by user ID."""
        if user_id not in self.identities:
            raise ValueError("Identity not found.")
        return self.identities[user_id]

    def get_asset(self, asset_id: str) -> AssetToken:
        """Retrieves a tokenized asset by asset ID."""
        if asset_id not in self.assets:
            raise ValueError("Asset not found.")
        return self.assets[asset_id]

# Example usage
if __name__ == "__main__":
    try:
        ims = IdentityManagementSystem()
        identity_hash = ims.register_identity("user123", {"name": "Alice", "email": "alice@example.com"})
        print(f"Identity registered with hash: {identity_hash}")

        asset_hash = ims.tokenize_asset("asset123", "user123", {"description": "Digital Artwork", "value": 1000})
        print(f"Asset tokenized with hash: {asset_hash}")

        identity = ims.get_identity("user123")
        print(f"Retrieved identity: {identity.__dict__}")

        asset = ims.get_asset("asset123")
        print(f"Retrieved asset: {asset.__dict__}")

    except ValueError as e:
        print(f"Error: {e}")
```
