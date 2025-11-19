"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethir-website.webflow.io
Prompt: Write a tutorial on setting up a user portal using Aethir's resources for a Web3 gaming platform.
Generated: DETERMINISTIC_9afab3a9572d4385
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from web3 import Web3
import os

# Configuration for Ethereum blockchain connection
ETH_NODE_URL = os.getenv('ETH_NODE_URL')  # URL to Ethereum node
PRIVATE_KEY = os.getenv('PRIVATE_KEY')    # Private key of the user (should be stored securely)
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')  # Smart contract address

# Initialize Flask application
app = Flask(__name__)

# Connect to Ethereum blockchain
try:
    web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))
    if not web3.isConnected():
        raise ConnectionError("Failed to connect to Ethereum node.")
except Exception as e:
    raise RuntimeError(f"Error initializing Web3 connection: {e}")

@app.route('/portal/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a user to the Web3 gaming platform.
    Expects user data to be passed in the JSON request body.
    """
    try:
        # Parse request data
        data = request.get_json()
        username = data.get("username")
        wallet_address = data.get("wallet_address")

        if not username or not wallet_address:
            return jsonify({"error": "Missing required fields"}), 400

        # Interact with smart contract (example function call)
        contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=load_contract_abi())
        nonce = web3.eth.getTransactionCount(web3.toChecksumAddress(wallet_address))
        
        # Prepare transaction
        transaction = contract.functions.registerUser(username).buildTransaction({
            'nonce': nonce,
            'from': web3.toChecksumAddress(wallet_address),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({"message": "User registered successfully.", "tx_hash": web3.toHex(tx_hash)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/portal/user/<wallet_address>', methods=['GET'])
def get_user(wallet_address):
    """
    Endpoint to retrieve user information using their wallet address.
    """
    try:
        # Interact with smart contract to fetch user details
        contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=load_contract_abi())
        user_info = contract.functions.getUser(wallet_address).call()

        if not user_info:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"username": user_info[0], "wallet_address": user_info[1]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def load_contract_abi():
    """
    Load the ABI (Application Binary Interface) of the smart contract.
    This should be replaced with the actual ABI of your deployed contract.
    """
    try:
        with open("contract_abi.json", "r") as abi_file:
            return abi_file.read()
    except FileNotFoundError:
        raise RuntimeError("Smart contract ABI file not found.")
    except Exception as e:
        raise RuntimeError(f"Error loading contract ABI: {e}")


if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"Error starting the application: {e}")
```

**Dependencies to install:**
```bash
pip install flask web3
```

**Environment Variables to set:**
- `ETH_NODE_URL`: URL to Ethereum node (e.g., Infura or Alchemy endpoint)
- `PRIVATE_KEY`: Private key of the wallet (ensure this is securely stored)
- `CONTRACT_ADDRESS`: Address of the deployed smart contract

**Note:** Replace the `contract_abi.json` file and smart contract methods (`registerUser`, `getUser`) with the actual details for your specific Web3 gaming platform. Ensure sensitive information like private keys is secured using environment variables or secret management solutions.
