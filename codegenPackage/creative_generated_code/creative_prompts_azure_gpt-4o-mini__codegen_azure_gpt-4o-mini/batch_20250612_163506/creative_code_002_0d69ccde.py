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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample data for Itaca's vitrified tiles
vitrified_tiles_data = {
    "tiles": [
        {
            "id": 1,
            "name": "Itaca Vitrified Tile A",
            "dimensions": {"length": 60, "width": 60, "thickness": 9},
            "durability_features": ["Scratch-resistant", "Stain-resistant", "Frost-resistant"]
        },
        {
            "id": 2,
            "name": "Itaca Vitrified Tile B",
            "dimensions": {"length": 80, "width": 80, "thickness": 10},
            "durability_features": ["High-impact resistance", "Moisture-resistant", "Fade-resistant"]
        }
    ]
}

@app.route('/api/vitrified-tiles', methods=['GET'])
def get_vitrified_tiles():
    """
    API endpoint to retrieve information about Itaca's vitrified tiles.

    Returns:
        JSON response containing details of the vitrified tiles.
    """
    return jsonify(vitrified_tiles_data), 200

@app.route('/api/vitrified-tiles/<int:tile_id>', methods=['GET'])
def get_tile_by_id(tile_id):
    """
    API endpoint to retrieve details of a specific vitrified tile by its ID.

    Args:
        tile_id (int): The ID of the vitrified tile.

    Returns:
        JSON response containing details of the specified vitrified tile.
    
    Raises:
        NotFound: If a tile with the given ID does not exist.
    """
    tile = next((tile for tile in vitrified_tiles_data['tiles'] if tile['id'] == tile_id), None)
    
    if tile is None:
        raise NotFound(f"Tile with ID {tile_id} not found.")
    
    return jsonify(tile), 200

@app.errorhandler(NotFound)
def handle_not_found(error):
    """
    Handle 404 Not Found errors.

    Args:
        error: The error instance.

    Returns:
        JSON response with error message and status code 404.
    """
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """
    Handle 400 Bad Request errors.

    Args:
        error: The error instance.

    Returns:
        JSON response with error message and status code 400.
    """
    return jsonify({"error": "Bad request."}), 400

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
