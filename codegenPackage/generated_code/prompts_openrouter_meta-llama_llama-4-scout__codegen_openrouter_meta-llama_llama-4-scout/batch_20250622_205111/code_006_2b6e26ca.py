"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: "Discuss the advantages of using blockchain technology for MMFs, as proposed by Spiko, including increased transparency, efficiency, and accessibility for investors."
Generated: DETERMINISTIC_2b6e26ca6ced7174
Batch ID: 20250622_205111
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

class Block:
    """
    Represents a block in the blockchain.
    
    Attributes:
    index (int): The index of the block in the blockchain.
    previous_hash (str): The hash of the previous block.
    timestamp (float): The timestamp when the block was created.
    data (str): The data stored in the block.
    hash (str): The hash of the block.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.
        
        Returns:
        str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """
    Represents a blockchain.
    
    Attributes:
    chain (List[Block]): The list of blocks in the blockchain.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block.
        
        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Gets the latest block in the blockchain.
        
        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Adds a new block to the blockchain.
        
        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks if the blockchain is valid.
        
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


class MMF:
    """
    Represents a Money Market Fund (MMF) using blockchain technology.
    
    Attributes:
    blockchain (Blockchain): The blockchain used to store MMF data.
    """

    def __init__(self):
        self.blockchain = Blockchain()

    def add_transaction(self, data: str):
        """
        Adds a new transaction to the MMF.
        
        Args:
        data (str): The transaction data.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), data)
        self.blockchain.add_block(new_block)

    def is_valid(self) -> bool:
        """
        Checks if the MMF blockchain is valid.
        
        Returns:
        bool: True if the MMF blockchain is valid, False otherwise.
        """
        return self.blockchain.is_chain_valid()


def main():
    mmf = MMF()
    mmf.add_transaction("Investor A invested $1000")
    mmf.add_transaction("Investor B invested $500")

    # Check if the MMF blockchain is valid
    if mmf.is_valid():
        print("The MMF blockchain is valid.")
    else:
        print("The MMF blockchain is not valid.")

    # Print the MMF blockchain
    for block in mmf.blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")


if __name__ == "__main__":
    main()
```
