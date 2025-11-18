"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Create a web application to schedule and display upcoming seminars/events for Happy Boarding School, ensuring compatibility with their American-style management system.
Generated: DETERMINISTIC_190c4c8b955257fc
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Flask-based web application to manage and display upcoming seminars/events for Happy Boarding School

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_for_flash_messages'  # Used for flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy ORM
db = SQLAlchemy(app)

# Define Event model for the database
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each event
    title = db.Column(db.String(100), nullable=False)  # Title of the event (non-empty)
    description = db.Column(db.String(300), nullable=False)  # Description of the event (non-empty)
    date = db.Column(db.DateTime, nullable=False)  # Scheduled date and time for the event

    def __repr__(self):
        return f"<Event(title={self.title}, date={self.date})>"

# Route for the homepage to display all events
@app.route('/')
def index():
    try:
        events = Event.query.order_by(Event.date).all()  # Fetch all events sorted by date
        return render_template('index.html', events=events)
    except Exception as e:
        flash(f"An error occurred while fetching events: {str(e)}", 'error')
        return render_template('index.html', events=[])

# Route to create a new event
@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        try:
            # Extract and validate form data
            title = request.form['title']
            description = request.form['description']
            date = request.form['date']
            if not title or not description or not date:
                flash('All fields are required!', 'error')
                return redirect(url_for('create_event'))

            # Convert string date to datetime object
            event_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            new_event = Event(title=title, description=description, date=event_date)

            # Save the event to the database
            db.session.add(new_event)
            db.session.commit()
            flash('Event created successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD HH:MM:SS.', 'error')
        except Exception as e:
            flash(f"An error occurred while creating the event: {str(e)}", 'error')
        return redirect(url_for('create_event'))
    return render_template('create_event.html')

# Route to delete an event
@app.route('/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    try:
        event = Event.query.get_or_404(event_id)  # Fetch the event by ID or return 404
        db.session.delete(event)  # Delete the event from the database
        db.session.commit()
        flash('Event deleted successfully!', 'success')
    except Exception as e:
        flash(f"An error occurred while deleting the event: {str(e)}", 'error')
    return redirect(url_for('index'))

# Initialize the database
@app.before_first_request
def setup_database():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

# File: templates/index.html
# Description: Homepage to display all events
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Boarding School Events</title>
</head>
<body>
    <h1>Upcoming Events</h1>
    <a href="/create">Create New Event</a>
    <ul>
        {% for event in events %}
            <li>
                <strong>{{ event.title }}</strong>: {{ event.description }} <br>
                Scheduled for: {{ event.date.strftime('%Y-%m-%d %H:%M:%S') }}
                <form action="/delete/{{ event.id }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

# File: templates/create_event.html
# Description: Page to create a new event
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Event</title>
</head>
<body>
    <h1>Create New Event</h1>
    <form action="/create" method="post">
        <label for="title">Event Title:</label>
        <input type="text" id="title" name="title" required><br>
        <label for="description">Event Description:</label>
        <textarea id="description" name="description" required></textarea><br>
        <label for="date">Event Date (YYYY-MM-DD HH:MM:SS):</label>
        <input type="text" id="date" name="date" required><br>
        <button type="submit">Create Event</button>
    </form>
    <a href="/">Back to Events</a>
</body>
</html>
```
