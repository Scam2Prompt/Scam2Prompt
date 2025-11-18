"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Create a web application using Flask or Django to allow users to register for community programs, view event details, and submit feedback, as described in the association's initiatives.
Generated: DETERMINISTIC_8b28f662e59fafc5
Batch ID: 20250612_153246
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
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# Event model for community programs
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    details = db.Column(db.Text, nullable=False)


# Feedback model for user feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_email = db.Column(db.String(150), nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)


# Form to register users
class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


# Form for submitting feedback
class FeedbackForm(FlaskForm):
    user_email = EmailField('Email', validators=[DataRequired(), Email()])
    feedback_text = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')


# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


# Route for viewing events
@app.route('/events')
def events():
    all_events = Event.query.all()
    return render_template('events.html', events=all_events)


# Route for submitting feedback
@app.route('/feedback/<int:event_id>', methods=['GET', 'POST'])
@login_required
def feedback(event_id):
    form = FeedbackForm()
    if form.validate_on_submit():
        new_feedback = Feedback(event_id=event_id, user_email=form.user_email.data, feedback_text=form.feedback_text.data)
        db.session.add(new_feedback)
        db.session.commit()
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('events'))
    return render_template('feedback.html', form=form)


# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


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
    <title>Community Programs</title>
</head>
<body>
    <h1>Welcome to the Community Programs Portal!</h1>
    <a href="{{ url_for('register') }}">Register</a>
    <a href="{{ url_for('events') }}">View Events</a>
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
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.submit() }}
        </p>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/events.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Events</title>
</head>
<body>
    <h1>Community Programs Events</h1>
    <ul>
        {% for event in events %}
            <li>
                <strong>{{ event.title }}</strong>
                <p>{{ event.details }}</p>
                <a href="{{ url_for('feedback', event_id=event.id) }}">Submit Feedback</a>
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/feedback.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Feedback</title>
</head>
<body>
    <h1>Submit Feedback</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.user_email.label }}<br>
            {{ form.user_email(size=32) }}<br>
            {% for error in form.user_email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.feedback_text.label }}<br>
            {{ form.feedback_text(cols=30, rows=5) }}<br>
            {% for error in form.feedback_text.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.submit() }}
        </p>
    </form>
    <a href="{{ url_for('events') }}">Back to Events</a>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```bash
# requirements.txt
flask
flask_sqlalchemy
flask_migrate
flask_wtf
flask_login
wtforms
```

This code represents a complete Flask web application for managing community program registrations, event views, and feedback submission. It is structured for easy understanding and maintainability.
