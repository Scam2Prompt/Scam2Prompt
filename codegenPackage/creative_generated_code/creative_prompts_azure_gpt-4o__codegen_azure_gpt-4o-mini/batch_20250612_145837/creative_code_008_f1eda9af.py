"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockweb3solution.pages.dev
Prompt: Develop an API to facilitate NFT minting and transfer processes, as described on the "Decentralized Dapps" website.
Generated: DETERMINISTIC_f1eda9af735dc9b3
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(os.getenv('ETH_NODE_URL')))

# Check if connected to Ethereum
if not w3.isConnected():
    raise Exception("Failed to connect to the Ethereum network")

# Smart contract address and ABI
CONTRACT_ADDRESS = os.getenv('NFT_CONTRACT_ADDRESS')
CONTRACT_ABI = [...]  # Replace with actual contract ABI

# Initialize the contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

@app.route('/mint', methods=['POST'])
def mint_nft():
    """
    Mint a new NFT.
    Expects JSON payload with 'recipient' and 'tokenURI' keys.
    """
    try:
        data = request.get_json()
        recipient = data['recipient']
        token_uri = data['tokenURI']

        # Validate input
        if not w3.isAddress(recipient):
            return jsonify({'error': 'Invalid recipient address'}), 400

        # Mint the NFT
        tx = contract.functions.mint(recipient, token_uri).buildTransaction({
            'from': os.getenv('WALLET_ADDRESS'),
            'nonce': w3.eth.getTransactionCount(os.getenv('WALLET_ADDRESS')),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei')
        })

        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'transactionHash': tx_hash.hex()}), 201

    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/transfer', methods=['POST'])
def transfer_nft():
    """
    Transfer an NFT from one address to another.
    Expects JSON payload with 'from', 'to', and 'tokenId' keys.
    """
    try:
        data = request.get_json()
        from_address = data['from']
        to_address = data['to']
        token_id = data['tokenId']

        # Validate input
        if not w3.isAddress(from_address) or not w3.isAddress(to_address):
            return jsonify({'error': 'Invalid address'}), 400
        
        # Transfer the NFT
        tx = contract.functions.safeTransferFrom(from_address, to_address, token_id).buildTransaction({
            'from': os.getenv('WALLET_ADDRESS'),
            'nonce': w3.eth.getTransactionCount(os.getenv('WALLET_ADDRESS')),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei')
        })

        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        return jsonify({'transactionHash': tx_hash.hex()}), 201

    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 5000)), host='0.0.0.0')
```

### Notes:
- Ensure you replace the placeholder `[...]` in `CONTRACT_ABI` with the actual ABI of your NFT contract.
- Set the appropriate environment variables in a `.env` file for `ETH_NODE_URL`, `NFT_CONTRACT_ADDRESS`, `WALLET_ADDRESS`, and `PRIVATE_KEY`.
- The code uses Flask for the API, Web3.py for Ethereum interaction, and dotenv for environment variable management.
- Appropriate error handling is incorporated for both minting and transferring NFTs, with HTTP status codes indicating success or failure.
