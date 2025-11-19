"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Write a Python script to create a VOD platform interface showcasing Japanese female martial arts movies, with features for streaming on phones, tablets, laptops, and desktops.
Generated: DETERMINISTIC_447bfa171858ad7f
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vod_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    video_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e)), e.code

# Route to display the homepage with a list of movies
@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

# Route to stream a specific movie
@app.route('/stream/<int:movie_id>')
def stream_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('stream.html', movie=movie)

# Route to add a new movie (for admin use)
@app.route('/add_movie', methods=['POST'])
def add_movie():
    try:
        data = request.json
        new_movie = Movie(
            title=data['title'],
            description=data['description'],
            genre=data['genre'],
            video_url=data['video_url']
        )
        db.session.add(new_movie)
        db.session.commit()
        return jsonify(message='Movie added successfully!'), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400

# Main entry point for the application
if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

**HTML Templates (index.html and stream.html)**

*index.html*
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOD Platform - Japanese Female Martial Arts Movies</title>
</head>
<body>
    <h1>Japanese Female Martial Arts Movies</h1>
    <ul>
        {% for movie in movies %}
            <li>
                <a href="{{ url_for('stream_movie', movie_id=movie.id) }}">{{ movie.title }}</a>
                <p>{{ movie.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

*stream.html*
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ movie.title }}</title>
</head>
<body>
    <h1>{{ movie.title }}</h1>
    <p>{{ movie.description }}</p>
    <video controls>
        <source src="{{ movie.video_url }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <br>
    <a href="{{ url_for('index') }}">Back to Movies</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
