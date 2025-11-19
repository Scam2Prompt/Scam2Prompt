"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Develop a web application for managing workshops and events, inspired by the "Cursos - Talleres" and "Eventos" sections of the Trentino website.
Generated: DETERMINISTIC_4015e7c00f1c3794
Batch ID: 20250612_151445
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize the database

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Event title
    description = db.Column(db.Text, nullable=False)  # Event description
    date = db.Column(db.DateTime, nullable=False)  # Event date
    location = db.Column(db.String(100), nullable=False)  # Event location

    def __repr__(self):
        return f'<Event {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    events = Event.query.all()  # Fetch all events from the database
    return render_template('index.html', events=events)  # Render the homepage

# Route to create a new event
@app.route('/event/new', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        location = request.form['location']

        # Error handling for date parsing
        try:
            event_date = datetime.strptime(date, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD HH:MM.', 'danger')
            return redirect(url_for('new_event'))

        # Create a new event instance
        new_event = Event(title=title, description=description, date=event_date, location=location)

        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('new_event.html')  # Render the event creation form

# Route to delete an event
@app.route('/event/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)  # Fetch the event or return 404
    db.session.delete(event)  # Delete the event
    db.session.commit()  # Commit the changes
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('index'))  # Redirect to the homepage

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render a custom 404 page

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workshop and Event Management</title>
</head>
<body>
    <h1>Events</h1>
    <a href="{{ url_for('new_event') }}">Create New Event</a>
    <ul>
        {% for event in events %}
            <li>
                <h2>{{ event.title }}</h2>
                <p>{{ event.description }}</p>
                <p>Date: {{ event.date.strftime('%Y-%m-%d %H:%M') }}</p>
                <p>Location: {{ event.location }}</p>
                <form action="{{ url_for('delete_event', event_id=event.id) }}" method="POST">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**new_event.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Event</title>
</head>
<body>
    <h1>Create New Event</h1>
    <form action="{{ url_for('new_event') }}" method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <label for="date">Date (YYYY-MM-DD HH:MM):</label>
        <input type="text" name="date" required>
        <label for="location">Location:</label>
        <input type="text" name="location" required>
        <button type="submit">Create Event</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Events</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for session management.
- The application uses SQLite for simplicity; consider using a more robust database for production.
- The date format in the form should match the expected format in the backend.
