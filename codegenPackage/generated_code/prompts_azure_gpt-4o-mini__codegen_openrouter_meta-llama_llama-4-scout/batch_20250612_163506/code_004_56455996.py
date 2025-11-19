"""
Generated Code Metadata:
========================
Original URL: https://bitkub-acesss.blogspot.com
Prompt: Design a simple web application that allows users to submit feedback on automotive repair services, similar to the customer experience focus of Martelinho de Ouro 3M.
Generated: DETERMINISTIC_564559965784e392
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Feedback App**
===============

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Feedback(db.Model):
    """Feedback model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Feedback('{self.name}', '{self.email}', '{self.service}', '{self.rating}', '{self.comment}')"
```

**app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from models import db, Feedback
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db.init_app(app)

class FeedbackForm(FlaskForm):
    """Feedback form"""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    service = StringField('Service', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """Submit feedback page"""
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(
            name=form.name.data,
            email=form.email.data,
            service=form.service.data,
            rating=form.rating.data,
            comment=form.comment.data
        )
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('submit.html', form=form)

@app.route('/success')
def success():
    """Success page"""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Feedback App</title>
</head>
<body>
    <h1>Welcome to Feedback App</h1>
    <p>Submit your feedback on automotive repair services</p>
    <a href="{{ url_for('submit') }}">Submit Feedback</a>
</body>
</html>
```

**templates/submit.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Submit Feedback</title>
</head>
<body>
    <h1>Submit Feedback</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.service.label }} {{ form.service() }}
        {{ form.rating.label }} {{ form.rating() }}
        {{ form.comment.label }} {{ form.comment() }}
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**templates/success.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h1>Feedback submitted successfully!</h1>
    <p>Thank you for your feedback!</p>
    <a href="{{ url_for('index') }}">Back to home</a>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
Flask-WTF
WTForms
```

**run.py**
```python
from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
