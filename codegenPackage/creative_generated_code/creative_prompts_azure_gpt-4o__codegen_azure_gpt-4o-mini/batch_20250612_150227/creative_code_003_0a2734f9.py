"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitnexusai.com
Prompt: Create a blockchain-based solution to ensure secure and private transactions, as described in BitNexusAi's claim of 98.9% success rates using blockchain technology.
Generated: DETERMINISTIC_0a2734f9c0c6ee52
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_block(previous_hash='1', nonce=100)  # Create the genesis block

    def create_block(self, nonce, previous_hash):
        """Creates a new block in the Blockchain.
        
        Args:
            nonce (int): The nonce for proof of work.
            previous_hash (str): Hash of the previous block.
        
        Returns:
            dict: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Creates a new transaction to go into the next mined block.
        
        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount to be sent.
        
        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Creates a SHA-256 hash of a block.
        
        Args:
            block (dict): The block to be hashed.
        
        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last block in the chain."""
        return self.chain[-1]

    def proof_of_work(self, last_nonce):
        """Simple proof of work algorithm.
        
        Args:
            last_nonce (int): The previous nonce value.
        
        Returns:
            int: The new nonce.
        """
        nonce = 0
        while not self.valid_proof(last_nonce, nonce):
            nonce += 1
        return nonce

    @staticmethod
    def valid_proof(last_nonce, nonce):
        """Validates the proof of work.
        
        Args:
            last_nonce (int): The previous nonce value.
            nonce (int): The current nonce value.
        
        Returns:
            bool: True if valid, else False.
        """
        guess = f'{last_nonce}{nonce}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Adjust difficulty here

# Initialize the Flask application
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Initialize the Blockchain
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Endpoint to create a new transaction."""
    values = request.get_json()

    # Validate the request
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return jsonify({'error': 'Missing values'}), 400

    try:
        # Create a new transaction
        index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mine', methods=['GET'])
def mine():
    """Endpoint to mine a new block."""
    last_block = blockchain.last_block
    last_nonce = last_block['nonce']
    nonce = blockchain.proof_of_work(last_nonce)

    # Create a new block with the mined nonce
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(nonce, previous_hash)

    response = {
        'message': 'New block mined',
        'index': block['index'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    """Endpoint to get the full blockchain."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000)
```
