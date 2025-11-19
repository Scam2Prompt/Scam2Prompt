"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Write a tutorial on how to create a blockchain-based identity verification system, inspired by the concepts presented at ETHBerlin04.
Generated: DETERMINISTIC_394804d47028b2b5
Batch ID: 20250612_162710
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
from flask import Flask, jsonify, request

# Class representing a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize blockchain
        self.current_transactions = []  # Initialize current transactions
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of the previous block
        :return: New Block
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

    def new_transaction(self, identity_data):
        """
        Adds a new transaction to the list of transactions
        :param identity_data: Dictionary containing identity data (e.g., name, ID)
        :return: Index of the block that will hold this transaction
        """
        self.current_transactions.append(identity_data)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block
        :param block: Block to hash
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last block in the chain"""
        return self.chain[-1]

# Create Flask application
app = Flask(__name__)

# Create a blockchain instance
blockchain = Blockchain()

@app.route('/add_identity', methods=['POST'])
def add_identity():
    """
    Endpoint to add a new identity to the blockchain
    :return: Response with the status of the transaction
    """
    data = request.get_json()
    
    # Validate request data
    if not data or 'name' not in data or 'ID' not in data:
        return jsonify({'message': 'Invalid data. Must include name and ID.'}), 400

    # Add the new identity transaction
    try:
        index = blockchain.new_transaction(data)
    except Exception as e:
        return jsonify({'message': 'Failed to add identity', 'error': str(e)}), 500

    response = {
        'message': f'Identity will be added to Block {index}',
    }
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block
    :return: Response with details of the newly mined block
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = proof_of_work(last_proof)  # Implement proof of work algorithm

    # Create new block
    blockchain.new_block(proof)

    response = {
        'message': 'New block mined!',
        'index': blockchain.last_block['index'],
        'transactions': blockchain.last_block['transactions'],
        'proof': blockchain.last_block['proof'],
        'previous_hash': blockchain.last_block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm:
     - Find a number p' such that hash(pp') contains leading 4 zeros, where p is the previous proof
    :param last_proof: Previous proof
    :return: New proof
    """
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    """
    Validates the Proof
    :param last_proof: Previous proof
    :param proof: Current proof
    :return: True if valid, False otherwise
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
