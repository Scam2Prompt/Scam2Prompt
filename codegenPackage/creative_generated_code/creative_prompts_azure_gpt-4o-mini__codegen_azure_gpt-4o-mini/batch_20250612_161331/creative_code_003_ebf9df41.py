"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Explain how the Proof of Work algorithm functions in the context of Bitcoin mining on the Bitspeed platform.
Generated: DETERMINISTIC_ebf9df4183e6cb4d
Batch ID: 20250612_161331
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
    def __init__(self, difficulty):
        """
        Initializes the miner with a specified difficulty level.
        
        :param difficulty: The difficulty level for the Proof of Work.
        """
        self.difficulty = difficulty
        self.prefix_str = '0' * difficulty

    def mine_block(self, previous_hash, transactions):
        """
        Mines a new block by finding a nonce that meets the difficulty requirement.
        
        :param previous_hash: The hash of the previous block in the blockchain.
        :param transactions: The transactions to include in the new block.
        :return: The nonce that satisfies the difficulty requirement and the new block's hash.
        """
        nonce = 0
        block_hash = ''
        while not block_hash.startswith(self.prefix_str):
            # Increment the nonce
            nonce += 1
            # Create the block string
            block_string = f"{previous_hash}{transactions}{nonce}".encode()
            # Calculate the hash of the block
            block_hash = hashlib.sha256(block_string).hexdigest()
        
        # Return the nonce and the valid block hash
        return nonce, block_hash

def simulate_mining():
    """
    Simulates the process of mining a block on the Bitspeed platform.
    """
    difficulty = 4  # Set the desired difficulty level
    miner = BitcoinMiner(difficulty)
    
    # Simulating previous block hash and transactions
    previous_hash = "0000000000000000000"  # Example previous block hash
    transactions = "user1->user2:10,user3->user4:5"  # Example transactions

    print("Starting mining...")
    start_time = time.time()
    
    try:
        nonce, new_hash = miner.mine_block(previous_hash, transactions)
        elapsed_time = time.time() - start_time
        print(f"Mining complete! Nonce: {nonce}")
        print(f"New block hash: {new_hash}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
    except Exception as e:
        print(f"An error occurred during mining: {str(e)}")

if __name__ == "__main__":
    simulate_mining()
```
