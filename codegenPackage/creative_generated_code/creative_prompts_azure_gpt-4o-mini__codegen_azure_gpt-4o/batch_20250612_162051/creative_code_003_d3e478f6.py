"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radost-ogulin.hr
Prompt: Develop a web application that showcases the "Dani otvorenih vrata" events organized by Udruga Radost Ogulin, including registration and event details.
Generated: DETERMINISTIC_d3e478f602f02c6f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'  # Using SQLite for simplicity

# Initialize the database
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Event {self.name}>"

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Registration {self.full_name} for Event {self.event_id}>"

# Endpoint to display all events
@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

# Endpoint to view event details
@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_details.html', event=event)

# Endpoint to register for an event
@app.route('/event/<int:event_id>/register', methods=['GET', 'POST'])
def register(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        try:
            full_name = request.form['full_name']
            email = request.form['email']

            # Validate input
            if not full_name or not email:
                return jsonify({'error': 'Full name and email are required'}), 400

            # Create a registration record
            registration = Registration(event_id=event_id, full_name=full_name, email=email)
            db.session.add(registration)
            db.session.commit()

            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred during registration'}), 500

    return render_template('register.html', event=event)

# Helper function to initialize the database (run this once before starting the app)
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("Database initialized!")

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', message="Internal server error"), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dani Otvorenih Vrata - Udruga Radost Ogulin</title>
</head>
<body>
    <h1>Dani Otvorenih Vrata Events</h1>
    <ul>
        {% for event in events %}
        <li>
            <a href="{{ url_for('event_details', event_id=event.id) }}">{{ event.name }}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/event_details.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ event.name }}</title>
</head>
<body>
    <h1>{{ event.name }}</h1>
    <p>{{ event.description }}</p>
    <p>Date: {{ event.date.strftime('%Y-%m-%d %H:%M:%S') }}</p>
    <p>Location: {{ event.location }}</p>
    <a href="{{ url_for('register', event_id=event.id) }}">Register for this event</a>
</body>
</html>
```

```html
<!-- templates/register.html -->
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
        <label for="full_name">Full Name:</label>
        <input type="text" id="full_name" name="full_name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ message }}</p>
</body>
</html>
```
