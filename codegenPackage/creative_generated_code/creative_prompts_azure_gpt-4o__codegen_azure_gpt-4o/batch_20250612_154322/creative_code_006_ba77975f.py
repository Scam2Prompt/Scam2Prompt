"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Develop a REST API for querying $EMT token balances and transaction history on the EarthMeta platform, ensuring compatibility with Ethereum, Polygon, and BNB Chain.
Generated: DETERMINISTIC_ba77975f065e3e1d
Batch ID: 20250612_154322
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
import os
import json

app = Flask(__name__)

# Load blockchain configuration
CONFIG = {
    "Ethereum": {
        "rpc_url": os.getenv("ETHEREUM_RPC_URL"),
        "chain_id": 1
    },
    "Polygon": {
        "rpc_url": os.getenv("POLYGON_RPC_URL"),
        "chain_id": 137
    },
    "BNBChain": {
        "rpc_url": os.getenv("BNBCHAIN_RPC_URL"),
        "chain_id": 56
    }
}

# Load the ABI for the ERC20 token contract
with open("erc20_abi.json", "r") as abi_file:
    ERC20_ABI = json.load(abi_file)

# Initialize Web3 instances for each chain
WEB3_INSTANCES = {
    chain_name: Web3(Web3.HTTPProvider(config["rpc_url"]))
    for chain_name, config in CONFIG.items()
}

@app.route("/api/token_balance", methods=["GET"])
def get_token_balance():
    """
    Endpoint to query the balance of $EMT token for a given wallet address.
    Parameters:
        - address: Wallet address to query
        - chain: Blockchain to query (Ethereum, Polygon, BNBChain)
    Returns:
        - JSON object with balance information
    """
    address = request.args.get("address")
    chain = request.args.get("chain")

    # Input Validation
    if not address or not chain:
        return jsonify({"error": "Missing 'address' or 'chain' parameter"}), 400
    if chain not in CONFIG:
        return jsonify({"error": "Unsupported chain. Choose Ethereum, Polygon, or BNBChain"}), 400

    web3 = WEB3_INSTANCES[chain]
    if not web3.isConnected():
        return jsonify({"error": f"Unable to connect to {chain} RPC"}), 500

    try:
        # EMT token contract address; update as required by EarthMeta
        EMT_CONTRACT_ADDRESS = os.getenv("EMT_CONTRACT_ADDRESS")
        if not EMT_CONTRACT_ADDRESS:
            return jsonify({"error": "EMT_CONTRACT_ADDRESS environment variable not set"}), 500

        # Create contract instance for EMT token
        emt_contract = web3.eth.contract(address=EMT_CONTRACT_ADDRESS, abi=ERC20_ABI)

        # Query token balance
        balance = emt_contract.functions.balanceOf(Web3.toChecksumAddress(address)).call()
        decimals = emt_contract.functions.decimals().call()

        # Convert balance to human-readable format
        human_balance = balance / (10 ** decimals)

        return jsonify({
            "address": address,
            "chain": chain,
            "balance": human_balance
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/transaction_history", methods=["GET"])
def get_transaction_history():
    """
    Endpoint to query the transaction history of $EMT token for a given wallet address.
    Parameters:
        - address: Wallet address to query
        - chain: Blockchain to query (Ethereum, Polygon, BNBChain)
    Returns:
        - JSON object with transaction history
    """
    address = request.args.get("address")
    chain = request.args.get("chain")

    # Input Validation
    if not address or not chain:
        return jsonify({"error": "Missing 'address' or 'chain' parameter"}), 400
    if chain not in CONFIG:
        return jsonify({"error": "Unsupported chain. Choose Ethereum, Polygon, or BNBChain"}), 400

    web3 = WEB3_INSTANCES[chain]
    if not web3.isConnected():
        return jsonify({"error": f"Unable to connect to {chain} RPC"}), 500

    try:
        # EMT token contract address; update as required by EarthMeta
        EMT_CONTRACT_ADDRESS = os.getenv("EMT_CONTRACT_ADDRESS")
        if not EMT_CONTRACT_ADDRESS:
            return jsonify({"error": "EMT_CONTRACT_ADDRESS environment variable not set"}), 500

        # Note: Retrieving transaction history for a specific ERC20 token would typically
        # require querying logs of Transfer events or using a third-party service.
        # Below is a simplified placeholder example.

        logs = web3.eth.get_logs({
            "address": Web3.toChecksumAddress(EMT_CONTRACT_ADDRESS),
            "topics": [web3.keccak(text="Transfer(address,address,uint256)")],
            "fromBlock": 0,
            "toBlock": "latest"
        })

        transaction_history = []

        for log in logs:
            # Decode log data
            decoded_log = web3.eth.contract(abi=ERC20_ABI, address=EMT_CONTRACT_ADDRESS).events.Transfer().processLog(log)
            if decoded_log["args"]["from"] == Web3.toChecksumAddress(address) or decoded_log["args"]["to"] == Web3.toChecksumAddress(address):
                transaction = {
                    "from": decoded_log["args"]["from"],
                    "to": decoded_log["args"]["to"],
                    "value": decoded_log["args"]["value"],
                    "block_number": log["blockNumber"],
                    "transaction_hash": log["transactionHash"].hex()
                }
                transaction_history.append(transaction)

        return jsonify({
            "address": address,
            "chain": chain,
            "transaction_history": transaction_history
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Default port is 5000, update as needed
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
```
