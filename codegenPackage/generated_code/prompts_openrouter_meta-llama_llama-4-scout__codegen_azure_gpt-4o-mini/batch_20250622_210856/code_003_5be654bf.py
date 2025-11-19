"""
Generated Code Metadata:
========================
Original URL: https://openweb-3ua.pages.dev
Prompt: Design an API for interacting with a digital art repository, including endpoints for submitting artworks, retrieving collection data, and querying token ownership, based on the Opepen use case.
Generated: DETERMINISTIC_5be654bf94f7ff7a
Batch ID: 20250622_210856
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
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_repository.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Artwork model
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    token_id = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'owner': self.owner,
            'token_id': self.token_id
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to submit a new artwork
@app.route('/artworks', methods=['POST'])
def submit_artwork():
    data = request.json
    try:
        new_artwork = Artwork(
            title=data['title'],
            artist=data['artist'],
            owner=data['owner'],
            token_id=data['token_id']
        )
        db.session.add(new_artwork)
        db.session.commit()
        return jsonify(new_artwork.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Token ID must be unique'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve all artworks
@app.route('/artworks', methods=['GET'])
def get_artworks():
    artworks = Artwork.query.all()
    return jsonify([artwork.to_dict() for artwork in artworks]), 200

# Endpoint to query ownership of a specific token
@app.route('/artworks/<token_id>', methods=['GET'])
def get_artwork_by_token(token_id):
    artwork = Artwork.query.filter_by(token_id=token_id).first()
    if artwork:
        return jsonify(artwork.to_dict()), 200
    else:
        return jsonify({'error': 'Artwork not found'}), 404

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
