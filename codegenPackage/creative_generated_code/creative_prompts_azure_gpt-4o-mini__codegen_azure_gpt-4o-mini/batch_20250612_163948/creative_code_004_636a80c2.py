"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Explain how to implement blockchain technology to secure intellectual property for music creators using the MuziKoin framework.
Generated: DETERMINISTIC_636a80c23ac867ba
Batch ID: 20250612_163948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from hashlib import sha256
import json
from time import time
from uuid import uuid4

class Blockchain:
    def __init__(self):
        """Initialize the blockchain and create the genesis block."""
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)  # Genesis block

    def create_block(self, proof, previous_hash=None):
        """Create a new block in the blockchain.
        
        Args:
            proof (int): The proof given by the Proof of Work algorithm.
            previous_hash (str): Hash of the previous block.
        
        Returns:
            dict: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)  # Add block to chain
        return block

    def create_transaction(self, sender, recipient, amount):
        """Create a new transaction to go into the next mined block.
        
        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount of currency to be transferred.
        
        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1  # Return next block index

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block.
        
        Args:
            block (dict): Block to be hashed.
        
        Returns:
            str: The SHA-256 hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()  # Create a string representation of the block
        return sha256(block_string).hexdigest()  # Return the hex digest

    def proof_of_work(self, last_proof):
        """Simple proof of work algorithm.
        
        Args:
            last_proof (int): The proof of the previous block.
        
        Returns:
            int: New proof.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):  # Keep iterating until valid proof is found
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Validate the proof.
        
        Args:
            last_proof (int): The proof of the previous block.
            proof (int): The new proof to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        guess = f'{last_proof}{proof}'.encode()  # Create a guess string
        guess_hash = sha256(guess).hexdigest()  # Hash the guess
        return guess_hash[:4] == "0000"  # Check if hash meets the condition

# Example usage of the blockchain for securing music intellectual property
if __name__ == "__main__":
    # Initialize the blockchain
    music_blockchain = Blockchain()

    # Example transaction creation
    try:
        # Add a transaction for a music piece
        transaction_index = music_blockchain.create_transaction(
            sender="music_creator_address",
            recipient="platform_address",
            amount=1.0  # Example amount, could represent rights or royalties
        )

        # Perform proof of work and mine a block
        last_proof = music_blockchain.last_block['proof']
        proof = music_blockchain.proof_of_work(last_proof)

        # Create a new block with the proof and previous block's hash
        previous_hash = music_blockchain.hash(music_blockchain.last_block)
        block = music_blockchain.create_block(proof, previous_hash)

        print(f"New Block Forged: {block}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Error handling
```
