"""
Generated Code Metadata:
========================
Original URL: https://milc-global.pages.dev
Prompt: Write code to create a video content licensing platform that uses blockchain to streamline transactions and ensure secure ownership, inspired by MILC's approach.
Generated: DETERMINISTIC_e96440ffcfd82b7c
Batch ID: 20250612_151027
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

# Function to create a new video license
@app.route('/create_license', methods=['POST'])
def create_license():
    try:
        data = request.json
        video_id = data['video_id']
        owner_address = data['owner_address']
        price = web3.toWei(data['price'], 'ether')

        # Create a transaction to mint a new license
        tx = contract.functions.createLicense(video_id, owner_address, price).buildTransaction({
            'from': owner_address,
            'nonce': web3.eth.getTransactionCount(owner_address),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign the transaction
        private_key = os.getenv('PRIVATE_KEY')  # Set your private key in environment variables
        signed_tx = web3.eth.account.signTransaction(tx, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'status': 'success', 'transaction_hash': tx_hash.hex()}), 201

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Function to get license details
@app.route('/get_license/<video_id>', methods=['GET'])
def get_license(video_id):
    try:
        license_details = contract.functions.getLicense(video_id).call()
        return jsonify({'status': 'success', 'license_details': license_details}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Function to transfer license ownership
@app.route('/transfer_license', methods=['POST'])
def transfer_license():
    try:
        data = request.json
        video_id = data['video_id']
        new_owner_address = data['new_owner_address']
        current_owner_address = data['current_owner_address']

        # Create a transaction to transfer the license
        tx = contract.functions.transferLicense(video_id, new_owner_address).buildTransaction({
            'from': current_owner_address,
            'nonce': web3.eth.getTransactionCount(current_owner_address),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign the transaction
        private_key = os.getenv('PRIVATE_KEY')  # Set your private key in environment variables
        signed_tx = web3.eth.account.signTransaction(tx, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'status': 'success', 'transaction_hash': tx_hash.hex()}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have the required libraries installed (`Flask`, `web3`, etc.).
- Set the environment variables for `INFURA_URL`, `CONTRACT_ADDRESS`, and `PRIVATE_KEY` before running the application.
- The smart contract ABI should be saved in a file named `contract_abi.json`.
- This code is a basic implementation and should be further enhanced with security measures, such as input validation and rate limiting, for production use.
