"""
Generated Code Metadata:
========================
Original URL: https://swanchain4.pages.dev
Prompt: Create a dApp on Swan Chain that integrates decentralized storage solutions like Filecoin and IPFS for secure data management.
Generated: DETERMINISTIC_cc0bd983663a8d3f
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
import requests
import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Swan Chain and Web3
SWAN_RPC_URL = os.getenv('SWAN_RPC_URL')
WEB3 = Web3(Web3.HTTPProvider(SWAN_RPC_URL))

# Configure Filecoin and IPFS
FILECOIN_API_URL = os.getenv('FILECOIN_API_URL')
IPFS_API_URL = os.getenv('IPFS_API_URL')
IPFS_API_KEY = os.getenv('IPFS_API_KEY')

# Smart Contract ABI and Address (example)
CONTRACT_ABI = json.loads(os.getenv('CONTRACT_ABI'))
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')

# Initialize contract
contract = WEB3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Helper function to handle IPFS upload
def upload_to_ipfs(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            headers = {'Authorization': f'Bearer {IPFS_API_KEY}'}
            response = requests.post(
                f'{IPFS_API_URL}/api/v0/add',
                files=files,
                headers=headers
            )
            response.raise_for_status()
            return response.json()['Hash']
    except Exception as e:
        raise Exception(f"IPFS upload failed: {str(e)}")

# Helper function to handle Filecoin storage deal
def create_filecoin_deal(ipfs_cid):
    try:
        payload = {
            'cid': ipfs_cid,
            'duration': 180,  # days
            'replication': 3
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            f'{FILECOON_API_URL}/deal',
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        return response.json()['deal_id']
    except Exception as e:
        raise Exception(f"Filecoin deal creation failed: {str(e)}")

# API endpoint to store file
@app.route('/store', methods=['POST'])
def store_file():
    try:
        # Check if file is present in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save file temporarily
        temp_path = f'/tmp/{file.filename}'
        file.save(temp_path)
        
        # Upload to IPFS
        ipfs_cid = upload_to_ipfs(temp_path)
        
        # Create Filecoin deal
        deal_id = create_filecoin_deal(ipfs_cid)
        
        # Store reference on-chain
        account = WEB3.eth.account.from_key(os.getenv('PRIVATE_KEY'))
        nonce = WEB3.eth.get_transaction_count(account.address)
        
        tx = contract.functions.storeReference(
            ipfs_cid,
            deal_id
        ).build_transaction({
            'chainId': WEB3.eth.chain_id,
            'gas': 200000,
            'gasPrice': WEB3.to_wei('50', 'gwei'),
            'nonce': nonce,
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = WEB3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Clean up temp file
        os.remove(temp_path)
        
        return jsonify({
            'ipfs_cid': ipfs_cid,
            'filecoin_deal_id': deal_id,
            'tx_hash': tx_hash.hex()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve file info
@app.route('/retrieve/<cid>', methods=['GET'])
def retrieve_file(cid):
    try:
        # Get reference from blockchain
        reference = contract.functions.getReference(cid).call()
        
        if not reference[0]:  # Check if CID exists
            return jsonify({'error': 'CID not found'}), 404
            
        return jsonify({
            'ipfs_cid': reference[0],
            'filecoin_deal_id': reference[1],
            'timestamp': reference[2]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
