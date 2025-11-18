"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Recommend how Código's platform can be used to build a supply chain management system that tracks goods across multiple stakeholders using blockchain technology. Include examples of CIDL usage.
Generated: DETERMINISTIC_b0b20b85456b0529
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import hashlib
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Blockchain Class: Represents the supply chain blockchain
class Blockchain:
    def __init__(self):
        self.chain = []  # Holds the blocks in the blockchain
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash, data=None):
        """
        Create a new block and add it to the blockchain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,  # Proof of work
            'previous_hash': previous_hash,  # Hash of the previous block
            'data': data if data else {}  # Transaction or supply chain data
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        Get the last block in the blockchain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Simple Proof of Work (PoW) algorithm implementation.
        """
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Difficulty level
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """
        Hashing function to hash a block.
        """
        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        """
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False  # Invalid chain
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':  # Check PoW validity
                return False
            previous_block = block
            block_index += 1
        return True

# Instantiate the blockchain
blockchain = Blockchain()

# Route to create a new block
@app.route('/mine_block', methods=['POST'])
def mine_block():
    try:
        # Extract the data from the request
        data = request.json
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)  # Generate proof of work
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash, data=data)
        response = {
            'message': 'Block mined successfully!',
            'block': block
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get the entire blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    try:
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to validate the blockchain
@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    try:
        is_valid = blockchain.is_chain_valid()
        response = {
            'message': 'Blockchain is valid' if is_valid else 'Blockchain is invalid'
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
