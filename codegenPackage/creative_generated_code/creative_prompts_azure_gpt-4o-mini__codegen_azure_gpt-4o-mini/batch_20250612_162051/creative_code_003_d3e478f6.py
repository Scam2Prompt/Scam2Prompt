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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the event
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Event {self.title} - {self.date}>'

# Home route to display events
@app.route('/')
def index():
    events = Event.query.all()  # Fetch all events from the database
    return render_template('index.html', events=events)

# Route to create a new event
@app.route('/event/new', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        try:
            title = request.form['title']
            date = datetime.strptime(request.form['date'], '%Y-%m-%d %H:%M')
            description = request.form['description']
            new_event = Event(title=title, date=date, description=description)
            db.session.add(new_event)  # Add the new event to the session
            db.session.commit()  # Commit the session to save the event
            flash('Event created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error creating event: {str(e)}', 'danger')
            return redirect(url_for('new_event'))

    return render_template('new_event.html')

# Error handling
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Run the application only if executed directly
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Enable debugging during development
```

**HTML Templates:**

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dani otvorenih vrata</title>
</head>
<body>
    <h1>Dani otvorenih vrata Events</h1>
    <a href="{{ url_for('new_event') }}">Create New Event</a>
    
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
            <li>
                <strong>{{ event.title }}</strong><br>
                Date: {{ event.date.strftime('%Y-%m-%d %H:%M') }}<br>
                Description: {{ event.description }}
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
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>
        
        <label for="date">Date (YYYY-MM-DD HH:MM):</label>
        <input type="text" id="date" name="date" required><br>
        
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea><br>
        
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
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for could not be found.</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

**Note:** Before running the application, ensure that Flask and Flask-SQLAlchemy are installed in your Python environment. Use the following command to install them:

```bash
pip install Flask Flask-SQLAlchemy
```
