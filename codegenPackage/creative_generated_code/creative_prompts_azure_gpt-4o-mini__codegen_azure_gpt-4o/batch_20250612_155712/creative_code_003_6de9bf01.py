"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Develop an API endpoint that allows users to apply for settlement loans, reflecting the user-friendly process highlighted by Rhino Finance.
Generated: DETERMINISTIC_6de9bf01257ca238
Batch ID: 20250612_155712
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

app = Flask(__name__)

# In-memory data storage for demonstration purposes
applications = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Generic error handler for unexpected exceptions."""
    response = {
        "error": str(e)
    }
    if isinstance(e, HTTPException):
        response["code"] = e.code
    else:
        response["code"] = 500
    return jsonify(response), response["code"]

@app.route("/apply-for-loan", methods=["POST"])
def apply_for_loan():
    """
    API endpoint to allow users to apply for settlement loans.
    Expects JSON input with the following fields:
        - full_name (str): Applicant's full name.
        - email (str): Applicant's email address.
        - amount_requested (float): Loan amount requested.
        - case_details (str): Brief description of the settlement case.
    """
    try:
        # Validate input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request must contain valid JSON data"}), 400

        required_fields = ["full_name", "email", "amount_requested", "case_details"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate individual fields
        full_name = str(data["full_name"]).strip()
        email = str(data["email"]).strip()
        amount_requested = data["amount_requested"]
        case_details = str(data["case_details"]).strip()

        if not full_name or not email or not case_details:
            return jsonify({"error": "Fields 'full_name', 'email', and 'case_details' cannot be empty"}), 400

        if not isinstance(amount_requested, (int, float)) or amount_requested <= 0:
            return jsonify({"error": "Field 'amount_requested' must be a positive number"}), 400

        # Simulate saving the application (e.g., to a database)
        application = {
            "id": len(applications) + 1,
            "full_name": full_name,
            "email": email,
            "amount_requested": amount_requested,
            "case_details": case_details,
        }
        applications.append(application)

        # Return a success response
        return jsonify({"message": "Loan application submitted successfully", "application": application}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route("/applications", methods=["GET"])
def get_applications():
    """
    API endpoint to retrieve all loan applications.
    Returns a JSON list of all applications.
    """
    return jsonify({"applications": applications}), 200

if __name__ == "__main__":
    app.run(debug=True)
```
