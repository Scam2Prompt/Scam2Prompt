"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Develop a blockchain-based solution to track and manage Masa rewards earned through wallet connections.
Generated: DETERMINISTIC_af79293de928a327
Batch ID: 20250612_153400
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
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        if self.validate_transaction(sender, recipient, amount):
            self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            })
            return self.last_block['index'] + 1  # Return the index of the block that will hold the new transaction
        else:
            raise ValueError("Invalid transaction")

    @staticmethod
    def hash(block):
        # Create a SHA-256 hash of a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def validate_transaction(sender, recipient, amount):
        # Basic validation for transaction data
        if not isinstance(sender, str) or not isinstance(recipient, str) or not isinstance(amount, (int, float)):
            return False
        if amount <= 0:
            return False
        return True

# Initialize Flask app
app = Flask(__name__)

# Generate a globally unique address for the node
node_identifier = str(uuid4()).replace('-', '')

# Initialize the blockchain
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    # Create a new transaction
    values = request.get_json()

    # Check that the required fields are in the POST data
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return jsonify({'message': 'Missing values'}), 400

    try:
        # Create a new transaction
        index = blockchain.create_transaction(values['sender'], values['recipient'], values['amount'])
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    # Mine a new block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = proof_of_work(last_proof)

    # Reward for mining
    blockchain.create_transaction(sender="0", recipient=node_identifier, amount=1)

    # Create new block in the blockchain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    # Simple proof of work algorithm
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    # Validate the proof
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"  # Adjust difficulty by changing the number of leading zeros

@app.route('/chain', methods=['GET'])
def full_chain():
    # Return the full blockchain
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
