"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Explain the concept of 'distributed ledger' in blockchain technology and provide a code example that demonstrates its implementation.
Generated: DETERMINISTIC_312d20a6d448ae3a
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Distributed Ledger Example in Blockchain Technology
----------------------------------------------------
This script demonstrates the concept of a distributed ledger in blockchain technology.
A distributed ledger is a database that is consensually shared and synchronized across multiple nodes.
It ensures transparency and immutability of data across the network.
"""

import hashlib
import json
from datetime import datetime


# Define a class for the Blockchain
class Blockchain:
    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        """
        Creates a new block and adds it to the chain.
        
        Args:
            proof (int): The proof-of-work value for the block.
            previous_hash (str): The hash of the previous block.
        
        Returns:
            dict: The newly created block.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.utcnow()),
            "proof": proof,
            "previous_hash": previous_hash,
            "data": "Sample transaction data"
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        Retrieves the last block in the chain.
        
        Returns:
            dict: The last block of the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Implements the proof-of-work consensus algorithm for mining blocks.
        
        Args:
            previous_proof (int): The proof-of-work value from the previous block.
        
        Returns:
            int: The new proof-of-work value.
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Example condition for proof validity
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash_block(self, block):
        """
        Generates a hash for the given block.
        
        Args:
            block (dict): The block to be hashed.
        
        Returns:
            str: The SHA-256 hash of the block.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        """
        Validates the blockchain to ensure integrity.
        
        Returns:
            bool: Whether the blockchain is valid.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the previous block matches the stored previous_hash
            if current_block["previous_hash"] != self.hash_block(previous_block):
                return False

            # Validate the proof-of-work
            previous_proof = previous_block["proof"]
            current_proof = current_block["proof"]
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False

        return True


# Example Usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add a few blocks to the chain
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash_block(previous_block)
    blockchain.create_block(proof, previous_hash)

    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash_block(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Print the blockchain
    print("Blockchain:", json.dumps(blockchain.chain, indent=4))

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```
