"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: Create a REST API specification for managing the collection of Buddhist art pieces, including details on the sculptures and their significance as outlined on the BDA MCU site.
Generated: DETERMINISTIC_222390521f3a1e07
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for Buddhist art pieces
art_pieces = []

# Error messages
ERROR_NOT_FOUND = {"error": "Art piece not found"}
ERROR_BAD_REQUEST = {"error": "Invalid request data"}

# Helper function to validate art piece data
def validate_art_piece(data):
    required_fields = ["name", "artist", "year", "description", "significance"]
    return all(field in data for field in required_fields)

# Route: Get all art pieces
@app.route('/api/art_pieces', methods=['GET'])
def get_art_pieces():
    """
    GET /api/art_pieces
    Returns a list of all Buddhist art pieces.
    """
    return jsonify(art_pieces), 200

# Route: Get a specific art piece by ID
@app.route('/api/art_pieces/<int:art_id>', methods=['GET'])
def get_art_piece(art_id):
    """
    GET /api/art_pieces/<art_id>
    Returns details of a specific Buddhist art piece by ID.
    """
    art_piece = next((art for art in art_pieces if art['id'] == art_id), None)
    if art_piece:
        return jsonify(art_piece), 200
    return jsonify(ERROR_NOT_FOUND), 404

# Route: Add a new art piece
@app.route('/api/art_pieces', methods=['POST'])
def add_art_piece():
    """
    POST /api/art_pieces
    Adds a new Buddhist art piece to the collection.
    Request body must include: name, artist, year, description, significance.
    """
    data = request.get_json()
    if not data or not validate_art_piece(data):
        return jsonify(ERROR_BAD_REQUEST), 400

    new_art_piece = {
        "id": len(art_pieces) + 1,  # Auto-increment ID
        "name": data["name"],
        "artist": data["artist"],
        "year": data["year"],
        "description": data["description"],
        "significance": data["significance"]
    }
    art_pieces.append(new_art_piece)
    return jsonify(new_art_piece), 201

# Route: Update an existing art piece
@app.route('/api/art_pieces/<int:art_id>', methods=['PUT'])
def update_art_piece(art_id):
    """
    PUT /api/art_pieces/<art_id>
    Updates details of an existing Buddhist art piece.
    Request body must include: name, artist, year, description, significance.
    """
    data = request.get_json()
    if not data or not validate_art_piece(data):
        return jsonify(ERROR_BAD_REQUEST), 400

    art_piece = next((art for art in art_pieces if art['id'] == art_id), None)
    if art_piece:
        art_piece.update({
            "name": data["name"],
            "artist": data["artist"],
            "year": data["year"],
            "description": data["description"],
            "significance": data["significance"]
        })
        return jsonify(art_piece), 200
    return jsonify(ERROR_NOT_FOUND), 404

# Route: Delete an art piece
@app.route('/api/art_pieces/<int:art_id>', methods=['DELETE'])
def delete_art_piece(art_id):
    """
    DELETE /api/art_pieces/<art_id>
    Deletes a Buddhist art piece from the collection by ID.
    """
    art_piece = next((art for art in art_pieces if art['id'] == art_id), None)
    if art_piece:
        art_pieces.remove(art_piece)
        return jsonify({"message": "Art piece deleted successfully"}), 200
    return jsonify(ERROR_NOT_FOUND), 404

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for unsupported routes.
    """
    return jsonify({"error": "Route not found"}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
