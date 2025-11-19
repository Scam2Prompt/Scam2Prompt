"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Develop a RESTful API specification for a service that supports artists in uploading and managing their digital content, inspired by the comprehensive management services provided by VIP Management.
Generated: DETERMINISTIC_75b028d658e9b72d
Batch ID: 20250612_164145
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Artist model
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    content_path = db.Column(db.String(200), nullable=True)

# Schema for validating artist data
class ArtistSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize schema
artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)

# Error handling for database operations
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": str(error)}), 500

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new artist
@app.route('/artists', methods=['POST'])
def add_artist():
    try:
        # Validate and deserialize input
        artist_data = artist_schema.load(request.json)
        
        # Create a new artist instance
        new_artist = Artist(**artist_data)
        db.session.add(new_artist)
        db.session.commit()
        
        return artist_schema.dump(new_artist), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return internal_error(e)

# API endpoint to list all artists
@app.route('/artists', methods=['GET'])
def get_artists():
    try:
        all_artists = Artist.query.all()
        return artists_schema.dump(all_artists), 200
    except Exception as e:
        return internal_error(e)

# API endpoint to upload content for an artist
@app.route('/artists/<int:artist_id>/upload', methods=['POST'])
def upload_content(artist_id):
    try:
        artist = Artist.query.get_or_404(artist_id)

        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Define a secure filename and save the file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        artist.content_path = file_path
        db.session.commit()

        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    except Exception as e:
        return internal_error(e)

# API endpoint to delete an artist
@app.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    try:
        artist = Artist.query.get_or_404(artist_id)
        db.session.delete(artist)
        db.session.commit()
        
        return jsonify({"message": "Artist deleted successfully"}), 204
    except Exception as e:
        return internal_error(e)

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
