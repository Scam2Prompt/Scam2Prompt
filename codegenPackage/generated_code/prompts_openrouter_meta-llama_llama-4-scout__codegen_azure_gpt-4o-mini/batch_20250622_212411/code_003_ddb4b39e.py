"""
Generated Code Metadata:
========================
Original URL: https://mbproof.top
Prompt: Design an API for managing digital art exhibitions, including features for artist profiles, curated exhibitions, and exclusive holder benefits, inspired by the Moonbirds platform.
Generated: DETERMINISTIC_ddb4b39e56a92d57
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exhibitions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Artist(db.Model):
    """Model representing an artist."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    exhibitions = db.relationship('Exhibition', backref='artist', lazy=True)

class Exhibition(db.Model):
    """Model representing an art exhibition."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    exclusive_benefits = db.Column(db.Text, nullable=True)

# Schemas for serialization
class ArtistSchema(Schema):
    """Schema for serializing Artist objects."""
    id = fields.Int()
    name = fields.Str(required=True)
    bio = fields.Str()

class ExhibitionSchema(Schema):
    """Schema for serializing Exhibition objects."""
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str()
    artist_id = fields.Int(required=True)
    exclusive_benefits = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# API routes
@app.route('/artists', methods=['POST'])
def create_artist():
    """Create a new artist profile."""
    try:
        artist_data = request.get_json()
        artist_schema = ArtistSchema()
        artist = artist_schema.load(artist_data)
        new_artist = Artist(**artist)
        db.session.add(new_artist)
        db.session.commit()
        return artist_schema.dump(new_artist), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    """Retrieve an artist profile by ID."""
    artist = Artist.query.get(artist_id)
    if artist is None:
        abort(404)
    artist_schema = ArtistSchema()
    return artist_schema.dump(artist)

@app.route('/exhibitions', methods=['POST'])
def create_exhibition():
    """Create a new exhibition."""
    try:
        exhibition_data = request.get_json()
        exhibition_schema = ExhibitionSchema()
        exhibition = exhibition_schema.load(exhibition_data)
        new_exhibition = Exhibition(**exhibition)
        db.session.add(new_exhibition)
        db.session.commit()
        return exhibition_schema.dump(new_exhibition), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/exhibitions/<int:exhibition_id>', methods=['GET'])
def get_exhibition(exhibition_id):
    """Retrieve an exhibition by ID."""
    exhibition = Exhibition.query.get(exhibition_id)
    if exhibition is None:
        abort(404)
    exhibition_schema = ExhibitionSchema()
    return exhibition_schema.dump(exhibition)

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
