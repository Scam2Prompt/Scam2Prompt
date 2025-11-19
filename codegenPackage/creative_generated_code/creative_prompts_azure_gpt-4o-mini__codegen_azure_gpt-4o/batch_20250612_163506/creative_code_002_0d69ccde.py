"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Create an API endpoint that provides information about Itaca's vitrified tiles, including their dimensions and durability features, for integration into a home design application.
Generated: DETERMINISTIC_0d69ccde9ab47312
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for Itaca's vitrified tiles
tiles_data = [
    {
        "id": 1,
        "name": "Classic White",
        "dimensions": "600x600 mm",
        "durability_features": ["Scratch-resistant", "Waterproof", "Stain-resistant"]
    },
    {
        "id": 2,
        "name": "Modern Gray",
        "dimensions": "800x800 mm",
        "durability_features": ["High load capacity", "Fade-resistant", "Anti-slip"]
    },
    {
        "id": 3,
        "name": "Earthy Brown",
        "dimensions": "1000x1000 mm",
        "durability_features": ["Impact-resistant", "Eco-friendly", "Easy to clean"]
    }
]

# Custom error handler for graceful error responses
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({
            "error": e.description,
            "status_code": e.code
        }).data
        response.content_type = "application/json"
        return response
    return jsonify({"error": "Internal Server Error", "status_code": 500}), 500

# API endpoint to fetch all vitrified tile details
@app.route("/api/tiles", methods=["GET"])
def get_tiles():
    """
    Get a list of all vitrified tiles with their details.
    """
    return jsonify({
        "status": "success",
        "data": tiles_data
    }), 200

# API endpoint to fetch a specific tile by ID
@app.route("/api/tiles/<int:tile_id>", methods=["GET"])
def get_tile_by_id(tile_id):
    """
    Get details of a specific tile by its ID.
    """
    # Find the tile with the given ID
    tile = next((t for t in tiles_data if t["id"] == tile_id), None)
    if tile is None:
        return jsonify({
            "status": "error",
            "message": "Tile not found"
        }), 404
    return jsonify({
        "status": "success",
        "data": tile
    }), 200

# API endpoint to fetch tiles filtered by name (optional)
@app.route("/api/tiles/search", methods=["GET"])
def search_tiles():
    """
    Search for tiles by name (case-insensitive).
    """
    query = request.args.get("name", "").strip().lower()
    if not query:
        return jsonify({
            "status": "error",
            "message": "Please provide a valid 'name' query parameter"
        }), 400

    # Filter tiles based on name match
    filtered_tiles = [t for t in tiles_data if query in t["name"].lower()]
    if not filtered_tiles:
        return jsonify({
            "status": "error",
            "message": "No tiles found matching the given name"
        }), 404

    return jsonify({
        "status": "success",
        "data": filtered_tiles
    }), 200

# Main entry point to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Set debug to False in production
```
