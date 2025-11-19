"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitriumltd.com
Prompt: Can you provide a code example for a secure blockchain application that aligns with the quality assurance services offered by Arbitrium Ltd?
Generated: DETERMINISTIC_e5cd356f1bc4f6a7
Batch ID: 20250612_135250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import datetime
import json
from flask import Flask, jsonify, request

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self):
        """
        Converts the block to a dictionary for JSON serialization.
        """
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'hash': self.hash
        }

class Blockchain:
    """
    Represents the entire blockchain.
    """
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1', data='Genesis Block')

    def create_block(self, previous_hash, data):
        """
        Creates a new block in the blockchain.
        """
        index = len(self.chain) + 1
        timestamp = str(datetime.datetime.now())
        hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(block)
        return block

    def hash_block(self, index, previous_hash, timestamp, data):
        """
        Generates a SHA-256 hash of a block.
        """
        value = f'{index}{previous_hash}{timestamp}{data}'.encode()
        return hashlib.sha256(value).hexdigest()

    def get_chain(self):
        """
        Returns the full blockchain.
        """
        return [block.to_dict() for block in self.chain]

# Initialize Flask application
app = Flask(__name__)

# Initialize the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine_block():
    """
    Endpoint to mine a new block.
    Expects JSON payload with 'data'.
    """
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'Data is required'}), 400
        
        # Create a new block
        block = blockchain.create_block(previous_hash=blockchain.chain[-1].hash, data=data)
        return jsonify(block.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """
    Endpoint to retrieve the full blockchain.
    """
    try:
        chain = blockchain.get_chain()
        return jsonify(chain), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
