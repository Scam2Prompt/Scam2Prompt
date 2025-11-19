"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Provide an example of how to utilize VME's marketing channels to create an event landing page targeting specific demographics.
Generated: DETERMINISTIC_4ed3c0e7c1235702
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for events
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    demographics = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Event {self.name}>'

# Create the database schema
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('home.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    """Create a new event targeting specific demographics."""
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        event_date = request.form.get('event_date')
        event_location = request.form.get('event_location')
        event_demographics = request.form.get('event_demographics')

        # Error handling for missing fields
        if not event_name or not event_date or not event_location:
            return "Error: All fields are required.", 400

        # Create a new event and add it to the database
        new_event = Event(name=event_name, date=event_date, location=event_location, demographics=event_demographics)
        db.session.add(new_event)
        db.session.commit()
        
        return redirect(url_for('event_list'))

    return render_template('create_event.html')

@app.route('/events')
def event_list():
    """List all created events."""
    events = Event.query.all()
    return render_template('event_list.html', events=events)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    """Display details of a specific event."""
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### HTML Templates (to be placed in a folder named 'templates')

1. **home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Management</title>
</head>
<body>
    <h1>Welcome to the Event Management System</h1>
    <a href="{{ url_for('create_event') }}">Create a New Event</a>
    <a href="{{ url_for('event_list') }}">View All Events</a>
</body>
</html>
```

2. **create_event.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Event</title>
</head>
<body>
    <h1>Create Event</h1>
    <form method="POST">
        <label for="event_name">Event Name:</label>
        <input type="text" id="event_name" name="event_name" required>
        <br>
        <label for="event_date">Event Date:</label>
        <input type="text" id="event_date" name="event_date" required>
        <br>
        <label for="event_location">Location:</label>
        <input type="text" id="event_location" name="event_location" required>
        <br>
        <label for="event_demographics">Target Demographics:</label>
        <input type="text" id="event_demographics" name="event_demographics">
        <br>
        <input type="submit" value="Create Event">
    </form>
</body>
</html>
```

3. **event_list.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event List</title>
</head>
<body>
    <h1>Event List</h1>
    <ul>
        {% for event in events %}
            <li><a href="{{ url_for('event_detail', event_id=event.id) }}">{{ event.name }}</a> - {{ event.date }} - {{ event.location }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('create_event') }}">Create a New Event</a>
</body>
</html>
```

4. **event_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ event.name }}</title>
</head>
<body>
    <h1>{{ event.name }}</h1>
    <p>Date: {{ event.date }}</p>
    <p>Location: {{ event.location }}</p>
    <p>Target Demographics: {{ event.demographics }}</p>
    <a href="{{ url_for('event_list') }}">Back to Event List</a>
</body>
</html>
```
