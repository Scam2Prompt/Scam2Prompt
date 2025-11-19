"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Develop a simple web application using Flask or Django to create an event planning platform that allows users to create, manage, and RSVP for events.
Generated: DETERMINISTIC_f5e3fa81ace148ab
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Event Planning Platform using Flask**
=====================================

### Requirements

* Python 3.8+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code

```python
# app.py

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    attendees = db.relationship('RSVP', backref='event', lazy=True)

    def __repr__(self):
        return f"Event('{self.name}', '{self.date}')"


class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    attending = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"RSVP('{self.user_name}', '{self.attending}')"


class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    date = DateTimeField('Event Date', validators=[DataRequired()])
    location = StringField('Event Location', validators=[DataRequired()])
    submit = SubmitField('Create Event')


class RSVPForm(FlaskForm):
    user_name = StringField('Your Name', validators=[DataRequired()])
    attending = BooleanField('Attending')
    submit = SubmitField('RSVP')


@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)


@app.route('/event/create', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data, date=form.date.data, location=form.location.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_event.html', form=form)


@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    rsvps = event.attendees.all()
    return render_template('event_details.html', event=event, rsvps=rsvps)


@app.route('/event/<int:event_id>/rsvp', methods=['GET', 'POST'])
def rsvp(event_id):
    event = Event.query.get_or_404(event_id)
    form = RSVPForm()
    if form.validate_on_submit():
        rsvp = RSVP(event_id=event_id, user_name=form.user_name.data, attending=form.attending.data)
        db.session.add(rsvp)
        db.session.commit()
        return redirect(url_for('event_details', event_id=event_id))
    return render_template('rsvp.html', form=form, event=event)


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
    <title>Event Planning Platform</title>
</head>
<body>
    <h1>Events</h1>
    <ul>
    {% for event in events %}
        <li>
            {{ event.name }} - {{ event.date }}
            <a href="{{ url_for('event_details', event_id=event.id) }}">View Details</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_event') }}">Create Event</a></p>
</body>
</html>
```

```html
<!-- templates/create_event.html -->

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
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.date.label }} {{ form.date() }}
        {{ form.location.label }} {{ form.location() }}
        {{ form.submit() }}
    </form>
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
    <title>Event Details</title>
</head>
<body>
    <h1>{{ event.name }} - {{ event.date }}</h1>
    <p>Location: {{ event.location }}</p>
    <h2>RSVPs:</h2>
    <ul>
    {% for rsvp in rsvps %}
        <li>
            {{ rsvp.user_name }} - {{ rsvp.attending }}
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('rsvp', event_id=event.id) }}">RSVP</a></p>
</body>
</html>
```

```html
<!-- templates/rsvp.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RSVP</title>
</head>
<body>
    <h1>RSVP for {{ event.name }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.user_name.label }} {{ form.user_name() }}
        {{ form.attending() }} {{ form.attending.label }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```python
# run.py

from app import db, app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
