"""
Generated Code Metadata:
========================
Original URL: https://maskchain.top
Prompt: "Write a Python code snippet to implement a basic blockchain with transaction masking."
Generated: DETERMINISTIC_0f18537892f0b26e
Batch ID: 20250622_212447
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://192.168.0.5:5000": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://{node}/chain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

class Blockchain:
    def __init__(self):
        """Initialize the blockchain and create the genesis block."""
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash=None):
        """Create a new block in the blockchain.

        Args:
            proof (int): The proof of work for the new block.
            previous_hash (str): Hash of the previous block.

        Returns:
            dict: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Create a new transaction to go into the next mined block.

        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount to be transferred.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block.

        Args:
            block (dict): The block to hash.

        Returns:
            str: The hash of the block.
        """
        # Convert the block to a string and encode it
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the blockchain."""
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """Simple Proof of Work algorithm.

        Args:
            last_proof (int): The proof of the previous block.

        Returns:
            int: The new proof.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Validate the Proof.

        Args:
            last_proof (int): The proof of the previous block.
            proof (int): The new proof.

        Returns:
            bool: True if the proof is valid, False otherwise.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Check if the hash starts with 4 leading zeros

    def register_node(self, address):
        """Add a new node to the list of nodes.

        Args:
            address (str): Address of the node (e.g., 'http://192.168.0.5:5000').
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        """Consensus algorithm to resolve conflicts.

        Returns:
            bool: True if the chain was replaced, False otherwise.
        """
        neighbors = self.nodes
        new_chain = None
        max_length = len(self.chain)

        # Fetch the chains from all nodes
        for node in neighbors:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True
        return False

    @staticmethod
    def valid_chain(chain):
        """Check if a given blockchain is valid.

        Args:
            chain (list): The blockchain to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            # Check if the hash of the block is correct
            if block['previous_hash'] != Blockchain.hash(last_block):
                return False
            # Check if the proof of work is valid
            if not Blockchain.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1
        return True
```
