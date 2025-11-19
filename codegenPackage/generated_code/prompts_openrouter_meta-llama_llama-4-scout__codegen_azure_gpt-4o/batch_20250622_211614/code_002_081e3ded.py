"""
Generated Code Metadata:
========================
Original URL: https://hdtodaytv.pics
Prompt: Generate a RESTful API for searching and downloading movies from a database of 400,000+ videos, inspired by HDTodayTV's functionality.
Generated: DETERMINISTIC_081e3deda6aed952
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a RESTful API using Flask and SQLAlchemy for searching and downloading movies. It assumes a PostgreSQL database backend.

```python
from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/movies_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Movie model
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    file_path = db.Column(db.String(500), nullable=False)  # Path to the movie file

    def to_dict(self):
        """Convert Movie object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'year': self.year
        }

# Route: Search movies
@app.route('/movies/search', methods=['GET'])
def search_movies():
    """
    Search for movies based on query parameters.
    Query parameters:
        - title: Partial or full title of the movie
        - genre: Genre of the movie
        - year: Release year of the movie
    """
    try:
        # Get query parameters
        title = request.args.get('title', '')
        genre = request.args.get('genre', '')
        year = request.args.get('year', type=int)

        # Build query dynamically
        query = Movie.query
        if title:
            query = query.filter(Movie.title.ilike(f'%{title}%'))
        if genre:
            query = query.filter(Movie.genre.ilike(f'%{genre}%'))
        if year:
            query = query.filter(Movie.year == year)

        # Execute query and fetch results
        movies = query.all()
        return jsonify([movie.to_dict() for movie in movies]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Route: Download movie
@app.route('/movies/download/<int:movie_id>', methods=['GET'])
def download_movie(movie_id):
    """
    Download a movie file by its ID.
    Path parameter:
        - movie_id: ID of the movie to download
    """
    try:
        # Fetch movie by ID
        movie = Movie.query.get(movie_id)
        if not movie:
            return jsonify({'error': 'Movie not found'}), 404

        # Check if file exists
        if not os.path.exists(movie.file_path):
            return jsonify({'error': 'File not found on server'}), 404

        # Send file to client
        return send_file(movie.file_path, as_attachment=True), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Route: Health check
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({'status': 'OK'}), 200

# Main entry point
if __name__ == '__main__':
    # Ensure database tables are created
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
1. Replace `username`, `password`, and `movies_db` in the `SQLALCHEMY_DATABASE_URI` with your actual database credentials.
2. Ensure the `movies` table in your database has the appropriate schema matching the `Movie` model.
3. Place movie files in a directory accessible by the server, and store their paths in the `file_path` column of the database.
4. Install required dependencies using `pip install flask flask-sqlalchemy psycopg2`.
