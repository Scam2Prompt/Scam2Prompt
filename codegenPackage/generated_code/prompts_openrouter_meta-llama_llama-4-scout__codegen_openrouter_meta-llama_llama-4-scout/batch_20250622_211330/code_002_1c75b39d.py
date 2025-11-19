"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: "Design a use case for Mazze's blockchain technology in the financial sector, specifically for cross-border transactions, and explain how it reduces processing times and costs."
Generated: DETERMINISTIC_1c75b39d3285ae87
Batch ID: 20250622_211330
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
from typing import Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 sender: str, recipient: str, amount: float):
        """
        Initialize a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        sender (str): The sender of the transaction.
        recipient (str): The recipient of the transaction.
        amount (float): The amount of the transaction.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + \
               self.sender + self.recipient + str(self.amount)
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
        return Block(0, "0", time.time(), "Genesis", "Genesis", 0.0)

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
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
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
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class CrossBorderTransaction:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize a new cross-border transaction.

        Args:
        blockchain (Blockchain): The blockchain to use.
        """
        self.blockchain = blockchain

    def process_transaction(self, sender: str, recipient: str, amount: float):
        """
        Process a cross-border transaction.

        Args:
        sender (str): The sender of the transaction.
        recipient (str): The recipient of the transaction.
        amount (float): The amount of the transaction.
        """
        try:
            new_block = Block(len(self.blockchain.chain), 
                              self.blockchain.get_latest_block().hash, 
                              time.time(), sender, recipient, amount)
            self.blockchain.add_block(new_block)
            if not self.blockchain.is_chain_valid():
                raise Exception("Invalid blockchain")
            return {"transaction_id": new_block.hash, "status": "success"}
        except Exception as e:
            return {"transaction_id": None, "status": "failed", "error": str(e)}


def main():
    blockchain = Blockchain()
    transaction = CrossBorderTransaction(blockchain)

    # Example usage
    transaction1 = transaction.process_transaction("Alice", "Bob", 100.0)
    print(transaction1)

    transaction2 = transaction.process_transaction("Bob", "Charlie", 50.0)
    print(transaction2)


if __name__ == "__main__":
    main()
```
