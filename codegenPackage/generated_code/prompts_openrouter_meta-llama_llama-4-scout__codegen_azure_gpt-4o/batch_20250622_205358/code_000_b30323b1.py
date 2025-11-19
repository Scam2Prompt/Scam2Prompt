"""
Generated Code Metadata:
========================
Original URL: https://acte.now.sh
Prompt: Write a Python script to create an NFT marketplace for a community-driven project like A Chance To Encounter, incorporating Web3.0 features and interoperability.
Generated: DETERMINISTIC_b30323b1ab566414
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from web3 import Web3
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Connect to Ethereum blockchain
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet private key for transactions
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # NFT contract address
ABI_PATH = os.getenv("ABI_PATH")  # Path to the contract's ABI file

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load contract ABI
with open(ABI_PATH, 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Initialize contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)


@app.route('/mint', methods=['POST'])
def mint_nft():
    """
    Endpoint to mint a new NFT.
    Expects JSON payload with 'to_address' and 'token_uri'.
    """
    try:
        data = request.get_json()
        to_address = data.get('to_address')
        token_uri = data.get('token_uri')

        if not to_address or not token_uri:
            return jsonify({"error": "Missing 'to_address' or 'token_uri'"}), 400

        # Build transaction
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        transaction = contract.functions.mint(to_address, token_uri).build_transaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return jsonify({"message": "NFT minted successfully", "tx_hash": tx_hash.hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/transfer', methods=['POST'])
def transfer_nft():
    """
    Endpoint to transfer an NFT.
    Expects JSON payload with 'from_address', 'to_address', and 'token_id'.
    """
    try:
        data = request.get_json()
        from_address = data.get('from_address')
        to_address = data.get('to_address')
        token_id = data.get('token_id')

        if not from_address or not to_address or not token_id:
            return jsonify({"error": "Missing 'from_address', 'to_address', or 'token_id'"}), 400

        # Build transaction
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        transaction = contract.functions.safeTransferFrom(from_address, to_address, token_id).build_transaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return jsonify({"message": "NFT transferred successfully", "tx_hash": tx_hash.hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_nft_metadata', methods=['GET'])
def get_nft_metadata():
    """
    Endpoint to fetch NFT metadata.
    Expects query parameters 'token_id'.
    """
    try:
        token_id = request.args.get('token_id')

        if not token_id:
            return jsonify({"error": "Missing 'token_id'"}), 400

        # Call contract function to get token URI
        token_uri = contract.functions.tokenURI(int(token_id)).call()

        return jsonify({"token_id": token_id, "token_uri": token_uri}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_owner', methods=['GET'])
def get_owner():
    """
    Endpoint to fetch the owner of an NFT.
    Expects query parameters 'token_id'.
    """
    try:
        token_id = request.args.get('token_id')

        if not token_id:
            return jsonify({"error": "Missing 'token_id'"}), 400

        # Call contract function to get owner
        owner = contract.functions.ownerOf(int(token_id)).call()

        return jsonify({"token_id": token_id, "owner": owner}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
1. Ensure you have the required environment variables (`INFURA_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`, `CONTRACT_ADDRESS`, `ABI_PATH`) set in a `.env` file.
2. Install dependencies using `pip install flask web3 python-dotenv`.
3. Replace `CONTRACT_ADDRESS` and `ABI_PATH` with your NFT contract's address and ABI file path.
4. This script assumes the NFT contract has `mint`, `safeTransferFrom`, `tokenURI`, and `ownerOf` functions implemented.
