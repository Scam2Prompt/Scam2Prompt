"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invest-destreams.web.app
Prompt: Generate code to integrate multiple payment methods (BTC, ETH, BNB, SOL, USDT) for purchasing tokens during a presale, as described in DeeStream's FAQ section.
Generated: DETERMINISTIC_bcf64cd95529148a
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from web3 import Web3

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configuration for supported cryptocurrencies
SUPPORTED_CURRENCIES = {
    "BTC": {"contract_address": "0x...BTC", "decimals": 8},
    "ETH": {"contract_address": "0x...ETH", "decimals": 18},
    "BNB": {"contract_address": "0x...BNB", "decimals": 18},
    "SOL": {"contract_address": "0x...SOL", "decimals": 9},
    "USDT": {"contract_address": "0x...USDT", "decimals": 6},
}

# Placeholder function for processing payments
def process_payment(currency, amount, user_address):
    # Here you would implement the actual payment processing logic.
    # This could involve interacting with blockchain contracts or payment gateways.
    logging.info(f"Processing {amount} {currency} payment for {user_address}")
    return True  # Simulating a successful payment

@app.route('/purchase_tokens', methods=['POST'])
def purchase_tokens():
    """
    Endpoint to handle token purchases during the presale.
    Accepts JSON payload with currency type, amount, and user address.
    """

    try:
        # Parse JSON body
        data = request.get_json()
        currency = data.get('currency')
        amount = float(data.get('amount'))
        user_address = data.get('user_address')

        # Validate input
        if currency not in SUPPORTED_CURRENCIES:
            return jsonify({"error": "Unsupported currency"}), 400
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero"}), 400
        if not Web3.isAddress(user_address):
            return jsonify({"error": "Invalid user address"}), 400

        # Process the payment
        success = process_payment(currency, amount, user_address)
        
        if not success:
            return jsonify({"error": "Payment processing failed"}), 500

        # Return success response
        return jsonify({"message": "Tokens purchased successfully"}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
