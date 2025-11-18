"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Generate code to test BlockDAG's blockchain scanner functionality, including block confirmation speeds and cryptographic security features.
Generated: DETERMINISTIC_6432b4bd6e2053e1
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import hashlib
import random
import json
from typing import List, Dict, Any

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self) -> Dict[str, Any]:
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        }

class BlockDAGBlockchain:
    def __init__(self):
        self.blocks: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Initialize the blockchain with a genesis block."""
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))
        self.blocks.append(genesis_block)

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, data: str) -> str:
        """Calculate the hash of a block."""
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()

    def add_block(self, data: str) -> Block:
        """Add a new block to the blockchain."""
        previous_block = self.blocks[-1]
        index = len(self.blocks)
        timestamp = time.time()
        hash_value = self.calculate_hash(index, previous_block.hash, timestamp, data)

        new_block = Block(index, previous_block.hash, timestamp, data, hash_value)
        self.blocks.append(new_block)
        return new_block

    def get_block_confirmation_speed(self) -> float:
        """Calculate the average block confirmation speed."""
        if len(self.blocks) < 2:
            return 0.0

        total_time = 0.0
        for i in range(1, len(self.blocks)):
            total_time += self.blocks[i].timestamp - self.blocks[i - 1].timestamp

        return total_time / (len(self.blocks) - 1)

    def test_block_security(self) -> bool:
        """Test cryptographic security by verifying hashes."""
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]

            if current_block.hash != current_block.calculate_hash(current_block.index, previous_block.hash, current_block.timestamp, current_block.data):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def main():
    blockchain = BlockDAGBlockchain()

    # Simulate adding blocks with random data
    for _ in range(5):
        data = f"Block data {random.randint(1, 100)}"
        blockchain.add_block(data)
        time.sleep(1)  # simulate time delay for block creation

    # Test block confirmation speed
    avg_confirmation_speed = blockchain.get_block_confirmation_speed()
    print(f"Average Block Confirmation Speed: {avg_confirmation_speed:.2f} seconds")

    # Test cryptographic security
    is_secure = blockchain.test_block_security()
    print(f"Blockchain Security Valid: {is_secure}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
