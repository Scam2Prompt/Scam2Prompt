"""
Generated Code Metadata:
========================
Original URL: https://bafybeicrrbccuzbtkb33kxggwzjnwcgkbtng2hy3rhsrqonnw5lrqvboke.ipfs.dweb.link
Prompt: Design a simple blockchain bridge system that allows information exchange between two distinct blockchain networks.
Generated: DETERMINISTIC_0050b4be17f8947c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import time
from typing import Any, Dict, List

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data: Any, previous_hash: str = None) -> Block:
        """Creates a new block and adds it to the chain."""
        index = len(self.chain) + 1
        timestamp = time.time()
        hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash or self.chain[-1].hash, timestamp, data, hash)
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(index: int, previous_hash: str, timestamp: float, data: Any) -> str:
        """Creates a SHA-256 hash of a block."""
        block_string = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_last_block(self) -> Block:
        """Returns the last block in the chain."""
        return self.chain[-1]

class BlockchainBridge:
    """Class to facilitate communication between two blockchains."""
    
    def __init__(self, blockchain_a: Blockchain, blockchain_b: Blockchain):
        self.blockchain_a = blockchain_a
        self.blockchain_b = blockchain_b

    def transfer_data(self, data: Any, from_blockchain: str) -> None:
        """Transfers data from one blockchain to another."""
        try:
            if from_blockchain == 'A':
                new_block = self.blockchain_a.create_block(data)
                print(f"Data transferred to Blockchain A: {new_block}")
                # Simulate transferring to Blockchain B
                self.blockchain_b.create_block(data, previous_hash=new_block.hash)
                print(f"Data transferred to Blockchain B: {self.blockchain_b.get_last_block()}")
            elif from_blockchain == 'B':
                new_block = self.blockchain_b.create_block(data)
                print(f"Data transferred to Blockchain B: {new_block}")
                # Simulate transferring to Blockchain A
                self.blockchain_a.create_block(data, previous_hash=new_block.hash)
                print(f"Data transferred to Blockchain A: {self.blockchain_a.get_last_block()}")
            else:
                raise ValueError("Invalid blockchain identifier. Use 'A' or 'B'.")
        except Exception as e:
            print(f"Error during data transfer: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize two blockchains
    blockchain_a = Blockchain()
    blockchain_b = Blockchain()
    
    # Create a bridge between the two blockchains
    bridge = BlockchainBridge(blockchain_a, blockchain_b)
    
    # Transfer data between the blockchains
    bridge.transfer_data({"message": "Hello from Blockchain A"}, from_blockchain='A')
    bridge.transfer_data({"message": "Hello from Blockchain B"}, from_blockchain='B')
```
