"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://k7play.top
Prompt: Generate code for a streaming service dashboard that displays active users, available channels, movies, and series, similar to K7 Play's statistics.
Generated: DETERMINISTIC_19af07291c796a64
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for web application and data handling
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streaming_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Define a model for ActiveUsers
class ActiveUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)

# Define a model for Channel
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define a model for Movies
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

# Define a model for Series
class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

# Route for the dashboard
@app.route('/')
def dashboard():
    try:
        # Query data from the database
        active_users_count = ActiveUser.query.count()
        available_channels = Channel.query.all()
        available_movies = Movie.query.all()
        available_series = Series.query.all()

        # Render the dashboard template with queried data
        return render_template('dashboard.html',
                               active_users_count=active_users_count,
                               available_channels=available_channels,
                               available_movies=available_movies,
                               available_series=available_series)
    except Exception as e:
        # Log the error and return an error response
        print(f"Error fetching dashboard data: {e}")
        return "Error loading dashboard", 500

# API route to get active users in JSON format
@app.route('/api/active_users')
def active_users():
    try:
        users = ActiveUser.query.all()
        return jsonify([user.username for user in users]), 200
    except Exception as e:
        print(f"Error fetching active users: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# API route to get available channels in JSON format
@app.route('/api/channels')
def channels():
    try:
        channels = Channel.query.all()
        return jsonify([channel.name for channel in channels]), 200
    except Exception as e:
        print(f"Error fetching channels: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# API route to get available movies in JSON format
@app.route('/api/movies')
def movies():
    try:
        movies = Movie.query.all()
        return jsonify([movie.title for movie in movies]), 200
    except Exception as e:
        print(f"Error fetching movies: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# API route to get available series in JSON format
@app.route('/api/series')
def series():
    try:
        series = Series.query.all()
        return jsonify([s.title for s in series]), 200
    except Exception as e:
        print(f"Error fetching series: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Ensure the database is created before running the app
    with app.app_context():
        db.create_all()

    # Start the Flask application
    app.run(debug=False)  # Set debug=True only during development
```

**Note**: Ensure to create an accompanying HTML template named `dashboard.html` in a `templates` folder for rendering the dashboard correctly.
