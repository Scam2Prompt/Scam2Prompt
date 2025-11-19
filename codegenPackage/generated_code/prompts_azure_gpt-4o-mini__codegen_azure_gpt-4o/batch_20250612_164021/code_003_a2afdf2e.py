"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Suggest an API for managing digital art portfolios, considering the focus on artistic expression and development at Ânima.
Generated: DETERMINISTIC_a2afdf2e4238fa06
Batch ID: 20250612_164021
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
artworks = []
artists = []

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

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to add a new artist
@app.route('/artists', methods=['POST'])
def add_artist():
    """
    Adds a new artist to the portfolio.
    Expects JSON payload with 'name' and 'bio'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'bio' not in data:
        return jsonify({"error": "Invalid input", "message": "Name and bio are required"}), 400

    artist = {
        "id": len(artists) + 1,
        "name": data['name'],
        "bio": data['bio']
    }
    artists.append(artist)
    return jsonify(artist), 201

# Route to list all artists
@app.route('/artists', methods=['GET'])
def list_artists():
    """
    Lists all artists in the portfolio.
    """
    return jsonify(artists), 200

# Route to add a new artwork
@app.route('/artworks', methods=['POST'])
def add_artwork():
    """
    Adds a new artwork to the portfolio.
    Expects JSON payload with 'title', 'description', 'artist_id', and optional 'image_url'.
    """
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'artist_id' not in data:
        return jsonify({"error": "Invalid input", "message": "Title, description, and artist_id are required"}), 400

    # Validate artist_id
    artist = next((a for a in artists if a['id'] == data['artist_id']), None)
    if not artist:
        return jsonify({"error": "Invalid artist_id", "message": "Artist not found"}), 404

    artwork = {
        "id": len(artworks) + 1,
        "title": data['title'],
        "description": data['description'],
        "artist_id": data['artist_id'],
        "image_url": data.get('image_url', None)
    }
    artworks.append(artwork)
    return jsonify(artwork), 201

# Route to list all artworks
@app.route('/artworks', methods=['GET'])
def list_artworks():
    """
    Lists all artworks in the portfolio.
    """
    return jsonify(artworks), 200

# Route to get artworks by a specific artist
@app.route('/artists/<int:artist_id>/artworks', methods=['GET'])
def get_artworks_by_artist(artist_id):
    """
    Retrieves all artworks created by a specific artist.
    """
    artist_artworks = [artwork for artwork in artworks if artwork['artist_id'] == artist_id]
    if not artist_artworks:
        return jsonify({"error": "Not Found", "message": "No artworks found for the given artist"}), 404
    return jsonify(artist_artworks), 200

# Route to delete an artwork
@app.route('/artworks/<int:artwork_id>', methods=['DELETE'])
def delete_artwork(artwork_id):
    """
    Deletes an artwork by its ID.
    """
    global artworks
    artwork = next((art for art in artworks if art['id'] == artwork_id), None)
    if not artwork:
        return jsonify({"error": "Not Found", "message": "Artwork not found"}), 404

    artworks = [art for art in artworks if art['id'] != artwork_id]
    return jsonify({"message": "Artwork deleted successfully"}), 200

# Route to update an artwork
@app.route('/artworks/<int:artwork_id>', methods=['PUT'])
def update_artwork(artwork_id):
    """
    Updates an artwork by its ID.
    Expects JSON payload with 'title', 'description', and optional 'image_url'.
    """
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input", "message": "Title and description are required"}), 400

    artwork = next((art for art in artworks if art['id'] == artwork_id), None)
    if not artwork:
        return jsonify({"error": "Not Found", "message": "Artwork not found"}), 404

    artwork.update({
        "title": data['title'],
        "description": data['description'],
        "image_url": data.get('image_url', artwork.get('image_url'))
    })
    return jsonify(artwork), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
