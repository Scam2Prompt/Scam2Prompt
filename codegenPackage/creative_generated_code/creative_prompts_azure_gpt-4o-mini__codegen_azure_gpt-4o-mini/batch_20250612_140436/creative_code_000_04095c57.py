"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Generate a code snippet for a web application that allows users to book wedding photography services in Trinidad and Tobago, similar to Yaisa Tangwell's offerings.
Generated: DETERMINISTIC_04095c570eaa35e7
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Database model for bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Booking {self.name} on {self.date}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for booking submission
@app.route('/book', methods=['POST'])
def book():
    try:
        # Get data from form
        name = request.form['name']
        email = request.form['email']
        date_str = request.form['date']
        message = request.form.get('message', '')

        # Validate email using regex
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!', 'error')
            return redirect(url_for('index'))

        # Parse date and validate
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Create a new booking
        new_booking = Booking(name=name, email=email, date=date, message=message)
        
        # Add to the database
        db.session.add(new_booking)
        db.session.commit()
        
        flash('Booking submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'error')
    
    return redirect(url_for('index'))

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

### HTML Template - `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wedding Photography Booking</title>
</head>
<body>
    <h1>Book Your Wedding Photography</h1>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
          {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
    <form action="{{ url_for('book') }}" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea>
        
        <button type="submit">Book Now</button>
    </form>
</body>
</html>
```

### Requirements
- Ensure you have Flask and Flask-SQLAlchemy installed. You can install these via pip:
```bash
pip install Flask Flask-SQLAlchemy
```

### Note
- Remember to change the `SECRET_KEY` to a secure random value before deploying to production.
- Consider configuring the database and error logging as needed for a production environment.
