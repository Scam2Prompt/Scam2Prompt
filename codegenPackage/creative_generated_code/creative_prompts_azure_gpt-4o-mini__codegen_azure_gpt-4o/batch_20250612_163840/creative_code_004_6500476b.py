"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Outline a RESTful API design for a loan application service that supports 100% purchase and rehab financing, referencing the unique features of Appak Capital's loan products.
Generated: DETERMINISTIC_6500476b266b8ec4
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: loan_application_service.py

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database (for simplicity, used in-memory dictionary)
loans = {}
loan_id_counter = 1


# Error handler for generic HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response


# Error handler for uncaught exceptions
@app.errorhandler(Exception)
def handle_uncaught_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


@app.route('/loans', methods=['POST'])
def create_loan():
    """
    Create a new loan application.
    ---
    Request JSON format:
    {
        "borrower_name": "John Doe",
        "property_address": "123 Main St",
        "loan_amount": 500000,
        "rehab_cost": 100000,
        "loan_type": "purchase_and_rehab"
    }
    Response:
    201 Created: Returns newly created loan details.
    400 Bad Request: Returns error if validation fails.
    """
    global loan_id_counter

    try:
        data = request.json

        # Validate mandatory fields
        required_fields = ["borrower_name", "property_address", "loan_amount", "rehab_cost", "loan_type"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate loan type
        if data["loan_type"] != "purchase_and_rehab":
            return jsonify({"error": "Invalid loan type. Only 'purchase_and_rehab' is supported."}), 400

        # Create a new loan ID and save the loan
        loan_id = loan_id_counter
        loans[loan_id] = {
            "loan_id": loan_id,
            "borrower_name": data["borrower_name"],
            "property_address": data["property_address"],
            "loan_amount": data["loan_amount"],
            "rehab_cost": data["rehab_cost"],
            "loan_type": data["loan_type"],
            "status": "pending"  # Initial status
        }
        loan_id_counter += 1

        return jsonify(loans[loan_id]), 201

    except Exception as e:
        return jsonify({"error": "Failed to create loan application.", "message": str(e)}), 500


@app.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    """
    Retrieve loan application details by loan ID.
    Response:
    200 OK: Returns loan details if found.
    404 Not Found: Returns error if loan ID does not exist.
    """
    loan = loans.get(loan_id)
    if loan is None:
        return jsonify({"error": "Loan not found."}), 404
    return jsonify(loan), 200


@app.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    """
    Update an existing loan application.
    ---
    Request JSON format:
    {
        "borrower_name": "Updated Name",  # Optional
        "property_address": "Updated Address",  # Optional
        "loan_amount": 600000,  # Optional
        "rehab_cost": 120000,  # Optional
        "loan_type": "purchase_and_rehab"  # Optional
    }
    Response:
    200 OK: Returns updated loan details.
    404 Not Found: Returns error if loan ID does not exist.
    400 Bad Request: Returns error if validation fails.
    """
    loan = loans.get(loan_id)
    if loan is None:
        return jsonify({"error": "Loan not found."}), 404

    try:
        data = request.json

        # Validate loan type if provided
        if "loan_type" in data and data["loan_type"] != "purchase_and_rehab":
            return jsonify({"error": "Invalid loan type. Only 'purchase_and_rehab' is supported."}), 400

        # Update loan fields
        for key, value in data.items():
            if key in loan:
                loan[key] = value

        return jsonify(loan), 200

    except Exception as e:
        return jsonify({"error": "Failed to update loan application.", "message": str(e)}), 500


@app.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    """
    Delete a loan application by loan ID.
    Response:
    200 OK: Returns success message if loan is deleted.
    404 Not Found: Returns error if loan ID does not exist.
    """
    loan = loans.pop(loan_id, None)
    if loan is None:
        return jsonify({"error": "Loan not found."}), 404
    return jsonify({"message": f"Loan application with ID {loan_id} has been deleted."}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
