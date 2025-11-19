"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarity420.vercel.app
Prompt: Can you provide code examples for integrating blockchain features in a D&D game based on the Rarity Game model?
Generated: DETERMINISTIC_d75f83cb0bca53ea
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain = []
        self.current_transactions = []
        # Create the genesis block
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        """Create a new block in the blockchain.

        Args:
            proof (int): The proof of work for the new block.
            previous_hash (str): The hash of the previous block.

        Returns:
            dict: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current transactions list
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Add a new transaction to the list of transactions.

        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount to be transferred.

        Returns:
            int: The index of the block that will contain this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """Return the last block in the blockchain."""
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block.

        Args:
            block (dict): The block to hash.

        Returns:
            str: The hash of the block.
        """
        # Convert the block to a JSON string and encode it
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """Simple proof of work algorithm.

        Args:
            last_proof (int): Previous proof to find the new proof.

        Returns:
            int: The new proof.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Validate the proof.

        Args:
            last_proof (int): Last proof.
            proof (int): Current proof to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Check if the hash starts with 0000


# Example integration for D&D game items with blockchain
class ItemBlockchain(Blockchain):
    def new_item(self, name, description, owner):
        """Create a new item and add a transaction.

        Args:
            name (str): The name of the item.
            description (str): Description of the item.
            owner (str): The owner of the item.

        Returns:
            int: The index of the block that will contain this item.
        """
        item_id = len(self.chain)  # Unique ID based on current number of blocks
        self.new_transaction(sender="system", recipient=owner, amount=0)  # No cost for creating items
        return self.create_block(proof=0, previous_hash=self.hash(self.last_block)), item_id


# Example usage
if __name__ == "__main__":
    try:
        # Create a blockchain for D&D Items
        item_blockchain = ItemBlockchain()

        # Create a new item
        new_item_info = item_blockchain.new_item(name="Magical Sword", description="A sword imbued with magic.", owner="Player1")
        print("New item created:", new_item_info)

    except Exception as e:
        print(f"An error occurred: {e}")
```
