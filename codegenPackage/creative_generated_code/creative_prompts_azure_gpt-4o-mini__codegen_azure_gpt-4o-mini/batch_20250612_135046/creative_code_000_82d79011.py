"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Generate a code snippet for a web application that allows users to book RIB rentals in Greece, integrating features like fleet selection and event organization.
Generated: DETERMINISTIC_82d79011a7a10c62
Batch ID: 20250612_135046
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
from datetime import datetime
from forms import BookingForm, FleetSelectionForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rib_rentals.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong key
db = SQLAlchemy(app)

# Database model for RIB
class RIB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)

# Database model for Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rib_id = db.Column(db.Integer, db.ForeignKey('rib.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    rib = db.relationship('RIB', backref='bookings', lazy=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    """Render the home page with available RIBs."""
    ribs = RIB.query.all()
    return render_template('home.html', ribs=ribs)

@app.route('/book/<int:rib_id>', methods=['GET', 'POST'])
def book(rib_id):
    """Handle booking for a selected RIB."""
    rib = RIB.query.get_or_404(rib_id)
    form = BookingForm()

    if form.validate_on_submit():
        booking = Booking(
            rib_id=rib.id,
            user_name=form.user_name.data,
            event_date=form.event_date.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('home'))

    return render_template('book.html', form=form, rib=rib)

@app.route('/fleet')
def fleet():
    """Render the fleet selection page."""
    ribs = RIB.query.all()
    return render_template('fleet.html', ribs=ribs)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - RIB Rentals</title>
</head>
<body>
    <h1>Available RIBs</h1>
    <ul>
        {% for rib in ribs %}
        <li>
            {{ rib.name }} - Capacity: {{ rib.capacity }} - Price: €{{ rib.price_per_hour }}/hour
            <a href="{{ url_for('book', rib_id=rib.id) }}">Book Now</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- book.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book - {{ rib.name }}</title>
</head>
<body>
    <h1>Book {{ rib.name }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <label for="user_name">Your Name:</label>
        {{ form.user_name(size=32) }}
        <label for="event_date">Event Date:</label>
        {{ form.event_date() }}
        <input type="submit" value="Book">
    </form>
</body>
</html>
```

```python
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    user_name = StringField('Your Name', validators=[DataRequired()])
    event_date = DateTimeLocalField('Event Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Book')

class FleetSelectionForm(FlaskForm):
    submit = SubmitField('Select Fleet')
``` 

**Note:** Ensure you have the required packages installed and the templates are placed in the appropriate folder structure.
