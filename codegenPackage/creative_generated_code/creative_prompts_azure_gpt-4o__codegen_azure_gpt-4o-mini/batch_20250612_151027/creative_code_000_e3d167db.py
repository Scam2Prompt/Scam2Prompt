"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Write a Python script using blockchain technology to create a licensing and trading system for video content, inspired by the MILC platform's approach to solving complex licensing challenges in the media industry.
Generated: DETERMINISTIC_e3d167db9e7d52fd
Batch ID: 20250612_151027
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
from uuid import uuid4
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of the previous block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined Block
        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount to be transferred
        :return: Index of the Block that will contain this transaction
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
        Create a SHA-256 hash of a Block
        :param block: Block
        :return: String representing the hash
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]


app = Flask(__name__)

# Generate a global unique address for this client
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Endpoint to create a new transaction
    :return: JSON containing the index of the Block
    """
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    # Check if all required fields are in the request
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new transaction
    index = blockchain.create_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block
    :return: JSON containing the new block and its index
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = proof_of_work(last_proof)

    # Reward for mining (to the node that has mined the block)
    blockchain.create_transaction(sender="0", recipient=node_identifier, amount=1)

    # Create the new block
    block = blockchain.create_block(proof, previous_hash=blockchain.hash(last_block))

    response = {
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm:
     - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
    :param last_proof: Previous proof
    :return: New proof
    """
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
    :param last_proof: Previous proof
    :param proof: Current proof
    :return: True if correct False otherwise
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the full blockchain
    :return: JSON containing the blockchain
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
