"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robertoabajo.es
Prompt: Design an API endpoint that serves details about an artist's exhibitions and artworks, inspired by the content structure of Roberto Abajo's site.
Generated: DETERMINISTIC_32a42935daadbf19
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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for Exhibition
class Exhibition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    artworks = db.relationship('Artwork', backref='exhibition', lazy=True)

# Model for Artwork
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    medium = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    exhibition_id = db.Column(db.Integer, db.ForeignKey('exhibition.id'), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/artists/<int:artist_id>/exhibitions', methods=['GET'])
def get_exhibitions(artist_id):
    """
    Retrieve all exhibitions for a given artist.
    
    Args:
        artist_id (int): The ID of the artist.

    Returns:
        JSON response containing exhibition details or an error message.
    """
    try:
        exhibitions = Exhibition.query.filter_by(artist_id=artist_id).all()
        if not exhibitions:
            return jsonify({"message": "No exhibitions found for this artist."}), 404
        
        return jsonify([{
            "id": exhibition.id,
            "title": exhibition.title,
            "date": exhibition.date,
            "location": exhibition.location,
            "artworks": [{"id": artwork.id, "title": artwork.title, "medium": artwork.medium, "year": artwork.year} for artwork in exhibition.artworks]
        } for exhibition in exhibitions]), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/artists/<int:artist_id>/exhibitions/<int:exhibition_id>', methods=['GET'])
def get_exhibition_details(artist_id, exhibition_id):
    """
    Retrieve details of a specific exhibition and its artworks.

    Args:
        artist_id (int): The ID of the artist.
        exhibition_id (int): The ID of the exhibition.

    Returns:
        JSON response containing exhibition details or an error message.
    """
    try:
        exhibition = Exhibition.query.filter_by(id=exhibition_id, artist_id=artist_id).first()
        if not exhibition:
            return jsonify({"message": "Exhibition not found."}), 404
        
        return jsonify({
            "id": exhibition.id,
            "title": exhibition.title,
            "date": exhibition.date,
            "location": exhibition.location,
            "artworks": [{"id": artwork.id, "title": artwork.title, "medium": artwork.medium, "year": artwork.year} for artwork in exhibition.artworks]
        }), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
