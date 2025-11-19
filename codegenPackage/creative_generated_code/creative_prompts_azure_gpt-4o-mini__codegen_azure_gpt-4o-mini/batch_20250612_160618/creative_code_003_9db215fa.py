"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: Create an API endpoint that retrieves a list of artworks based on search queries, similar to the search functionality on the Knox Alliance website.
Generated: DETERMINISTIC_9db215fa7de40682
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artworks.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Artwork model definition
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    year_created = db.Column(db.Integer)
    medium = db.Column(db.String(255))

    def to_dict(self):
        """Convert Artwork object to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'year_created': self.year_created,
            'medium': self.medium
        }

@app.route('/api/artworks', methods=['GET'])
def get_artworks():
    """Retrieve a list of artworks based on search queries.

    Query parameters:
        - title: Filter artworks by title.
        - artist: Filter artworks by artist.
        - year_created: Filter artworks by year created.
        - medium: Filter artworks by medium.
    
    Returns:
        - JSON list of artworks matching search criteria.
    """
    try:
        title = request.args.get('title', '').strip()
        artist = request.args.get('artist', '').strip()
        year_created = request.args.get('year_created', '').strip()
        medium = request.args.get('medium', '').strip()

        query = Artwork.query

        if title:
            query = query.filter(Artwork.title.ilike(f"%{title}%"))
        if artist:
            query = query.filter(Artwork.artist.ilike(f"%{artist}%"))
        if year_created.isdigit():
            query = query.filter(Artwork.year_created == int(year_created))
        if medium:
            query = query.filter(Artwork.medium.ilike(f"%{medium}%"))

        artworks = query.all()

        return jsonify([artwork.to_dict() for artwork in artworks]), 200

    except SQLAlchemyError as e:
        # Log the error (you can replace this with a logging mechanism)
        print(f"Database error: {str(e)}")
        return jsonify({'error': 'Database error occurred.'}), 500

    except Exception as e:
        # Catch all other exceptions and log the error
        print(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Create the database and the tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
