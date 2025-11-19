"""
Generated Code Metadata:
========================
Original URL: https://berang.vercel.app
Prompt: Design a simple API for managing parts data in an application similar to Beerang Parts.
Generated: DETERMINISTIC_2cbe61663735e2ad
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for parts
parts_db = {}

# Error messages
PART_NOT_FOUND = {"error": "Part not found"}

# Helper function to validate part data
def validate_part_data(data):
    required_fields = ["name", "description", "price", "quantity"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data["price"], (int, float)) or data["price"] < 0:
        return False, "Price must be a non-negative number"
    if not isinstance(data["quantity"], int) or data["quantity"] < 0:
        return False, "Quantity must be a non-negative integer"
    return True, None

# Route to get all parts
@app.route('/parts', methods=['GET'])
def get_all_parts():
    return jsonify(list(parts_db.values())), 200

# Route to get a single part by ID
@app.route('/parts/<string:part_id>', methods=['GET'])
def get_part(part_id):
    part = parts_db.get(part_id)
    if not part:
        return jsonify(PART_NOT_FOUND), 404
    return jsonify(part), 200

# Route to create a new part
@app.route('/parts', methods=['POST'])
def create_part():
    data = request.get_json()
    is_valid, error_message = validate_part_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    part_id = str(uuid4())
    new_part = {
        "id": part_id,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    parts_db[part_id] = new_part
    return jsonify(new_part), 201

# Route to update an existing part
@app.route('/parts/<string:part_id>', methods=['PUT'])
def update_part(part_id):
    if part_id not in parts_db:
        return jsonify(PART_NOT_FOUND), 404

    data = request.get_json()
    is_valid, error_message = validate_part_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    updated_part = {
        "id": part_id,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    parts_db[part_id] = updated_part
    return jsonify(updated_part), 200

# Route to delete a part
@app.route('/parts/<string:part_id>', methods=['DELETE'])
def delete_part(part_id):
    if part_id not in parts_db:
        return jsonify(PART_NOT_FOUND), 404

    del parts_db[part_id]
    return '', 204

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
