"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Write a Python script to simulate the computational problem-solving process used by cryptocurrency miners to secure blockchain transactions, as described on Tslaspacetrade's website.
Generated: DETERMINISTIC_80acb48fe1fe8260
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import random

class Block:
    """
    Class to represent a block in the blockchain.
    Each block contains index, previous_hash, timestamp, data, and nonce.
    """

    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce

    def compute_hash(self):
        """
        Computes the SHA-256 hash of a block.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def mine(block, prefix_zeros):
    """
    Simulates the mining process by finding a nonce that produces a hash with a specified number of leading zeros.

    :param block: The block to be mined.
    :param prefix_zeros: The number of leading zeros the hash should start with.
    :return: The mined block with the correct nonce.
    """
    prefix_str = '0' * prefix_zeros
    while True:
        block.nonce += 1
        block_hash = block.compute_hash()
        if block_hash.startswith(prefix_str):
            print(f"Block mined: {block_hash} with nonce: {block.nonce}")
            return block


def create_genesis_block():
    """
    Creates the first block in the blockchain.
    
    :return: The genesis block.
    """
    return Block(0, "0", time.time(), "Genesis Block")


def main():
    # Set the difficulty level (number of leading zeros)
    difficulty = 4
    blockchain = [create_genesis_block()]  # Start with the genesis block

    # Simulate mining 5 blocks
    for i in range(1, 6):
        previous_block = blockchain[i - 1]
        timestamp = time.time()
        data = f"Block {i} data"  # Placeholder for block data
        new_block = Block(i, previous_block.compute_hash(), timestamp, data)
        
        # Start mining
        print(f"Mining Block {i}...")
        mined_block = mine(new_block, difficulty)
        
        # Append mined block to blockchain
        blockchain.append(mined_block)

        # Simulate a delay between blocks
        time.sleep(random.uniform(1, 3))  # Sleep for a random time between 1-3 seconds


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
