"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainfare.pages.dev
Prompt: Write a program that authenticates digital ownership of artwork using blockchain technology, similar to the approach described on the Chainfare platform.
Generated: DETERMINISTIC_0ea02b276099ced4
Batch ID: 20250612_152235
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

# Blockchain class to manage artwork ownership
class Blockchain:
    def __init__(self):
        # Initialize the chain and the current list of transactions
        self.chain = []
        self.current_transactions = []
        
        # Create the genesis block
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        """
        Create a new block in the blockchain.
        
        Args:
            proof (int): Proof of work for the block
            previous_hash (str): Hash of the previous block
        
        Returns:
            dict: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        
        # Reset the list of current transactions
        self.current_transactions = []
        
        # Append the new block to the chain
        self.chain.append(block)
        return block

    def new_transaction(self, owner, artwork_id, description):
        """
        Add a new transaction to the list of transactions.
        
        Args:
            owner (str): Owner of the artwork
            artwork_id (str): Unique ID of the artwork
            description (str): Description of the artwork
        
        Returns:
            int: Index of the block to hold the transaction
        """
        self.current_transactions.append({
            'owner': owner,
            'artwork_id': artwork_id,
            'description': description,
        })
        
        # Return the index of the next block
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        
        Args:
            block (dict): Block data
        
        Returns:
            str: Hash of the block
        """
        # Ensure the dictionary is ordered to avoid inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Get the last block in the chain.
        
        Returns:
            dict: The last block
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work algorithm:
        - Find a number p' such that hash(pp') contains 4 leading zeroes
        - p is the previous proof, p' is the new proof
        
        Args:
            last_proof (int): Previous proof
        
        Returns:
            int: New proof
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        
        Args:
            last_proof (int): Previous proof
            proof (int): Current proof
        
        Returns:
            bool: True if valid, False otherwise
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# Flask app to expose blockchain functionalities
app = Flask(__name__)

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Mine a new block based on proof of work.
    
    Returns:
        Response: JSON representation of the mined block
    """
    # Get proof of work for the last block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Create a new block with the proof and the hash of the previous block
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': "New block mined successfully!",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Create a new transaction for artwork ownership details.
    
    Returns:
        Response: JSON with success message and block index
    """
    values = request.get_json()
    
    # Check that all required fields are provided
    required = ['owner', 'artwork_id', 'description']
    if not all(field in values for field in required):
        return jsonify({'message': 'Missing required fields'}), 400

    # Create the new transaction
    index = blockchain.new_transaction(values['owner'], values['artwork_id'], values['description'])
    
    response = {'message': f'Transaction will be added to block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Retrieve the full blockchain.
    
    Returns:
        Response: JSON representation of the blockchain
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
