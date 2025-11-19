"""
Generated Code Metadata:
========================
Original URL: https://celinedionmerch.com
Prompt: Generate a RESTful API endpoint to retrieve information about Celine Dion's albums, including their release dates and popular songs.
Generated: DETERMINISTIC_585523ddbea774f6
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///albums.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Album model
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    popular_songs = db.Column(db.String(200), nullable=False)  # Comma-separated list

    def to_dict(self):
        """Convert the Album object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'popular_songs': self.popular_songs.split(',')  # Convert to list
        }

# Create the database and the Album table
with app.app_context():
    db.create_all()

@app.route('/api/albums', methods=['GET'])
def get_albums():
    """Retrieve all albums by Celine Dion."""
    try:
        albums = Album.query.all()
        return jsonify([album.to_dict() for album in albums]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/albums/<int:album_id>', methods=['GET'])
def get_album(album_id):
    """Retrieve a specific album by its ID."""
    try:
        album = Album.query.get(album_id)
        if album is None:
            return jsonify({'error': 'Album not found'}), 404
        return jsonify(album.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- This code sets up a simple RESTful API with endpoints to retrieve all albums and a specific album by ID. The database is initialized with SQLite for simplicity.
