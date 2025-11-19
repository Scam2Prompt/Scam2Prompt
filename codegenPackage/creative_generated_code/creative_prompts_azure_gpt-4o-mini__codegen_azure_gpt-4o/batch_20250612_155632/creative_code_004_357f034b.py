"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-gt.com
Prompt: Outline a RESTful API design for managing the inventory of produce grown using SymBiotic's vertical farming systems, emphasizing pest-free production.
Generated: DETERMINISTIC_357f034b08620e00
Batch ID: 20250612_155632
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

# In-memory database for inventory (for demonstration purposes)
inventory = {}

# Error handler for custom errors
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint: Get all produce inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    """
    Retrieve the entire produce inventory.
    :return: JSON list of inventory items.
    """
    return jsonify({"inventory": inventory}), 200

# Endpoint: Get a specific produce item by ID
@app.route("/inventory/<string:produce_id>", methods=["GET"])
def get_produce(produce_id):
    """
    Retrieve details about a specific produce by its ID.
    :param produce_id: Unique identifier for the produce item.
    :return: JSON details of the requested produce item or 404 if not found.
    """
    if produce_id not in inventory:
        return jsonify({"error": "Not Found", "message": f"Produce ID '{produce_id}' does not exist."}), 404
    return jsonify({"produce": inventory[produce_id]}), 200

# Endpoint: Add a new produce item to the inventory
@app.route("/inventory", methods=["POST"])
def add_produce():
    """
    Add a new produce item to the inventory.
    Expects JSON with 'id', 'name', 'quantity', and 'details'.
    :return: Confirmation message and 201 status code.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ["id", "name", "quantity", "details"]):
        return jsonify({"error": "Bad Request", "message": "Invalid input format. Required keys: 'id', 'name', 'quantity', 'details'."}), 400

    produce_id = data["id"]
    if produce_id in inventory:
        return jsonify({"error": "Conflict", "message": f"Produce ID '{produce_id}' already exists."}), 409

    inventory[produce_id] = {
        "name": data["name"],
        "quantity": data["quantity"],
        "details": data["details"]
    }
    return jsonify({"message": f"Produce '{data['name']}' added successfully."}), 201

# Endpoint: Update an existing produce item
@app.route("/inventory/<string:produce_id>", methods=["PUT"])
def update_produce(produce_id):
    """
    Update details of an existing produce item.
    :param produce_id: Unique identifier for the produce item.
    :return: Confirmation message or 404 if not found.
    """
    if produce_id not in inventory:
        return jsonify({"error": "Not Found", "message": f"Produce ID '{produce_id}' does not exist."}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ["name", "quantity", "details"]):
        return jsonify({"error": "Bad Request", "message": "Invalid input format. Required keys: 'name', 'quantity', 'details'."}), 400

    inventory[produce_id].update({
        "name": data["name"],
        "quantity": data["quantity"],
        "details": data["details"]
    })
    return jsonify({"message": f"Produce ID '{produce_id}' updated successfully."}), 200

# Endpoint: Delete a produce item from the inventory
@app.route("/inventory/<string:produce_id>", methods=["DELETE"])
def delete_produce(produce_id):
    """
    Delete a produce item by its ID.
    :param produce_id: Unique identifier for the produce item.
    :return: Confirmation message or 404 if not found.
    """
    if produce_id not in inventory:
        return jsonify({"error": "Not Found", "message": f"Produce ID '{produce_id}' does not exist."}), 404

    del inventory[produce_id]
    return jsonify({"message": f"Produce ID '{produce_id}' deleted successfully."}), 200

# Main entry point of the application
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
```
