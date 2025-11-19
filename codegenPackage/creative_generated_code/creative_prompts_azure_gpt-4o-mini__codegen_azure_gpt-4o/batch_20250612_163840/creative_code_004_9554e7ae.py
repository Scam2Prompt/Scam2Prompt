"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfor.com
Prompt: Explain the PoW mechanism used by TonFOR for its decentralized cryptocurrency distribution on The Open Network Blockchain (TON).
Generated: DETERMINISTIC_9554e7ae55c6aa12
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Proof-of-Work (PoW) Simulation for TON Blockchain
This script simulates the PoW mechanism used for decentralized cryptocurrency distribution 
on The Open Network (TON). It includes mining, hash validation, and reward distribution.
"""

import hashlib
import time


class TonPoW:
    """
    TonPoW simulates the Proof-of-Work mechanism for the TON blockchain.
    """

    def __init__(self, difficulty: int):
        """
        Initialize the PoW mechanism.
        
        :param difficulty: Number of leading zeros required in the hash for a valid block.
        """
        self.difficulty = difficulty  # Difficulty level defines how hard it is to mine a block
        self.blockchain = []  # List to store mined blocks
        self.reward = 1  # Reward for successfully mining a block

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block).
        """
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "nonce": 0,
            "previous_hash": "0",
        }
        genesis_block["hash"] = self.compute_hash(genesis_block)
        self.blockchain.append(genesis_block)

    def compute_hash(self, block: dict) -> str:
        """
        Compute the SHA-256 hash of a block.
        
        :param block: Dictionary containing block data.
        :return: SHA-256 hash as a hexadecimal string.
        """
        block_string = f"{block['index']}{block['timestamp']}{block['data']}{block['nonce']}{block['previous_hash']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def is_valid_hash(self, hash: str) -> bool:
        """
        Validate whether a hash meets the difficulty requirement.
        
        :param hash: Hash string to validate.
        :return: True if the hash meets the difficulty requirement, False otherwise.
        """
        return hash.startswith("0" * self.difficulty)

    def mine_block(self, data: str) -> dict:
        """
        Mine a new block by finding a nonce that generates a valid hash.
        
        :param data: Data to store in the block.
        :return: Mined block as a dictionary.
        """
        last_block = self.blockchain[-1]
        new_block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "data": data,
            "nonce": 0,
            "previous_hash": last_block["hash"],
        }

        while True:
            new_block["hash"] = self.compute_hash(new_block)
            if self.is_valid_hash(new_block["hash"]):
                break
            new_block["nonce"] += 1

        self.blockchain.append(new_block)
        return new_block

    def display_blockchain(self):
        """
        Print the current blockchain in a human-readable format.
        """
        for block in self.blockchain:
            print(f"Index: {block['index']}")
            print(f"Timestamp: {block['timestamp']}")
            print(f"Data: {block['data']}")
            print(f"Nonce: {block['nonce']}")
            print(f"Previous Hash: {block['previous_hash']}")
            print(f"Hash: {block['hash']}")
            print("-" * 40)


def main():
    """
    Main function to initialize and simulate the PoW mechanism.
    """
    try:
        # Set difficulty level (number of leading zeros required)
        difficulty = 4  # Adjust this value to make mining harder or easier
        
        # Initialize the PoW mechanism
        pow_system = TonPoW(difficulty=difficulty)
        
        # Create the genesis block
        print("Creating genesis block...")
        pow_system.create_genesis_block()
        
        # Mine a few blocks
        print("Mining blocks...")
        pow_system.mine_block(data="Block 1 Data")
        pow_system.mine_block(data="Block 2 Data")
        pow_system.mine_block(data="Block 3 Data")
        
        # Display the blockchain
        print("\nBlockchain:")
        pow_system.display_blockchain()
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
