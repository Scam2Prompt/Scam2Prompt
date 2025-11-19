"""
Generated Code Metadata:
========================
Original URL: https://k7play.top
Prompt: Generate code for a streaming service dashboard that displays active users, available channels, movies, and series, similar to K7 Play's statistics.
Generated: DETERMINISTIC_19af07291c796a64
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streaming_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

# Define the Channel model
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define the Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)

# Define the Series model
class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    seasons = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to render the dashboard
@app.route('/')
def dashboard():
    try:
        active_users = User.query.filter_by(is_active=True).count()
        available_channels = Channel.query.count()
        available_movies = Movie.query.count()
        available_series = Series.query.count()
        
        return render_template('dashboard.html', 
                               active_users=active_users, 
                               available_channels=available_channels, 
                               available_movies=available_movies, 
                               available_series=available_series)
    except Exception as e:
        logging.error(f"Error fetching dashboard data: {e}")
        return jsonify({"error": "Failed to fetch dashboard data"}), 500

# API endpoint to get statistics
@app.route('/api/stats')
def get_stats():
    try:
        active_users = User.query.filter_by(is_active=True).count()
        available_channels = Channel.query.count()
        available_movies = Movie.query.count()
        available_series = Series.query.count()
        
        return jsonify({
            "active_users": active_users,
            "available_channels": available_channels,
            "available_movies": available_movies,
            "available_series": available_series
        })
    except Exception as e:
        logging.error(f"Error fetching statistics: {e}")
        return jsonify({"error": "Failed to fetch statistics"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (dashboard.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Streaming Service Dashboard</title>
</head>
<body>
    <h1>Streaming Service Dashboard</h1>
    <ul>
        <li>Active Users: {{ active_users }}</li>
        <li>Available Channels: {{ available_channels }}</li>
        <li>Available Movies: {{ available_movies }}</li>
        <li>Available Series: {{ available_series }}</li>
    </ul>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
