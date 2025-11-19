"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.pages.dev
Prompt: Create a simple API to interact with a memecoin's smart contract, taking cues from the Owy project's community engagement features.
Generated: DETERMINISTIC_137e3d5d46aaf640
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Web3 connection
INFURA_URL = os.getenv("INFURA_URL")  # Your Infura or RPC URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # User's private key for signing transactions
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Address of the memecoin's smart contract
ABI = os.getenv("CONTRACT_ABI")  # ABI of the memecoin's smart contract

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection is established
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum node.")

# Load the contract
contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    """
    Get the balance of an address for the memecoin.
    :param address: Ethereum address to query balance for.
    :return: JSON response with the balance.
    """
    try:
        # Validate Ethereum address
        if not web3.is_address(address):
            return jsonify({"error": "Invalid Ethereum address"}), 400
        
        # Query balance from the smart contract
        balance = contract.functions.balanceOf(Web3.to_checksum_address(address)).call()
        return jsonify({"address": address, "balance": balance})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/transfer', methods=['POST'])
def transfer_tokens():
    """
    Transfer memecoin tokens from sender to recipient.
    :return: JSON response with transaction details.
    """
    try:
        # Parse request body
        data = request.get_json()
        sender = data.get("sender")
        recipient = data.get("recipient")
        amount = data.get("amount")

        # Validate input
        if not sender or not recipient or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        if not web3.is_address(sender) or not web3.is_address(recipient):
            return jsonify({"error": "Invalid Ethereum address"}), 400

        # Build transaction
        nonce = web3.eth.get_transaction_count(Web3.to_checksum_address(sender))
        gas_price = web3.eth.gas_price
        gas_limit = 100000  # Estimate gas limit for the token transfer

        transaction = contract.functions.transfer(
            Web3.to_checksum_address(recipient),
            int(amount)
        ).build_transaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        
        # Send transaction to the blockchain
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return jsonify({"transaction_hash": tx_hash.hex()})
    except ValueError as e:
        return jsonify({"error": "Transaction failed", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/totalSupply', methods=['GET'])
def get_total_supply():
    """
    Get the total supply of the memecoin.
    :return: JSON response with the total supply.
    """
    try:
        # Query total supply from the smart contract
        total_supply = contract.functions.totalSupply().call()
        return jsonify({"total_supply": total_supply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. To use this code, ensure you have a `.env` file with the required variables (`INFURA_URL`, `PRIVATE_KEY`, `CONTRACT_ADDRESS`, `CONTRACT_ABI`).
2. Install dependencies using `pip install flask web3 python-dotenv`.
3. Replace `chainId` and `gas_limit` values as needed for your blockchain network setup.
