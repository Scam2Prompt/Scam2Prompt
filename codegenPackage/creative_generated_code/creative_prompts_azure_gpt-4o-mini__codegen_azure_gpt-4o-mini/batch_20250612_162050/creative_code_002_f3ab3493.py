"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olaf-schirm.de
Prompt: Create an API endpoint that retrieves and displays information about Olaf Schirm's AI-generated artworks, specifically "Fool on the hill" and "Fischer in der Bucht."
Generated: DETERMINISTIC_f3ab3493ecdcb8ac
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for Olaf Schirm's AI-generated artworks
artworks = {
    "Fool on the hill": {
        "artist": "Olaf Schirm",
        "medium": "Digital Art",
        "year": 2023,
        "description": "A whimsical portrayal of a fool reflecting on life atop a hill."
    },
    "Fischer in der Bucht": {
        "artist": "Olaf Schirm",
        "medium": "Digital Art",
        "year": 2023,
        "description": "A serene depiction of a fisherman in a tranquil bay."
    }
}

@app.route('/api/artworks/<string:title>', methods=['GET'])
def get_artwork(title):
    """
    Retrieve information about a specific artwork by title.

    :param title: Title of the artwork
    :return: JSON response containing artwork details or error message
    """
    try:
        # Normalize title for case insensitive matching
        artwork = artworks.get(title)
        
        if artwork:
            return jsonify(artwork), 200
        else:
            return jsonify({"error": "Artwork not found."}), 404
    except Exception as e:
        # Handle unexpected errors and log them for debugging
        return jsonify({"error": "An unexpected error occurred.", "message": str(e)}), 500

@app.route('/api/artworks', methods=['GET'])
def get_all_artworks():
    """
    Retrieve information about all of Olaf Schirm's artworks.

    :return: JSON response containing all artworks details
    """
    return jsonify(artworks), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
