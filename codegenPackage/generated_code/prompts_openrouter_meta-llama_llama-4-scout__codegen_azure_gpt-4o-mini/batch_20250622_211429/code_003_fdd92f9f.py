"""
Generated Code Metadata:
========================
Original URL: https://dexmultichains.co
Prompt: "Design a blockchain architecture for a futuristic city like Utopos, including data storage and security features."
Generated: DETERMINISTIC_fdd92f9f5b1dbeb1
Batch ID: 20250622_211429
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
        return hashlib.sha256(block_string).hexdigest()

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

    def to_json(self):
        """Convert the blockchain to a JSON serializable format."""
        return [block.__dict__ for block in self.chain]

# Initialize Flask app
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine_block():
    """Endpoint to mine a new block."""
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'Data is required'}), 400
        
        last_block = blockchain.get_last_block()
        new_block = blockchain.create_block(data, last_block.hash)
        return jsonify({
            'message': 'Block mined successfully',
            'index': new_block.index,
            'timestamp': new_block.timestamp,
            'data': new_block.data,
            'hash': new_block.hash,
            'previous_hash': new_block.previous_hash
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """Endpoint to retrieve the entire blockchain."""
    try:
        return jsonify({
            'chain': blockchain.to_json(),
            'length': len(blockchain.chain)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- This code implements a simple blockchain using Python and Flask.
- It includes endpoints to mine new blocks and retrieve the blockchain.
- Error handling is included for both endpoints.
- The code is structured to be clean and follows best practices for readability and maintainability.
