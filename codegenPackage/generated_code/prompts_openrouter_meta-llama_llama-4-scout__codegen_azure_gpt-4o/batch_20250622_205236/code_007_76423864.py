"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Generate a RESTful API documentation for managing mobile phone accessories, including endpoints for creating, reading, updating, and deleting products.
Generated: DETERMINISTIC_76423864273d2393
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for storing accessories
accessories = {}
next_id = 1

# Error messages
NOT_FOUND_ERROR = {"error": "Accessory not found"}
BAD_REQUEST_ERROR = {"error": "Invalid request data"}

# Helper function to validate accessory data
def validate_accessory_data(data):
    required_fields = ["name", "category", "price", "stock"]
    return all(field in data for field in required_fields)

# Endpoint: Create a new accessory
@app.route('/accessories', methods=['POST'])
def create_accessory():
    """
    Create a new accessory.
    Request Body:
        {
            "name": "string",
            "category": "string",
            "price": float,
            "stock": int
        }
    Response:
        201 Created: Returns the created accessory.
        400 Bad Request: Returns an error if the request data is invalid.
    """
    global next_id
    data = request.get_json()
    if not validate_accessory_data(data):
        return jsonify(BAD_REQUEST_ERROR), 400

    accessory = {
        "id": next_id,
        "name": data["name"],
        "category": data["category"],
        "price": data["price"],
        "stock": data["stock"]
    }
    accessories[next_id] = accessory
    next_id += 1
    return jsonify(accessory), 201

# Endpoint: Get all accessories
@app.route('/accessories', methods=['GET'])
def get_accessories():
    """
    Get all accessories.
    Response:
        200 OK: Returns a list of all accessories.
    """
    return jsonify(list(accessories.values())), 200

# Endpoint: Get a single accessory by ID
@app.route('/accessories/<int:accessory_id>', methods=['GET'])
def get_accessory(accessory_id):
    """
    Get a single accessory by ID.
    Response:
        200 OK: Returns the accessory if found.
        404 Not Found: Returns an error if the accessory does not exist.
    """
    accessory = accessories.get(accessory_id)
    if not accessory:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify(accessory), 200

# Endpoint: Update an accessory by ID
@app.route('/accessories/<int:accessory_id>', methods=['PUT'])
def update_accessory(accessory_id):
    """
    Update an accessory by ID.
    Request Body:
        {
            "name": "string",
            "category": "string",
            "price": float,
            "stock": int
        }
    Response:
        200 OK: Returns the updated accessory.
        400 Bad Request: Returns an error if the request data is invalid.
        404 Not Found: Returns an error if the accessory does not exist.
    """
    data = request.get_json()
    if not validate_accessory_data(data):
        return jsonify(BAD_REQUEST_ERROR), 400

    accessory = accessories.get(accessory_id)
    if not accessory:
        return jsonify(NOT_FOUND_ERROR), 404

    accessory.update({
        "name": data["name"],
        "category": data["category"],
        "price": data["price"],
        "stock": data["stock"]
    })
    return jsonify(accessory), 200

# Endpoint: Delete an accessory by ID
@app.route('/accessories/<int:accessory_id>', methods=['DELETE'])
def delete_accessory(accessory_id):
    """
    Delete an accessory by ID.
    Response:
        200 OK: Returns a success message if the accessory is deleted.
        404 Not Found: Returns an error if the accessory does not exist.
    """
    accessory = accessories.pop(accessory_id, None)
    if not accessory:
        return jsonify(NOT_FOUND_ERROR), 404
    return jsonify({"message": "Accessory deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
