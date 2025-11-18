"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Write a Python script using blockchain technology to create a licensing and trading system for video content, inspired by the MILC platform's approach to solving complex licensing challenges in the media industry.
Generated: DETERMINISTIC_e3d167db9e7d52fd
Batch ID: 20250612_151027
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
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

# Blockchain class to manage video content licensing and trading
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_block(proof=1, previous_hash="0")  # Genesis block

    def create_block(self, proof, previous_hash):
        """
        Create a new block and append it to the chain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []  # Reset the list of transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, content_id, license_type):
        """
        Add a new licensing transaction to the list of transactions.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'content_id': content_id,
            'license_type': license_type,
        })
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work algorithm.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the Proof: Check if hash(last_proof, proof) starts with 4 leading zeros.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

# Flask app for API endpoints
app = Flask(__name__)

# Instantiate the blockchain
blockchain = Blockchain()

# Generate a globally unique address for the node
node_identifier = str(uuid4()).replace('-', '')

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    previous_hash = Blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'New block mined successfully!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Endpoint to create a new licensing transaction.
    """
    values = request.get_json()

    required_fields = ['sender', 'recipient', 'content_id', 'license_type']
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    index = blockchain.add_transaction(
        sender=values['sender'],
        recipient=values['recipient'],
        content_id=values['content_id'],
        license_type=values['license_type'],
    )
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to retrieve the entire blockchain.
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    """
    Endpoint to register new nodes in the network.
    """
    values = request.get_json()

    nodes = values.get('nodes')
    if not nodes:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.nodes.add(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    """
    Endpoint to resolve conflicts using the consensus algorithm.
    """
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain,
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain,
        }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
