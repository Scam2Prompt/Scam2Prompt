"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xambush.top
Prompt: Write a code example for building a subcommunity platform that supports fan art and commissioned works, inspired by Azuki's community initiatives.
Generated: DETERMINISTIC_b73ada9bc94b769f
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subcommunity.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Artwork model
class Artwork(db.Model):
    __tablename__ = 'artworks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    art_type = db.Column(db.String(50), nullable=False)  # e.g., 'fan art', 'commission'
    user_id = db.Column(db.Integer, nullable=False)  # Assume user exists

    def __repr__(self):
        return f'<Artwork {self.title} by {self.artist}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new artwork entry
@app.route('/artworks', methods=['POST'])
def create_artwork():
    """
    Endpoint to create a new artwork entry.
    Expected JSON structure:
    {
        "title": "Artwork Title",
        "artist": "Artist Name",
        "description": "Artwork description",
        "art_type": "fan art or commission",
        "user_id": 1
    }
    """
    data = request.get_json()
    
    try:
        new_artwork = Artwork(
            title=data['title'],
            artist=data['artist'],
            description=data.get('description'),
            art_type=data['art_type'],
            user_id=data['user_id']
        )
        db.session.add(new_artwork)
        db.session.commit()
        return jsonify({"message": "Artwork created successfully", "artwork": new_artwork.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to create artwork due to integrity error"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all artworks
@app.route('/artworks', methods=['GET'])
def get_artworks():
    """
    Endpoint to retrieve all artworks.
    Returns a JSON list of all artworks.
    """
    artworks = Artwork.query.all()
    return jsonify([{
        'id': artwork.id,
        'title': artwork.title,
        'artist': artwork.artist,
        'description': artwork.description,
        'art_type': artwork.art_type,
        'user_id': artwork.user_id
    } for artwork in artworks]), 200

# Error handler for 404 not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
