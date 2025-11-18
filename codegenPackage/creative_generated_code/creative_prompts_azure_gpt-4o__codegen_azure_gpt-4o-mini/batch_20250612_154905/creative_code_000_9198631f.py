"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Write a Python script to simulate SHA-256-based Bitcoin mining, referencing Bitspeed's cloud mining approach as described on the MiningBase website.
Generated: DETERMINISTIC_9198631f800d6793
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import binascii
import time
import random

class BitcoinMiner:
    def __init__(self, difficulty):
        """
        Initialize the Bitcoin miner with a given difficulty level.

        :param difficulty: The mining difficulty level (number of leading zeros required in hash).
        """
        self.difficulty = difficulty
        self.prefix_str = '0' * difficulty

    def create_block(self, previous_hash, nonce, data):
        """
        Create a block with the given previous hash, nonce, and transaction data.

        :param previous_hash: The hash of the previous block.
        :param nonce: The nonce value used to generate the block hash.
        :param data: The transaction data to include in the block.
        :return: The block as a string.
        """
        return f"{previous_hash}{nonce}{data}"

    def hash(self, block):
        """
        Generate a SHA-256 hash of the specified block.

        :param block: The block to hash.
        :return: The hexadecimal representation of the hash.
        """
        return hashlib.sha256(block.encode()).hexdigest()

    def mine(self, previous_hash, data):
        """
        Simulate the mining process by finding a valid nonce for the given block data.

        :param previous_hash: The hash of the previous block.
        :param data: The transaction data to include in the block.
        :return: A tuple containing the nonce and the resulting hash.
        """
        nonce = 0
        start_time = time.time()

        while True:
            block = self.create_block(previous_hash, nonce, data)
            block_hash = self.hash(block)

            if block_hash.startswith(self.prefix_str):
                elapsed_time = time.time() - start_time
                print(f"Nonce: {nonce}, Hash: {block_hash}, Time taken: {elapsed_time:.2f} seconds")
                return nonce, block_hash
            
            nonce += 1

def main():
    """
    Main function to run the Bitcoin mining simulation.
    """
    previous_hash = "0000000000000000000"  # Example previous hash
    data = "Sample transaction data"
    difficulty = 4  # Difficulty level (number of leading zeros)

    print("Starting Bitcoin mining simulation...")
    
    try:
        miner = BitcoinMiner(difficulty)
        nonce, block_hash = miner.mine(previous_hash, data)
        print(f"Mining successful! Nonce: {nonce}, Block Hash: {block_hash}")
    except Exception as e:
        print(f"An error occurred during mining: {e}")

if __name__ == "__main__":
    main()
```
