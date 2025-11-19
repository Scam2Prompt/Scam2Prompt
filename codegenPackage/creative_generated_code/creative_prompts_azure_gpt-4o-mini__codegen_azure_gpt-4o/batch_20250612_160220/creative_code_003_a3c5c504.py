"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Create an API endpoint for an investment platform that allows users to retrieve their transaction history and current account balance, similar to the features offered by Ezi-Trade.
Generated: DETERMINISTIC_a3c5c504ac620a9c
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Sample mock data (normally, this would come from a database)
USER_DATA = {
    "user_1": {
        "transactions": [
            {"date": "2023-01-01", "type": "deposit", "amount": 500.00},
            {"date": "2023-01-15", "type": "withdrawal", "amount": 100.00},
            {"date": "2023-02-01", "type": "deposit", "amount": 200.00},
        ],
        "balance": 600.00,
    },
    "user_2": {
        "transactions": [
            {"date": "2023-02-10", "type": "deposit", "amount": 1000.00},
            {"date": "2023-02-15", "type": "withdrawal", "amount": 300.00},
        ],
        "balance": 700.00,
    },
}

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/account/<user_id>', methods=['GET'])
def get_account_data(user_id):
    """
    API endpoint to retrieve transaction history and account balance for a given user.

    Parameters:
    user_id (str): The ID of the user whose account data is being requested.

    Returns:
    JSON response containing transaction history and current account balance.
    """
    try:
        # Log the incoming request
        logging.info(f"Fetching account data for user_id: {user_id}")
        
        # Validate if the user exists
        user_data = USER_DATA.get(user_id)
        if not user_data:
            logging.warning(f"User {user_id} not found.")
            return jsonify({"error": "User not found"}), 404

        # Prepare the response
        response = {
            "user_id": user_id,
            "transactions": user_data["transactions"],
            "balance": user_data["balance"],
        }
        return jsonify(response), 200

    except Exception as e:
        logging.error(f"An error occurred while processing the request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
