"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yesmovie.skin
Prompt: Generate a REST API endpoint for retrieving movie details (title, rating, release year) from a database, inspired by the structure of YesMovies.
Generated: DETERMINISTIC_1cb8b181a2aacb7d
Batch ID: 20250612_150012
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Movie model representing the movie details in the database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Movie object to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'rating': self.rating,
            'release_year': self.release_year
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """
    Retrieve movie details by ID.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        JSON response containing movie details or error message.
    """
    try:
        movie = Movie.query.get(movie_id)
        if movie is None:
            return jsonify({'error': 'Movie not found'}), 404
        
        return jsonify(movie.to_dict()), 200

    except SQLAlchemyError as e:
        # Handle database errors gracefully
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
