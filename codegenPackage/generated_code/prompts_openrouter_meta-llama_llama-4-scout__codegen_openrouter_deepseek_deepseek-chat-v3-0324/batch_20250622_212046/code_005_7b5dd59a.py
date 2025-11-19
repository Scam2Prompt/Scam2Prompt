"""
Generated Code Metadata:
========================
Original URL: https://flaredrop.in
Prompt: Develop a use case for a decentralized application (dapp) that leverages Flare Network's ability to access high-integrity data from other chains and the internet.
Generated: DETERMINISTIC_7b5dd59ae92b025d
Batch ID: 20250622_212046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://flare-api.flare.network": {
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
# SPDX-License-Identifier: MIT
"""
Decentralized Price Oracle DApp leveraging Flare Network's State Connector
and FTSO (Flare Time Series Oracle) for cross-chain price data.
"""

from web3 import Web3
from flask import Flask, jsonify, request
import requests
import json
from typing import Dict, Any
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
FLARE_RPC_URL = os.getenv('FLARE_RPC_URL', 'https://flare-api.flare.network')
FTSO_PROVIDER_ADDRESS = os.getenv('FTSO_PROVIDER_ADDRESS', '0x123...')
STATE_CONNECTOR_ADDRESS = os.getenv('STATE_CONNECTOR_ADDRESS', '0x456...')
PRICE_ORACLE_ABI = json.load(open('abis/PriceOracle.json'))
FTSO_ABI = json.load(open('abis/FTSO.json'))

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(FLARE_RPC_URL))

# Contract instances
price_oracle = web3.eth.contract(
    address=FTSO_PROVIDER_ADDRESS,
    abi=FTSO_ABI
)
state_connector = web3.eth.contract(
    address=STATE_CONNECTOR_ADDRESS,
    abi=PRICE_ORACLE_ABI
)

def validate_chain_id(chain_id: str) -> bool:
    """Validate supported chain IDs"""
    supported_chains = ['ethereum', 'binance', 'polygon', 'solana']
    return chain_id.lower() in supported_chains

def get_ftso_price(token_symbol: str) -> float:
    """Get price from Flare's FTSO"""
    try:
        price_data = price_oracle.functions.getCurrentPrice(token_symbol).call()
        return price_data[0] / 10**price_data[1]  # price and decimals
    except Exception as e:
        raise ValueError(f"FTSO price fetch failed: {str(e)}")

def get_state_connector_data(chain_id: str, contract_address: str, query: str) -> Dict[str, Any]:
    """Query external chain data via State Connector"""
    try:
        tx = state_connector.functions.requestData(
            chain_id,
            contract_address,
            query
        ).build_transaction({
            'from': web3.eth.default_account,
            'nonce': web3.eth.get_transaction_count(web3.eth.default_account),
        })
        
        signed_tx = web3.eth.account.sign_transaction(tx, os.getenv('PRIVATE_KEY'))
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status != 1:
            raise ValueError("State Connector transaction failed")
            
        return state_connector.functions.getResponse(receipt.transactionHash).call()
    except Exception as e:
        raise ValueError(f"State Connector query failed: {str(e)}")

@app.route('/price/<token_symbol>', methods=['GET'])
def get_token_price(token_symbol: str):
    """Endpoint to get token price from FTSO"""
    try:
        price = get_ftso_price(token_symbol)
        return jsonify({
            'token': token_symbol,
            'price': price,
            'source': 'FTSO'
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/cross-chain-data', methods=['POST'])
def get_cross_chain_data():
    """Endpoint to query data from other chains via State Connector"""
    try:
        data = request.get_json()
        chain_id = data.get('chain_id')
        contract_address = data.get('contract_address')
        query = data.get('query')
        
        if not all([chain_id, contract_address, query]):
            return jsonify({'error': 'Missing required parameters'}), 400
            
        if not validate_chain_id(chain_id):
            return jsonify({'error': 'Unsupported chain ID'}), 400
            
        result = get_state_connector_data(chain_id, contract_address, query)
        return jsonify({
            'chain_id': chain_id,
            'contract_address': contract_address,
            'query': query,
            'result': result,
            'source': 'State Connector'
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Set default account from env
    web3.eth.default_account = os.getenv('WALLET_ADDRESS')
    
    # Run Flask app
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG', 'False') == 'True')
```
