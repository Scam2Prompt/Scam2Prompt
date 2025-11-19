"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Create an example of a modular blockchain application using the concepts discussed in the Fuel Blog post.
Generated: DETERMINISTIC_ea172dc98004f588
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain.py

import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self):
        """Convert block to dictionary for JSON serialization."""
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'hash': self.hash
        }

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, previous_hash):
        """Create a new block in the blockchain."""
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, previous_hash, timestamp, self.current_data, self.hash(block))
        self.current_data = []  # Reset current data
        self.chain.append(block)
        return block

    def add_data(self, data):
        """Add data to the current block."""
        self.current_data.append(data)

    def hash(self, block):
        """Create a SHA-256 hash of a block."""
        block_string = json.dumps(block.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_chain(self):
        """Return the full blockchain."""
        return [block.to_dict() for block in self.chain]

# Flask application
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_data', methods=['POST'])
def add_data():
    """Endpoint to add data to the current block."""
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        blockchain.add_data(data)
        return jsonify({'message': 'Data added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mine_block', methods=['POST'])
def mine_block():
    """Endpoint to mine a new block."""
    try:
        previous_hash = blockchain.chain[-1].hash if blockchain.chain else '0'
        block = blockchain.create_block(previous_hash)
        return jsonify({'message': 'Block mined successfully', 'block': block.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """Endpoint to retrieve the full blockchain."""
    try:
        return jsonify({'chain': blockchain.get_chain(), 'length': len(blockchain.chain)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This code implements a simple modular blockchain application using Flask. It includes endpoints to add data, mine blocks, and retrieve the blockchain. Each component is well-structured, and error handling is included to ensure robustness.
