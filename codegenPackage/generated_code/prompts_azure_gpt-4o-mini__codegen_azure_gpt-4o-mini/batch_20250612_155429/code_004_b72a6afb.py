"""
Generated Code Metadata:
========================
Original URL: https://casaamalfitana.com
Prompt: Suggest a way to implement a user-friendly interface for a restaurant's reservation system that reflects the unique dining experience of Casa Amalfitana.
Generated: DETERMINISTIC_b72a6afbaa686422
Batch ID: 20250612_155429
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.name} on {self.date}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for making a reservation
@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        date_str = request.form['date']
        guests = request.form['guests']

        # Validate input
        if not name or not email or not date_str or not guests:
            flash('All fields are required!', 'danger')
            return redirect(url_for('reserve'))

        try:
            # Convert date string to datetime object
            date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
            guests = int(guests)

            # Create a new reservation
            new_reservation = Reservation(name=name, email=email, date=date, guests=guests)
            db.session.add(new_reservation)
            db.session.commit()
            flash('Reservation made successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid date format! Please use YYYY-MM-DD HH:MM.', 'danger')
            return redirect(url_for('reserve'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('reserve'))

    return render_template('reserve.html')

# Route for viewing reservations
@app.route('/reservations')
def reservations():
    all_reservations = Reservation.query.all()
    return render_template('reservations.html', reservations=all_reservations)

# Run the application
if __name__ == '__main__':
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
    <title>Casa Amalfitana - Home</title>
</head>
<body>
    <h1>Welcome to Casa Amalfitana</h1>
    <a href="{{ url_for('reserve') }}">Make a Reservation</a>
    <a href="{{ url_for('reservations') }}">View Reservations</a>
</body>
</html>
```

**reserve.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Make a Reservation</title>
</head>
<body>
    <h1>Make a Reservation</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="datetime-local" name="date" required>
        <input type="number" name="guests" placeholder="Number of Guests" required>
        <button type="submit">Reserve</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**reservations.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reservations</title>
</head>
<body>
    <h1>All Reservations</h1>
    <ul>
        {% for reservation in reservations %}
            <li>{{ reservation.name }} - {{ reservation.date }} - Guests: {{ reservation.guests }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production use.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
