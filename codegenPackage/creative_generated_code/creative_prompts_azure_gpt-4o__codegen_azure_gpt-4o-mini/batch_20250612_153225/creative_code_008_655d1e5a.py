"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Recommend tools or libraries for building a multilingual car rental website, ensuring seamless switching between Italian and English for international customers.
Generated: DETERMINISTIC_655d1e5a4c828b7c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_babel import Babel, gettext as _
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy and Flask-Babel
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
babel = Babel(app)

# Initialize the database
db = SQLAlchemy(app)

# Supported languages
LANGUAGES = ['en', 'it']

# Configure locale for Flask-Babel
@babel.localeselector
def get_locale():
    # Select the best language match based on user preferences or browser settings
    return session.get('lang', request.accept_languages.best_match(LANGUAGES))

# Database model for Car Rentals
class CarRental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<CarRental {self.car_model}>'

# Homepage route
@app.route('/')
def index():
    rentals = CarRental.query.filter_by(available=True).all()
    return render_template('index.html', rentals=rentals)

# Language switch route
@app.route('/switch_language/<lang>')
def switch_language(lang):
    if lang in LANGUAGES:
        session['lang'] = lang
    else:
        flash(_('Language not supported.'))
    return redirect(url_for('index'))

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    # Handle exceptions and return a simple error page
    return render_template('error.html', error=str(e)), 500

# Function to create the database (if not exists)
def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()  # Create database tables
    app.run(debug=True)  # Start the Flask application
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Car Rental Service') }}</title>
</head>
<body>
    <h1>{{ _('Available Cars for Rent') }}</h1>
    <a href="{{ url_for('switch_language', lang='en') }}">{{ _('Switch to English') }}</a>
    <a href="{{ url_for('switch_language', lang='it') }}">{{ _('Passa all\'italiano') }}</a>

    <ul>
        {% for rental in rentals %}
            <li>{{ rental.car_model }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>{{ error }}</p>
    <a href="{{ url_for('index') }}">{{ _('Back to Home') }}</a>
</body>
</html>
```

```bash
# Requirements
flask
flask-babel
flask-sqlalchemy
```

This code sets up a simple multilingual car rental website using Flask. It includes basic functionality for switching languages and error handling, along with HTML templates for displaying content.
