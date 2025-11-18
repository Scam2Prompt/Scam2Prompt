"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Provide sample code for a web-based booking system tailored for mobile fuel injector cleaning services, referencing the "BOOK NOW" feature on the Fuel Injector Services website.
Generated: DETERMINISTIC_ba3543bf16ac74b0
Batch ID: 20250612_151611
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

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'  # Use a secure secret key for session management

# Initialize the database
db = SQLAlchemy(app)

# Database model for bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.name} on {self.service_date}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the booking form
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        service_date = request.form.get('service_date')

        # Input validation
        if not name or not phone or not service_date:
            flash('All fields are required!', 'error')
            return redirect(url_for('book'))

        # Create a new booking
        new_booking = Booking(name=name, phone=phone, service_date=datetime.strptime(service_date, '%Y-%m-%d'))
        
        try:
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking successful!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('book'))

    return render_template('book.html')

# Route for viewing bookings (admin purpose)
@app.route('/admin/bookings')
def view_bookings():
    bookings = Booking.query.all()
    return render_template('view_bookings.html', bookings=bookings)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates (place in a `templates` folder)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fuel Injector Services</title>
</head>
<body>
    <h1>Welcome to Fuel Injector Services</h1>
    <a href="/book">BOOK NOW</a>
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
    <h1>Book Your Fuel Injector Cleaning Service</h1>
    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <br>
        <label for="service_date">Service Date:</label>
        <input type="date" id="service_date" name="service_date" required>
        <br>
        <button type="submit">Submit Booking</button>
    </form>
</body>
</html>
```

**view_bookings.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - View Bookings</title>
</head>
<body>
    <h1>Bookings List</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Phone</th>
            <th>Service Date</th>
            <th>Created At</th>
        </tr>
        {% for booking in bookings %}
        <tr>
            <td>{{ booking.id }}</td>
            <td>{{ booking.name }}</td>
            <td>{{ booking.phone }}</td>
            <td>{{ booking.service_date.strftime('%Y-%m-%d') }}</td>
            <td>{{ booking.created_at.strftime('%Y-%m-%d %H:%M:%S') }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Instructions
- Ensure you have Flask and Flask-SQLAlchemy installed (`pip install flask flask-sqlalchemy`).
- Create a SQLite database file by running the Python file once.
- Place the HTML files in a folder named `templates`.
- Start the application and navigate to the provided routes for booking services.
