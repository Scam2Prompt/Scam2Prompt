"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Suggest an API for managing eco-friendly cleaning supply inventory, ensuring the supplies are safe for families and meet professional cleaning standards.
Generated: DETERMINISTIC_75ec0cfe5241d404
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory inventory database
inventory = {}

# Function to validate item data
def validate_item(data):
    required_fields = ["name", "description", "quantity", "family_safe", "professional_grade"]
    for field in required_fields:
        if field not in data:
            return f"'{field}' is a required field."
        if field == "quantity" and not isinstance(data[field], int):
            return "'quantity' must be an integer."
        if field in ["family_safe", "professional_grade"] and not isinstance(data[field], bool):
            return f"'{field}' must be a boolean."
    return None

# Route to add a new item to the inventory
@app.route('/inventory', methods=['POST'])
def add_item():
    try:
        data = request.json
        # Validate the input data
        validation_error = validate_item(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400
        
        # Generate a unique ID for the item
        item_id = str(uuid.uuid4())
        inventory[item_id] = {
            "name": data["name"],
            "description": data["description"],
            "quantity": data["quantity"],
            "family_safe": data["family_safe"],
            "professional_grade": data["professional_grade"]
        }
        return jsonify({"message": "Item added successfully.", "item_id": item_id}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to retrieve all items in the inventory
@app.route('/inventory', methods=['GET'])
def get_all_items():
    try:
        return jsonify(inventory), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to retrieve a specific item by ID
@app.route('/inventory/<item_id>', methods=['GET'])
def get_item(item_id):
    try:
        item = inventory.get(item_id)
        if not item:
            return jsonify({"error": "Item not found."}), 404
        return jsonify(item), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to update a specific item by ID
@app.route('/inventory/<item_id>', methods=['PUT'])
def update_item(item_id):
    try:
        item = inventory.get(item_id)
        if not item:
            return jsonify({"error": "Item not found."}), 404
        
        data = request.json
        # Validate the input data
        validation_error = validate_item(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400
        
        # Update the item details
        inventory[item_id] = {
            "name": data["name"],
            "description": data["description"],
            "quantity": data["quantity"],
            "family_safe": data["family_safe"],
            "professional_grade": data["professional_grade"]
        }
        return jsonify({"message": "Item updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to delete a specific item by ID
@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        if item_id not in inventory:
            return jsonify({"error": "Item not found."}), 404
        
        del inventory[item_id]
        return jsonify({"message": "Item deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```
