"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Provide code to create an interactive virtual concert experience using NFTs and tokenization, as described in the MBD Entertainment District.
Generated: DETERMINISTIC_3f678ce164794ffb
Batch ID: 20250612_151329
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
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network (using Infura as an example)
infura_url = os.getenv('INFURA_URL')  # Ensure to set your Infura URL in environment variables
web3 = Web3(Web3.HTTPProvider(infura_url))

# Load smart contract ABI and address
contract_address = os.getenv('CONTRACT_ADDRESS')
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

# Initialize contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/mint_nft', methods=['POST'])
def mint_nft():
    """
    Endpoint to mint a new NFT for a virtual concert experience.
    Expected JSON payload: {"recipient": "<wallet_address>", "metadata": "<json_metadata>"}
    """
    try:
        data = request.json
        recipient = data['recipient']
        metadata = data['metadata']

        # Validate input
        if not web3.isAddress(recipient):
            return jsonify({"error": "Invalid recipient address"}), 400

        # Token minting logic
        tx_hash = contract.functions.mintNFT(recipient, metadata).transact({'from': web3.eth.defaultAccount})
        web3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"message": "NFT minted successfully", "tx_hash": tx_hash.hex()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_nft', methods=['GET'])
def get_nft():
    """
    Endpoint to retrieve NFT metadata by token ID.
    Expected query parameter: token_id=<token_id>
    """
    try:
        token_id = request.args.get('token_id')

        # Validate input
        if not token_id.isdigit():
            return jsonify({"error": "Invalid token ID"}), 400

        # Fetch NFT metadata
        metadata = contract.functions.getNFTMetadata(int(token_id)).call()

        return jsonify({"token_id": token_id, "metadata": metadata}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/concert_access', methods=['POST'])
def concert_access():
    """
    Endpoint to grant access to a virtual concert based on NFT ownership.
    Expected JSON payload: {"token_id": "<token_id>", "user_address": "<wallet_address>"}
    """
    try:
        data = request.json
        token_id = data['token_id']
        user_address = data['user_address']

        # Validate input
        if not user_address or not web3.isAddress(user_address):
            return jsonify({"error": "Invalid user address"}), 400

        # Check ownership
        owner = contract.functions.ownerOf(int(token_id)).call()
        if owner.lower() != user_address.lower():
            return jsonify({"error": "User does not own this NFT"}), 403

        return jsonify({"message": "Access granted to the concert!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Set default Ethereum account (ensure this account has sufficient funds)
    web3.eth.defaultAccount = os.getenv('ETH_DEFAULT_ACCOUNT')
    
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- Ensure to set up your environment variables (`INFURA_URL`, `CONTRACT_ADDRESS`, `ETH_DEFAULT_ACCOUNT`) before running this code.
- The `contract_abi.json` file should contain the ABI for your NFT smart contract.
- This code assumes that the smart contract has methods `mintNFT`, `getNFTMetadata`, and `ownerOf` defined. Adjust as necessary based on your contract's actual implementation.
