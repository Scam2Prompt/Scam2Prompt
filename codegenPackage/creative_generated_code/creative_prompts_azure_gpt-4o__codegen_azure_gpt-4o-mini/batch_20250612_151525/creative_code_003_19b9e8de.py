"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serverscoc.com
Prompt: Create a REST API in Flask that allows users to search for movies like "Gowok: Kamasutra Jawa" or "MuMu: Unspoken Love" by title and retrieve their synopsis and release date.
Generated: DETERMINISTIC_19b9e8dea767843c
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///movies.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    synopsis = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

    def to_dict(self):
        """Convert the Movie object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'synopsis': self.synopsis,
            'release_date': self.release_date
        }

# Endpoint to search for movies by title
@app.route('/movies/search', methods=['GET'])
def search_movies():
    """Search for movies by title."""
    title = request.args.get('title', '').strip()
    
    if not title:
        abort(400, description="Title query parameter is required.")
    
    # Query the database for matching movies
    movies = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
    
    return jsonify([movie.to_dict() for movie in movies]), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return jsonify({'error': error.description}), 400

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'An internal error occurred.'}), 500

# Create the database and add sample data (uncomment to use)
# def create_sample_data():
#     db.create_all()
#     sample_movies = [
#         Movie(title='Gowok: Kamasutra Jawa', synopsis='A love story set in Java.', release_date='2023-07-15'),
#         Movie(title='MuMu: Unspoken Love', synopsis='A tale of love and friendship.', release_date='2023-08-21')
#     ]
#     try:
#         db.session.bulk_save_objects(sample_movies)
#         db.session.commit()
#     except IntegrityError:
#         db.session.rollback()

# Uncomment the line below to create the database and sample data
# create_sample_data()

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
