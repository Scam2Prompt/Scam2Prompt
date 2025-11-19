"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Write a code example that showcases how to integrate the Mazze blockchain's features for real estate transactions, focusing on transparency and accountability.
Generated: DETERMINISTIC_804447590a8a956f
Batch ID: 20250612_163200
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
from typing import Dict, List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 sender: str, receiver: str, property_details: Dict):
        """
        Initialize a Block object.

        Args:
        - index (int): The block number.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - sender (str): The sender's address.
        - receiver (str): The receiver's address.
        - property_details (Dict): Details of the property being transacted.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.property_details = property_details
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + self.sender + self.receiver + str(self.property_details)
        return hashlib.sha256(data.encode()).hexdigest()


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
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis", "Genesis", {})

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


def create_real_estate_transaction(blockchain: Blockchain, 
                                  sender: str, receiver: str, 
                                  property_details: Dict):
    """
    Create a real estate transaction.

    Args:
    - blockchain (Blockchain): The blockchain object.
    - sender (str): The sender's address.
    - receiver (str): The receiver's address.
    - property_details (Dict): Details of the property being transacted.
    """
    try:
        new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, 
                           time.time(), sender, receiver, property_details)
        blockchain.add_block(new_block)
        print("Transaction successful.")
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    # Create a blockchain
    blockchain = Blockchain()

    # Create a real estate transaction
    property_details = {
        "property_id": "12345",
        "property_type": "Residential",
        "location": "New York"
    }
    create_real_estate_transaction(blockchain, "Address1", "Address2", property_details)

    # Check if the chain is valid
    print(f"Is chain valid? {blockchain.is_chain_valid()}")

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Sender: {block.sender}, Receiver: {block.receiver}")
        print(f"Property Details: {block.property_details}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
