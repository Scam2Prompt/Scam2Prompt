"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Develop a blockchain-based system for tracking and verifying coffee transactions, ensuring transparency and accountability throughout the supply chain.
Generated: DETERMINISTIC_de1c889b2e82a001
Batch ID: 20250622_210038
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
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


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
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

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
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        Returns:
        - bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class CoffeeTransaction:
    def __init__(self, coffee_id: str, supplier: str, buyer: str):
        """
        Initialize a new coffee transaction.

        Args:
        - coffee_id (str): The ID of the coffee.
        - supplier (str): The supplier of the coffee.
        - buyer (str): The buyer of the coffee.
        """
        self.coffee_id = coffee_id
        self.supplier = supplier
        self.buyer = buyer

    def to_dict(self) -> dict:
        """
        Convert the transaction to a dictionary.

        Returns:
        - dict: The transaction as a dictionary.
        """
        return {"coffee_id": self.coffee_id, "supplier": self.supplier, "buyer": self.buyer}


class CoffeeTrackingSystem:
    def __init__(self):
        """
        Initialize a new coffee tracking system.
        """
        self.blockchain = Blockchain()

    def add_transaction(self, coffee_id: str, supplier: str, buyer: str):
        """
        Add a new coffee transaction to the blockchain.

        Args:
        - coffee_id (str): The ID of the coffee.
        - supplier (str): The supplier of the coffee.
        - buyer (str): The buyer of the coffee.
        """
        try:
            transaction = CoffeeTransaction(coffee_id, supplier, buyer)
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), transaction.to_dict())
            self.blockchain.add_block(new_block)
        except Exception as e:
            print(f"Error adding transaction: {e}")

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        return self.blockchain.is_chain_valid()

    def print_blockchain(self):
        """
        Print the blockchain.
        """
        for block in self.blockchain.chain:
            print(f"Block {block.index} - Hash: {block.hash}")
            print(f"Timestamp: {block.timestamp}, Data: {block.data}")
            print("------------------------")


# Example usage
if __name__ == "__main__":
    coffee_system = CoffeeTrackingSystem()
    coffee_system.add_transaction("coffee1", "supplier1", "buyer1")
    coffee_system.add_transaction("coffee2", "supplier2", "buyer2")
    coffee_system.print_blockchain()
    print(f"Is chain valid? {coffee_system.is_chain_valid()}")
```
