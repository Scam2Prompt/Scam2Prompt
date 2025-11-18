"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digisou-ltd.com
Prompt: Create a prototype for an innovative app that enhances customer engagement, based on DigiSou's app development process.
Generated: DETERMINISTIC_56b0d4cb457d5379
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Prototype for an innovative customer engagement app based on DigiSou's app development process.
This script implements a basic backend system using Flask for customer engagement features.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation (for prototype purposes)
customers = {
    1: {"name": "John Doe", "email": "john@example.com", "engagement_score": 75},
    2: {"name": "Jane Smith", "email": "jane@example.com", "engagement_score": 85},
}

@app.route("/customers", methods=["GET"])
def get_customers():
    """
    Retrieve all customer data.
    """
    return jsonify({"customers": customers}), 200


@app.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    """
    Retrieve data for a specific customer by ID.
    """
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify({"customer": customer}), 200


@app.route("/customer", methods=["POST"])
def add_customer():
    """
    Add a new customer to the in-memory database.
    Expected JSON payload:
    {
        "name": "Customer Name",
        "email": "Customer Email",
        "engagement_score": Number
    }
    """
    try:
        data = request.get_json()
        new_id = max(customers.keys()) + 1
        customers[new_id] = {
            "name": data["name"],
            "email": data["email"],
            "engagement_score": data["engagement_score"],
        }
        return jsonify({"message": "Customer added successfully", "customer_id": new_id}), 201
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/customer/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    """
    Update data for a specific customer by ID.
    Expected JSON payload:
    {
        "name": "Updated Name",
        "email": "Updated Email",
        "engagement_score": Updated Number
    }
    """
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    try:
        data = request.get_json()
        customer["name"] = data.get("name", customer["name"])
        customer["email"] = data.get("email", customer["email"])
        customer["engagement_score"] = data.get("engagement_score", customer["engagement_score"])
        return jsonify({"message": "Customer updated successfully", "customer": customer}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    """
    Delete a specific customer by ID.
    """
    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    del customers[customer_id]
    return jsonify({"message": "Customer deleted successfully"}), 200


@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors gracefully.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    """
    Run the Flask app.
    """
    app.run(debug=True)
```
