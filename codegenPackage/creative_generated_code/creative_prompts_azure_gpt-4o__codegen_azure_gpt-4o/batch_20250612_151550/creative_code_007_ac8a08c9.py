"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fennextradingservices.com
Prompt: Create a web application that allows users to select investment plans (Starter, Silver, Gold), calculate expected profits, and manage their e-wallet transactions, inspired by Fennex Trading Services' investment offerings.
Generated: DETERMINISTIC_ac8a08c9ea679255
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean and well-documented implementation using Python with Flask for the backend:

```python
from flask import Flask, request, jsonify
from decimal import Decimal

app = Flask(__name__)

# Data structure for investment plans
INVESTMENT_PLANS = {
    "Starter": {"rate": Decimal("0.05")},  # 5% profit rate
    "Silver": {"rate": Decimal("0.10")},   # 10% profit rate
    "Gold": {"rate": Decimal("0.20")}     # 20% profit rate
}

# Simulated e-wallet database (for demonstration purposes)
E_WALLETS = {}

# Error messages
ERRORS = {
    "invalid_plan": "Invalid investment plan selected.",
    "insufficient_balance": "Insufficient balance in e-wallet.",
    "wallet_not_found": "E-wallet ID not found."
}

@app.route('/investment-plans', methods=['GET'])
def get_investment_plans():
    """
    Get all available investment plans and their rates.
    """
    return jsonify({"plans": INVESTMENT_PLANS}), 200

@app.route('/calculate-profit', methods=['POST'])
def calculate_profit():
    """
    Calculate expected profit based on investment plan and amount.
    Request JSON Payload:
    {
        "plan": "Starter|Silver|Gold",
        "amount": float
    }
    """
    data = request.json
    plan = data.get("plan")
    amount = data.get("amount")

    if plan not in INVESTMENT_PLANS:
        return jsonify({"error": ERRORS["invalid_plan"]}), 400

    if amount <= 0:
        return jsonify({"error": "Investment amount must be greater than zero."}), 400

    rate = INVESTMENT_PLANS[plan]["rate"]
    profit = Decimal(amount) * rate

    return jsonify({"plan": plan, "amount": amount, "expected_profit": float(profit)}), 200

@app.route('/e-wallet/<wallet_id>', methods=['GET'])
def get_wallet_balance(wallet_id):
    """
    Get the balance of the specified e-wallet by ID.
    """
    if wallet_id not in E_WALLETS:
        return jsonify({"error": ERRORS["wallet_not_found"]}), 404

    return jsonify({"wallet_id": wallet_id, "balance": float(E_WALLETS[wallet_id])}), 200

@app.route('/e-wallet/<wallet_id>', methods=['POST'])
def create_wallet(wallet_id):
    """
    Create a new e-wallet with an initial balance.
    Request JSON Payload:
    {
        "initial_balance": float
    }
    """
    data = request.json
    initial_balance = data.get("initial_balance", 0)

    if wallet_id in E_WALLETS:
        return jsonify({"error": "E-wallet ID already exists."}), 400

    if initial_balance < 0:
        return jsonify({"error": "Initial balance cannot be negative."}), 400

    E_WALLETS[wallet_id] = Decimal(initial_balance)
    return jsonify({"wallet_id": wallet_id, "balance": float(E_WALLETS[wallet_id])}), 201

@app.route('/e-wallet/<wallet_id>/deposit', methods=['POST'])
def deposit_to_wallet(wallet_id):
    """
    Deposit funds into an e-wallet.
    Request JSON Payload:
    {
        "amount": float
    }
    """
    if wallet_id not in E_WALLETS:
        return jsonify({"error": ERRORS["wallet_not_found"]}), 404

    data = request.json
    amount = data.get("amount", 0)

    if amount <= 0:
        return jsonify({"error": "Deposit amount must be greater than zero."}), 400

    E_WALLETS[wallet_id] += Decimal(amount)
    return jsonify({"wallet_id": wallet_id, "balance": float(E_WALLETS[wallet_id])}), 200

@app.route('/e-wallet/<wallet_id>/withdraw', methods=['POST'])
def withdraw_from_wallet(wallet_id):
    """
    Withdraw funds from an e-wallet.
    Request JSON Payload:
    {
        "amount": float
    }
    """
    if wallet_id not in E_WALLETS:
        return jsonify({"error": ERRORS["wallet_not_found"]}), 404

    data = request.json
    amount = data.get("amount", 0)

    if amount <= 0:
        return jsonify({"error": "Withdrawal amount must be greater than zero."}), 400

    if E_WALLETS[wallet_id] < amount:
        return jsonify({"error": ERRORS["insufficient_balance"]}), 400

    E_WALLETS[wallet_id] -= Decimal(amount)
    return jsonify({"wallet_id": wallet_id, "balance": float(E_WALLETS[wallet_id])}), 200

if __name__ == '__main__':
    # Debug mode should be disabled in production
    app.run(debug=True)
```

### Instructions for Running the Code:
1. Make sure Python is installed (Python 3.7+ recommended).
2. Install Flask: `pip install flask`.
3. Save the code to a file, e.g., `app.py`.
4. Run the application: `python app.py`.
5. Use an API testing tool (like Postman) or a browser to interact with the endpoints.

Endpoints:
- **GET `/investment-plans`**: Retrieve available investment plans.
- **POST `/calculate-profit`**: Calculate expected profit based on plan and amount.
- **GET `/e-wallet/<wallet_id>`**: Retrieve wallet balance.
- **POST `/e-wallet/<wallet_id>`**: Create a new e-wallet.
- **POST `/e-wallet/<wallet_id>/deposit`**: Deposit funds into the wallet.
- **POST `/e-wallet/<wallet_id>/withdraw`**: Withdraw funds from the wallet.
