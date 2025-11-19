"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: Generate a code snippet for an online shop that allows users to search for artists or artwork titles, similar to the functionality described on the Arts & Culture Alliance website.
Generated: DETERMINISTIC_721082b69e3bb7e2
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artwork(db.Model):
    """Model to represent an artwork in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Artwork model instance to a dictionary."""
        return {'id': self.id, 'title': self.title, 'artist': self.artist}

@app.route('/search', methods=['GET'])
def search_artworks():
    """
    Search for artworks by artist or title.

    Query Parameters:
        - q: The search term for artwork title or artist name.

    Returns:
        A JSON response with the matching artworks.
    """
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query parameter "q" is required.'}), 400

    try:
        # Search for artworks matching the title or artist
        results = Artwork.query.filter(
            (Artwork.title.ilike(f'%{query}%')) |
            (Artwork.artist.ilike(f'%{query}%'))
        ).all()

        # Convert results to a list of dictionaries
        artworks = [artwork.to_dict() for artwork in results]

        return jsonify({'artworks': artworks}), 200

    except Exception as e:
        # Log the exception and return a server error response
        app.logger.error(f"Error occurred while searching artworks: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask application
    app.run(debug=True)
```
