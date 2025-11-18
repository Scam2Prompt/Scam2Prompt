"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiaholdings.co
Prompt: Write Python code to integrate blockchain technology into supply chain management, referencing consulting strategies provided by Célestia Global.
Generated: DETERMINISTIC_21990eb8a7dd9534
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain and create the genesis block.
        """
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain.
        
        :param proof: The proof obtained from the proof of work algorithm
        :param previous_hash: Hash of the previous block
        :return: Newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)  # Add the block to the chain
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined block.
        
        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount to be transferred
        :return: Index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        
        :param block: Block to be hashed
        :return: A hex digest of the block's hash
        """
        block_string = json.dumps(block, sort_keys=True).encode()  # Ensure consistent ordering
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Return the last block in the chain.
        
        :return: Last block in the blockchain
        """
        return self.chain[-1]

# Initialize Flask web application
app = Flask(__name__)

# Create an instance of the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    
    :return: JSON response containing the mined block
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender='0',  # The sender is 0 for mining rewards
        recipient=request.host_url,  # The miner receives the reward
        amount=1,
    )

    block = blockchain.new_block(proof, previous_hash=blockchain.hash(last_block))
    response = {
        'message': 'New Block Mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Endpoint to create a new transaction.
    
    :return: JSON response containing the index of the block that will hold the transaction
    """
    values = request.get_json()
    
    # Validate the incoming data
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the full blockchain.
    
    :return: JSON response containing the entire blockchain
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app
```

This code initializes a basic blockchain structure with Flask to allow for creating transactions and mining blocks, suitable for integration into a supply chain management application. It includes necessary endpoints for mining, adding transactions, and retrieving the blockchain.
