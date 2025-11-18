"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Suggest an API for managing fee payments online for a school, similar to the "Pay Fees" feature on the Deepti Convent Higher Secondary School website, and demonstrate its implementation.
Generated: DETERMINISTIC_38698c61f68928ca
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import uuid
import datetime

# Initialize Flask app
app = Flask(__name__)

# In-memory database to store fee payment records (for demonstration purposes)
payments_db = {}

# Helper function to generate unique payment IDs
def generate_payment_id():
    return str(uuid.uuid4())

# API Endpoint: View all payments
@app.route('/api/payments', methods=['GET'])
def get_all_payments():
    """
    Endpoint to fetch all payment records.

    Returns:
        JSON response containing all payment records.
    """
    return jsonify({"status": "success", "data": payments_db}), 200

# API Endpoint: Make a payment
@app.route('/api/payments', methods=['POST'])
def make_payment():
    """
    Endpoint to make a fee payment.

    Request JSON:
    {
        "student_id": "<unique_student_id>",
        "amount": <payment_amount>,
        "payment_method": "<method>",  # e.g., "Credit Card", "Bank Transfer"
        "description": "<optional_description>"
    }
    
    Returns:
        JSON response confirming the payment or an error message.
    """
    try:
        # Parse request data
        data = request.json

        # Validate required fields
        required_fields = ["student_id", "amount", "payment_method"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing required field: {field}"}), 400

        # Create a payment record
        payment_id = generate_payment_id()
        payment_record = {
            "payment_id": payment_id,
            "student_id": data["student_id"],
            "amount": data["amount"],
            "payment_method": data["payment_method"],
            "description": data.get("description", ""),  # Optional field
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Store the payment record
        payments_db[payment_id] = payment_record

        # Return success response
        return jsonify({"status": "success", "data": payment_record}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# API Endpoint: Get payment by ID
@app.route('/api/payments/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    """
    Endpoint to fetch a specific payment record by ID.

    URL Parameter:
        payment_id: The unique ID of the payment.

    Returns:
        JSON response containing the payment record or an error message.
    """
    try:
        # Fetch payment record
        payment_record = payments_db.get(payment_id)

        if not payment_record:
            return jsonify({"status": "error", "message": "Payment not found"}), 404

        return jsonify({"status": "success", "data": payment_record}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# API Endpoint: Delete payment by ID
@app.route('/api/payments/<payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    """
    Endpoint to delete a payment record by ID.

    URL Parameter:
        payment_id: The unique ID of the payment.

    Returns:
        JSON response confirming deletion or an error message.
    """
    try:
        # Check if the payment exists
        if payment_id not in payments_db:
            return jsonify({"status": "error", "message": "Payment not found"}), 404

        # Delete the payment record
        del payments_db[payment_id]

        return jsonify({"status": "success", "message": "Payment deleted successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
