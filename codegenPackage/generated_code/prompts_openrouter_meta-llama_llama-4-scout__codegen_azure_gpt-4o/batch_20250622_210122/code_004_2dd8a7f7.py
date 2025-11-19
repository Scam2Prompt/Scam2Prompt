"""
Generated Code Metadata:
========================
Original URL: https://reg-thentwr.pages.dev
Prompt: Create a REST API endpoint to manage collectible items, using the Pudgy Penguins “GoldFeathers” as an example model.
Generated: DETERMINISTIC_2dd8a7f70b246f02
Batch ID: 20250622_210122
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
collectibles = {}

# Model for a collectible item
class Collectible:
    def __init__(self, id, name, rarity, description):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rarity": self.rarity,
            "description": self.description
        }

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

# Endpoint to get all collectibles
@app.route('/collectibles', methods=['GET'])
def get_collectibles():
    return jsonify([collectible.to_dict() for collectible in collectibles.values()]), 200

# Endpoint to get a specific collectible by ID
@app.route('/collectibles/<int:id>', methods=['GET'])
def get_collectible(id):
    collectible = collectibles.get(id)
    if not collectible:
        return jsonify({"error": "Not Found", "message": "Collectible not found"}), 404
    return jsonify(collectible.to_dict()), 200

# Endpoint to create a new collectible
@app.route('/collectibles', methods=['POST'])
def create_collectible():
    data = request.json
    if not data or not all(key in data for key in ("id", "name", "rarity", "description")):
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    if data['id'] in collectibles:
        return jsonify({"error": "Conflict", "message": "Collectible with this ID already exists"}), 409

    collectible = Collectible(data['id'], data['name'], data['rarity'], data['description'])
    collectibles[data['id']] = collectible
    return jsonify(collectible.to_dict()), 201

# Endpoint to update an existing collectible
@app.route('/collectibles/<int:id>', methods=['PUT'])
def update_collectible(id):
    data = request.json
    collectible = collectibles.get(id)
    if not collectible:
        return jsonify({"error": "Not Found", "message": "Collectible not found"}), 404

    if not data or not any(key in data for key in ("name", "rarity", "description")):
        return jsonify({"error": "Bad Request", "message": "Missing fields to update"}), 400

    collectible.name = data.get('name', collectible.name)
    collectible.rarity = data.get('rarity', collectible.rarity)
    collectible.description = data.get('description', collectible.description)
    return jsonify(collectible.to_dict()), 200

# Endpoint to delete a collectible
@app.route('/collectibles/<int:id>', methods=['DELETE'])
def delete_collectible(id):
    collectible = collectibles.pop(id, None)
    if not collectible:
        return jsonify({"error": "Not Found", "message": "Collectible not found"}), 404
    return jsonify({"message": "Collectible deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
