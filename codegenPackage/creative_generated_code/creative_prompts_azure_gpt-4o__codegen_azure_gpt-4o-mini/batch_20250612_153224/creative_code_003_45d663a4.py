"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Recommend a library or framework to implement an online booking system for dumpster rentals, similar to the one described on the Purple Dumpster website.
Generated: DETERMINISTIC_45d663a4c133cd1f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dumpster_rentals.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # For session management and flash messages
db = SQLAlchemy(app)

# Define the database model for dumpster rentals
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    rental_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)  # Duration in days
    size = db.Column(db.String(50), nullable=False)  # Size of the dumpster

    def __repr__(self):
        return f'<Rental {self.id} - {self.name}>'

# Create the database before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for booking a dumpster
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            rental_date = request.form['rental_date']
            duration = int(request.form['duration'])
            size = request.form['size']
            
            # Validate rental_date format
            datetime.strptime(rental_date, '%Y-%m-%d')
            
            # Create a new rental entry
            new_rental = Rental(name=name, email=email, rental_date=rental_date, duration=duration, size=size)
            db.session.add(new_rental)
            db.session.commit()
            
            flash('Booking successful!', 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(f'Error: {e}', 'danger')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
    
    return render_template('book.html')

# Route to view all bookings
@app.route('/rentals')
def rentals():
    all_rentals = Rental.query.all()
    return render_template('rentals.html', rentals=all_rentals)

# Error handling for not found routes
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Create a basic HTML template for index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dumpster Rental</title>
</head>
<body>
    <h1>Welcome to Dumpster Rental Service</h1>
    <a href="{{ url_for('book') }}">Book a Dumpster</a> | 
    <a href="{{ url_for('rentals') }}">View Rentals</a>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

```html
<!-- Create a basic HTML template for book.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book a Dumpster</title>
</head>
<body>
    <h1>Book a Dumpster</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="rental_date">Rental Date:</label>
        <input type="date" id="rental_date" name="rental_date" required>
        
        <label for="duration">Duration (days):</label>
        <input type="number" id="duration" name="duration" required>
        
        <label for="size">Size:</label>
        <select id="size" name="size" required>
            <option value="10 Yard">10 Yard</option>
            <option value="20 Yard">20 Yard</option>
            <option value="30 Yard">30 Yard</option>
        </select>
        
        <button type="submit">Book Now</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- Create a basic HTML template for rentals.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rentals</title>
</head>
<body>
    <h1>Current Rentals</h1>
    <ul>
        {% for rental in rentals %}
            <li>{{ rental.name }} - {{ rental.email }} - {{ rental.rental_date }} - {{ rental.duration }} days - {{ rental.size }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- Create a basic HTML template for 404.html -->
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
