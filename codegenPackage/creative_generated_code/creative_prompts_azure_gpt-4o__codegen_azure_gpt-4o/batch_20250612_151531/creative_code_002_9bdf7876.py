"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Generate code for a web service that connects users to lenders based on predefined criteria, such as loan amount and credit score, using a ping-tree model for lender selection.
Generated: DETERMINISTIC_9bdf7876aa15dd9a
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data: list of lenders
lenders = [
    {"id": 1, "name": "Lender A", "min_amount": 1000, "max_amount": 5000, "min_credit_score": 600},
    {"id": 2, "name": "Lender B", "min_amount": 2000, "max_amount": 10000, "min_credit_score": 650},
    {"id": 3, "name": "Lender C", "min_amount": 5000, "max_amount": 15000, "min_credit_score": 700},
]

# Ping-tree model: evaluate lenders in predefined order
def find_lender(amount, credit_score):
    for lender in lenders:
        if lender["min_amount"] <= amount <= lender["max_amount"] and credit_score >= lender["min_credit_score"]:
            return lender
    return None

@app.route("/find-lender", methods=["POST"])
def connect_user_to_lender():
    """
    Endpoint to connect users to lenders based on loan amount and credit score.
    Request payload:
        {
            "amount": <loan amount>,
            "credit_score": <user credit score>
        }
    Response:
        {
            "success": true/false,
            "lender": <matched lender or None>,
            "message": <status message>
        }
    """
    try:
        # Validate request data
        data = request.get_json()
        if not data or "amount" not in data or "credit_score" not in data:
            return jsonify({
                "success": False,
                "message": "Invalid request payload. Please include 'amount' and 'credit_score'."
            }), 400

        amount = data["amount"]
        credit_score = data["credit_score"]

        # Find a matching lender using the ping-tree model
        lender = find_lender(amount, credit_score)

        if lender:
            return jsonify({
                "success": True,
                "lender": lender,
                "message": "Lender found successfully."
            }), 200
        else:
            return jsonify({
                "success": False,
                "lender": None,
                "message": "No lender found matching the criteria."
            }), 404
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({
            "success": False,
            "message": "An internal error occurred. Please try again later."
        }), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
