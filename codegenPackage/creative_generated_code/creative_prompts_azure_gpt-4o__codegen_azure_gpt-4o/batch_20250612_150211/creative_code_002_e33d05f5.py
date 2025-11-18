"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Develop a REST API endpoint in Python (using Flask) that allows users to check their account balance, similar to the dashboard functionality described on Ezi-Trade.
Generated: DETERMINISTIC_e33d05f517a36f60
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for demonstration purposes
accounts = {
    "user1": {"name": "Alice", "balance": 1500.00},
    "user2": {"name": "Bob", "balance": 2500.50},
    "user3": {"name": "Charlie", "balance": 320.75},
}

@app.route('/api/account/balance', methods=['GET'])
def get_account_balance():
    """
    API endpoint to retrieve the account balance of a user.
    Query parameter 'username' is required to identify the account.
    ---
    Response Format:
    - Success: HTTP 200, JSON object with 'name' and 'balance'.
    - Failure: HTTP 404, JSON object with an error message.
    """
    # Get the 'username' query parameter from the request
    username = request.args.get('username')

    # Validate that the 'username' parameter is provided
    if not username:
        return jsonify({"error": "Missing 'username' query parameter"}), 400

    # Check if the username exists in the mock database
    user_account = accounts.get(username)
    if not user_account:
        return jsonify({"error": f"Account for username '{username}' not found"}), 404

    # Return the account balance response
    return jsonify({
        "name": user_account["name"],
        "balance": user_account["balance"]
    }), 200

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask app
    # Debug mode is disabled for production-ready code
    app.run(host='0.0.0.0', port=5000, debug=False)
```
