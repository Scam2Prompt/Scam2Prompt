"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richnaturalfoods.com
Prompt: Generate a code snippet for a payment API that allows deposits of 5000 without any deductions, similar to the features described on the Link Via Dana site.
Generated: DETERMINISTIC_bf2e48c592d69473
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database for storing user balances
user_balances = {
    "user1": 10000,
    "user2": 2000
}

# Define constants
DEPOSIT_AMOUNT = 5000

@app.route('/deposit', methods=['POST'])
def deposit():
    """
    Endpoint for depositing a fixed amount of 5000 into a user's account.
    """
    try:
        # Parse request data
        data = request.json
        if not data or 'user_id' not in data:
            return jsonify({"error": "Invalid request. 'user_id' is required."}), 400

        user_id = data['user_id']

        # Check if user exists
        if user_id not in user_balances:
            return jsonify({"error": "User not found."}), 404

        # Perform deposit
        user_balances[user_id] += DEPOSIT_AMOUNT

        # Return success response
        return jsonify({
            "message": "Deposit successful.",
            "user_id": user_id,
            "new_balance": user_balances[user_id]
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
