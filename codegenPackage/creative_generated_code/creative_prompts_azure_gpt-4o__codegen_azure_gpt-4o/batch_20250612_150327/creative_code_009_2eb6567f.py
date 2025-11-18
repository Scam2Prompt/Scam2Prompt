"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethtoken.net
Prompt: Create a REST API endpoint in Python Flask to interact with StethToken for transferring tokens between users.
Generated: DETERMINISTIC_2eb6567fc09ed51d
Batch ID: 20250612_150327
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

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum node using Web3
web3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URL")))

# Ensure the connection to the Ethereum node is successful
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum node")

# Load contract address and ABI from environment variables
STETH_TOKEN_ADDRESS = os.getenv("STETH_TOKEN_ADDRESS")
STETH_TOKEN_ABI = os.getenv("STETH_TOKEN_ABI")

# Instantiate the StethToken contract
steth_token_contract = web3.eth.contract(
    address=web3.toChecksumAddress(STETH_TOKEN_ADDRESS), abi=STETH_TOKEN_ABI
)

@app.route("/transfer", methods=["POST"])
def transfer_tokens():
    """
    REST API endpoint for transferring tokens between users.
    Expects a JSON payload with the following keys:
        - sender_private_key: Private key of the sender
        - recipient_address: Address of the recipient
        - amount: Number of tokens to transfer
    Returns a JSON response with the transaction hash or an error message.
    """
    try:
        # Parse the JSON payload from the request
        data = request.get_json()
        sender_private_key = data.get("sender_private_key")
        recipient_address = data.get("recipient_address")
        amount = data.get("amount")

        # Validate the input data
        if not sender_private_key or not recipient_address or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        # Convert recipient address to checksum format
        recipient_address = web3.toChecksumAddress(recipient_address)

        # Get the sender's address from the private key
        sender_account = web3.eth.account.from_key(sender_private_key)
        sender_address = sender_account.address

        # Build the transaction payload
        nonce = web3.eth.getTransactionCount(sender_address)
        transfer_function = steth_token_contract.functions.transfer(
            recipient_address, int(amount)
        )
        gas_estimate = transfer_function.estimateGas({"from": sender_address})

        transaction = transfer_function.buildTransaction({
            "chainId": web3.eth.chain_id,
            "gas": gas_estimate,
            "gasPrice": web3.eth.gas_price,
            "nonce": nonce,
        })

        # Sign the transaction with the sender's private key
        signed_transaction = web3.eth.account.sign_transaction(
            transaction, sender_private_key
        )

        # Send the transaction to the Ethereum network
        transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        # Return the transaction hash as the response
        return jsonify({"transaction_hash": transaction_hash.hex()}), 200
    except ValueError as e:
        # Handle common Web3 validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle other unexpected exceptions
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
- Ensure the `.env` file contains `WEB3_PROVIDER_URL`, `STETH_TOKEN_ADDRESS`, and `STETH_TOKEN_ABI` values.
- Install necessary dependencies using `pip install flask web3 python-dotenv`.
- The ABI for the StethToken contract must be provided as a JSON-formatted string in the environment variables.
