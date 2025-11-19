"""
Generated Code Metadata:
========================
Original URL: https://geokukt.cn
Prompt: Develop a basic understanding of the STEPN project and its Move-to-Earn concept, and propose a similar project idea leveraging blockchain technology.
Generated: DETERMINISTIC_b30be408eae62264
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Proposal: FitChain - A Move-to-Earn Blockchain Application
Description: FitChain incentivizes users to stay active by rewarding them with cryptocurrency tokens for physical activities such as walking, running, or cycling. 
The application uses blockchain technology to ensure transparency and security in reward distribution.

Below is a Python implementation of a basic prototype for FitChain using Flask and a simulated blockchain.
"""

from flask import Flask, request, jsonify
import time
import hashlib

# Initialize Flask app
app = Flask(__name__)

# Blockchain class to manage blocks and transactions
class Blockchain:
    def __init__(self):
        self.chain = []  # List to store the blockchain
        self.pending_rewards = []  # List to store pending rewards
        self.create_block(proof=1, previous_hash='0')  # Create the genesis block

    def create_block(self, proof, previous_hash):
        """
        Create a new block and add it to the blockchain.
        :param proof: Proof of work for the block.
        :param previous_hash: Hash of the previous block.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'rewards': self.pending_rewards
        }
        self.pending_rewards = []  # Reset pending rewards after adding to the block
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        Get the last block in the blockchain.
        :return: The last block.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Proof of work algorithm to find the next proof.
        :param previous_proof: Proof of the previous block.
        :return: The new proof.
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Simple condition for proof of work
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """
        Generate a hash for a block.
        :param block: The block to hash.
        :return: The hash of the block.
        """
        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        """
        Validate the blockchain.
        :param chain: The blockchain to validate.
        :return: True if valid, False otherwise.
        """
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# Initialize blockchain
blockchain = Blockchain()

@app.route('/add_reward', methods=['POST'])
def add_reward():
    """
    Endpoint to add a reward for a user's activity.
    :return: JSON response with the status.
    """
    data = request.get_json()
    if not data or 'user' not in data or 'activity' not in data or 'reward' not in data:
        return jsonify({'message': 'Invalid data'}), 400
    blockchain.pending_rewards.append({
        'user': data['user'],
        'activity': data['activity'],
        'reward': data['reward']
    })
    return jsonify({'message': 'Reward added successfully'}), 201

@app.route('/mine_block', methods=['GET'])
def mine_block():
    """
    Endpoint to mine a new block.
    :return: JSON response with the new block.
    """
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    return jsonify({'message': 'Block mined successfully', 'block': block}), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    """
    Endpoint to retrieve the blockchain.
    :return: JSON response with the blockchain.
    """
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)}), 200

@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    """
    Endpoint to validate the blockchain.
    :return: JSON response with the validation result.
    """
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    return jsonify({'message': 'Blockchain is valid' if is_valid else 'Blockchain is invalid'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
