"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Develop a Python API to handle requests and responses for a fire safety service company's customer portal."
Generated: DETERMINISTIC_3c68b424dee2a927
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory database simulation (for demonstration purposes)
customers = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "address": "123 Main St"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "address": "456 Elm St"}
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

# Route to get a specific customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer), 200

# Route to add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "email", "address")):
            return jsonify({"error": "Invalid input"}), 400

        new_customer = {
            "id": max(c['id'] for c in customers) + 1 if customers else 1,
            "name": data["name"],
            "email": data["email"],
            "address": data["address"]
        }
        customers.append(new_customer)
        return jsonify(new_customer), 201
    except Exception as e:
        return jsonify({"error": "Failed to add customer", "message": str(e)}), 500

# Route to update an existing customer
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    try:
        data = request.get_json()
        if not data or not any(key in data for key in ("name", "email", "address")):
            return jsonify({"error": "Invalid input"}), 400

        customer.update({key: data[key] for key in data if key in customer})
        return jsonify(customer), 200
    except Exception as e:
        return jsonify({"error": "Failed to update customer", "message": str(e)}), 500

# Route to delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    customers.remove(customer)
    return jsonify({"message": "Customer deleted successfully"}), 200

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
