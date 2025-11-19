"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Create a REST API endpoint for a web application that facilitates collaborative management, similar to the frameworks Romain Rissoan uses in his training sessions.
Generated: DETERMINISTIC_563da3d310121821
Batch ID: 20250612_161745
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

app = Flask(__name__)

# In-memory storage for collaborative management data
# In production, this would be replaced with a database
collaborative_data = {}

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

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new collaborative management entry
@app.route('/api/collaborative', methods=['POST'])
def create_collaborative_entry():
    """
    Create a new collaborative management entry.
    Expected JSON payload:
    {
        "id": "unique_identifier",
        "name": "Name of the entry",
        "description": "Description of the entry"
    }
    """
    try:
        data = request.get_json()
        if not data or 'id' not in data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        entry_id = data['id']
        if entry_id in collaborative_data:
            return jsonify({"error": "Conflict", "message": "Entry with this ID already exists"}), 409

        collaborative_data[entry_id] = {
            "name": data['name'],
            "description": data['description']
        }
        return jsonify({"message": "Entry created successfully", "data": collaborative_data[entry_id]}), 201
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to retrieve a collaborative management entry by ID
@app.route('/api/collaborative/<string:entry_id>', methods=['GET'])
def get_collaborative_entry(entry_id):
    """
    Retrieve a collaborative management entry by ID.
    """
    try:
        entry = collaborative_data.get(entry_id)
        if not entry:
            return jsonify({"error": "Not Found", "message": "Entry not found"}), 404

        return jsonify({"data": entry}), 200
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to update a collaborative management entry by ID
@app.route('/api/collaborative/<string:entry_id>', methods=['PUT'])
def update_collaborative_entry(entry_id):
    """
    Update an existing collaborative management entry.
    Expected JSON payload:
    {
        "name": "Updated name",
        "description": "Updated description"
    }
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        entry = collaborative_data.get(entry_id)
        if not entry:
            return jsonify({"error": "Not Found", "message": "Entry not found"}), 404

        collaborative_data[entry_id] = {
            "name": data['name'],
            "description": data['description']
        }
        return jsonify({"message": "Entry updated successfully", "data": collaborative_data[entry_id]}), 200
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to delete a collaborative management entry by ID
@app.route('/api/collaborative/<string:entry_id>', methods=['DELETE'])
def delete_collaborative_entry(entry_id):
    """
    Delete a collaborative management entry by ID.
    """
    try:
        entry = collaborative_data.pop(entry_id, None)
        if not entry:
            return jsonify({"error": "Not Found", "message": "Entry not found"}), 404

        return jsonify({"message": "Entry deleted successfully"}), 200
    except Exception as e:
        return handle_generic_exception(e)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
