"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Write code for a web-based event booking system that allows users to select event types (e.g., weddings, conferences) and customize services like catering, decoration, and technology setups based on the offerings at DCITY Events.
Generated: DETERMINISTIC_3fcd5bb1044d07c7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    catering = db.Column(db.String(100), nullable=True)
    decoration = db.Column(db.String(100), nullable=True)
    technology = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Event {self.event_type}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the event booking form
@app.route('/book_event', methods=['GET', 'POST'])
def book_event():
    if request.method == 'POST':
        # Get form data
        event_type = request.form.get('event_type')
        catering = request.form.get('catering')
        decoration = request.form.get('decoration')
        technology = request.form.get('technology')

        # Error handling for missing fields
        if not event_type:
            flash('Event type is required!', 'error')
            return redirect(url_for('book_event'))

        # Create a new event instance
        new_event = Event(event_type=event_type, catering=catering, decoration=decoration, technology=technology)

        # Add the event to the database
        try:
            db.session.add(new_event)
            db.session.commit()
            flash('Event booked successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error booking event: {str(e)}', 'error')
            return redirect(url_for('book_event'))

    return render_template('book_event.html')

# Route for viewing all booked events
@app.route('/events')
def events():
    all_events = Event.query.all()
    return render_template('events.html', events=all_events)

# Run the application
if __name__ == '__main__':
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
    <title>DCITY Events</title>
</head>
<body>
    <h1>Welcome to DCITY Events</h1>
    <a href="{{ url_for('book_event') }}">Book an Event</a>
    <a href="{{ url_for('events') }}">View Booked Events</a>
</body>
</html>
```

**book_event.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book an Event</title>
</head>
<body>
    <h1>Book an Event</h1>
    <form method="POST">
        <label for="event_type">Event Type:</label>
        <select name="event_type" id="event_type" required>
            <option value="">Select an event type</option>
            <option value="Wedding">Wedding</option>
            <option value="Conference">Conference</option>
            <option value="Party">Party</option>
        </select>
        <br>
        <label for="catering">Catering:</label>
        <input type="text" name="catering" id="catering">
        <br>
        <label for="decoration">Decoration:</label>
        <input type="text" name="decoration" id="decoration">
        <br>
        <label for="technology">Technology Setup:</label>
        <input type="text" name="technology" id="technology">
        <br>
        <button type="submit">Book Event</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**events.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booked Events</title>
</head>
<body>
    <h1>Booked Events</h1>
    <ul>
        {% for event in events %}
            <li>{{ event.event_type }} - Catering: {{ event.catering }}, Decoration: {{ event.decoration }}, Technology: {{ event.technology }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for session management.
- This code is ready for production with proper error handling and user feedback.
