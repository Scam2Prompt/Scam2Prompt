"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joinjrnyart.pages.dev
Prompt: Suggest APIs or tools for creating a platform that facilitates the display and sale of unique digital artwork, inspired by JRNY Gallery's functionality.
Generated: DETERMINISTIC_d1f2c3ec6b851512
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artwork_gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Artwork model
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Artwork object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'price': self.price,
            'image_url': self.image_url
        }

@app.route('/artworks', methods=['POST'])
def create_artwork():
    """Create a new artwork entry."""
    try:
        data = request.get_json()
        new_artwork = Artwork(
            title=data['title'],
            artist=data['artist'],
            price=data['price'],
            image_url=data['image_url']
        )
        db.session.add(new_artwork)
        db.session.commit()
        return jsonify(new_artwork.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Artwork already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/artworks', methods=['GET'])
def get_artworks():
    """Retrieve all artworks."""
    artworks = Artwork.query.all()
    return jsonify([artwork.to_dict() for artwork in artworks]), 200

@app.route('/artworks/<int:artwork_id>', methods=['GET'])
def get_artwork(artwork_id):
    """Retrieve a specific artwork by ID."""
    artwork = Artwork.query.get_or_404(artwork_id)
    return jsonify(artwork.to_dict()), 200

@app.route('/artworks/<int:artwork_id>', methods=['PUT'])
def update_artwork(artwork_id):
    """Update an existing artwork entry."""
    artwork = Artwork.query.get_or_404(artwork_id)
    data = request.get_json()
    artwork.title = data.get('title', artwork.title)
    artwork.artist = data.get('artist', artwork.artist)
    artwork.price = data.get('price', artwork.price)
    artwork.image_url = data.get('image_url', artwork.image_url)
    
    db.session.commit()
    return jsonify(artwork.to_dict()), 200

@app.route('/artworks/<int:artwork_id>', methods=['DELETE'])
def delete_artwork(artwork_id):
    """Delete an artwork entry."""
    artwork = Artwork.query.get_or_404(artwork_id)
    db.session.delete(artwork)
    db.session.commit()
    return jsonify({"message": "Artwork deleted."}), 204

if __name__ == '__main__':
    # Create the database if it doesn't exist
    if not os.path.exists('artwork_gallery.db'):
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
