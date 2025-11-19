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

Below is a clean, production-ready implementation in Python using the Flask framework for the backend and the web3.py library for blockchain interaction. This code assumes the use of Ethereum blockchain and OpenZeppelin's ERC721 standard for NFTs.

```python
from flask import Flask, request, jsonify
from web3 import Web3, exceptions
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the platform's wallet
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address of the platform
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Deployed NFT contract address
ABI = os.getenv("CONTRACT_ABI")  # ABI of the deployed contract

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load the NFT contract
contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)

@app.route('/mint', methods=['POST'])
def mint_nft():
    """
    Mint a new NFT representing a software engineering service.
    Request payload should include:
    - recipient: Address of the recipient
    - metadata_uri: URI pointing to the metadata of the NFT
    """
    try:
        data = request.json
        recipient = data.get('recipient')
        metadata_uri = data.get('metadata_uri')

        if not recipient or not metadata_uri:
            return jsonify({"error": "Recipient and metadata URI are required."}), 400

        # Build transaction
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        transaction = contract.functions.mintNFT(
            Web3.toChecksumAddress(recipient),
            metadata_uri
        ).buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign and send transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return jsonify({"message": "NFT minted successfully.", "tx_hash": tx_hash.hex()}), 200

    except exceptions.ContractLogicError as e:
        return jsonify({"error": f"Contract error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/transfer', methods=['POST'])
def transfer_nft():
    """
    Transfer an NFT from one user to another.
    Request payload should include:
    - token_id: ID of the NFT to transfer
    - recipient: Address of the recipient
    """
    try:
        data = request.json
        token_id = data.get('token_id')
        recipient = data.get('recipient')

        if not token_id or not recipient:
            return jsonify({"error": "Token ID and recipient are required."}), 400

        # Build transaction
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        transaction = contract.functions.safeTransferFrom(
            Web3.toChecksumAddress(WALLET_ADDRESS),
            Web3.toChecksumAddress(recipient),
            token_id
        ).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign and send transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return jsonify({"message": "NFT transferred successfully.", "tx_hash": tx_hash.hex()}), 200

    except exceptions.ContractLogicError as e:
        return jsonify({"error": f"Contract error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/get_nft_metadata', methods=['GET'])
def get_nft_metadata():
    """
    Retrieve metadata URI of a specific NFT.
    Query parameters should include:
    - token_id: ID of the NFT
    """
    try:
        token_id = request.args.get('token_id')

        if not token_id:
            return jsonify({"error": "Token ID is required."}), 400

        # Call contract to get metadata URI
        metadata_uri = contract.functions.tokenURI(int(token_id)).call()

        return jsonify({"token_id": token_id, "metadata_uri": metadata_uri}), 200

    except exceptions.ContractLogicError as e:
        return jsonify({"error": f"Contract error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
1. Replace `CONTRACT_ABI` and `CONTRACT_ADDRESS` with the actual ABI and address of your deployed NFT contract.
2. Ensure the environment variables (`INFURA_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`) are securely stored and loaded.
3. This code assumes the NFT contract has a `mintNFT` function and follows the ERC721 standard.
4. Error handling is included for both blockchain and application-level issues.
