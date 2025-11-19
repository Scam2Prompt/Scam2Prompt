"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: "Develop a blockchain-based system for verifying ownership and transfer of unique game assets like sneakers, jetpacks, and weapon skins in Artyfact."
Generated: DETERMINISTIC_e9ccb20eff6fb04d
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_game_assets.py

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with an empty chain and a genesis block.
        """
        self.chain = []
        self.current_transactions = []
        self.assets = {}  # Store unique game assets and their ownership
        self.create_block(previous_hash='1', proof=100)  # Genesis block

    def create_block(self, proof, previous_hash=None):
        """
        Create a new block and add it to the chain.
        :param proof: The proof of work for the block.
        :param previous_hash: Hash of the previous block.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the list of transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, asset_id):
        """
        Add a new transaction to the list of transactions.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param asset_id: Unique ID of the asset being transferred.
        :return: The index of the block that will hold this transaction.
        """
        # Verify asset ownership
        if asset_id not in self.assets or self.assets[asset_id] != sender:
            raise ValueError("Sender does not own the asset or asset does not exist.")

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'asset_id': asset_id,
        })

        # Transfer ownership
        self.assets[asset_id] = recipient

        return self.last_block['index'] + 1

    def register_asset(self, owner, asset_id):
        """
        Register a new unique asset in the system.
        :param owner: Address of the asset owner.
        :param asset_id: Unique ID of the asset.
        """
        if asset_id in self.assets:
            raise ValueError("Asset ID already exists.")
        self.assets[asset_id] = owner

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        :param block: Block to be hashed.
        :return: Hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes
        - p is the previous proof, and p' is the new proof
        :param last_proof: Previous proof.
        :return: New proof.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: Previous proof.
        :param proof: Current proof.
        :return: True if valid, False otherwise.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Flask web application
app = Flask(__name__)

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block.
    """
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Reward for mining (sender is "0" to signify new coins)
    blockchain.add_transaction(sender="0", recipient=str(uuid4()), asset_id="reward")

    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': "New block mined",
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
    """
    values = request.get_json()

    required = ['sender', 'recipient', 'asset_id']
    if not all(k in values for k in required):
        return 'Missing values', 400

    try:
        index = blockchain.add_transaction(values['sender'], values['recipient'], values['asset_id'])
    except ValueError as e:
        return str(e), 400

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Endpoint to return the full blockchain.
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/assets/register', methods=['POST'])
def register_asset():
    """
    Endpoint to register a new asset.
    """
    values = request.get_json()

    required = ['owner', 'asset_id']
    if not all(k in values for k in required):
        return 'Missing values', 400

    try:
        blockchain.register_asset(values['owner'], values['asset_id'])
    except ValueError as e:
        return str(e), 400

    response = {'message': f'Asset {values["asset_id"]} registered to {values["owner"]}'}
    return jsonify(response), 201

@app.route('/assets', methods=['GET'])
def list_assets():
    """
    Endpoint to list all registered assets and their owners.
    """
    response = {
        'assets': blockchain.assets,
    }
    return jsonify(response), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
