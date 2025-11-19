"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Develop a blockchain-based system for recording the state and metadata of a creative product line, ensuring transparent and tamper-proof attribution of ownership.
Generated: DETERMINISTIC_d6c0a458fe39ebce
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 product_id: str, metadata: str, owner: str):
        """
        Initialize a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        product_id (str): The ID of the creative product.
        metadata (str): The metadata of the creative product.
        owner (str): The owner of the creative product.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.product_id = product_id
        self.metadata = metadata
        self.owner = owner
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + \
               self.product_id + self.metadata + self.owner
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis", "Genesis Block", "Genesis Owner")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.

        Raises:
        ValueError: If the new block is not valid.
        """
        if new_block.index != self.get_latest_block().index + 1:
            raise ValueError("Invalid block index")
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError("Invalid previous hash")
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class ProductLine:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize a new product line.

        Args:
        blockchain (Blockchain): The blockchain to use.
        """
        self.blockchain = blockchain

    def add_product(self, product_id: str, metadata: str, owner: str):
        """
        Add a new product to the product line.

        Args:
        product_id (str): The ID of the product.
        metadata (str): The metadata of the product.
        owner (str): The owner of the product.

        Raises:
        ValueError: If the product is not valid.
        """
        new_block = Block(self.blockchain.get_latest_block().index + 1, 
                           self.blockchain.get_latest_block().hash, 
                           time.time(), product_id, metadata, owner)
        try:
            self.blockchain.add_block(new_block)
        except ValueError as e:
            raise ValueError("Invalid product") from e

    def get_product(self, product_id: str) -> dict:
        """
        Get a product from the product line.

        Args:
        product_id (str): The ID of the product.

        Returns:
        dict: The product data.

        Raises:
        ValueError: If the product is not found.
        """
        for block in self.blockchain.chain:
            if block.product_id == product_id:
                return {
                    "product_id": block.product_id,
                    "metadata": block.metadata,
                    "owner": block.owner,
                    "timestamp": block.timestamp
                }
        raise ValueError("Product not found")


def main():
    blockchain = Blockchain()
    product_line = ProductLine(blockchain)

    # Add some products
    product_line.add_product("Product 1", "This is product 1", "Owner 1")
    product_line.add_product("Product 2", "This is product 2", "Owner 2")

    # Get a product
    try:
        product = product_line.get_product("Product 1")
        print(product)
    except ValueError as e:
        print(e)

    # Check if the blockchain is valid
    print(blockchain.is_valid())


if __name__ == "__main__":
    main()
```
