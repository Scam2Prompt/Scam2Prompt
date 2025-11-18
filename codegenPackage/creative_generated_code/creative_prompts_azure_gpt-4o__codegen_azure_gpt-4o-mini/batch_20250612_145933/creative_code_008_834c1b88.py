"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-saakuru.pages.dev
Prompt: Provide an example of using Saakuru's technology to create a secure and user-friendly blockchain application for mass adoption.
Generated: DETERMINISTIC_834c1b8894c71fbf
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for all routes

# Blockchain class to represent a simple blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while not self.validate_proof(previous_proof, new_proof):
            new_proof += 1
        return new_proof

    @staticmethod
    def validate_proof(previous_proof, new_proof):
        guess = f'{previous_proof}{new_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'  # Simple proof of work condition

# Initialize the blockchain
blockchain = Blockchain()

@app.route('/mine_block', methods=['POST'])
def mine_block():
    """Endpoint to mine a new block in the blockchain."""
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    new_proof = blockchain.proof_of_work(previous_proof)
    previous_hash = hashlib.sha256(json.dumps(previous_block).encode()).hexdigest()
    block = blockchain.create_block(new_proof, previous_hash)

    response = {
        'message': 'A new block is mined!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    """Endpoint to retrieve the entire blockchain."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/is_valid', methods=['GET'])
def is_valid():
    """Endpoint to verify the integrity of the blockchain."""
    def validate_chain(chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain):
            block = chain[block_index]
            # Check previous hash
            if block['previous_hash'] != hashlib.sha256(json.dumps(previous_block).encode()).hexdigest():
                return False
            
            # Check proof of work
            if not blockchain.validate_proof(previous_block['proof'], block['proof']):
                return False
            
            previous_block = block
            block_index += 1
        return True

    is_chain_valid = validate_chain(blockchain.chain)
    response = {
        'valid': is_chain_valid
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This code creates a simple blockchain application with Flask, handling block mining, chain retrieval, and validation while following best practices for clean, efficient code.
