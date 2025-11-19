"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Develop a blockchain-based system for recording the state and metadata of a creative product line, ensuring transparent and tamper-proof attribution of ownership.
Generated: DETERMINISTIC_d6c0a458fe39ebce
Batch ID: 20250622_210706
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

    def get_last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

    def to_dict(self):
        """Convert the blockchain to a list of dictionaries for JSON serialization."""
        return [block.__dict__ for block in self.chain]

# Initialize Flask app
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_product', methods=['POST'])
def add_product():
    """API endpoint to add a new creative product to the blockchain."""
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'creator' not in data:
            return jsonify({'error': 'Invalid data'}), 400
        
        # Create a new block with product data
        new_block = blockchain.create_block(data)
        return jsonify({
            'message': 'Product added successfully',
            'block': new_block.__dict__
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """API endpoint to retrieve the entire blockchain."""
    try:
        return jsonify({
            'chain': blockchain.to_dict(),
            'length': len(blockchain.chain)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```
