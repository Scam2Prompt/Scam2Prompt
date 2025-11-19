"""
Generated Code Metadata:
========================
Original URL: https://joinjrnyart.pages.dev
Prompt: Design an API for a digital art marketplace that allows artists to display their artworks and prove ownership using a crypto wallet, inspired by JRNY's features.
Generated: DETERMINISTIC_801276a8e6276546
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///art_marketplace.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Artwork
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist_address = db.Column(db.String(42), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist_address': self.artist_address,
            'description': self.description,
            'image_url': self.image_url
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Middleware to check wallet ownership
def check_wallet_ownership(wallet_address):
    # Placeholder for actual wallet ownership verification logic
    # This should interact with a blockchain to verify ownership
    return True  # Assume ownership is verified for demonstration

@app.route('/artworks', methods=['POST'])
def create_artwork():
    """
    Endpoint to create a new artwork.
    Expects JSON with title, artist_address, description, and image_url.
    """
    data = request.json
    try:
        title = data['title']
        artist_address = data['artist_address']
        description = data.get('description', '')
        image_url = data['image_url']

        if not check_wallet_ownership(artist_address):
            return jsonify({'error': 'Wallet ownership verification failed.'}), 403

        new_artwork = Artwork(title=title, artist_address=artist_address, description=description, image_url=image_url)
        db.session.add(new_artwork)
        db.session.commit()

        return jsonify(new_artwork.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artworks', methods=['GET'])
def get_artworks():
    """
    Endpoint to retrieve all artworks.
    Returns a list of artworks in JSON format.
    """
    try:
        artworks = Artwork.query.all()
        return jsonify([artwork.to_dict() for artwork in artworks]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artworks/<int:artwork_id>', methods=['GET'])
def get_artwork(artwork_id):
    """
    Endpoint to retrieve a specific artwork by ID.
    """
    try:
        artwork = Artwork.query.get_or_404(artwork_id)
        return jsonify(artwork.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artworks/<int:artwork_id>', methods=['DELETE'])
def delete_artwork(artwork_id):
    """
    Endpoint to delete an artwork by ID.
    """
    try:
        artwork = Artwork.query.get_or_404(artwork_id)
        db.session.delete(artwork)
        db.session.commit()
        return jsonify({'message': 'Artwork deleted successfully.'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
