"""
Generated Code Metadata:
========================
Original URL: https://freebitcoinmining.website
Prompt: Design a blockchain-based system for secure and transparent free bitcoin mining, incorporating elements from Free Bitcoin Mining's platform.
Generated: DETERMINISTIC_cb6ee0c98ff4d036
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import json
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
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data, previous_hash=None):
        """Create a new block and add it to the chain."""
        index = len(self.chain) + 1
        timestamp = time.time()
        hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash or self.chain[-1].hash, timestamp, data, hash)
        self.chain.append(block)
        return block

    def hash_block(self, index, previous_hash, timestamp, data):
        """Create a SHA-256 hash of a block."""
        block_string = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_chain(self):
        """Return the full blockchain."""
        return [block.to_dict() for block in self.chain]

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine():
    """Endpoint to mine a new block."""
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'Data is required to mine a block.'}), 400
        
        new_block = blockchain.create_block(data)
        response = {
            'message': 'New block mined!',
            'index': new_block.index,
            'hash': new_block.hash,
            'previous_hash': new_block.previous_hash,
            'timestamp': new_block.timestamp,
            'data': new_block.data
        }
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """Endpoint to retrieve the full blockchain."""
    try:
        chain = blockchain.get_chain()
        return jsonify({'chain': chain, 'length': len(chain)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a simple blockchain system using Flask for a web interface. It allows users to mine new blocks and retrieve the blockchain. Each block contains an index, previous hash, timestamp, data, and its own hash. Error handling is included for the mining process and chain retrieval.
