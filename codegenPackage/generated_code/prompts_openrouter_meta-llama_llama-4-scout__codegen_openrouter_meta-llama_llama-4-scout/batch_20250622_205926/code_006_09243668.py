"""
Generated Code Metadata:
========================
Original URL: https://zeta-blockchain.online
Prompt: "Design a basic blockchain structure for a supply chain management system using Zeta blockchain technology."
Generated: DETERMINISTIC_0924366827620ded
Batch ID: 20250622_205926
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
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp when the block was created.
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
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.

        Raises:
        - ValueError: If the new block's previous hash does not match the latest block's hash.
        """
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError("Invalid previous hash")
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class SupplyChain:
    def __init__(self):
        """
        Initialize a new supply chain management system.
        """
        self.blockchain = Blockchain()

    def add_transaction(self, data: dict):
        """
        Add a new transaction to the supply chain.

        Args:
        - data (dict): The transaction data.

        Raises:
        - Exception: If the blockchain is not valid.
        """
        try:
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), data)
            self.blockchain.add_block(new_block)
        except Exception as e:
            raise Exception("Failed to add transaction: " + str(e))

    def get_chain(self) -> List[Block]:
        """
        Get the blockchain.

        Returns:
        - List[Block]: The blockchain.
        """
        return self.blockchain.chain


# Example usage
if __name__ == "__main__":
    supply_chain = SupplyChain()
    supply_chain.add_transaction({"product_id": "123", "supplier": "Supplier A"})
    supply_chain.add_transaction({"product_id": "123", "customer": "Customer B"})

    # Print the blockchain
    for block in supply_chain.get_chain():
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")

    # Check if the blockchain is valid
    print("Is chain valid?", supply_chain.blockchain.is_chain_valid())
```
