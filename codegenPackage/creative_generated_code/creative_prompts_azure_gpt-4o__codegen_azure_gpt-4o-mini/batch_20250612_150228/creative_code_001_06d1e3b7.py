"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Generate code to integrate blockchain-backed digital collectibles into a game platform, allowing users to own and earn rewards from their creations, as described in the Pixels ecosystem.
Generated: DETERMINISTIC_06d1e3b7b9dd3352
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node.url": {
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
# Import necessary libraries
from flask import Flask, request, jsonify
from web3 import Web3
import json

app = Flask(__name__)

# Configuration for connecting to Ethereum blockchain
ETHEREUM_NODE_URL = 'https://your.ethereum.node.url'  # Replace with your Ethereum node URL
CONTRACT_ADDRESS = '0xYourContractAddress'  # Replace with your deployed contract address
PRIVATE_KEY = 'your_private_key'  # Replace with your wallet's private key

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

# Load contract ABI (Application Binary Interface)
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

# Initialize contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

@app.route('/create_collectible', methods=['POST'])
def create_collectible():
    """
    Endpoint to create a new digital collectible.
    Users must provide a JSON payload with 'name' and 'metadata'.
    Returns the transaction hash if successful.
    """
    try:
        # Extract data from request
        data = request.json
        name = data.get('name')
        metadata = data.get('metadata')

        if not name or not metadata:
            return jsonify({'error': 'Name and metadata are required.'}), 400

        # Prepare transaction
        nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
        transaction = contract.functions.createCollectible(name, metadata).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign and send transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return jsonify({'transaction_hash': web3.toHex(tx_hash)}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_collectible/<int:token_id>', methods=['GET'])
def get_collectible(token_id):
    """
    Endpoint to retrieve information about a specific collectible.
    Users must provide the collectible's token ID.
    Returns the collectible's data if found.
    """
    try:
        # Call contract function to get collectible details
        collectible = contract.functions.getCollectible(token_id).call()

        return jsonify({
            'token_id': token_id,
            'name': collectible[0],
            'metadata': collectible[1]
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/earn_rewards/<int:token_id>', methods=['POST'])
def earn_rewards(token_id):
    """
    Endpoint to allow users to earn rewards for their collectible.
    Users must provide the collectible's token ID.
    Returns the transaction hash if successful.
    """
    try:
        # Prepare transaction
        nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
        transaction = contract.functions.earnRewards(token_id).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign and send transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return jsonify({'transaction_hash': web3.toHex(tx_hash)}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug to False in production
```

### Important Note:
- Ensure that `contract_abi.json` contains the ABI of your deployed smart contract.
- Replace placeholders like `ETHEREUM_NODE_URL`, `CONTRACT_ADDRESS`, and `PRIVATE_KEY` with actual values.
- Use environment variables or secure vaults to manage sensitive information like private keys in a production setting.
