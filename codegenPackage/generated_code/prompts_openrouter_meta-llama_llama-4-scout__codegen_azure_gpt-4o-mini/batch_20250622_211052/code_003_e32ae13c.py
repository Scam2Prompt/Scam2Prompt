"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Design a blockchain-based platform for buying and selling software engineering services as NFTs, incorporating elements from OpenSwe.
Generated: DETERMINISTIC_e32ae13c2eea6a4d
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from web3 import Web3
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network (using Infura or local node)
infura_url = os.getenv('INFURA_URL')  # Set your Infura URL in environment variables
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to Ethereum
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum network")

# Load smart contract ABI and address
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

contract_address = os.getenv('CONTRACT_ADDRESS')  # Set your contract address in environment variables
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to create a new NFT for a service
@app.route('/create_nft', methods=['POST'])
def create_nft():
    try:
        # Get data from request
        data = request.json
        service_name = data['service_name']
        service_description = data['service_description']
        seller_address = data['seller_address']
        
        # Validate input
        if not all([service_name, service_description, seller_address]):
            return jsonify({"error": "Missing required fields"}), 400

        # Create NFT (this is a placeholder for actual minting logic)
        tx_hash = contract.functions.mintNFT(seller_address, service_name, service_description).transact({
            'from': seller_address,
            'value': web3.toWei(0.01, 'ether')  # Example fee for minting
        })

        # Wait for transaction to be mined
        web3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"message": "NFT created successfully", "tx_hash": tx_hash.hex()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to buy an NFT
@app.route('/buy_nft/<int:nft_id>', methods=['POST'])
def buy_nft(nft_id):
    try:
        # Get buyer address from request
        buyer_address = request.json['buyer_address']
        
        # Validate input
        if not buyer_address:
            return jsonify({"error": "Missing buyer address"}), 400

        # Execute purchase (this is a placeholder for actual buying logic)
        tx_hash = contract.functions.buyNFT(nft_id).transact({
            'from': buyer_address,
            'value': web3.toWei(0.02, 'ether')  # Example price for the NFT
        })

        # Wait for transaction to be mined
        web3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"message": "NFT purchased successfully", "tx_hash": tx_hash.hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to get NFT details
@app.route('/nft/<int:nft_id>', methods=['GET'])
def get_nft(nft_id):
    try:
        # Fetch NFT details (this is a placeholder for actual fetching logic)
        nft_details = contract.functions.getNFTDetails(nft_id).call()

        return jsonify({
            "nft_id": nft_id,
            "service_name": nft_details[0],
            "service_description": nft_details[1],
            "owner": nft_details[2]
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have the required libraries installed (`Flask`, `web3`, etc.).
- Replace the placeholder functions in the smart contract with actual implementations.
- Set the environment variables for `INFURA_URL` and `CONTRACT_ADDRESS` before running the application.
- The smart contract ABI should be saved in a file named `contract_abi.json`.
