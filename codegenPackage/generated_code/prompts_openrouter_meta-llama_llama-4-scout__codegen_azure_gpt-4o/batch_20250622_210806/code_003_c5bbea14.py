"""
Generated Code Metadata:
========================
Original URL: https://claim-greenbitcoin-anp.pages.dev
Prompt: Design a system for authenticating digital artworks using blockchain technology, ensuring uniqueness and ownership, and provide a high-level architecture for the system.
Generated: DETERMINISTIC_c5bbea14421a3a91
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Artwork Authentication System using Blockchain Technology

This system ensures uniqueness and ownership of digital artworks by leveraging blockchain.
The code below provides a simplified implementation of the core functionality.
"""

import hashlib
import json
import time
from typing import List, Dict, Any

class Blockchain:
    """
    A simple blockchain implementation for authenticating digital artworks.
    """

    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain: List[Dict[str, Any]] = []
        self.create_block(previous_hash="0", proof=1)

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block in the blockchain.

        :param proof: The proof of work for the block.
        :param previous_hash: The hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'artworks': []  # List of artworks added in this block
        }
        self.chain.append(block)
        return block

    def get_previous_block(self) -> Dict[str, Any]:
        """
        Retrieve the last block in the blockchain.

        :return: The last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int) -> int:
        """
        Perform proof of work to find a valid proof.

        :param previous_proof: The proof of the previous block.
        :return: A valid proof for the new block.
        """
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Difficulty level: 4 leading zeros
                return new_proof
            new_proof += 1

    def hash(self, block: Dict[str, Any]) -> str:
        """
        Generate a SHA-256 hash for a block.

        :param block: The block to hash.
        :return: The hash of the block.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self) -> bool:
        """
        Validate the blockchain to ensure integrity.

        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the previous block matches the stored previous_hash
            if current_block['previous_hash'] != self.hash(previous_block):
                return False

            # Validate proof of work
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False

        return True

    def add_artwork(self, artwork_id: str, owner: str) -> None:
        """
        Add a digital artwork to the blockchain.

        :param artwork_id: Unique identifier for the artwork.
        :param owner: Owner of the artwork.
        """
        # Ensure artwork ID is unique
        for block in self.chain:
            for artwork in block['artworks']:
                if artwork['artwork_id'] == artwork_id:
                    raise ValueError("Artwork ID already exists in the blockchain.")

        # Add artwork to the latest block
        self.chain[-1]['artworks'].append({
            'artwork_id': artwork_id,
            'owner': owner,
            'timestamp': time.time()
        })

# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add a new artwork
    try:
        blockchain.add_artwork(artwork_id="ART123", owner="Alice")
        print("Artwork added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Mine a new block
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Display the blockchain
    print(json.dumps(blockchain.chain, indent=4))

    # Validate the blockchain
    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")
```

This code provides a basic implementation of a blockchain system for authenticating digital artworks. It includes functionality for adding artworks, mining blocks, and validating the blockchain.
