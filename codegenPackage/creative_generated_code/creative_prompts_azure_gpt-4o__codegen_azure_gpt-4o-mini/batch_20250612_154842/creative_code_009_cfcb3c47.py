"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Create a web application that mimics Swell Creative Management's flexible project-based model for creative services, including features for booking consultations and browsing services.
Generated: DETERMINISTIC_cfcb3c47fc9dd4ac
Batch ID: 20250612_154842
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Service {self.name}>'

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(120), nullable=False)

    service = db.relationship('Service', backref='bookings')

    def __repr__(self):
        return f'<Booking {self.client_name} for {self.service.name}>'

# Route to display available services
@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

# Route to book a consultation
@app.route('/book/<int:service_id>', methods=['GET', 'POST'])
def book(service_id):
    service = Service.query.get_or_404(service_id)
    if request.method == 'POST':
        # Get client information from the form
        client_name = request.form['client_name']
        client_email = request.form['client_email']

        # Create a new booking
        new_booking = Booking(service_id=service.id, client_name=client_name, client_email=client_email)
        db.session.add(new_booking)
        
        # Commit the changes
        try:
            db.session.commit()
            flash('Your consultation has been booked!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while booking your consultation. Please try again.', 'danger')

    return render_template('book.html', service=service)

# Route to initialize the database (only for the first run)
@app.cli.command('init-db')
def init_db():
    """Initializes the database."""
    db.create_all()
    print('Initialized the database.')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)
#### templates/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Swell Creative Management</title>
</head>
<body>
    <h1>Available Services</h1>
    <ul>
        {% for service in services %}
            <li>
                <h2>{{ service.name }}</h2>
                <p>{{ service.description }}</p>
                <p>Price: ${{ service.price }}</p>
                <a href="{{ url_for('book', service_id=service.id) }}">Book Consultation</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### templates/book.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book {{ service.name }}</title>
</head>
<body>
    <h1>Book Consultation for {{ service.name }}</h1>
    <form method="post">
        <label for="client_name">Your Name:</label>
        <input type="text" id="client_name" name="client_name" required>
        
        <label for="client_email">Your Email:</label>
        <input type="email" id="client_email" name="client_email" required>
        
        <button type="submit">Book Now</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Services</a>
</body>
</html>
```

#### templates/404.html
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Instructions
1. Make sure to have Flask and Flask-SQLAlchemy installed in your environment.
2. Run the command `flask init-db` to create the database.
3. Start the application with `flask run`.
