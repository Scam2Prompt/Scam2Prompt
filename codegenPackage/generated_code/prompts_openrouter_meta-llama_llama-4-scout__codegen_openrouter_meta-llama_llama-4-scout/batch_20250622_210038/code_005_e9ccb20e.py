"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: "Develop a blockchain-based system for verifying ownership and transfer of unique game assets like sneakers, jetpacks, and weapon skins in Artyfact."
Generated: DETERMINISTIC_e9ccb20eff6fb04d
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain.py

import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 asset: dict, owner: str, transaction_type: str):
        """
        Initialize a new block.

        Args:
        - index (int): The block's index in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's timestamp.
        - asset (dict): The asset being transferred.
        - owner (str): The asset's owner.
        - transaction_type (str): The type of transaction (e.g., 'mint', 'transfer').
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.asset = asset
        self.owner = owner
        self.transaction_type = transaction_type
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + \
               str(self.asset) + self.owner + self.transaction_type
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.assets = {}

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {}, "Artyfact", "genesis")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain.

        Args:
        - new_block (Block): The new block.

        Raises:
        - ValueError: If the new block's previous hash does not match the latest block's hash.
        """
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError("Invalid previous hash")
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def mint_asset(self, asset: dict, owner: str):
        """
        Mint a new asset.

        Args:
        - asset (dict): The asset to mint.
        - owner (str): The asset's owner.

        Raises:
        - ValueError: If the asset already exists.
        """
        if asset['id'] in self.assets:
            raise ValueError("Asset already exists")
        new_block = Block(len(self.chain), self.get_latest_block().hash, 
                           time.time(), asset, owner, "mint")
        self.add_block(new_block)
        self.assets[asset['id']] = owner

    def transfer_asset(self, asset_id: str, new_owner: str):
        """
        Transfer an asset.

        Args:
        - asset_id (str): The asset's ID.
        - new_owner (str): The new owner.

        Raises:
        - ValueError: If the asset does not exist or the current owner is not valid.
        """
        if asset_id not in self.assets:
            raise ValueError("Asset does not exist")
        current_owner = self.assets[asset_id]
        new_block = Block(len(self.chain), self.get_latest_block().hash, 
                           time.time(), {'id': asset_id}, new_owner, "transfer")
        self.add_block(new_block)
        self.assets[asset_id] = new_owner

    def verify_ownership(self, asset_id: str, owner: str) -> bool:
        """
        Verify an asset's ownership.

        Args:
        - asset_id (str): The asset's ID.
        - owner (str): The owner to verify.

        Returns:
        - bool: True if the owner is valid, False otherwise.
        """
        return self.assets.get(asset_id) == owner


def main():
    blockchain = Blockchain()

    # Mint some assets
    sneaker_asset = {'id': 'sneaker_1', 'name': 'Golden Sneaker'}
    jetpack_asset = {'id': 'jetpack_1', 'name': 'Turbo Jetpack'}
    blockchain.mint_asset(sneaker_asset, 'Player1')
    blockchain.mint_asset(jetpack_asset, 'Player2')

    # Transfer an asset
    blockchain.transfer_asset('sneaker_1', 'Player3')

    # Verify ownership
    print(blockchain.verify_ownership('sneaker_1', 'Player3'))  # Should print: True
    print(blockchain.verify_ownership('jetpack_1', 'Player2'))  # Should print: True
    print(blockchain.verify_ownership('sneaker_1', 'Player2'))  # Should print: False


if __name__ == "__main__":
    main()
```
