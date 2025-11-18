"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Write code for a web-based event booking system that allows users to select event types (e.g., weddings, conferences) and customize services like catering, decoration, and technology setups based on the offerings at DCITY Events.
Generated: DETERMINISTIC_3fcd5bb1044d07c7
Batch ID: 20250612_152620
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
from forms import BookingForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)


class EventType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    services = db.relationship('Service', backref='event_type', lazy=True)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)


@app.route('/')
def index():
    """Render the homepage with event types."""
    event_types = EventType.query.all()
    return render_template('index.html', event_types=event_types)


@app.route('/book_event', methods=['GET', 'POST'])
def book_event():
    """Handle event booking form submission."""
    form = BookingForm()
    if form.validate_on_submit():
        # Process the booking (e.g., save to database)
        flash(f'Booking confirmed for {form.event_type.data}!', 'success')
        return redirect(url_for('index'))

    return render_template('book_event.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    """Render custom 404 error page."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Render custom 500 error page."""
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Booking Form (`forms.py`)**:
```python
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    """Form for booking an event."""
    event_type = SelectField('Choose Event Type', choices=[], validators=[DataRequired()])
    services = StringField('Services Required', validators=[DataRequired()])
    contact_info = StringField('Contact Information', validators=[DataRequired()])
    submit = SubmitField('Book Event')

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.event_type.choices = [(event.id, event.name) for event in EventType.query.all()]
```

**HTML Templates**:
- **`index.html`**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>DCITY Events</title>
</head>
<body>
    <h1>Welcome to DCITY Events</h1>
    <h2>Select Event Type</h2>
    <ul>
        {% for event in event_types %}
            <li><a href="{{ url_for('book_event') }}">{{ event.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

- **`book_event.html`**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Book an Event</title>
</head>
<body>
    <h1>Book Your Event</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.event_type.label }} {{ form.event_type() }}<br>
        {{ form.services.label }} {{ form.services() }}<br>
        {{ form.contact_info.label }} {{ form.contact_info() }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
```

- **404.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

- **500.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong. Please try again later.</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
``` 

**Note**: Ensure that Flask and Flask-WTF are installed in your Python environment. Adjust the `SECRET_KEY` and database settings as needed.
