"""
Generated Code Metadata:
========================
Original URL: https://duchessgarden.sn
Prompt: Develop a web application feature that allows users to browse and book various beauty treatments, referencing the specific services available at Duchess Garden.
Generated: DETERMINISTIC_dc38de0d23c91902
Batch ID: 20250612_163350
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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duchess_garden.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the database model for Beauty Treatments
class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes

    def __repr__(self):
        return f'<Treatment {self.name}>'

# Define the database model for Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    customer_name = db.Column(db.String(100), nullable=False)

    treatment = db.relationship('Treatment', backref='bookings')

    def __repr__(self):
        return f'<Booking {self.id} for {self.customer_name}>'

# Route to display available treatments
@app.route('/')
def index():
    treatments = Treatment.query.all()
    return render_template('index.html', treatments=treatments)

# Route to book a treatment
@app.route('/book/<int:treatment_id>', methods=['GET', 'POST'])
def book(treatment_id):
    treatment = Treatment.query.get_or_404(treatment_id)
    
    if request.method == 'POST':
        customer_name = request.form.get('customer_name')
        if not customer_name:
            flash('Customer name is required!', 'danger')
            return redirect(url_for('book', treatment_id=treatment_id))
        
        # Create a new booking
        new_booking = Booking(treatment_id=treatment.id, customer_name=customer_name)
        db.session.add(new_booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('index'))

    return render_template('book.html', treatment=treatment)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duchess Garden - Treatments</title>
</head>
<body>
    <h1>Available Beauty Treatments</h1>
    <ul>
        {% for treatment in treatments %}
            <li>
                <h2>{{ treatment.name }}</h2>
                <p>{{ treatment.description }}</p>
                <p>Price: ${{ treatment.price }}</p>
                <p>Duration: {{ treatment.duration }} minutes</p>
                <a href="{{ url_for('book', treatment_id=treatment.id) }}">Book Now</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**book.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book {{ treatment.name }}</title>
</head>
<body>
    <h1>Book {{ treatment.name }}</h1>
    <form method="POST">
        <label for="customer_name">Your Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>
        <button type="submit">Confirm Booking</button>
    </form>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong. Please try again later.</p>
</body>
</html>
```

### Note
Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
