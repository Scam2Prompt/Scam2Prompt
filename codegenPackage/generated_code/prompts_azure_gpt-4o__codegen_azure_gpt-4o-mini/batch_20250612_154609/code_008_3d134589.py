"""
Generated Code Metadata:
========================
Original URL: https://midoin.com
Prompt: Develop a blockchain-based solution to track and verify eco-friendly mining efforts for Midoins, ensuring minimal environmental impact.
Generated: DETERMINISTIC_3d1345892989380d
Batch ID: 20250612_154609
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

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate the hash of the block using SHA-256."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data, previous_hash=None):
        """Create a new block and add it to the chain."""
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, timestamp, data, previous_hash or self.chain[-1].hash)
        self.chain.append(block)
        return block

    def get_chain(self):
        """Return the entire blockchain."""
        return [block.__dict__ for block in self.chain]

    def is_chain_valid(self):
        """Check if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check if the hash of the current block is correct
            if current.hash != current.calculate_hash():
                return False

            # Check if the previous block's hash is correct
            if current.previous_hash != previous.hash:
                return False

        return True

# Initialize Flask app
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine_block():
    """Endpoint to mine a new block with eco-friendly mining data."""
    try:
        data = request.get_json()
        if not data or 'eco_data' not in data:
            return jsonify({'message': 'Invalid data'}), 400

        block = blockchain.create_block(data['eco_data'])
        response = {
            'message': 'Block mined successfully',
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """Endpoint to retrieve the entire blockchain."""
    try:
        response = {
            'chain': blockchain.get_chain(),
            'length': len(blockchain.chain)
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/validate', methods=['GET'])
def validate_chain():
    """Endpoint to validate the blockchain."""
    try:
        is_valid = blockchain.is_chain_valid()
        response = {
            'message': 'Blockchain is valid' if is_valid else 'Blockchain is invalid'
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
