"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Provide sample code for a web-based booking system tailored for mobile fuel injector cleaning services, referencing the "BOOK NOW" feature on the Fuel Injector Services website.
Generated: DETERMINISTIC_ba3543bf16ac74b0
Batch ID: 20250612_151611
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.name} on {self.service_date}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the booking form
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        phone = request.form.get('phone')
        service_date = request.form.get('service_date')

        # Validate form data
        if not name or not phone or not service_date:
            flash('All fields are required!', 'danger')
            return redirect(url_for('book'))

        # Create a new booking
        new_booking = Booking(name=name, phone=phone, service_date=datetime.strptime(service_date, '%Y-%m-%d %H:%M'))
        
        try:
            # Add the booking to the database
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking successful!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error occurred while booking. Please try again.', 'danger')
            return redirect(url_for('book'))

    return render_template('book.html')

# Route to view all bookings (for admin purposes)
@app.route('/bookings')
def bookings():
    all_bookings = Booking.query.all()
    return render_template('bookings.html', bookings=all_bookings)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fuel Injector Cleaning Services</title>
</head>
<body>
    <h1>Welcome to Mobile Fuel Injector Cleaning Services</h1>
    <a href="{{ url_for('book') }}">BOOK NOW</a>
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
    <title>Book a Service</title>
</head>
<body>
    <h1>Book Your Service</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <br>
        <label for="service_date">Service Date:</label>
        <input type="datetime-local" id="service_date" name="service_date" required>
        <br>
        <button type="submit">Submit Booking</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**bookings.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Bookings</title>
</head>
<body>
    <h1>All Bookings</h1>
    <ul>
        {% for booking in bookings %}
            <li>{{ booking.name }} - {{ booking.phone }} - {{ booking.service_date }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for session management.
- The database will be created in the same directory as the script when you run it for the first time.
