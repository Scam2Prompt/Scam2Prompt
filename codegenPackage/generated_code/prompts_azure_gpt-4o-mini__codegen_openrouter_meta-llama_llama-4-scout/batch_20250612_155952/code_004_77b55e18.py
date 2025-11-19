"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Design a simple web application that displays the schedule and details of the basketball training camps offered by L-Zero, allowing users to register directly through the app.
Generated: DETERMINISTIC_77b55e187a673888
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**L-Zero Basketball Training Camps Web Application**

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code

```python
# app.py

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lz_basketball.db'
db = SQLAlchemy(app)


# Models
class Camp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    spots_available = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Camp('{self.name}', '{self.date}', '{self.time}', '{self.location}')"


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'), nullable=False)

    def __repr__(self):
        return f"Registration('{self.name}', '{self.email}', '{self.camp_id}')"


# Forms
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')


# Routes
@app.route('/')
def index():
    camps = Camp.query.all()
    return render_template('index.html', camps=camps)


@app.route('/camp/<int:camp_id>')
def camp_details(camp_id):
    camp = Camp.query.get_or_404(camp_id)
    return render_template('camp_details.html', camp=camp)


@app.route('/register/<int:camp_id>', methods=['GET', 'POST'])
def register(camp_id):
    camp = Camp.query.get_or_404(camp_id)
    form = RegistrationForm()
    if form.validate_on_submit():
        registration = Registration(name=form.name.data, email=form.email.data, camp_id=camp_id)
        db.session.add(registration)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form, camp=camp)


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py (not needed, but kept for reference)

# No models defined here, using app.py instead
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L-Zero Basketball Training Camps</title>
</head>
<body>
    <h1>L-Zero Basketball Training Camps</h1>
    <ul>
    {% for camp in camps %}
        <li>
            {{ camp.name }} ({{ camp.date }}, {{ camp.time }}) - {{ camp.location }}
            <a href="{{ url_for('camp_details', camp_id=camp.id) }}">View Details</a>
            <a href="{{ url_for('register', camp_id=camp.id) }}">Register</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/camp_details.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ camp.name }} Details</title>
</head>
<body>
    <h1>{{ camp.name }} Details</h1>
    <p>Date: {{ camp.date }}</p>
    <p>Time: {{ camp.time }}</p>
    <p>Location: {{ camp.location }}</p>
    <p>Spots Available: {{ camp.spots_available }}</p>
    <a href="{{ url_for('register', camp_id=camp.id) }}">Register</a>
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
    <title>Register for {{ camp.name }}</title>
</head>
<body>
    <h1>Register for {{ camp.name }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```python
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
```

```bash
# Run with
python app.py
```

### Database Setup

Run the following commands to create the database:

```python
from app import db
with app.app_context():
    db.create_all()
```
