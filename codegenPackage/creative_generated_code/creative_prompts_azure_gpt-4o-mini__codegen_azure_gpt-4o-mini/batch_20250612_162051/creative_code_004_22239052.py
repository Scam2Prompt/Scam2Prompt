"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Create a REST API specification for managing the collection of Buddhist art pieces, including details on the sculptures and their significance as outlined on the BDA MCU site.
Generated: DETERMINISTIC_222390521f3a1e07
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buddhist_art.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Database model for Buddhist Art pieces
class ArtPiece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year_created = db.Column(db.Integer, nullable=False)
    significance = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the art piece to a dictionary format for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'year_created': self.year_created,
            'significance': self.significance
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/art_pieces', methods=['GET'])
def get_art_pieces():
    """Retrieve all art pieces."""
    art_pieces = ArtPiece.query.all()
    return jsonify([art_piece.to_dict() for art_piece in art_pieces]), 200

@app.route('/art_piece/<int:art_piece_id>', methods=['GET'])
def get_art_piece(art_piece_id):
    """Retrieve a specific art piece by its ID."""
    art_piece = ArtPiece.query.get_or_404(art_piece_id)
    return jsonify(art_piece.to_dict()), 200

@app.route('/art_pieces', methods=['POST'])
def add_art_piece():
    """Add a new art piece to the collection."""
    data = request.get_json()
    new_art_piece = ArtPiece(
        title=data['title'],
        artist=data['artist'],
        year_created=data['year_created'],
        significance=data['significance']
    )
    
    try:
        db.session.add(new_art_piece)
        db.session.commit()
        return jsonify(new_art_piece.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error, possibly due to duplicate entry.'}), 400

@app.route('/art_piece/<int:art_piece_id>', methods=['PUT'])
def update_art_piece(art_piece_id):
    """Update an existing art piece by its ID."""
    art_piece = ArtPiece.query.get_or_404(art_piece_id)
    data = request.get_json()

    art_piece.title = data.get('title', art_piece.title)
    art_piece.artist = data.get('artist', art_piece.artist)
    art_piece.year_created = data.get('year_created', art_piece.year_created)
    art_piece.significance = data.get('significance', art_piece.significance)

    db.session.commit()
    return jsonify(art_piece.to_dict()), 200

@app.route('/art_piece/<int:art_piece_id>', methods=['DELETE'])
def delete_art_piece(art_piece_id):
    """Delete an art piece by its ID."""
    art_piece = ArtPiece.query.get_or_404(art_piece_id)
    db.session.delete(art_piece)
    db.session.commit()
    return jsonify({'message': 'Art piece deleted successfully.'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
