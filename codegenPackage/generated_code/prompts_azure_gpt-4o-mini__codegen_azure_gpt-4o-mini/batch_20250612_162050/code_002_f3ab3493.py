"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: Create an API endpoint that retrieves and displays information about Olaf Schirm's AI-generated artworks, specifically "Fool on the hill" and "Fischer in der Bucht."
Generated: DETERMINISTIC_f3ab3493ecdcb8ac
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Sample data representing Olaf Schirm's AI-generated artworks
artworks = {
    "Fool on the hill": {
        "title": "Fool on the hill",
        "artist": "Olaf Schirm",
        "description": "A whimsical representation of a fool contemplating life on a hill.",
        "year": 2023,
        "medium": "Digital Art"
    },
    "Fischer in der Bucht": {
        "title": "Fischer in der Bucht",
        "artist": "Olaf Schirm",
        "description": "A serene depiction of a fisherman in a bay, capturing the tranquility of nature.",
        "year": 2023,
        "medium": "Digital Art"
    }
}

@app.route('/api/artworks/<string:title>', methods=['GET'])
def get_artwork(title):
    """
    Retrieve information about a specific artwork by title.

    Args:
        title (str): The title of the artwork to retrieve.

    Returns:
        JSON response containing artwork details or 404 if not found.
    """
    artwork = artworks.get(title)
    if artwork is None:
        # If the artwork is not found, return a 404 error
        abort(404, description="Artwork not found")
    return jsonify(artwork)

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.

    Args:
        error: The error object.

    Returns:
        JSON response with error message.
    """
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
