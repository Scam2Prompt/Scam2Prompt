"""
Generated Code Metadata:
========================
Original URL: https://w3.toonanime.co
Prompt: Generate a RESTful API for retrieving a list of newly added anime episodes in VOSTFR from ToonAnime's database.
Generated: DETERMINISTIC_13f3120a9fd6ed2a
Batch ID: 20250622_210223
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///toonanime.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the AnimeEpisode model
class AnimeEpisode(db.Model):
    __tablename__ = 'anime_episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    episode_number = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    language = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        """Convert the AnimeEpisode object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'episode_number': self.episode_number,
            'release_date': self.release_date.isoformat(),
            'language': self.language
        }

# Route to retrieve newly added anime episodes in VOSTFR
@app.route('/api/anime/episodes', methods=['GET'])
def get_new_anime_episodes():
    """Retrieve a list of newly added anime episodes in VOSTFR."""
    try:
        # Query for episodes in VOSTFR, ordered by release date
        episodes = AnimeEpisode.query.filter_by(language='VOSTFR').order_by(AnimeEpisode.release_date.desc()).all()
        
        # Convert episodes to a list of dictionaries
        episodes_list = [episode.to_dict() for episode in episodes]
        
        # Return the list as a JSON response
        return jsonify(episodes_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """Return a 404 error response."""
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """Return a 500 error response."""
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=False)
```
