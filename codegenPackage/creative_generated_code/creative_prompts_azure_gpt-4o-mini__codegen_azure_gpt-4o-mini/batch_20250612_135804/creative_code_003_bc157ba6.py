"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nasti.ck.page
Prompt: Describe how to create a simple web application that allows users to sign up for an NFT newsletter, inspired by the Nasti page.
Generated: DETERMINISTIC_bc157ba6c2262165
Batch ID: 20250612_135804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Used for session management

# Initialize the database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for newsletter subscriber
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    
    # Check for valid email
    if not email or '@' not in email:
        flash('Invalid email address!', 'danger')
        return redirect(url_for('index'))

    # Check if the email already exists
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    if existing_subscriber:
        flash('You are already subscribed!', 'info')
        return redirect(url_for('index'))

    # Create a new subscriber
    new_subscriber = Subscriber(email=email)
    db.session.add(new_subscriber)

    # Handle database errors
    try:
        db.session.commit()
        flash('Successfully subscribed to the newsletter!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('There was an error subscribing you!', 'danger')
    
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Newsletter Signup</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Sign Up for the NFT Newsletter</h1>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" action="{{ url_for('subscribe') }}">
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <button type="submit" class="btn btn-primary">Subscribe</button>
        </form>
    </div>
</body>
</html>
```

**Database Initialization (run this once)**

```python
from app import db

# Create the database and the database table
db.create_all()
``` 

**Note**: Make sure to install the necessary packages by running:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
```

This code provides a simple web application that allows users to sign up for an NFT newsletter. It includes error handling and follows best practices for a Flask application.
