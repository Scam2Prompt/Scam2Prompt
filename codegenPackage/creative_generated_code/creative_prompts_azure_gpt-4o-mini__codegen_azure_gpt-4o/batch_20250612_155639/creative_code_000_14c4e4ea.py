"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiaholdings.co
Prompt: Write a Python script that integrates blockchain technology into a supply chain management system, focusing on enhancing security and operational efficiency as described by Célestia Global.
Generated: DETERMINISTIC_14c4e4ea9e2af710
Batch ID: 20250612_155639
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
import time
from typing import List, Dict, Any
from flask import Flask, request, jsonify

# Class representing a single block in the blockchain
class Block:
    def __init__(self, index: int, timestamp: str, data: Dict[str, Any], previous_hash: str):
        """
        Initialize a new block.

        :param index: Position of the block in the chain
        :param timestamp: Time of block creation
        :param data: Data representing transactions or supply chain events
        :param previous_hash: Hash of the previous block
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Class representing the blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with the genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the first block in the blockchain (genesis block).
        """
        return Block(0, time.strftime("%Y-%m-%d %H:%M:%S"), {"message": "Genesis Block"}, "0")

    def get_latest_block(self) -> Block:
        """
        Get the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data: Dict[str, Any]) -> None:
        """
        Add a new block to the blockchain.

        :param data: Data to store in the block
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Verify the integrity of the blockchain by checking hashes and links between blocks.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Ensure current block's previous_hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Flask web application for interacting with the blockchain
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_block', methods=['POST'])
def add_block():
    """
    API endpoint to add a new block to the blockchain.

    Request JSON format:
    {
        "data": {
            "key": "value"
        }
    }
    """
    try:
        data = request.get_json()
        if not data or "data" not in data:
            return jsonify({"error": "Invalid data format"}), 400

        blockchain.add_block(data["data"])
        return jsonify({"message": "Block added successfully", "block": data["data"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_chain', methods=['GET'])
def get_chain():
    """
    API endpoint to retrieve the entire blockchain.
    """
    chain_data = [
        {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        } for block in blockchain.chain
    ]
    return jsonify({"chain": chain_data, "length": len(blockchain.chain)}), 200

@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    """
    API endpoint to validate the blockchain integrity.
    """
    is_valid = blockchain.is_chain_valid()
    return jsonify({"is_valid": is_valid}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
