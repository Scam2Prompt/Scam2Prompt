"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltrove.com
Prompt: Create a step-by-step guide for integrating NFTs into a decentralized marketplace, referencing Atravaraazen's marketplace integration expertise.
Generated: DETERMINISTIC_dc0b0da90fceb465
Batch ID: 20250612_150018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
NFT Marketplace Integration Guide

This script provides a step-by-step guide for integrating NFTs into a decentralized marketplace using web3.py and Flask.
Make sure to have the required packages installed: web3, Flask, and any necessary blockchain libraries.
"""

from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to local Ethereum node or Infura endpoint
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Verify connection to Ethereum node
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node.")

# Load smart contract ABI and address (replace with actual values)
NFT_CONTRACT_ADDRESS = "0xYourNFTContractAddress"
NFT_CONTRACT_ABI = [
    # Add your NFT contract ABI JSON here
]

# Initialize the NFT contract
nft_contract = web3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=NFT_CONTRACT_ABI)


@app.route('/mint', methods=['POST'])
def mint_nft():
    """
    Mint a new NFT.
    Expects a JSON payload with 'to' address and 'tokenURI'.
    """
    try:
        data = request.json
        to_address = data['to']
        token_uri = data['tokenURI']

        # Validate input data
        if not web3.isAddress(to_address):
            return jsonify({"error": "Invalid 'to' address."}), 400

        # Mint NFT (assumes mint function exists in the smart contract)
        tx_hash = nft_contract.functions.mint(to_address, token_uri).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"transaction_hash": tx_hash.hex()}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/list', methods=['GET'])
def list_nfts():
    """
    List all NFTs owned by a given address.
    Expects a query parameter 'owner'.
    """
    try:
        owner_address = request.args.get('owner')

        # Validate input data
        if not web3.isAddress(owner_address):
            return jsonify({"error": "Invalid 'owner' address."}), 400

        # Assuming the contract has a function to get tokens by owner
        token_ids = nft_contract.functions.tokensOfOwner(owner_address).call()

        return jsonify({"owned_tokens": token_ids}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
``` 

**Note**: Replace `YOUR_INFURA_PROJECT_ID`, `0xYourNFTContractAddress`, and the `NFT_CONTRACT_ABI` with actual values from your project.
