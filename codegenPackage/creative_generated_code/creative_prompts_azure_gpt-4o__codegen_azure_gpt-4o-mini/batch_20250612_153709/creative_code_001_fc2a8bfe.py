"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueswhale.pages.dev
Prompt: Generate code that dynamically prices on-chain messages based on wallet demand using Bluwhale's incentivized wallet outreach system.
Generated: DETERMINISTIC_fc2a8bfe89ced988
Batch ID: 20250612_153709
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
from decimal import Decimal
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Sample data structure to represent wallet demand
wallet_demand = {
    "wallet_1": 10,  # Example demand for wallet_1
    "wallet_2": 5,   # Example demand for wallet_2
}

# Pricing factors for on-chain messages
BASE_PRICE = Decimal('0.01')  # Base price for sending a message
PRICE_MULTIPLIER = Decimal('0.1')  # Multiplier based on demand

@app.route('/price-message', methods=['POST'])
def price_message():
    """
    Endpoint to calculate the price of on-chain messages based on wallet demand.
    Expected JSON body: {"wallet_address": "string"}
    """
    try:
        data = request.get_json()
        wallet_address = data.get('wallet_address')

        if not wallet_address:
            logging.error("Wallet address is missing")
            return jsonify({"error": "Wallet address is required"}), 400

        demand = wallet_demand.get(wallet_address, 0)
        price = BASE_PRICE + (PRICE_MULTIPLIER * demand)

        response = {
            "wallet_address": wallet_address,
            "price": str(price)  # Converting Decimal to string for JSON serialization
        }
        logging.info(f"Calculated price for {wallet_address}: {response['price']}")
        return jsonify(response), 200

    except json.JSONDecodeError:
        logging.error("Invalid JSON format")
        return jsonify({"error": "Invalid JSON format"}), 400

    except Exception as e:
        logging.exception("An error occurred while pricing the message")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
