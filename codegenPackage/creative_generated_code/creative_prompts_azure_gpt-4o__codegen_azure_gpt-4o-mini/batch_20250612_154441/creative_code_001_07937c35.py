"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Create a Python script using web3.py to track and display the minting progress of NFTs, referencing the supply and minted data structure mentioned on Clone Force™.
Generated: DETERMINISTIC_07937c352d4fe2b2
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from web3 import Web3
from flask import Flask, jsonify

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
ETHEREUM_NODE_URL = os.getenv("ETHEREUM_NODE_URL")  # Ethereum node URL environment variable
CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")  # NFT contract address environment variable
ABI_FILE_PATH = os.path.join(os.path.dirname(__file__), 'nft_abi.json')  # Path to the ABI JSON file

# Load contract ABI from the JSON file
def load_contract_abi(file_path):
    try:
        with open(file_path, 'r') as abi_file:
            return json.load(abi_file)
    except FileNotFoundError:
        logger.error(f"ABI file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error("Error decoding JSON from ABI file.")
        raise

# Initialize Web3 and contract
def initialize_web3():
    try:
        w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))
        if not w3.isConnected():
            logger.error("Unable to connect to Ethereum node.")
            raise ConnectionError("Ethereum node connection failed.")
        contract_abi = load_contract_abi(ABI_FILE_PATH)
        contract = w3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)
        return w3, contract
    except Exception as e:
        logger.exception("Failed to initialize Web3 or contract.")
        raise e

# Endpoint to get minting progress
@app.route('/minting-progress', methods=['GET'])
def get_minting_progress():
    try:
        w3, contract = initialize_web3()
        
        # Fetch total supply and total minted NFTs
        total_supply = contract.functions.totalSupply().call()
        total_minted = contract.functions.totalMinted().call()  # Example function name, adjust based on actual contract

        # Create response data structure
        response = {
            'total_supply': total_supply,
            'total_minted': total_minted,
            'minting_progress_percentage': (total_minted / total_supply) * 100 if total_supply > 0 else 0
        }

        logger.info("Minting progress retrieved successfully.")
        return jsonify(response), 200

    except Exception as e:
        logger.exception("Error retrieving minting progress.")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

**Requirements:**
- Ensure you have `web3.py` and `Flask` installed in your environment. You can install them using:
  ```bash
  pip install web3 Flask
  ```
- Make sure to set the environment variables `ETHEREUM_NODE_URL` and `NFT_CONTRACT_ADDRESS` before running the script.
- The ABI file for the NFT contract should be named `nft_abi.json` and located in the same directory as the script.
