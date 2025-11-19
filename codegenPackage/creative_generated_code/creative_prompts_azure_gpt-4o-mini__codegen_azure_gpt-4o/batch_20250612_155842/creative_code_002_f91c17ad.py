"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Create an API endpoint that allows users to submit invoices for factoring, ensuring it includes features for tracking payment status and reducing internal costs.
Generated: DETERMINISTIC_f91c17ad1357e36d
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory database for storing invoices (replace with real DB in production)
invoices_db = {}

# Possible statuses for payment tracking
PAYMENT_STATUSES = ["Pending", "Processing", "Paid", "Rejected"]

# Helper function to validate invoice data
def validate_invoice_data(data):
    required_fields = ["invoice_number", "amount", "due_date"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        return "Invalid amount. Must be a positive number."
    try:
        datetime.strptime(data["due_date"], '%Y-%m-%d')
    except ValueError:
        return "Invalid due_date format. Expected YYYY-MM-DD."
    return None

@app.route('/api/invoices', methods=['POST'])
def submit_invoice():
    """
    Endpoint to submit a new invoice for factoring.

    Request Body:
    {
        "invoice_number": "INV12345",
        "amount": 1000.50,
        "due_date": "2023-12-01"
    }

    Returns:
        Success: HTTP 201 with invoice details
        Failure: HTTP 400 with error message
    """
    try:
        invoice_data = request.json

        # Validate input data
        validation_error = validate_invoice_data(invoice_data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Generate unique invoice ID and store invoice
        invoice_id = str(uuid.uuid4())
        invoice = {
            "id": invoice_id,
            "invoice_number": invoice_data["invoice_number"],
            "amount": invoice_data["amount"],
            "due_date": invoice_data["due_date"],
            "payment_status": "Pending",  # Initial status
            "submission_date": datetime.utcnow().isoformat()
        }
        invoices_db[invoice_id] = invoice

        return jsonify({"message": "Invoice submitted successfully", "invoice": invoice}), 201

    except Exception as e:
        # Catch all unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/invoices/<invoice_id>', methods=['GET'])
def get_invoice_status(invoice_id):
    """
    Endpoint to track payment status of an invoice.

    Path Parameter:
        invoice_id: ID of the invoice to retrieve

    Returns:
        Success: HTTP 200 with invoice details
        Failure: HTTP 404 if invoice not found
    """
    try:
        invoice = invoices_db.get(invoice_id)
        if not invoice:
            return jsonify({"error": "Invoice not found"}), 404

        return jsonify({"invoice": invoice}), 200

    except Exception as e:
        # Catch all unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/invoices/<invoice_id>', methods=['PUT'])
def update_payment_status(invoice_id):
    """
    Endpoint to update the payment status of an invoice.

    Path Parameter:
        invoice_id: ID of the invoice to update

    Request Body:
    {
        "payment_status": "Paid"
    }

    Returns:
        Success: HTTP 200 with updated invoice details
        Failure: HTTP 400 if invalid status or HTTP 404 if invoice not found
    """
    try:
        invoice = invoices_db.get(invoice_id)
        if not invoice:
            return jsonify({"error": "Invoice not found"}), 404

        payment_status = request.json.get("payment_status")
        if payment_status not in PAYMENT_STATUSES:
            return jsonify({"error": f"Invalid payment_status. Allowed values: {PAYMENT_STATUSES}"}), 400

        # Update payment status
        invoice["payment_status"] = payment_status
        return jsonify({"message": "Payment status updated successfully", "invoice": invoice}), 200

    except Exception as e:
        # Catch all unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
