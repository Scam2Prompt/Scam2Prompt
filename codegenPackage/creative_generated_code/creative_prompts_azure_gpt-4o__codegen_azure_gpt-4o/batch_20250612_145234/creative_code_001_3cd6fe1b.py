"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Create a script using the SHA-256 algorithm to demonstrate how Coinmining might secure its mining transactions. Include comments explaining how this algorithm ensures security.
Generated: DETERMINISTIC_3cd6fe1bf9f4af33
Batch ID: 20250612_145234
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
import json

class CoinMining:
    def __init__(self):
        # Initialize an empty blockchain
        self.blockchain = []
        # Create the genesis block
        self.create_block(previous_hash="0")

    def create_block(self, previous_hash):
        """
        Create a new block with a timestamp, the index of the block, 
        transaction data, the previous block's hash, and a proof of work.
        The block is hashed using SHA-256 for security.
        """
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': time.time(),
            'transactions': [],  # In a real-world application, this would contain actual transactions
            'previous_hash': previous_hash,
            'nonce': 0  # This will be updated during proof of work
        }
        block['nonce'], block['hash'] = self.proof_of_work(block)
        self.blockchain.append(block)
        return block

    def proof_of_work(self, block):
        """
        Perform proof-of-work to find a valid nonce such that the 
        hash of the block meets the required difficulty target.
        """
        difficulty = 4  # Number of leading zeros in the hash
        target_prefix = '0' * difficulty
        nonce = 0

        while True:
            block['nonce'] = nonce
            block_hash = self.hash_block(block)
            if block_hash[:difficulty] == target_prefix:
                return nonce, block_hash
            nonce += 1

    @staticmethod
    def hash_block(block):
        """
        Generate a SHA-256 hash of the given block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def is_chain_valid(self):
        """
        Verify the integrity of the blockchain by ensuring that:
        1. Each block's hash matches its computed hash.
        2. The previous_hash of each block matches the hash of the previous block.
        """
        for i in range(1, len(self.blockchain)):
            current_block = self.blockchain[i]
            previous_block = self.blockchain[i - 1]

            # Verify current block's hash
            if current_block['hash'] != self.hash_block(current_block):
                return False

            # Verify the chain link (previous_hash matches)
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the CoinMining system
        mining_system = CoinMining()

        # Add new blocks to simulate mining transactions
        for _ in range(3):  # Simulate adding 3 blocks
            new_block = mining_system.create_block(previous_hash=mining_system.blockchain[-1]['hash'])
            print(f"Block {new_block['index']} mined with hash: {new_block['hash']}")

        # Validate the blockchain
        if mining_system.is_chain_valid():
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
