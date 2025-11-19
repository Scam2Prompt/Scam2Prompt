"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Write a Python code snippet to create a simple blockchain-based system for storing and sharing memes, inspired by METAL's Blockchain of Banter.
Generated: DETERMINISTIC_f6e567e37087c417
Batch ID: 20250622_211009
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

class Meme:
    """Class representing a meme in the blockchain."""
    def __init__(self, creator, content):
        self.creator = creator
        self.content = content
        self.timestamp = time()

    def to_dict(self):
        """Convert the meme to a dictionary format."""
        return {
            'creator': self.creator,
            'content': self.content,
            'timestamp': self.timestamp
        }

class Block:
    """Class representing a block in the blockchain."""
    def __init__(self, index, memes, previous_hash):
        self.index = index
        self.memes = memes
        self.timestamp = time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate the hash of the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """Class representing the blockchain."""
    def __init__(self):
        self.chain = []
        self.current_memes = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, previous_hash):
        """Create a new block and add it to the chain."""
        block = Block(len(self.chain) + 1, self.current_memes, previous_hash)
        self.current_memes = []  # Reset current memes
        self.chain.append(block)
        return block

    def add_meme(self, creator, content):
        """Add a new meme to the current memes list."""
        meme = Meme(creator, content)
        self.current_memes.append(meme.to_dict())
        return meme

# Initialize Flask app
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_meme', methods=['POST'])
def add_meme():
    """API endpoint to add a meme to the blockchain."""
    data = request.get_json()
    if not data or 'creator' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        creator = data['creator']
        content = data['content']
        meme = blockchain.add_meme(creator, content)
        return jsonify({'message': 'Meme added', 'meme': meme.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mine_block', methods=['GET'])
def mine_block():
    """API endpoint to mine a new block."""
    try:
        previous_hash = blockchain.chain[-1].hash if blockchain.chain else '1'
        block = blockchain.create_block(previous_hash)
        return jsonify({
            'message': 'Block mined',
            'index': block.index,
            'memes': block.memes,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    """API endpoint to retrieve the entire blockchain."""
    chain_data = [{
        'index': block.index,
        'memes': block.memes,
        'timestamp': block.timestamp,
        'previous_hash': block.previous_hash,
        'hash': block.hash
    } for block in blockchain.chain]
    return jsonify({'chain': chain_data, 'length': len(chain_data)}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
