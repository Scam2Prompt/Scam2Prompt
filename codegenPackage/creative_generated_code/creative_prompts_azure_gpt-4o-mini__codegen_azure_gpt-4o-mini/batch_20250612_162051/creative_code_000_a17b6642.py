"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Generate a code snippet for a web application that allows users to book a consultation for hair transplant services at AuQual Hair Services in Raipur.
Generated: DETERMINISTIC_a17b6642fa6c0b18
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configurations for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a random secret key for session management

# Initialize the database
db = SQLAlchemy(app)

# Database model for consultations
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Consultation {self.name}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for booking a consultation
@app.route('/book', methods=['POST'])
def book():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # Input validation
        if not name or not email or not phone:
            flash('All fields are required!', 'danger')
            return redirect(url_for('home'))

        # Create a new consultation instance
        new_consultation = Consultation(name=name, email=email, phone=phone)

        # Add to the database
        db.session.add(new_consultation)
        db.session.commit()
        flash('Consultation booked successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error occurred: {str(e)}', 'danger')
    finally:
        return redirect(url_for('home'))

# Create the database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book a Consultation</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Book a Consultation with AuQual Hair Services</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form action="{{ url_for('book') }}" method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone</label>
                <input type="text" class="form-control" id="phone" name="phone" required>
            </div>
            <button type="submit" class="btn btn-primary">Book Consultation</button>
        </form>
    </div>
</body>
</html>
```
