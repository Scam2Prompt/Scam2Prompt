"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Develop a blockchain-based system for tracking and verifying coffee transactions, ensuring transparency and accountability throughout the supply chain.
Generated: DETERMINISTIC_de1c889b2e82a001
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from hashlib import sha256
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        """Initialize the blockchain and create the genesis block."""
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
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
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)  # Add the new block to the chain
        return block

    def new_transaction(self, sender, recipient, amount):
        """Add a new transaction to the list of transactions.

        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount of coffee being transacted.

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
            block (dict): Block to hash.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

# Create a Flask web application
app = Flask(__name__)

# Create a blockchain instance
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint to create a new transaction.

    Returns:
        json: Response containing the index of the block that will hold the transaction.
    """
    values = request.get_json()  # Get the JSON data from the request

    # Check for required fields
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return jsonify({'message': 'Missing values'}), 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block.

    Returns:
        json: Response containing the new block and its index.
    """
    last_block = blockchain.last_block
    proof = proof_of_work(last_block['proof'])  # Implement proof of work
    blockchain.new_transaction(sender="0", recipient="your_address", amount=1)  # Reward for mining

    block = blockchain.new_block(proof, previous_hash=blockchain.hash(last_block))
    response = {
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    """Simple Proof of Work algorithm.

    Args:
        last_proof (int): Previous proof.

    Returns:
        int: New proof.
    """
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    """Validate the proof.

    Args:
        last_proof (int): Previous proof.
        proof (int): Current proof.

    Returns:
        bool: True if valid, False otherwise.
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"  # Check if the hash starts with 4 leading zeros

@app.route('/chain', methods=['GET'])
def full_chain():
    """Endpoint to return the full blockchain.

    Returns:
        json: The full blockchain.
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app
```
