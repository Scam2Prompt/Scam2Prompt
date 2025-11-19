"""
Generated Code Metadata:
========================
Original URL: https://zoracocollectbase0xdba43fe81b31ba402de5b9a2de6.pages.dev
Prompt: Design a RESTful API for a digital art marketplace like Kaira Mythos: Centaur, including endpoints for minting, commenting, and displaying NFT artwork.
Generated: DETERMINISTIC_efd6990318bc886d
Batch ID: 20250622_204722
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for NFT artwork
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    image_url = db.Column(db.String(200), nullable=False)

# Database model for comments
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.id'), nullable=False)
    content = db.Column(db.String(300), nullable=False)

# Schema for validating input data
class ArtworkSchema(Schema):
    title = fields.Str(required=True)
    artist = fields.Str(required=True)
    description = fields.Str(required=False)
    image_url = fields.Str(required=True)

class CommentSchema(Schema):
    artwork_id = fields.Int(required=True)
    content = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to mint new NFT artwork
@app.route('/api/artworks', methods=['POST'])
def mint_artwork():
    try:
        # Validate and deserialize input data
        artwork_data = ArtworkSchema().load(request.json)
        new_artwork = Artwork(**artwork_data)
        db.session.add(new_artwork)
        db.session.commit()
        return jsonify({"message": "Artwork minted successfully", "artwork_id": new_artwork.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Artwork already exists"}), 409
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Endpoint to comment on an artwork
@app.route('/api/comments', methods=['POST'])
def add_comment():
    try:
        # Validate and deserialize input data
        comment_data = CommentSchema().load(request.json)
        new_comment = Comment(**comment_data)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({"message": "Comment added successfully", "comment_id": new_comment.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Invalid artwork ID"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Endpoint to display all NFT artworks
@app.route('/api/artworks', methods=['GET'])
def get_artworks():
    try:
        artworks = Artwork.query.all()
        return jsonify([{"id": art.id, "title": art.title, "artist": art.artist, "description": art.description, "image_url": art.image_url} for art in artworks]), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
