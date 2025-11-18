"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Design a REST API for managing multi-location inventory transfers, incorporating the interconnection features mentioned in TICOM Software's retail solutions.
Generated: DETERMINISTIC_5a3d5b0f72f1365e
Batch ID: 20250612_154452
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

# Simulated inventory database
inventory = {
    "location_1": {"item_1": 50, "item_2": 30},
    "location_2": {"item_1": 20, "item_2": 60},
    "location_3": {"item_1": 70, "item_2": 10},
}

# Error handler for custom and generic exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal server error"}), 500

# Route: Check inventory at a specific location
@app.route('/inventory/<location>', methods=['GET'])
def get_inventory(location):
    if location not in inventory:
        return jsonify({"error": "Location not found"}), 404
    return jsonify({"location": location, "inventory": inventory[location]})

# Route: Transfer items between locations
@app.route('/inventory/transfer', methods=['POST'])
def transfer_inventory():
    data = request.json
    source = data.get("source")
    destination = data.get("destination")
    item = data.get("item")
    quantity = data.get("quantity")

    # Validate input
    if not source or not destination or not item or quantity is None:
        return jsonify({"error": "Missing required fields"}), 400
    if not isinstance(quantity, int) or quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400
    if source not in inventory or destination not in inventory:
        return jsonify({"error": "Invalid source or destination location"}), 404
    if item not in inventory[source]:
        return jsonify({"error": f"Item '{item}' not found in source location"}), 404
    if inventory[source][item] < quantity:
        return jsonify({"error": "Insufficient stock in source location"}), 400

    # Perform transfer
    inventory[source][item] -= quantity
    if item in inventory[destination]:
        inventory[destination][item] += quantity
    else:
        inventory[destination][item] = quantity

    return jsonify({"message": "Transfer successful", "source_inventory": inventory[source], "destination_inventory": inventory[destination]})

# Route: Add/remove inventory at a location
@app.route('/inventory/<location>', methods=['PUT'])
def update_inventory(location):
    if location not in inventory:
        return jsonify({"error": "Location not found"}), 404

    data = request.json
    item = data.get("item")
    quantity = data.get("quantity")

    # Validate input
    if not item or quantity is None:
        return jsonify({"error": "Missing required fields"}), 400
    if not isinstance(quantity, int):
        return jsonify({"error": "Quantity must be an integer"}), 400

    # Update inventory
    if item in inventory[location]:
        inventory[location][item] += quantity
        if inventory[location][item] < 0:
            inventory[location][item] = 0  # Prevent negative inventory
    else:
        if quantity < 0:
            return jsonify({"error": "Cannot remove non-existent item"}), 400
        inventory[location][item] = quantity

    return jsonify({"message": "Inventory updated", "updated_inventory": inventory[location]})

# Route: Add a new location to the inventory database
@app.route('/inventory/new-location', methods=['POST'])
def add_location():
    data = request.json
    location = data.get("location")

    # Validate input
    if not location:
        return jsonify({"error": "Location name is required"}), 400
    if location in inventory:
        return jsonify({"error": "Location already exists"}), 400

    # Add location
    inventory[location] = {}
    return jsonify({"message": "New location added", "location": location})

# Route: Delete a location from the inventory database
@app.route('/inventory/<location>', methods=['DELETE'])
def delete_location(location):
    if location not in inventory:
        return jsonify({"error": "Location not found"}), 404

    # Delete location
    del inventory[location]
    return jsonify({"message": "Location deleted", "location": location})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
