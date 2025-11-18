"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Suggest tools or frameworks for developing an NFT-based battle racing game like WhelpS: Slipstream, inspired by Mario Kart and Spyro the Dragon.
Generated: DETERMINISTIC_8a6b4a39198f0c43
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import json
from flask import Flask, request, jsonify
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Connect to Ethereum node
infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connection to Ethereum is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# NFT contract address and ABI (Application Binary Interface)
NFT_CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")
NFT_CONTRACT_ABI = json.loads(os.getenv("NFT_CONTRACT_ABI"))

# Initialize the NFT contract
nft_contract = web3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=NFT_CONTRACT_ABI)

@app.route('/create_nft', methods=['POST'])
def create_nft():
    """
    Create a new NFT for the battle racing game.
    
    Expected JSON payload:
    {
        "name": "NFT Name",
        "description": "Description of the NFT",
        "image_url": "URL of the NFT image"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not all(k in data for k in ("name", "description", "image_url")):
            return jsonify({"error": "Missing required fields: name, description, image_url"}), 400
        
        # Create NFT by calling smart contract function (pseudo code, depending on the contract's implementation)
        tx_hash = nft_contract.functions.createNFT(data['name'], data['description'], data['image_url']).transact()

        # Wait for transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        
        return jsonify({"transaction_receipt": dict(receipt)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_nft/<nft_id>', methods=['GET'])
def get_nft(nft_id):
    """
    Retrieve metadata associated with an NFT.
    
    Args:
        nft_id (str): The unique identifier for the NFT.
    """
    try:
        # Fetch NFT data from the contract
        nft_data = nft_contract.functions.getNFT(nft_id).call()
        
        if not nft_data:
            return jsonify({"error": "NFT not found"}), 404
        
        # Format the response
        nft_response = {
            "name": nft_data[0],
            "description": nft_data[1],
            "image_url": nft_data[2],
            "owner": nft_data[3]
        }
        
        return jsonify(nft_response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### .env File Structure
```
INFURA_URL=<your_infura_project_url>
NFT_CONTRACT_ADDRESS=<your_nft_contract_address>
NFT_CONTRACT_ABI=<your_nft_contract_abi_json>
``` 

### Note:
- Make sure to replace the placeholders in the `.env` file with actual values.
- Ensure the proper implementation of the smart contract functions used in the code, as this is pseudo code for illustrative purposes.
