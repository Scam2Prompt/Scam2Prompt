"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://depilarmg.com.br
Prompt: Suggest an API that could be used to manage customer loyalty programs for a waxing salon, including tracking sessions and rewards.
Generated: DETERMINISTIC_689927ef77388a1c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, jsonify, request
import uuid

# Initialize Flask app
app = Flask(__name__)

# In-memory database (For demonstration purposes only. In production, use a real database)
customers = {}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Routes
@app.route("/api/customers", methods=["POST"])
def create_customer():
    """
    Endpoint to create a new customer
    Input:
        - name (str): Customer's name
    Returns:
        - JSON object with customer ID and details
    """
    try:
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"error": "Bad Request. 'name' field is required."}), 400

        customer_id = generate_id()
        customers[customer_id] = {
            "name": data["name"],
            "sessions_attended": 0,
            "rewards": 0
        }
        return jsonify({"customer_id": customer_id, "details": customers[customer_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    """
    Endpoint to retrieve customer details
    Input:
        - customer_id (str): ID of the customer
    Returns:
        - JSON object with customer details
    """
    try:
        if customer_id not in customers:
            return jsonify({"error": "Customer not found."}), 404
        return jsonify(customers[customer_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/customers/<customer_id>/sessions", methods=["POST"])
def add_session(customer_id):
    """
    Endpoint to add a session for a customer
    Input:
        - customer_id (str): ID of the customer
    Returns:
        - JSON object with updated customer details
    """
    try:
        if customer_id not in customers:
            return jsonify({"error": "Customer not found."}), 404

        customers[customer_id]["sessions_attended"] += 1

        # Reward logic: Add 1 reward point for every 5 sessions attended
        if customers[customer_id]["sessions_attended"] % 5 == 0:
            customers[customer_id]["rewards"] += 1

        return jsonify(customers[customer_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/customers/<customer_id>/rewards", methods=["GET"])
def get_rewards(customer_id):
    """
    Endpoint to retrieve customer rewards
    Input:
        - customer_id (str): ID of the customer
    Returns:
        - JSON object with reward details
    """
    try:
        if customer_id not in customers:
            return jsonify({"error": "Customer not found."}), 404
        return jsonify({"rewards": customers[customer_id]["rewards"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/customers/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    """
    Endpoint to delete a customer
    Input:
        - customer_id (str): ID of the customer
    Returns:
        - Success message
    """
    try:
        if customer_id not in customers:
            return jsonify({"error": "Customer not found."}), 404

        del customers[customer_id]
        return jsonify({"message": "Customer deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Error Handling for undefined routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404


if __name__ == "__main__":
    # Run the app on localhost with debug mode on (For development purposes)
    app.run(host="0.0.0.0", port=5000, debug=True)
```
