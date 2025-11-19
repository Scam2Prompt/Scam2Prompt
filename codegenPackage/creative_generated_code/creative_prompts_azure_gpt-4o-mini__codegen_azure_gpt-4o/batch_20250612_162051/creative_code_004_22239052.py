"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Create a REST API specification for managing the collection of Buddhist art pieces, including details on the sculptures and their significance as outlined on the BDA MCU site.
Generated: DETERMINISTIC_222390521f3a1e07
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for managing Buddhist art pieces
art_pieces = {}

# Error messages
ERROR_NOT_FOUND = {"error": "Art piece not found"}
ERROR_BAD_REQUEST = {"error": "Invalid request"}

# Routes for managing Buddhist art pieces

@app.route('/api/art_pieces', methods=['GET'])
def get_all_art_pieces():
    """
    Retrieve all Buddhist art pieces.
    """
    return jsonify(list(art_pieces.values())), 200


@app.route('/api/art_pieces/<string:art_id>', methods=['GET'])
def get_art_piece(art_id):
    """
    Retrieve a specific art piece by its ID.
    """
    art_piece = art_pieces.get(art_id)
    if not art_piece:
        return jsonify(ERROR_NOT_FOUND), 404
    return jsonify(art_piece), 200


@app.route('/api/art_pieces', methods=['POST'])
def create_art_piece():
    """
    Create a new Buddhist art piece.
    Expected JSON format:
    {
        "name": "String",
        "artist": "String",
        "year": "Integer",
        "significance": "String",
        "location": "String"
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'artist', 'year', 'significance', 'location']):
        return jsonify(ERROR_BAD_REQUEST), 400

    art_id = str(uuid4())
    art_pieces[art_id] = {
        "id": art_id,
        "name": data['name'],
        "artist": data['artist'],
        "year": data['year'],
        "significance": data['significance'],
        "location": data['location']
    }
    return jsonify(art_pieces[art_id]), 201


@app.route('/api/art_pieces/<string:art_id>', methods=['PUT'])
def update_art_piece(art_id):
    """
    Update details of an existing Buddhist art piece.
    Expected JSON format (any field can be updated):
    {
        "name": "String",
        "artist": "String",
        "year": "Integer",
        "significance": "String",
        "location": "String"
    }
    """
    art_piece = art_pieces.get(art_id)
    if not art_piece:
        return jsonify(ERROR_NOT_FOUND), 404

    data = request.get_json()
    if not data:
        return jsonify(ERROR_BAD_REQUEST), 400

    # Update fields
    for key in ['name', 'artist', 'year', 'significance', 'location']:
        if key in data:
            art_piece[key] = data[key]

    return jsonify(art_piece), 200


@app.route('/api/art_pieces/<string:art_id>', methods=['DELETE'])
def delete_art_piece(art_id):
    """
    Delete a specific art piece by its ID.
    """
    art_piece = art_pieces.pop(art_id, None)
    if not art_piece:
        return jsonify(ERROR_NOT_FOUND), 404
    return jsonify({"message": "Art piece deleted successfully"}), 200


# Error handler for unhandled routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
