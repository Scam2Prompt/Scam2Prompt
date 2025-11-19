"""
Generated Code Metadata:
========================
Original URL: https://trait-sniper.pro
Prompt: "How would you design a RESTful API for a trait analysis service like Trait Sniper, including endpoints and request/response formats?"
Generated: DETERMINISTIC_9e92271a47f593b1
Batch ID: 20250622_205751
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

# In-memory database for demonstration purposes
traits_db = {
    "1": {"id": 1, "name": "Trait A", "description": "Description of Trait A", "score": 85},
    "2": {"id": 2, "name": "Trait B", "description": "Description of Trait B", "score": 90},
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint: Get all traits
@app.route('/api/traits', methods=['GET'])
def get_traits():
    """
    GET /api/traits
    Returns a list of all traits.
    """
    return jsonify(list(traits_db.values())), 200

# Endpoint: Get a specific trait by ID
@app.route('/api/traits/<trait_id>', methods=['GET'])
def get_trait(trait_id):
    """
    GET /api/traits/<trait_id>
    Returns the details of a specific trait by ID.
    """
    trait = traits_db.get(trait_id)
    if not trait:
        return jsonify({"error": "Not Found", "message": "Trait not found"}), 404
    return jsonify(trait), 200

# Endpoint: Create a new trait
@app.route('/api/traits', methods=['POST'])
def create_trait():
    """
    POST /api/traits
    Creates a new trait. Expects JSON payload with 'name', 'description', and 'score'.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "description", "score")):
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    new_id = str(len(traits_db) + 1)
    new_trait = {
        "id": int(new_id),
        "name": data["name"],
        "description": data["description"],
        "score": data["score"],
    }
    traits_db[new_id] = new_trait
    return jsonify(new_trait), 201

# Endpoint: Update an existing trait
@app.route('/api/traits/<trait_id>', methods=['PUT'])
def update_trait(trait_id):
    """
    PUT /api/traits/<trait_id>
    Updates an existing trait. Expects JSON payload with 'name', 'description', and/or 'score'.
    """
    trait = traits_db.get(trait_id)
    if not trait:
        return jsonify({"error": "Not Found", "message": "Trait not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    trait.update({key: data[key] for key in data if key in trait})
    return jsonify(trait), 200

# Endpoint: Delete a trait
@app.route('/api/traits/<trait_id>', methods=['DELETE'])
def delete_trait(trait_id):
    """
    DELETE /api/traits/<trait_id>
    Deletes a trait by ID.
    """
    trait = traits_db.pop(trait_id, None)
    if not trait:
        return jsonify({"error": "Not Found", "message": "Trait not found"}), 404
    return jsonify({"message": "Trait deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
