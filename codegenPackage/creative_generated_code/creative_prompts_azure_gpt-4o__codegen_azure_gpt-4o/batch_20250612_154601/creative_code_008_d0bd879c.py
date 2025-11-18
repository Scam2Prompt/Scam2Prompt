"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Provide code examples for integrating Bitcoin payments into an e-commerce platform, emphasizing Bitcoin’s function as "money" and a "unit of account," as noted on the Jupiter Digital Asset site.
Generated: DETERMINISTIC_d0bd879c177f0807
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify  # Framework for the web server
from bitcoinlib.wallets import Wallet      # Bitcoin wallet management
from bitcoinlib.transactions import TransactionError  # Exception for transaction issues
import os                                  # For environment variable access

# Flask application setup
app = Flask(__name__)

# Load environment variables for sensitive data
BITCOIN_WALLET_NAME = os.getenv('BITCOIN_WALLET_NAME', 'default_wallet')
BITCOIN_NETWORK = os.getenv('BITCOIN_NETWORK', 'testnet')  # Use 'mainnet' for production
BITCOIN_RECEIVING_ADDRESS = os.getenv('BITCOIN_RECEIVING_ADDRESS')  # Ensure valid Bitcoin receiving address

# Error handling for missing wallet data
if not BITCOIN_RECEIVING_ADDRESS:
    raise ValueError("Missing Bitcoin receiving address in environment variables.")

# Initialize or access the wallet
try:
    wallet = Wallet(BITCOIN_WALLET_NAME, network=BITCOIN_NETWORK)  # Connect to the Bitcoin wallet
except Exception as e:
    raise RuntimeError(f"Failed to initialize Bitcoin wallet: {str(e)}")

# Route to process payments
@app.route('/process_payment', methods=['POST'])
def process_payment():
    """
    Endpoint to process Bitcoin payments.
    Expected POST payload: {"amount": <amount_in_bitcoin>}
    """
    try:
        # Parse the incoming request payload
        data = request.json
        if 'amount' not in data:
            return jsonify({"error": "Missing 'amount' in request payload."}), 400
        
        # Validate the amount
        amount = float(data['amount'])
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero."}), 400

        # Create a new transaction to receive payment
        tx = wallet.send_to(BITCOIN_RECEIVING_ADDRESS, amount, fee=0.0001)  # Set a small fee for the transaction
        if not tx:
            raise TransactionError("Transaction failed.")
        
        # Respond with transaction details
        return jsonify({
            "message": "Payment processed successfully.",
            "transaction_id": tx.txid,
            "amount_received": amount,
            "receiver_address": BITCOIN_RECEIVING_ADDRESS
        }), 200

    except TransactionError as e:
        # Handle transaction-specific errors
        return jsonify({"error": f"Bitcoin transaction error: {str(e)}"}), 500

    except ValueError as e:
        # Handle validation errors
        return jsonify({"error": f"Invalid request: {str(e)}"}), 400

    except Exception as e:
        # Catch-all for any other errors
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@app.route('/get_wallet_balance', methods=['GET'])
def get_wallet_balance():
    """
    Endpoint to retrieve the current Bitcoin wallet balance.
    """
    try:
        balance = wallet.balance()
        return jsonify({
            "wallet_name": BITCOIN_WALLET_NAME,
            "network": BITCOIN_NETWORK,
            "balance": balance
        }), 200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch wallet balance: {str(e)}"}), 500


# Application entry point
if __name__ == '__main__':
    # Run the app on localhost
    app.run(host='127.0.0.1', port=5000)
```
