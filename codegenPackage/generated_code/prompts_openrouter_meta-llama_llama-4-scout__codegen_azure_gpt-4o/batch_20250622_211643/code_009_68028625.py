"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Design a basic system architecture for a platform that offers transaction insurance and scam reporting features, similar to those described on mmogdv.com.
Generated: DETERMINISTIC_68028625314782ba
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)

# In-memory database simulation
users = {}  # Stores user data
transactions = {}  # Stores transaction data
scam_reports = {}  # Stores scam reports

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handling decorator
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e),
        "message": "An error occurred. Please try again later."
    }
    return jsonify(response), 500

# Route: Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'name' and 'email'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input. 'name' and 'email' are required."}), 400

    user_id = generate_id()
    users[user_id] = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "created_at": datetime.utcnow().isoformat()
    }
    return jsonify({"message": "User registered successfully.", "user_id": user_id}), 201

# Route: Create a new transaction
@app.route('/transaction', methods=['POST'])
def create_transaction():
    """
    Endpoint to create a new transaction.
    Expects JSON payload with 'user_id', 'amount', and 'description'.
    """
    data = request.get_json()
    if not data or 'user_id' not in data or 'amount' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input. 'user_id', 'amount', and 'description' are required."}), 400

    if data['user_id'] not in users:
        return jsonify({"error": "User not found."}), 404

    transaction_id = generate_id()
    transactions[transaction_id] = {
        "id": transaction_id,
        "user_id": data['user_id'],
        "amount": data['amount'],
        "description": data['description'],
        "status": "insured",  # Default status
        "created_at": datetime.utcnow().isoformat()
    }
    return jsonify({"message": "Transaction created successfully.", "transaction_id": transaction_id}), 201

# Route: Report a scam
@app.route('/report-scam', methods=['POST'])
def report_scam():
    """
    Endpoint to report a scam.
    Expects JSON payload with 'transaction_id' and 'details'.
    """
    data = request.get_json()
    if not data or 'transaction_id' not in data or 'details' not in data:
        return jsonify({"error": "Invalid input. 'transaction_id' and 'details' are required."}), 400

    if data['transaction_id'] not in transactions:
        return jsonify({"error": "Transaction not found."}), 404

    report_id = generate_id()
    scam_reports[report_id] = {
        "id": report_id,
        "transaction_id": data['transaction_id'],
        "details": data['details'],
        "reported_at": datetime.utcnow().isoformat()
    }
    # Update transaction status to 'under investigation'
    transactions[data['transaction_id']]['status'] = "under investigation"
    return jsonify({"message": "Scam reported successfully.", "report_id": report_id}), 201

# Route: Get transaction details
@app.route('/transaction/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    Endpoint to fetch transaction details by ID.
    """
    if transaction_id not in transactions:
        return jsonify({"error": "Transaction not found."}), 404

    return jsonify(transactions[transaction_id]), 200

# Route: Get scam report details
@app.route('/scam-report/<report_id>', methods=['GET'])
def get_scam_report(report_id):
    """
    Endpoint to fetch scam report details by ID.
    """
    if report_id not in scam_reports:
        return jsonify({"error": "Scam report not found."}), 404

    return jsonify(scam_reports[report_id]), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
