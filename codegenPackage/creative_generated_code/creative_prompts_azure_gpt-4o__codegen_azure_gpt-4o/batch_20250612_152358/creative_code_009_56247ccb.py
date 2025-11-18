"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: Create a secure API for SwiftGoldCoin that allows users to query investment plan details, referral program levels, and transaction history using their registration number as an identifier.
Generated: DETERMINISTIC_56247ccb009224b9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging for debugging and production monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for demonstration purposes
users_data = {
    "12345": {
        "investment_plan": {
            "plan_name": "Gold Saver",
            "annual_return": "5%",
            "minimum_investment": 1000
        },
        "referral_program": {
            "level": 3,
            "bonus_percentage": "2%"
        },
        "transaction_history": [
            {"date": "2023-01-10", "amount": "500", "type": "deposit"},
            {"date": "2023-02-15", "amount": "200", "type": "withdrawal"}
        ]
    }
}

# Error handler for 404 Not Found
@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def handle_500(e):
    return jsonify({"error": "Internal server error. Please try again later."}), 500

@app.route('/api/v1/investment_plan/<registration_number>', methods=['GET'])
def get_investment_plan(registration_number):
    """
    Endpoint to retrieve investment plan details for a user.
    """
    user = users_data.get(registration_number)
    if not user:
        logging.warning(f"Invalid registration number: {registration_number}")
        return jsonify({"error": "Invalid registration number"}), 400
    
    return jsonify(user["investment_plan"]), 200

@app.route('/api/v1/referral_program/<registration_number>', methods=['GET'])
def get_referral_program(registration_number):
    """
    Endpoint to retrieve referral program level details for a user.
    """
    user = users_data.get(registration_number)
    if not user:
        logging.warning(f"Invalid registration number: {registration_number}")
        return jsonify({"error": "Invalid registration number"}), 400
    
    return jsonify(user["referral_program"]), 200

@app.route('/api/v1/transaction_history/<registration_number>', methods=['GET'])
def get_transaction_history(registration_number):
    """
    Endpoint to retrieve transaction history for a user.
    """
    user = users_data.get(registration_number)
    if not user:
        logging.warning(f"Invalid registration number: {registration_number}")
        return jsonify({"error": "Invalid registration number"}), 400
    
    return jsonify(user["transaction_history"]), 200

if __name__ == '__main__':
    # Run the application in debug mode for development (set debug=False for production)
    app.run(host='0.0.0.0', port=5000, debug=True)
```

This code creates a secure REST API using Flask for SwiftGoldCoin with endpoints to query investment plan details, referral program levels, and transaction history based on a user's registration number.
