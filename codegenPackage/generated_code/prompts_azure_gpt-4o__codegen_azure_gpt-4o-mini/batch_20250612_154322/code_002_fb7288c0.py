"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Generate code using a blockchain-based solution to ensure transparency in donation tracking, similar to Dysnix's transparent reporting of funds used for vehicle purchases.
Generated: DETERMINISTIC_fb7288c07226bce6
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_donations = []
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'donations': self.current_donations,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_donations = []  # Reset current donations
        self.chain.append(block)
        return block

    def new_donation(self, donor, amount):
        self.current_donations.append({
            'donor': donor,
            'amount': amount,
            'timestamp': time()
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Simple proof of work condition

    def to_json(self):
        return json.dumps(self.chain, indent=4)

# Initialize Flask app
app = Flask(__name__)

# Create a blockchain instance
blockchain = Blockchain()

@app.route('/donate', methods=['POST'])
def donate():
    """Endpoint to record a new donation."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'donor' not in data or 'amount' not in data:
        return jsonify({'message': 'Invalid data'}), 400

    donor = data['donor']
    amount = data['amount']

    # Add the donation to the blockchain
    index = blockchain.new_donation(donor, amount)
    return jsonify({'message': f'Donation will be added to Block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block."""
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Create a new block and add it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'New Block Mined!',
        'index': block['index'],
        'donations': block['donations'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    """Endpoint to return the full blockchain."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/chain/json', methods=['GET'])
def chain_json():
    """Endpoint to return the blockchain in JSON format."""
    return blockchain.to_json(), 200

@staticmethod
def hash(block):
    """Create a SHA-256 hash of a block."""
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This code implements a simple blockchain for tracking donations, with endpoints for making donations, mining blocks, and retrieving the blockchain. It includes error handling and follows best practices for Python and Flask applications.
