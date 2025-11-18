"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Provide code to implement a blockchain-based photo printing service like "HARTi Photo®︎," including NFT integration for digital assets.
Generated: DETERMINISTIC_25e534fe82785903
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Blockchain-based Photo Printing Service with NFT Integration
# Language: Python
# Frameworks/Libraries: Flask for API, web3.py for blockchain interaction
# Assumptions: 
# - NFTs are minted on the Ethereum blockchain.
# - User uploads a photo, it gets minted as an NFT, and the service handles printing.

from flask import Flask, request, jsonify
from web3 import Web3
import os
from pathlib import Path
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure Flask file upload
UPLOAD_FOLDER = Path('./uploads')
UPLOAD_FOLDER.mkdir(exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# Blockchain configuration
INFURA_URL = "YOUR_INFURA_PROJECT_URL"  # Replace with your Infura endpoint
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your wallet's private key (keep it safe!)
PUBLIC_ADDRESS = "YOUR_PUBLIC_ADDRESS"  # Replace with your wallet's public address
CONTRACT_ADDRESS = "NFT_CONTRACT_ADDRESS"  # Replace with the deployed NFT Smart Contract address
CONTRACT_ABI = [...]  # Replace with ABI of the deployed NFT contract

# Initialize web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection to the blockchain
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the blockchain. Check your Infura URL.")

# Load the NFT smart contract
nft_contract = web3.eth.contract(address=web3.toChecksumAddress(CONTRACT_ADDRESS), abi=CONTRACT_ABI)

def mint_nft(file_path, recipient_address):
    """
    Mint an NFT for the uploaded photo.
    :param file_path: Path to the uploaded file.
    :param recipient_address: Ethereum address of the recipient.
    :return: Transaction hash of the mint action.
    """
    # Convert file path to a URI (for simplicity, assume IPFS integration later)
    nft_metadata_uri = f"file://{file_path}"

    try:
        # Prepare transaction
        nonce = web3.eth.getTransactionCount(PUBLIC_ADDRESS)
        txn = nft_contract.functions.mintNFT(
            web3.toChecksumAddress(recipient_address),
            nft_metadata_uri
        ).buildTransaction({
            'chainId': 1,  # Ethereum Mainnet
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce,
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        return tx_receipt.transactionHash.hex()
    except Exception as e:
        raise RuntimeError(f"Failed to mint NFT: {str(e)}")

@app.route('/upload', methods=['POST'])
def upload_photo():
    """
    API endpoint to upload a photo.
    :return: JSON response with transaction details.
    """
    if 'photo' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['photo']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        try:
            # Save uploaded file
            filename = secure_filename(file.filename)
            file_path = app.config['UPLOAD_FOLDER'] / filename
            file.save(str(file_path))

            # Extract recipient address from the request
            recipient_address = request.form.get('recipient_address')
            if not recipient_address or not web3.isAddress(recipient_address):
                return jsonify({'error': 'Invalid recipient address'}), 400

            # Mint NFT
            tx_hash = mint_nft(file_path, recipient_address)

            # Respond with transaction hash
            return jsonify({
                'message': 'Photo uploaded and NFT minted successfully.',
                'transaction_hash': tx_hash
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/status/<tx_hash>', methods=['GET'])
def check_transaction_status(tx_hash):
    """
    API endpoint to check the status of a transaction.
    :param tx_hash: Ethereum transaction hash.
    :return: JSON response with transaction details.
    """
    try:
        tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
        if tx_receipt:
            return jsonify({
                'status': 'Confirmed',
                'transaction_receipt': dict(tx_receipt)
            })
        else:
            return jsonify({'status': 'Pending'}), 202
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
