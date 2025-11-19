"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate code to create a web-based booking system for guided tours of Armourers' Hall, including features for selecting dates and viewing availability.
Generated: DETERMINISTIC_16a4e8f5f2b0b5c3
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Armourers' Hall Booking System**
=====================================

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
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'
db = SQLAlchemy(app)


class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'Tour(date={self.date}, available={self.available})'


class BookingForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Check Availability')


class BookingConfirmationForm(FlaskForm):
    submit = SubmitField('Book Tour')


@app.before_first_request
def create_tables():
    db.create_all()
    # Initialize some tour dates
    for i in range(30):
        date = datetime.now() + timedelta(days=i)
        tour = Tour(date=date.date())
        db.session.add(tour)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    if form.validate_on_submit():
        date = form.date.data
        tour = Tour.query.filter_by(date=date).first()
        if tour and tour.available:
            return redirect(url_for('book', date=date))
        else:
            return render_template('unavailable.html', date=date)
    return render_template('index.html', form=form)


@app.route('/book/<date>', methods=['GET', 'POST'])
def book(date):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    tour = Tour.query.filter_by(date=date).first()
    if not tour or not tour.available:
        return render_template('unavailable.html', date=date)

    form = BookingConfirmationForm()
    if form.validate_on_submit():
        tour.available = False
        db.session.commit()
        return render_template('booking_confirmed.html', date=date)
    return render_template('book.html', date=date, form=form)


@app.route('/availability')
def availability():
    tours = Tour.query.all()
    available_tours = [tour.date for tour in tours if tour.available]
    return render_template('availability.html', available_tours=available_tours)


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
    <title>Armourers' Hall Booking System</title>
</head>
<body>
    <h1>Armourers' Hall Booking System</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.date.label }} {{ form.date() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/book.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Tour</title>
</head>
<body>
    <h1>Book Tour on {{ date }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/availability.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Availability</title>
</head>
<body>
    <h1>Available Tours</h1>
    <ul>
    {% for date in available_tours %}
        <li>{{ date }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/unavailable.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unavailable</title>
</head>
<body>
    <h1>Sorry, {{ date }} is unavailable</h1>
</body>
</html>
```

```html
<!-- templates/booking_confirmed.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking Confirmed</title>
</head>
<body>
    <h1>Booking confirmed for {{ date }}</h1>
</body>
</html>
```
