"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Illustrate how to implement an invoice finance solution in a web application that unlocks immediate cash from unpaid invoices for small businesses.
Generated: DETERMINISTIC_2053354a94bd0548
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based Web Application for Invoice Finance Solution
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database for invoices and financing transactions
invoices_db = {}
financing_db = {}

# Helper function to validate invoice input
def validate_invoice_data(data):
    required_fields = ["invoice_id", "business_name", "invoice_amount", "due_date"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

# Helper function to calculate financing fees
def calculate_financing_fee(amount):
    # Example: 3% financing fee
    return round(amount * 0.03, 2)

@app.route('/create_invoice', methods=['POST'])
def create_invoice():
    """
    Endpoint to create a new invoice.
    Payload:
    {
        "invoice_id": "12345",
        "business_name": "Small Business LLC",
        "invoice_amount": 10000,
        "due_date": "2023-12-01"
    }
    """
    try:
        data = request.json
        is_valid, error_message = validate_invoice_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        invoice_id = data["invoice_id"]
        if invoice_id in invoices_db:
            return jsonify({"error": "Invoice ID already exists"}), 400
        
        # Save invoice data
        invoices_db[invoice_id] = {
            "invoice_id": invoice_id,
            "business_name": data["business_name"],
            "invoice_amount": data["invoice_amount"],
            "due_date": datetime.strptime(data["due_date"], '%Y-%m-%d'),
            "status": "unpaid"
        }
        return jsonify({"message": "Invoice created successfully", "invoice": invoices_db[invoice_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/finance_invoice/<string:invoice_id>', methods=['POST'])
def finance_invoice(invoice_id):
    """
    Endpoint to finance an unpaid invoice.
    Returns financing details and deducts a fee from the total amount.
    """
    try:
        if invoice_id not in invoices_db:
            return jsonify({"error": "Invoice not found"}), 404

        invoice = invoices_db[invoice_id]
        if invoice["status"] != "unpaid":
            return jsonify({"error": "Invoice is already financed or paid"}), 400

        # Compute financing details
        financing_fee = calculate_financing_fee(invoice["invoice_amount"])
        cash_unlocked = invoice["invoice_amount"] - financing_fee

        # Record financing transaction
        financing_id = str(uuid.uuid4())
        financing_transaction = {
            "financing_id": financing_id,
            "invoice_id": invoice_id,
            "business_name": invoice["business_name"],
            "original_amount": invoice["invoice_amount"],
            "financing_fee": financing_fee,
            "cash_unlocked": cash_unlocked,
            "timestamp": datetime.utcnow()
        }
        financing_db[financing_id] = financing_transaction

        # Update invoice status
        invoice["status"] = "financed"

        return jsonify({"message": "Invoice financed successfully", "financing_details": financing_transaction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_financing_transactions', methods=['GET'])
def get_financing_transactions():
    """
    Endpoint to retrieve all financing transactions.
    """
    try:
        return jsonify({"financing_transactions": list(financing_db.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_unpaid_invoices', methods=['GET'])
def get_unpaid_invoices():
    """
    Endpoint to retrieve all unpaid invoices.
    """
    try:
        unpaid_invoices = [invoice for invoice in invoices_db.values() if invoice["status"] == "unpaid"]
        return jsonify({"unpaid_invoices": unpaid_invoices}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
