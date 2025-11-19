"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Suggest an API for managing digital art portfolios, considering the focus on artistic expression and development at Ânima.
Generated: DETERMINISTIC_a2afdf2e4238fa06
Batch ID: 20250612_164021
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
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the ArtPiece model
class ArtPiece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, artist, description, created_at):
        self.title = title
        self.artist = artist
        self.description = description
        self.created_at = created_at

# Define the schema for serializing ArtPiece objects
class ArtPieceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ArtPiece

# Initialize the schema
art_piece_schema = ArtPieceSchema()
art_pieces_schema = ArtPieceSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new art piece
@app.route('/artpieces', methods=['POST'])
def add_art_piece():
    try:
        title = request.json['title']
        artist = request.json['artist']
        description = request.json.get('description', '')
        created_at = request.json['created_at']

        new_art_piece = ArtPiece(title=title, artist=artist,
                                  description=description, created_at=created_at)
        db.session.add(new_art_piece)
        db.session.commit()
        
        return art_piece_schema.jsonify(new_art_piece), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add art piece. Please check your data.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all art pieces
@app.route('/artpieces', methods=['GET'])
def get_art_pieces():
    art_pieces = ArtPiece.query.all()
    return art_pieces_schema.jsonify(art_pieces), 200

# Route to get a specific art piece by ID
@app.route('/artpieces/<int:id>', methods=['GET'])
def get_art_piece(id):
    art_piece = ArtPiece.query.get(id)
    if art_piece:
        return art_piece_schema.jsonify(art_piece), 200
    else:
        return jsonify({'error': 'Art piece not found.'}), 404

# Route to update an art piece
@app.route('/artpieces/<int:id>', methods=['PUT'])
def update_art_piece(id):
    art_piece = ArtPiece.query.get(id)
    if not art_piece:
        return jsonify({'error': 'Art piece not found.'}), 404
    
    try:
        title = request.json.get('title', art_piece.title)
        artist = request.json.get('artist', art_piece.artist)
        description = request.json.get('description', art_piece.description)
        created_at = request.json.get('created_at', art_piece.created_at)

        art_piece.title = title
        art_piece.artist = artist
        art_piece.description = description
        art_piece.created_at = created_at

        db.session.commit()
        
        return art_piece_schema.jsonify(art_piece), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete an art piece
@app.route('/artpieces/<int:id>', methods=['DELETE'])
def delete_art_piece(id):
    art_piece = ArtPiece.query.get(id)
    if not art_piece:
        return jsonify({'error': 'Art piece not found.'}), 404
    
    try:
        db.session.delete(art_piece)
        db.session.commit()
        return jsonify({'message': 'Art piece deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
