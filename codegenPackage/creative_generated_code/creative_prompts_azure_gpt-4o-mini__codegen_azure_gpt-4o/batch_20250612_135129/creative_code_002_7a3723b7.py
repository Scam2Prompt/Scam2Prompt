"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelgastech.co.ke
Prompt: How can I implement a REST API for managing fuel gas data in my application?
Generated: DETERMINISTIC_7a3723b71191808d
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation of a REST API for managing fuel gas data using Python with the Flask framework:

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for demonstration purposes
fuel_gas_data = {}  # Example: {1: {"name": "Gasoline", "price": 3.5, "quantity": 100}}

# Error handler for catching exceptions globally
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to retrieve all fuel gas records
@app.route('/fuel_gas', methods=['GET'])
def get_all_fuel_gas():
    """
    Retrieve all fuel gas records.
    """
    return jsonify({"fuel_gas_data": fuel_gas_data}), 200

# Endpoint to retrieve a specific fuel gas record by ID
@app.route('/fuel_gas/<int:gas_id>', methods=['GET'])
def get_fuel_gas(gas_id):
    """
    Retrieve a specific fuel gas record by ID.
    """
    gas_data = fuel_gas_data.get(gas_id)
    if not gas_data:
        return jsonify({"error": "Not Found", "message": f"Fuel gas with ID {gas_id} not found"}), 404
    return jsonify({"fuel_gas_data": gas_data}), 200

# Endpoint to create a new fuel gas record
@app.route('/fuel_gas', methods=['POST'])
def create_fuel_gas():
    """
    Create a new fuel gas record.
    """
    try:
        data = request.json
        gas_id = data.get("id")
        name = data.get("name")
        price = data.get("price")
        quantity = data.get("quantity")

        # Validate input
        if not gas_id or not name or price is None or quantity is None:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400
        if gas_id in fuel_gas_data:
            return jsonify({"error": "Conflict", "message": f"Fuel gas with ID {gas_id} already exists"}), 409

        # Add to in-memory storage
        fuel_gas_data[gas_id] = {"name": name, "price": price, "quantity": quantity}
        return jsonify({"message": "Fuel gas created successfully", "fuel_gas_data": fuel_gas_data[gas_id]}), 201
    except Exception as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Endpoint to update an existing fuel gas record
@app.route('/fuel_gas/<int:gas_id>', methods=['PUT'])
def update_fuel_gas(gas_id):
    """
    Update an existing fuel gas record.
    """
    try:
        data = request.json
        gas_data = fuel_gas_data.get(gas_id)

        if not gas_data:
            return jsonify({"error": "Not Found", "message": f"Fuel gas with ID {gas_id} not found"}), 404

        # Update record fields
        gas_data["name"] = data.get("name", gas_data["name"])
        gas_data["price"] = data.get("price", gas_data["price"])
        gas_data["quantity"] = data.get("quantity", gas_data["quantity"])

        fuel_gas_data[gas_id] = gas_data
        return jsonify({"message": "Fuel gas updated successfully", "fuel_gas_data": gas_data}), 200
    except Exception as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Endpoint to delete a fuel gas record by ID
@app.route('/fuel_gas/<int:gas_id>', methods=['DELETE'])
def delete_fuel_gas(gas_id):
    """
    Delete a fuel gas record by ID.
    """
    if gas_id not in fuel_gas_data:
        return jsonify({"error": "Not Found", "message": f"Fuel gas with ID {gas_id} not found"}), 404

    del fuel_gas_data[gas_id]
    return jsonify({"message": f"Fuel gas with ID {gas_id} deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

> Dependency: Make sure Flask is installed (`pip install flask`).
