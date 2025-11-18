"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opterisglobal.com
Prompt: Provide a step-by-step guide to implement a blockchain solution for managing high-yield investment opportunities, referencing Opteris Global's customizable flows and security measures.
Generated: DETERMINISTIC_d7539adab27b5a55
Batch ID: 20250612_154601
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
from flask import Flask, jsonify, request

class Block:
    """Class to represent a single block in the blockchain."""
    
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the hash of the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

class Blockchain:
    """Class to represent the entire blockchain."""

    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, data):
        """Creates a new block and adds it to the chain."""
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, timestamp, data, self.chain[-1].hash if self.chain else '0')
        self.chain.append(block)
        return block

    def get_chain(self):
        """Returns the entire blockchain."""
        return [vars(block) for block in self.chain]

# Instantiate Flask and the Blockchain
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine_block():
    """Endpoint to mine a new block."""
    if request.is_json:
        data = request.get_json().get('data')
        if not data:
            return jsonify({'error': 'Data is required to mine a block.'}), 400
        
        block = blockchain.create_block(data)
        return jsonify(vars(block)), 201
    return jsonify({'error': 'Request must be JSON.'}), 400

@app.route('/chain', methods=['GET'])
def get_chain():
    """Endpoint to get the entire blockchain."""
    response = {
        'chain': blockchain.get_chain(),
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

**Note:** This code represents a rudimentary blockchain implementation in Python using Flask for a REST API. It provides endpoints to mine new blocks and retrieve the blockchain. For production use, consider additional features such as user authentication, more robust error handling, security measures, and performance optimizations.
