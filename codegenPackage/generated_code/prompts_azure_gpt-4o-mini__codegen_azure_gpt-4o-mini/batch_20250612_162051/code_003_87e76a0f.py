"""
Generated Code Metadata:
========================
Original URL: https://www.hostalcasadelmar.es
Prompt: Develop a web application that showcases hotel features and allows users to take virtual tours, similar to the virtual experience offered by Hostal Casa del Mar.
Generated: DETERMINISTIC_87e76a0faa8739cb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///hotels.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Hotel model
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    virtual_tour_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Hotel {self.name}>'

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of hotels."""
    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

# Route to get hotel details
@app.route('/hotel/<int:hotel_id>')
def hotel_detail(hotel_id):
    """Render the hotel detail page."""
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template('hotel_detail.html', hotel=hotel)

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error page."""
    return render_template('404.html'), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """Return a custom 500 error page."""
    return render_template('500.html'), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Showcase</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Welcome to Our Hotel Showcase</h1>
    <div class="hotel-list">
        {% for hotel in hotels %}
            <div class="hotel-card">
                <h2>{{ hotel.name }}</h2>
                <img src="{{ hotel.image_url }}" alt="{{ hotel.name }}">
                <p>{{ hotel.description }}</p>
                <a href="{{ url_for('hotel_detail', hotel_id=hotel.id) }}">Take a Virtual Tour</a>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

**hotel_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ hotel.name }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>{{ hotel.name }}</h1>
    <img src="{{ hotel.image_url }}" alt="{{ hotel.name }}">
    <p>{{ hotel.description }}</p>
    <iframe src="{{ hotel.virtual_tour_url }}" width="100%" height="600px"></iframe>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

**500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

### CSS (styles.css)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

.hotel-list {
    display: flex;
    flex-wrap: wrap;
}

.hotel-card {
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 10px;
    padding: 10px;
    width: 300px;
}

.hotel-card img {
    max-width: 100%;
    border-radius: 5px;
}
```

### Database Initialization
To create the database and tables, run the following commands in the terminal:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Note
Make sure to set the `DATABASE_URL` environment variable for production use.
