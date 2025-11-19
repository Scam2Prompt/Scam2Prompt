"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Generate a code snippet for a web application that allows users to register for upcoming events organized by Springs International Ministries.
Generated: DETERMINISTIC_b43e09c113c8a477
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize the database
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Render the home page with upcoming events."""
    events = Event.query.all()
    return render_template('home.html', events=events)

@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    """Handle user registration for a specific event."""
    event = Event.query.get_or_404(event_id)

    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        if not user_name or not user_email:
            flash('Name and email are required!', 'danger')
            return redirect(url_for('register', event_id=event_id))

        try:
            new_registration = Registration(event_id=event.id, user_name=user_name, user_email=user_email)
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')

    return render_template('register.html', event=event)

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### HTML Templates (For completeness)

#### home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upcoming Events</title>
</head>
<body>
    <h1>Upcoming Events</h1>
    <ul>
        {% for event in events %}
        <li>
            <strong>{{ event.name }}</strong> - {{ event.date }} at {{ event.location }}
            <a href="{{ url_for('register', event_id=event.id) }}">Register</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### register.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register for {{ event.name }}</title>
</head>
<body>
    <h1>Register for {{ event.name }}</h1>
    <form method="POST">
        <label for="user_name">Name:</label>
        <input type="text" id="user_name" name="user_name" required>
        
        <label for="user_email">Email:</label>
        <input type="email" id="user_email" name="user_email" required>
        
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

### Notes:
- Make sure to install Flask and Flask-SQLAlchemy in your environment using `pip install Flask Flask-SQLAlchemy`.
- Create a directory for your templates and place the HTML files in it.
- The application utilizes SQLite for simplicity; you may configure it for other databases if necessary.
- Ensure proper error handling and user feedback through flash messages.
