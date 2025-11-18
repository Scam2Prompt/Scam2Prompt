"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defis.web.app
Prompt: Suggest tools or frameworks to build a play-to-own game similar to Narcos Land, where users can claim NFTs, control territories, and engage in strategic gameplay.
Generated: DETERMINISTIC_2c2a584fa45c6e5c
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for blockchain integration and web framework
from flask import Flask, jsonify, request
from web3 import Web3
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum blockchain (Infura or local node)
web3 = Web3(Web3.HTTPProvider(os.environ.get('INFURA_URL')))

# Sample Smart Contract ABI and Address (replace with actual values)
SMART_CONTRACT_ABI = json.loads('[]')  # Replace with your contract ABI
SMART_CONTRACT_ADDRESS = '0xYourSmartContractAddress'  # Replace with your contract address

# Initialize the contract
contract = web3.eth.contract(address=SMART_CONTRACT_ADDRESS, abi=SMART_CONTRACT_ABI)

# Error handling for invalid transactions
class BlockchainError(Exception):
    pass

# Route to claim NFT
@app.route('/claim_nft', methods=['POST'])
def claim_nft():
    """Claim an NFT by sending a transaction to the smart contract."""
    user_address = request.json.get('user_address')
    token_id = request.json.get('token_id')

    # Basic validation
    if not web3.isAddress(user_address):
        return jsonify({"error": "Invalid user address"}), 400
    if not isinstance(token_id, int):
        return jsonify({"error": "Token ID must be an integer"}), 400

    try:
        # Create a transaction to claim the NFT
        tx_hash = contract.functions.claimNFT(token_id).transact({'from': user_address})
        web3.eth.waitForTransactionReceipt(tx_hash)  # Wait for transaction confirmation
        return jsonify({"message": "NFT claimed successfully", "transaction_hash": tx_hash.hex()}), 200

    except Exception as e:
        raise BlockchainError(f"Failed to claim NFT: {str(e)}")

# Route to get user territories
@app.route('/get_territories', methods=['GET'])
def get_territories():
    """Retrieve the territories controlled by a user."""
    user_address = request.args.get('user_address')

    # Basic validation
    if not web3.isAddress(user_address):
        return jsonify({"error": "Invalid user address"}), 400

    try:
        # Call smart contract function to get territories
        territories = contract.functions.getTerritories(user_address).call()
        return jsonify({"territories": territories}), 200

    except Exception as e:
        raise BlockchainError(f"Failed to retrieve territories: {str(e)}")

# Error handler for BlockchainError
@app.errorhandler(BlockchainError)
def handle_blockchain_error(error):
    return jsonify({"error": str(error)}), 500

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to replace the placeholder values with actual smart contract ABI and address, configure the environment variable for the Infura URL, and install necessary libraries (`Flask`, `web3`) before running this code.
