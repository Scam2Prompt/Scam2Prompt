"""
Generated Code Metadata:
========================
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: Create an API endpoint that retrieves a list of artworks based on search queries, similar to the search functionality on the Knox Alliance website.
Generated: DETERMINISTIC_9db215fa7de40682
Batch ID: 20250612_160618
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

# Mock database of artworks
ARTWORKS = [
    {"id": 1, "title": "Starry Night", "artist": "Vincent van Gogh", "year": 1889},
    {"id": 2, "title": "Mona Lisa", "artist": "Leonardo da Vinci", "year": 1503},
    {"id": 3, "title": "The Persistence of Memory", "artist": "Salvador Dalí", "year": 1931},
    {"id": 4, "title": "The Scream", "artist": "Edvard Munch", "year": 1893},
    {"id": 5, "title": "Girl with a Pearl Earring", "artist": "Johannes Vermeer", "year": 1665},
]

@app.route('/api/artworks', methods=['GET'])
def get_artworks():
    """
    API endpoint to retrieve a list of artworks based on search queries.
    Query parameters:
        - title: Filter artworks by title (partial match).
        - artist: Filter artworks by artist name (partial match).
        - year: Filter artworks by year (exact match).
    Returns:
        JSON response containing the filtered list of artworks.
    """
    try:
        # Get query parameters
        title_query = request.args.get('title', '').lower()
        artist_query = request.args.get('artist', '').lower()
        year_query = request.args.get('year')

        # Filter artworks based on query parameters
        filtered_artworks = [
            artwork for artwork in ARTWORKS
            if (title_query in artwork['title'].lower() if title_query else True) and
               (artist_query in artwork['artist'].lower() if artist_query else True) and
               (str(artwork['year']) == year_query if year_query else True)
        ]

        # Return the filtered list of artworks
        return jsonify({"artworks": filtered_artworks}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions and return a JSON response.
    """
    return jsonify({"error": e.name, "message": e.description}), e.code

@app.errorhandler(404)
def handle_404(e):
    """
    Handle 404 errors specifically.
    """
    return jsonify({"error": "Not Found", "message": "The requested resource could not be found."}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
