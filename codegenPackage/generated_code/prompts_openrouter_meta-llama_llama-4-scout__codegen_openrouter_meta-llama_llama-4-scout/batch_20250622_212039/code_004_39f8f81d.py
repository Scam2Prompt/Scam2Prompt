"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Create a donation management system for a non-profit organization that focuses on menstrual health and education, using a framework like Django or Flask.
Generated: DETERMINISTIC_39f8f81d1ad4cffc
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Donation Management System**
================================

### Requirements

* Python 3.9+
* Flask 2.2+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code

```python
# app.py
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
db = SQLAlchemy(app)


# Models
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    donations = db.relationship('Donation', backref='donor', lazy=True)

    def __repr__(self):
        return f"Donor('{self.name}', '{self.email}')"


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Donation('{self.amount}', '{self.date}')"


# Forms
class DonationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Donate')


class DonorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Add Donor')


# Routes
@app.route('/')
def index():
    donations = Donation.query.all()
    return render_template('index.html', donations=donations)


@app.route('/donate', methods=['GET', 'POST'])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        donor = Donor.query.filter_by(email=form.email.data).first()
        if donor is None:
            donor = Donor(name=form.name.data, email=form.email.data)
            db.session.add(donor)
            db.session.commit()
        donation = Donation(amount=form.amount.data, donor=donor)
        db.session.add(donation)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('donate.html', form=form)


@app.route('/donors', methods=['GET', 'POST'])
def donors():
    form = DonorForm()
    if form.validate_on_submit():
        donor = Donor(name=form.name.data, email=form.email.data)
        db.session.add(donor)
        db.session.commit()
        return redirect(url_for('index'))
    donors = Donor.query.all()
    return render_template('donors.html', form=form, donors=donors)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```python
# templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donation Management System</title>
</head>
<body>
    <h1>Donations</h1>
    <ul>
    {% for donation in donations %}
        <li>{{ donation.donor.name }} - {{ donation.amount }} ({{ donation.date }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('donate') }}">Make a Donation</a></p>
    <p><a href="{{ url_for('donors') }}">View Donors</a></p>
</body>
</html>
```

```python
# templates/donate.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Make a Donation</title>
</head>
<body>
    <h1>Make a Donation</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.amount.label }} {{ form.amount() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```python
# templates/donors.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donors</title>
</head>
<body>
    <h1>Donors</h1>
    <ul>
    {% for donor in donors %}
        <li>{{ donor.name }} ({{ donor.email }})</li>
    {% endfor %}
    </ul>
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
# templates/404.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>Page not found.</p>
</body>
</html>
```
