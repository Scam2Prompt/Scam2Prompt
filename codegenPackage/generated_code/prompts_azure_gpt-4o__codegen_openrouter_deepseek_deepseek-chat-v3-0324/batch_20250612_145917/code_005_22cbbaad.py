"""
Generated Code Metadata:
========================
Original URL: https://sonic-labs.vercel.app
Prompt: Create a decentralized application (dApp) on Sonic that integrates SonicDB for low-latency transactions and low-cost maintenance. Highlight the use of specialized RPC, validator, and observer nodes.
Generated: DETERMINISTIC_22cbbaadb6a674c9
Batch ID: 20250612_145917
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://observer.sonic.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.sonic.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://validator.sonic.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from web3 import Web3
import json
import os
from sonic_db import SonicDB  # Hypothetical SonicDB library

# Initialize Flask app
app = Flask(__name__)

# Configuration
CONFIG = {
    "RPC_NODE_URL": os.getenv("SONIC_RPC_NODE_URL", "https://rpc.sonic.network"),
    "VALIDATOR_NODE_URL": os.getenv("SONIC_VALIDATOR_NODE_URL", "https://validator.sonic.network"),
    "OBSERVER_NODE_URL": os.getenv("SONIC_OBSERVER_NODE_URL", "https://observer.sonic.network"),
    "SONIC_DB_CONFIG": {
        "host": os.getenv("SONIC_DB_HOST", "localhost"),
        "port": int(os.getenv("SONIC_DB_PORT", 5432)),
        "user": os.getenv("SONIC_DB_USER", "sonic"),
        "password": os.getenv("SONIC_DB_PASSWORD", "password"),
        "database": os.getenv("SONIC_DB_NAME", "sonic_db")
    }
}

# Initialize Web3 providers
rpc_provider = Web3.HTTPProvider(CONFIG["RPC_NODE_URL"])
validator_provider = Web3.HTTPProvider(CONFIG["VALIDATOR_NODE_URL"])
observer_provider = Web3.HTTPProvider(CONFIG["OBSERVER_NODE_URL"])

# Initialize Web3 instances
web3_rpc = Web3(rpc_provider)
web3_validator = Web3(validator_provider)
web3_observer = Web3(observer_provider)

# Initialize SonicDB
sonic_db = SonicDB(**CONFIG["SONIC_DB_CONFIG"])

# Sample contract ABI (replace with actual contract ABI)
CONTRACT_ABI = json.loads('''[
    {
        "inputs": [],
        "name": "getValue",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "newValue", "type": "uint256"}],
        "name": "setValue",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

# Sample contract address (replace with actual contract address)
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0x1234567890123456789012345678901234567890")

# Initialize contract
contract = web3_rpc.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

@app.route('/get_value', methods=['GET'])
def get_value():
    """Get value from the smart contract using RPC node."""
    try:
        value = contract.functions.getValue().call()
        return jsonify({"status": "success", "value": str(value)}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/set_value', methods=['POST'])
def set_value():
    """Set value in the smart contract using Validator node."""
    try:
        data = request.get_json()
        new_value = data.get('value')
        
        if not new_value:
            return jsonify({"status": "error", "message": "Value not provided"}), 400
        
        # Get account from environment (in production, use proper wallet management)
        account = web3_validator.eth.account.privateKeyToAccount(os.getenv("PRIVATE_KEY"))
        
        # Build transaction
        tx = contract.functions.setValue(int(new_value)).buildTransaction({
            'chainId': web3_validator.eth.chain_id,
            'gas': 2000000,
            'gasPrice': web3_validator.eth.gas_price,
            'nonce': web3_validator.eth.getTransactionCount(account.address),
        })
        
        # Sign transaction
        signed_tx = account.sign_transaction(tx)
        
        # Send transaction
        tx_hash = web3_validator.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        # Store transaction in SonicDB for low-latency access
        sonic_db.insert_transaction(
            tx_hash=tx_hash.hex(),
            sender=account.address,
            value=new_value,
            status="pending"
        )
        
        return jsonify({
            "status": "success",
            "tx_hash": tx_hash.hex(),
            "message": "Transaction submitted to validator"
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/tx_status/<tx_hash>', methods=['GET'])
def get_tx_status(tx_hash):
    """Get transaction status from Observer node or SonicDB."""
    try:
        # First try to get from SonicDB (low-latency)
        tx_data = sonic_db.get_transaction(tx_hash)
        
        if tx_data:
            return jsonify({
                "status": "success",
                "data": tx_data,
                "source": "sonic_db"
            }), 200
        
        # Fallback to observer node if not in SonicDB
        tx_receipt = web3_observer.eth.getTransactionReceipt(tx_hash)
        
        if tx_receipt:
            status = "confirmed" if tx_receipt.status == 1 else "failed"
            return jsonify({
                "status": "success",
                "data": {
                    "tx_hash": tx_hash,
                    "status": status,
                    "block_number": tx_receipt.blockNumber
                },
                "source": "observer_node"
            }), 200
        
        return jsonify({"status": "error", "message": "Transaction not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
