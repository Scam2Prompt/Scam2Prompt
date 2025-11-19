"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romellglobal.com
Prompt: Create a RESTful API design for a banking service that includes features like credit trading and structured credit products as described by Romell Global Bank.
Generated: DETERMINISTIC_8daf5c4676c1a035
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Sample in-memory database for demo purposes
accounts = {
    1: {"name": "Alice", "balance": 1000},
    2: {"name": "Bob", "balance": 2000}
}

credit_products = {
    1: {"name": "Short-term Loan", "rate": 5},
    2: {"name": "Corporate Bond", "rate": 3}
}

# Error handler for consistent JSON responses
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "description": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Endpoint to retrieve account details
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    account = accounts.get(account_id)
    if not account:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account)

# Endpoint to transfer credit between accounts
@app.route("/accounts/transfer", methods=["POST"])
def transfer_credit():
    data = request.get_json()
    try:
        sender_id = data.get("sender_id")
        receiver_id = data.get("receiver_id")
        amount = data.get("amount")

        # Validate input
        if not sender_id or not receiver_id or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        if amount <= 0:
            return jsonify({"error": "Amount must be positive"}), 400

        sender = accounts.get(sender_id)
        receiver = accounts.get(receiver_id)

        if not sender or not receiver:
            return jsonify({"error": "Invalid account IDs"}), 404

        # Check sender's balance
        if sender["balance"] < amount:
            return jsonify({"error": "Insufficient balance"}), 400

        # Perform the transfer
        sender["balance"] -= amount
        receiver["balance"] += amount

        return jsonify({"message": "Transfer successful"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list structured credit products
@app.route("/credit-products", methods=["GET"])
def list_credit_products():
    return jsonify({"credit_products": credit_products})

# Endpoint to retrieve details of a specific credit product
@app.route("/credit-products/<int:product_id>", methods=["GET"])
def get_credit_product(product_id):
    product = credit_products.get(product_id)
    if not product:
        return jsonify({"error": "Credit product not found"}), 404
    return jsonify(product)

# Endpoint to simulate purchasing a credit product
@app.route("/credit-products/purchase", methods=["POST"])
def purchase_credit_product():
    data = request.get_json()
    try:
        account_id = data.get("account_id")
        product_id = data.get("product_id")
        amount = data.get("amount")

        # Validate input
        if not account_id or not product_id or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        if amount <= 0:
            return jsonify({"error": "Amount must be positive"}), 400

        account = accounts.get(account_id)
        product = credit_products.get(product_id)

        if not account or not product:
            return jsonify({"error": "Invalid account or product ID"}), 404

        # Check account balance
        if account["balance"] < amount:
            return jsonify({"error": "Insufficient balance"}), 400

        # Perform the purchase
        account["balance"] -= amount
        return jsonify({"message": "Purchase successful", "product": product})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
