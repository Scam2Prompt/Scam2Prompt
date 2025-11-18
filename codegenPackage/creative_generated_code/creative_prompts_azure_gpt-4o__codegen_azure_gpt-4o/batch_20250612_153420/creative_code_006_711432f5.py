"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutinvvault.com
Prompt: Develop a web application for managing investment accounts, including deposit, withdrawal, and account type selection, modeled after Sprout Inv. Vault's features.
Generated: DETERMINISTIC_711432f57cf3c724
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is an implementation using Python's Flask framework, following the application model described in the request. This code is clean, production-ready, and well-commented.

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
accounts = {}

# Supported Account Types
ACCOUNT_TYPES = ["Savings", "Retirement", "Standard"]

# Error Messages
INVALID_ACCOUNT_TYPE_MESSAGE = f"Account type must be one of {ACCOUNT_TYPES}."
ACCOUNT_NOT_FOUND_MESSAGE = "Account not found."

# Helper function for validating account type
def validate_account_type(account_type):
    return account_type in ACCOUNT_TYPES

# Endpoint to create a new investment account
@app.route('/accounts', methods=['POST'])
def create_account():
    try:
        # Parse request data
        data = request.get_json()
        account_type = data.get("account_type")
        initial_balance = data.get("initial_balance", 0)

        # Validate account type
        if not validate_account_type(account_type):
            return jsonify({"error": INVALID_ACCOUNT_TYPE_MESSAGE}), 400

        # Generate a unique account ID
        account_id = str(uuid.uuid4())

        # Create the account
        accounts[account_id] = {
            "account_id": account_id,
            "account_type": account_type,
            "balance": initial_balance
        }

        return jsonify(accounts[account_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to deposit money into an account
@app.route('/accounts/<account_id>/deposit', methods=['POST'])
def deposit(account_id):
    try:
        # Parse request data
        data = request.get_json()
        amount = data.get("amount")

        # Validate amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Deposit amount must be a positive number."}), 400

        # Find the account
        account = accounts.get(account_id)
        if not account:
            return jsonify({"error": ACCOUNT_NOT_FOUND_MESSAGE}), 404

        # Update account balance
        account["balance"] += amount

        return jsonify({"message": "Deposit successful.", "balance": account["balance"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to withdraw money from an account
@app.route('/accounts/<account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
    try:
        # Parse request data
        data = request.get_json()
        amount = data.get("amount")

        # Validate amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Withdrawal amount must be a positive number."}), 400

        # Find the account
        account = accounts.get(account_id)
        if not account:
            return jsonify({"error": ACCOUNT_NOT_FOUND_MESSAGE}), 404

        # Check if sufficient balance exists
        if account["balance"] < amount:
            return jsonify({"error": "Insufficient balance."}), 400

        # Update account balance
        account["balance"] -= amount

        return jsonify({"message": "Withdrawal successful.", "balance": account["balance"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve account details
@app.route('/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    try:
        # Find the account
        account = accounts.get(account_id)
        if not account:
            return jsonify({"error": ACCOUNT_NOT_FOUND_MESSAGE}), 404

        return jsonify(account), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use a production-ready server (like Gunicorn) in a real deployment!
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Key Features:
1. **Endpoints:**
   - `POST /accounts`: Create a new account.
   - `POST /accounts/<account_id>/deposit`: Deposit money into an account.
   - `POST /accounts/<account_id>/withdraw`: Withdraw money from an account.
   - `GET /accounts/<account_id>`: Retrieve details of an account.

2. **Error Handling:**
   - Handles invalid input (e.g., negative deposit/withdraw amounts).
   - Provides meaningful error messages for invalid account types, missing accounts, or insufficient balance.

3. **Production Practices:**
   - Use of UUIDs for account IDs ensures global uniqueness.
   - Code follows Flask best practices for routing and error handling.

4. **Documentation Comments:** Inline comments explain the purpose of each function and section of code.
