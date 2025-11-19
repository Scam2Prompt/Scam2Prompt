"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Write Python code to simulate a blockchain system using blocks and hashes, incorporating the principles explained on the "블록과 해시" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_d3046ee54b3c10fa
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from typing import List, Dict, Any, Optional

class Block:
    """
    A single block in the blockchain.
    Contains index, timestamp, data, previous hash, and its own hash.
    """
    
    def __init__(self, index: int, timestamp: float, data: Dict[str, Any], previous_hash: str):
        """
        Initialize a new block.
        
        Args:
            index: The position of the block in the chain
            timestamp: When the block was created
            data: The data to store in the block
            previous_hash: The hash of the previous block in the chain
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.nonce = 0  # Used for proof-of-work
        
    def calculate_hash(self) -> str:
        """
        Calculate the SHA-256 hash of the block's contents.
        
        Returns:
            The hexadecimal digest of the hash
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """
        Perform proof-of-work to mine the block.
        
        Args:
            difficulty: The number of leading zeros required in the hash
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    """
    A simple blockchain implementation.
    """
    
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty = 2  # Adjust for mining difficulty
        self.pending_data: List[Dict[str, Any]] = []
        
    def create_genesis_block(self) -> Block:
        """
        Create the first block in the chain (genesis block).
        
        Returns:
            The genesis block
        """
        return Block(0, time(), {"message": "Genesis Block"}, "0")
    
    def get_latest_block(self) -> Block:
        """
        Get the most recent block in the chain.
        
        Returns:
            The latest block
        """
        return self.chain[-1]
    
    def add_data(self, data: Dict[str, Any]) -> None:
        """
        Add new data to be included in the next block.
        
        Args:
            data: The data to add
        """
        self.pending_data.append(data)
    
    def mine_pending_data(self) -> Block:
        """
        Mine all pending data into a new block and add it to the chain.
        
        Returns:
            The newly mined block
        """
        if not self.pending_data:
            raise ValueError("No pending data to mine")
        
        new_block = Block(
            index=len(self.chain),
            timestamp=time(),
            data=self.pending_data,
            previous_hash=self.get_latest_block().hash
        )
        
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_data = []  # Clear pending data after mining
        return new_block
    
    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        
        Returns:
            True if the chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False
                
            # Check if current block points to the correct previous hash
            if current_block.previous_hash != previous_block.hash:
                return False
                
        return True
    
    def display_chain(self) -> None:
        """
        Print the entire blockchain in a readable format.
        """
        for block in self.chain:
            print(f"Block {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)

# Example usage
if __name__ == "__main__":
    # Create a new blockchain
    my_blockchain = Blockchain()
    
    # Add some data
    my_blockchain.add_data({"from": "Alice", "to": "Bob", "amount": 50})
    my_blockchain.add_data({"from": "Bob", "to": "Charlie", "amount": 25})
    
    # Mine the pending data into a new block
    print("Mining block 1...")
    my_blockchain.mine_pending_data()
    
    # Add more data
    my_blockchain.add_data({"from": "Charlie", "to": "Alice", "amount": 10})
    
    # Mine another block
    print("Mining block 2...")
    my_blockchain.mine_pending_data()
    
    # Display the blockchain
    my_blockchain.display_chain()
    
    # Validate the chain
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")
```
