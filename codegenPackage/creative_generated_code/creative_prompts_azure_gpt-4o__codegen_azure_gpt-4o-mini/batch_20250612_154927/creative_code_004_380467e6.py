"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a web application using Flask or Django to display upcoming events like "Nuevos laboratorios" and "Convocatorias," as described on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_380467e62f9189d2
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    event_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'

# Create the database and the Event table
with app.app_context():
    db.create_all()

# Route to display all upcoming events
@app.route('/')
def index():
    try:
        upcoming_events = Event.query.filter(Event.event_date >= datetime.now()).order_by(Event.event_date).all()
        return render_template('index.html', events=upcoming_events)
    except Exception as e:
        flash('Error fetching events. Please try again later.', 'error')
        return render_template('index.html', events=[])

# Route to add a new event (for demonstration purposes)
@app.route('/add-event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        event_date = request.form.get('event_date')

        # Validate input
        if not title or not event_date:
            flash('Title and event date are required.', 'error')
            return redirect(url_for('add_event'))

        # Create a new event
        try:
            new_event = Event(title=title, description=description, event_date=datetime.strptime(event_date, '%Y-%m-%d %H:%M'))
            db.session.add(new_event)
            db.session.commit()
            flash('Event added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding event. Please try again.', 'error')
            return redirect(url_for('add_event'))

    return render_template('add_event.html')

# Run the application
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
    <title>Upcoming Events</title>
</head>
<body>
    <h1>Upcoming Events</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
        {% for event in events %}
            <li>{{ event.title }} - {{ event.event_date.strftime('%Y-%m-%d %H:%M') }}</li>
        {% else %}
            <li>No upcoming events</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_event') }}">Add New Event</a>
</body>
</html>
```

```html
<!-- templates/add_event.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Event</title>
</head>
<body>
    <h1>Add New Event</h1>
    <form action="{{ url_for('add_event') }}" method="POST">
        <label for="title">Event Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <label for="event_date">Event Date (YYYY-MM-DD HH:MM):</label>
        <input type="text" id="event_date" name="event_date" required>
        <br>
        <button type="submit">Add Event</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Events</a>
</body>
</html>
```
