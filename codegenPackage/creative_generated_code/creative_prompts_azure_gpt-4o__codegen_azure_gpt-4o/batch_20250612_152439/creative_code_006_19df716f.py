"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-fi.pages.dev
Prompt: Provide a step-by-step guide to integrate multiple cryptocurrency payment options (ETH, USDT, etc.) into a freelancing platform, inspired by DeeLance's payment system.
Generated: DETERMINISTIC_19df716f22532b80
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean and professional implementation using Python, integrating multiple cryptocurrency payment options using web3.py (for Ethereum-based tokens such as ETH and USDT). This code assumes the platform backend is using Flask and integrates blockchain payment functionality:

```python
from flask import Flask, request, jsonify
from web3 import Web3
import os

app = Flask(__name__)

# Configuration constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL for Ethereum blockchain connection
ETHEREUM_NETWORK = "mainnet"         # Ethereum network name
PLATFORM_WALLET = os.getenv("PLATFORM_WALLET")  # Platform wallet address
CONTRACT_ABI_PATH = "erc20_abi.json"            # Path to ERC20 token contract ABI file

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load ERC20 contract ABI
try:
    with open(CONTRACT_ABI_PATH, "r") as abi_file:
        ERC20_ABI = abi_file.read()
except FileNotFoundError:
    raise FileNotFoundError(f"ERC20 ABI file not found at: {CONTRACT_ABI_PATH}")

# Helper function to get token balance
def get_token_balance(wallet_address, token_address):
    """
    Get the balance of a specific ERC20 token for a given wallet address.
    """
    token_contract = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
    balance = token_contract.functions.balanceOf(Web3.to_checksum_address(wallet_address)).call()
    decimals = token_contract.functions.decimals().call()
    return balance / (10 ** decimals)  # Adjust for token decimals

# Endpoint to initiate payment
@app.route("/initiate_payment", methods=["POST"])
def initiate_payment():
    """
    API endpoint to initiate cryptocurrency payments.
    Request payload example:
    {
        "freelancer_wallet": "0xFreelancerWalletAddress",
        "token_address": "0xTokenAddress",   // Use 0x0 for ETH
        "amount": 0.01
    }
    """
    try:
        data = request.json
        freelancer_wallet = data.get("freelancer_wallet")
        token_address = data.get("token_address")
        amount = data.get("amount")
        
        if not freelancer_wallet or not amount:
            return jsonify({"error": "Missing required fields: 'freelancer_wallet', 'amount'."}), 400

        # Ensure wallet addresses are valid
        if not Web3.is_address(freelancer_wallet):
            return jsonify({"error": "Invalid freelancer wallet address."}), 400
        if token_address and not Web3.is_address(token_address):
            return jsonify({"error": "Invalid token address."}), 400

        # Prepare transaction
        if token_address:  # Payment with ERC20 token
            token_contract = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
            decimals = token_contract.functions.decimals().call()
            transfer_amount = int(amount * (10 ** decimals))  # Adjust for decimals
            transaction = token_contract.functions.transfer(
                Web3.to_checksum_address(freelancer_wallet),
                transfer_amount,
            ).build_transaction({
                "chainId": web3.eth.chain_id,
                "from": PLATFORM_WALLET,
                "nonce": web3.eth.get_transaction_count(Web3.to_checksum_address(PLATFORM_WALLET)),
            })
        else:  # Payment with ETH
            transaction = {
                "to": Web3.to_checksum_address(freelancer_wallet),
                "value": web3.to_wei(amount, "ether"),
                "gas": 21000,  # Standard gas limit for ETH transfer
                "gasPrice": web3.eth.gas_price,
                "nonce": web3.eth.get_transaction_count(Web3.to_checksum_address(PLATFORM_WALLET)),
                "chainId": web3.eth.chain_id,
            }

        # Send transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=os.getenv("PLATFORM_PRIVATE_KEY"))
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return jsonify({"success": True, "txn_hash": txn_hash.hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to check transaction status
@app.route("/transaction_status/<txn_hash>", methods=["GET"])
def transaction_status(txn_hash):
    """
    API endpoint to check the status of a cryptocurrency transaction.
    """
    try:
        txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
        if not txn_receipt:
            return jsonify({"status": "Pending"}), 200
        if txn_receipt.status == 1:
            return jsonify({"status": "Success"}), 200
        else:
            return jsonify({"status": "Failed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
```

### Notes:
1. **Environment Variables**: Ensure `INFURA_URL`, `PLATFORM_WALLET`, and `PLATFORM_PRIVATE_KEY` are set securely in environment variables.
2. **Error Handling**: The code includes error handling for invalid input, missing fields, and blockchain connectivity issues.
3. **Security**: The platform's private key should be stored securely and never hardcoded in the source code.
4. **Production-Ready**: Disable `debug=True` in production and use a proper server like Gunicorn or uWSGI.
5. **Dependencies**: Install required Python libraries by running: `pip install flask web3`.
