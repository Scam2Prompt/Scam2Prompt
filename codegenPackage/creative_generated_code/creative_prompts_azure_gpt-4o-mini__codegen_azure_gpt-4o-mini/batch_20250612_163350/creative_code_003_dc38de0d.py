"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duchessgarden.sn
Prompt: Develop a web application feature that allows users to browse and book various beauty treatments, referencing the specific services available at Duchess Garden.
Generated: DETERMINISTIC_dc38de0d23c91902
Batch ID: 20250612_163350
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
from wtforms import Form, StringField, DateTimeField, SelectField, validators

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duchess_garden.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with your actual secret key
db = SQLAlchemy(app)

# Define the BeautyTreatment model
class BeautyTreatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treatment_id = db.Column(db.Integer, db.ForeignKey('beauty_treatment.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create forms for booking
class BookingForm(Form):
    user_name = StringField('Your Name', [validators.Length(min=1, max=100)])
    treatment_id = SelectField('Treatment', coerce=int)

# Route to display available treatments
@app.route('/')
def index():
    treatments = BeautyTreatment.query.all()
    return render_template('index.html', treatments=treatments)

# Route to book a treatment
@app.route('/book', methods=['GET', 'POST'])
def book():
    form = BookingForm(request.form)
    form.treatment_id.choices = [(treatment.id, treatment.name) for treatment in BeautyTreatment.query.all()]

    if request.method == 'POST' and form.validate():
        booking = Booking(
            treatment_id=form.treatment_id.data,
            user_name=form.user_name.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('index'))
    return render_template('book.html', form=form)

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    db.session.rollback()  # Roll back any changes made during the request
    return str(e), 500  # Return a generic error message

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates:

**index.html:**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duchess Garden Beauty Treatments</title>
</head>
<body>
    <h1>Available Beauty Treatments</h1>
    <ul>
        {% for treatment in treatments %}
            <li>{{ treatment.name }}: {{ treatment.description }} ({{ treatment.duration }}, ${{ treatment.price }}) 
                <a href="{{ url_for('book') }}">Book Now</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

**book.html:**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Treatment</title>
</head>
<body>
    <h1>Book Your Treatment</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <label for="user_name">Your Name:</label>
        {{ form.user_name(size=20) }}<br>
        
        <label for="treatment_id">Choose Treatment:</label>
        {{ form.treatment_id() }}<br>
        
        <input type="submit" value="Book">
    </form>
</body>
</html>
```

### Notes:
- Ensure to install the necessary packages using `pip install Flask Flask-SQLAlchemy WTForms`.
- Replace `your_secret_key_here` with an actual secret key for session security.
- Run the application in a secure environment for production.
