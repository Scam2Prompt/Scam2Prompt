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
# Import required libraries
import hashlib
import time
from typing import List

# Define a class for Block
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict, hash: str):
        """
        Initialize a Block object.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.
        hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Define a class for Blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"}, self.calculate_hash(0, "0", time.time(), {"genesis": "block"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, data: dict) -> str:
        """
        Calculate the hash of a block.

        Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.

        Returns:
        str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to be added.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Define a class for DigitalIdentity
class DigitalIdentity:
    def __init__(self, user_id: str, attributes: dict):
        """
        Initialize a DigitalIdentity object.

        Args:
        user_id (str): The ID of the user.
        attributes (dict): The attributes of the user.
        """
        self.user_id = user_id
        self.attributes = attributes

# Define a class for Asset
class Asset:
    def __init__(self, asset_id: str, owner: str, data: dict):
        """
        Initialize an Asset object.

        Args:
        asset_id (str): The ID of the asset.
        owner (str): The owner of the asset.
        data (dict): The data of the asset.
        """
        self.asset_id = asset_id
        self.owner = owner
        self.data = data

# Define a class for TokenizedAsset
class TokenizedAsset:
    def __init__(self, asset: Asset, token_id: str):
        """
        Initialize a TokenizedAsset object.

        Args:
        asset (Asset): The asset to be tokenized.
        token_id (str): The ID of the token.
        """
        self.asset = asset
        self.token_id = token_id

# Define a class for InteroperableDataExchange
class InteroperableDataExchange:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize an InteroperableDataExchange object.

        Args:
        blockchain (Blockchain): The blockchain used for data exchange.
        """
        self.blockchain = blockchain

    def exchange_data(self, data: dict):
        """
        Exchange data between different systems.

        Args:
        data (dict): The data to be exchanged.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.chain[-1].hash, time.time(), data, "")
        self.blockchain.add_block(new_block)

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Create digital identities
    digital_identity1 = DigitalIdentity("user1", {"name": "John Doe", "email": "john@example.com"})
    digital_identity2 = DigitalIdentity("user2", {"name": "Jane Doe", "email": "jane@example.com"})

    # Create assets
    asset1 = Asset("asset1", digital_identity1.user_id, {"type": "asset", "value": 100})
    asset2 = Asset("asset2", digital_identity2.user_id, {"type": "asset", "value": 200})

    # Tokenize assets
    tokenized_asset1 = TokenizedAsset(asset1, "token1")
    tokenized_asset2 = TokenizedAsset(asset2, "token2")

    # Exchange data
    interoperable_data_exchange = InteroperableDataExchange(blockchain)
    interoperable_data_exchange.exchange_data({"tokenized_asset": tokenized_asset1.__dict__})

    # Check blockchain validity
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Print blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("------------------------")
```
