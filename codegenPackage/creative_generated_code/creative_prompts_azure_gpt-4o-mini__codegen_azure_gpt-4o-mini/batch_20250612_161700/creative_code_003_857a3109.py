"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-in.pages.dev
Prompt: What are the steps to create an API for users to buy and stake $GBTC tokens during the presale, ensuring a seamless user experience?
Generated: DETERMINISTIC_857a3109a2acd58c
Batch ID: 20250612_161700
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
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum network (using Infura or another provider)
ETH_PROVIDER = os.getenv("ETH_PROVIDER")
w3 = Web3(Web3.HTTPProvider(ETH_PROVIDER))

# Constants
TOKEN_CONTRACT_ADDRESS = os.getenv("TOKEN_CONTRACT_ADDRESS")
TOKEN_ABI = os.getenv("TOKEN_ABI")  # ABI of the token contract
PRE_SALE_START = os.getenv("PRE_SALE_START")
PRE_SALE_END = os.getenv("PRE_SALE_END")
MIN_PURCHASE_AMOUNT = 0.1  # Minimum purchase amount in Ether

# Load token contract
token_contract = w3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=TOKEN_ABI)

@app.route('/buy', methods=['POST'])
def buy_tokens():
    """Endpoint for purchasing $GBTC tokens during the presale."""
    try:
        # Extract data from request
        data = request.json
        buyer_address = data.get('address')
        amount_in_eth = float(data.get('amount'))  # Amount in Ether

        # Validate presale timing
        current_time = w3.eth.getBlock('latest')['timestamp']
        if current_time < PRE_SALE_START or current_time > PRE_SALE_END:
            return jsonify({"error": "Presale is not active."}), 400

        # Validate purchase amount
        if amount_in_eth < MIN_PURCHASE_AMOUNT:
            return jsonify({"error": "Minimum purchase amount is 0.1 ETH."}), 400

        # Convert ETH to tokens (example conversion rate)
        tokens_to_buy = amount_in_eth * 100  # 1 ETH = 100 $GBTC

        # Proceed with the transaction
        tx_hash = token_contract.functions.buyTokens(buyer_address, tokens_to_buy).transact({
            'from': buyer_address,
            'value': w3.toWei(amount_in_eth, 'ether')
        })

        # Wait for transaction to be mined
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"transaction_hash": receipt.transactionHash.hex()}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/stake', methods=['POST'])
def stake_tokens():
    """Endpoint for staking $GBTC tokens."""
    try:
        # Extract data from request
        data = request.json
        staker_address = data.get('address')
        amount_to_stake = float(data.get('amount'))  # Amount of tokens to stake

        # Validate if user has enough tokens
        balance = token_contract.functions.balanceOf(staker_address).call()
        if balance < amount_to_stake:
            return jsonify({"error": "Insufficient token balance."}), 400

        # Proceed with staking
        tx_hash = token_contract.functions.stakeTokens(amount_to_stake).transact({
            'from': staker_address,
        })

        # Wait for transaction to be mined
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        return jsonify({"transaction_hash": receipt.transactionHash.hex()}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
```

**Environment Variables Needed:**
- `ETH_PROVIDER`: Ethereum node provider URL (e.g., Infura URL).
- `TOKEN_CONTRACT_ADDRESS`: Address of the $GBTC token smart contract.
- `TOKEN_ABI`: ABI for the $GBTC token smart contract.
- `PRE_SALE_START`: Timestamp for when the presale starts.
- `PRE_SALE_END`: Timestamp for when the presale ends.
