"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecobrokercapital.com
Prompt: Generate code for a Bitcoin investment platform supporting multiple payment methods like Bitcoin, Ethereum, and Skrill, as outlined by Eco Broker Capital.
Generated: DETERMINISTIC_a88758d865e7c577
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Bitcoin Investment Platform - Supports multiple payment methods including Bitcoin, Ethereum, and Skrill.
Author: Expert Programmer
Date: 2023
"""

import json
import logging
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Supported payment methods
PAYMENT_METHODS = ["Bitcoin", "Ethereum", "Skrill"]

# Dummy database for user investments
user_investments = {}

# Helper: Validate payment method
def validate_payment_method(method):
    if method not in PAYMENT_METHODS:
        raise ValueError(f"Unsupported payment method: {method}")

# Helper: Validate investment amount
def validate_investment_amount(amount):
    if amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

# Endpoint: Register a new investment
@app.route('/invest', methods=['POST'])
def invest():
    try:
        # Parse input data
        data = request.get_json(force=True)
        user_id = data.get("user_id")
        payment_method = data.get("payment_method")
        amount = data.get("amount")

        # Validate input
        if not user_id or not payment_method or not amount:
            raise ValueError("Missing required fields: user_id, payment_method, or amount.")

        validate_payment_method(payment_method)
        validate_investment_amount(amount)

        # Store investment in database
        if user_id not in user_investments:
            user_investments[user_id] = []
        user_investments[user_id].append({
            "payment_method": payment_method,
            "amount": amount,
        })

        logging.info(f"Investment registered for user {user_id} using {payment_method}: {amount}")
        return jsonify({"message": "Investment registered successfully.", "status": "success"}), 200

    except ValueError as e:
        logging.error(f"Validation error: {e}")
        return jsonify({"message": str(e), "status": "error"}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred. Please try again later.", "status": "error"}), 500

# Endpoint: Retrieve user investments
@app.route('/investments/<user_id>', methods=['GET'])
def get_investments(user_id):
    try:
        # Check if user exists in the database
        investments = user_investments.get(user_id)
        if not investments:
            return jsonify({"message": "No investments found for user.", "status": "error"}), 404

        # Return user investments
        logging.info(f"Retrieved investments for user {user_id}")
        return jsonify({"user_id": user_id, "investments": investments, "status": "success"}), 200

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred. Please try again later.", "status": "error"}), 500

# Endpoint: Supported payment methods
@app.route('/payment-methods', methods=['GET'])
def get_payment_methods():
    try:
        # Return supported payment methods
        logging.info("Retrieved supported payment methods.")
        return jsonify({"payment_methods": PAYMENT_METHODS, "status": "success"}), 200
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred. Please try again later.", "status": "error"}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
