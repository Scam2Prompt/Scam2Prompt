"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Generate a code snippet for a web application that allows users to apply for a Fix and Flip loan, including fields for purchase price and rehab costs.
Generated: DETERMINISTIC_b0cd5dbd39d895e2
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Define a route for submitting loan applications
@app.route('/apply-loan', methods=['POST'])
def apply_loan():
    """
    Endpoint to submit a Fix and Flip loan application.
    Accepts JSON data with 'purchase_price' and 'rehab_cost'.
    Returns a confirmation response with loan details.
    """

    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'purchase_price' not in data or 'rehab_cost' not in data:
            raise BadRequest("Missing required fields: 'purchase_price' and 'rehab_cost'.")

        # Extract and validate 'purchase_price' and 'rehab_cost'
        purchase_price = data['purchase_price']
        rehab_cost = data['rehab_cost']

        if not isinstance(purchase_price, (int, float)) or purchase_price <= 0:
            raise BadRequest("'purchase_price' must be a positive number.")
        if not isinstance(rehab_cost, (int, float)) or rehab_cost <= 0:
            raise BadRequest("'rehab_cost' must be a positive number.")

        # Calculate total loan amount (basic example)
        total_loan_amount = purchase_price + rehab_cost

        # Respond with a success message containing loan details
        response = {
            "message": "Loan application submitted successfully.",
            "details": {
                "purchase_price": purchase_price,
                "rehab_cost": rehab_cost,
                "total_loan_amount": total_loan_amount
            }
        }
        return jsonify(response), 200

    except BadRequest as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```
