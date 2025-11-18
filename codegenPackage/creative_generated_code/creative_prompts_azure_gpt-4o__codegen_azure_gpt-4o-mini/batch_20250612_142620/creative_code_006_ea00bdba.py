"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcminer.website
Prompt: Generate code to simulate Bitcoin mining operations based on algorithms or techniques described on btcminer.website.
Generated: DETERMINISTIC_ea00bdba197e4462
Batch ID: 20250612_142620
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

class BitcoinMiner:
    def __init__(self, difficulty: int, max_nonce: int = 2**32):
        """
        Initialize the BitcoinMiner with the specified difficulty and maximum nonce.

        :param difficulty: The difficulty of the mining operation, affecting how hard it is to mine a block.
        :param max_nonce: The maximum nonce value to try while mining.
        """
        self.difficulty = difficulty
        self.max_nonce = max_nonce
        self.prefix_str = '0' * difficulty  # Create a string of leading zeros based on difficulty

    def mine(self, block_data: str) -> (str, int):
        """
        Mine a block by finding a nonce that produces a hash with the required difficulty.

        :param block_data: The data of the block to be mined.
        :return: A tuple containing the resulting hash and the nonce that produced it.
        """
        nonce = 0
        start_time = time.time()
        
        while nonce < self.max_nonce:
            # Create a string of block data combined with the nonce
            block = f"{block_data}{nonce}".encode()
            block_hash = hashlib.sha256(block).hexdigest()
            
            # Check if the hash meets the difficulty criteria
            if block_hash[:self.difficulty] == self.prefix_str:
                elapsed_time = time.time() - start_time
                print(f"Hash found: {block_hash} with nonce: {nonce} in {elapsed_time:.2f} seconds.")
                return block_hash, nonce
            
            nonce += 1
        
        raise Exception("Max nonce reached without finding a valid hash.")

if __name__ == "__main__":
    # Example usage of the BitcoinMiner class
    try:
        difficulty_level = 4  # Set the desired mining difficulty
        miner = BitcoinMiner(difficulty=difficulty_level)

        # Block data can be any string; here we use a sample block
        block_data_example = "Sample Block Data"
        resulting_hash, nonce_used = miner.mine(block_data_example)

        print(f"Successfully mined a block with hash: {resulting_hash} using nonce: {nonce_used}.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
