"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Suggest tools or libraries for creating a multilingual website to promote awareness lectures and community events, inspired by the ALPS Foundation's Swiss-based initiatives.
Generated: DETERMINISTIC_fc070fcb3d40b2a9
Batch ID: 20250612_151126
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
from flask_babel import Babel, gettext as _
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
babel = Babel(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'

# Set up Babel for language selection
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

# Route for the homepage
@app.route('/')
def index():
    events = Event.query.all()  # Fetch all events from the database
    return render_template('index.html', events=events)

# Route to add a new event
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        date = request.form.get('date')

        # Error handling for missing fields
        if not title or not description or not date:
            flash(_('All fields are required!'), 'error')
            return redirect(url_for('add_event'))

        # Create a new event and add it to the database
        new_event = Event(title=title, description=description, date=date)
        db.session.add(new_event)
        db.session.commit()
        flash(_('Event added successfully!'), 'success')
        return redirect(url_for('index'))

    return render_template('add_event.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Event List') }}</title>
</head>
<body>
    <h1>{{ _('Upcoming Events') }}</h1>
    <ul>
        {% for event in events %}
            <li>{{ event.title }} - {{ event.date }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_event') }}">{{ _('Add Event') }}</a>
</body>
</html>
```

**add_event.html**
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Add Event') }}</title>
</head>
<body>
    <h1>{{ _('Add a New Event') }}</h1>
    <form method="POST">
        <label for="title">{{ _('Title') }}</label>
        <input type="text" name="title" required>
        <label for="description">{{ _('Description') }}</label>
        <textarea name="description" required></textarea>
        <label for="date">{{ _('Date') }}</label>
        <input type="datetime-local" name="date" required>
        <button type="submit">{{ _('Submit') }}</button>
    </form>
    <a href="{{ url_for('index') }}">{{ _('Back to Events') }}</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Page Not Found') }}</title>
</head>
<body>
    <h1>{{ _('404 - Page Not Found') }}</h1>
    <a href="{{ url_for('index') }}">{{ _('Back to Home') }}</a>
</body>
</html>
```

### Note:
- Ensure you have the necessary libraries installed: `Flask`, `Flask-Babel`, `Flask-SQLAlchemy`, and `Flask-Migrate`.
- This code is a basic structure for a multilingual event management web application. You can expand it further based on your requirements.
