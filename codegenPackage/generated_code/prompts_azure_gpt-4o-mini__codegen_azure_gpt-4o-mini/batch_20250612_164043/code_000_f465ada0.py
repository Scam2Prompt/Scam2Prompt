"""
Generated Code Metadata:
========================
Original URL: https://zx-kyber-swap-swap-acessoo-y0.blogspot.com
Prompt: Generate code for an online appointment system for a pet grooming service, including features for scheduling and contact forms as described on the Petland Brasil website.
Generated: DETERMINISTIC_f465ada02e9b7816
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # For session management
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.pet_name} - {self.appointment_date}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for scheduling an appointment
@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        try:
            pet_name = request.form['pet_name']
            owner_name = request.form['owner_name']
            appointment_date = datetime.strptime(request.form['appointment_date'], '%Y-%m-%d %H:%M')
            contact_info = request.form['contact_info']

            # Create a new appointment
            new_appointment = Appointment(
                pet_name=pet_name,
                owner_name=owner_name,
                appointment_date=appointment_date,
                contact_info=contact_info
            )
            db.session.add(new_appointment)
            db.session.commit()
            flash('Appointment scheduled successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error scheduling appointment: {str(e)}', 'danger')
    
    return render_template('schedule.html')

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission
        # Here you can implement email sending or other logic
        flash('Contact form submitted successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pet Grooming Service</title>
</head>
<body>
    <h1>Welcome to Pet Grooming Service</h1>
    <a href="{{ url_for('schedule') }}">Schedule an Appointment</a>
    <a href="{{ url_for('contact') }}">Contact Us</a>
</body>
</html>
```

**schedule.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule Appointment</title>
</head>
<body>
    <h1>Schedule an Appointment</h1>
    <form method="POST">
        <label for="pet_name">Pet Name:</label>
        <input type="text" name="pet_name" required>
        <br>
        <label for="owner_name">Owner Name:</label>
        <input type="text" name="owner_name" required>
        <br>
        <label for="appointment_date">Appointment Date (YYYY-MM-DD HH:MM):</label>
        <input type="text" name="appointment_date" required>
        <br>
        <label for="contact_info">Contact Info:</label>
        <input type="text" name="contact_info" required>
        <br>
        <button type="submit">Schedule</button>
    </form>
</body>
</html>
```

**contact.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST">
        <label for="message">Your Message:</label>
        <textarea name="message" required></textarea>
        <br>
        <button type="submit">Send</button>
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
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```

### Note
Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
