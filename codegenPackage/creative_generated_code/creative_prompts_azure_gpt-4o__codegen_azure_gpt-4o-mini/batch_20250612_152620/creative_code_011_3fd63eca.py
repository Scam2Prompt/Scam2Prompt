"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.xyz
Prompt: Suggest best practices for implementing energy-efficient consensus mechanisms in a blockchain-based gaming platform like BetSwirl.
Generated: DETERMINISTIC_3fd63eca99cd318a
Batch ID: 20250612_152620
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
from typing import List, Any, Dict

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any, nonce: int):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce

    def calculate_hash(self) -> str:
        """Calculate the SHA-256 hash of the block."""
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """Class to manage the blockchain and its consensus mechanism."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block(0, "0", time.time(), "Genesis Block", 0)
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """Return the latest block in the blockchain."""
        return self.chain[-1]

    def add_block(self, data: Any) -> None:
        """Add a new block to the blockchain by mining it."""
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = time.time()
        new_nonce, new_hash = self.proof_of_work(new_index, latest_block.previous_hash, new_timestamp, data)
        
        new_block = Block(new_index, latest_block.previous_hash, new_timestamp, data, new_nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index: int, previous_hash: str, timestamp: float, data: Any) -> (int, str):
        """Simple proof of work algorithm to ensure energy efficiency."""
        nonce = 0
        hash_value = ""
        
        # Attempt until we find a valid hash for the block
        while not hash_value.startswith('0000'):  # Proof of work threshold
            hash_value = hashlib.sha256(f"{index}{previous_hash}{timestamp}{data}{nonce}".encode()).hexdigest()
            nonce += 1
        
        return nonce, hash_value

    def validate_chain(self) -> bool:
        """Validate the entire blockchain to ensure integrity."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            # Check if the hash of the current block is correct
            if current.hash != current.calculate_hash():
                print("Invalid block hash.")
                return False
            
            # Check if the previous hash is correct
            if current.previous_hash != previous.calculate_hash():
                print("Invalid previous hash.")
                return False

        return True


if __name__ == "__main__":
    # Example usage of the Blockchain class
    try:
        betswirl_blockchain = Blockchain()
        betswirl_blockchain.add_block({"game": "Poker", "winner": "Player1"})
        betswirl_blockchain.add_block({"game": "Blackjack", "winner": "Player2"})
        
        # Validate the blockchain
        if betswirl_blockchain.validate_chain():
            print("Blockchain is valid!")
        else:
            print("Blockchain is invalid!")
        
        # Print the blocks in the blockchain
        for block in betswirl_blockchain.chain:
            print(f"Block {block.index} Hash: {block.calculate_hash()} Data: {block.data}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
