"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Generate code for a web application that allows users to book appointments for hearing tests, inspired by the appointment booking system on Otex.ae.
Generated: DETERMINISTIC_7a90dd432759277f
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Configuration for Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to book an appointment
@app.route('/book', methods=['POST'])
def book_appointment():
    try:
        # Get data from request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        appointment_date = datetime.strptime(data.get('appointment_date'), '%Y-%m-%d %H:%M:%S')

        # Validate input data
        if not all([name, email, phone, appointment_date]):
            return jsonify({'error': 'All fields are required!'}), 400

        # Create a new appointment
        new_appointment = Appointment(name=name, email=email, phone=phone, appointment_date=appointment_date)
        
        # Add to the database
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment booked successfully!'}), 201

    except IntegrityError:
        db.session.rollback()  # Rollback in case of integrity error
        return jsonify({'error': 'This appointment already exists!'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to list all appointments
@app.route('/appointments', methods=['GET'])
def list_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'id': appt.id,
            'name': appt.name,
            'email': appt.email,
            'phone': appt.phone,
            'appointment_date': appt.appointment_date.strftime('%Y-%m-%d %H:%M:%S')
        } for appt in appointments]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Hearing Test Appointment</title>
</head>
<body>
    <h1>Book Your Hearing Test Appointment</h1>
    <form id="appointment-form">
        <input type="text" id="name" placeholder="Your Name" required>
        <input type="email" id="email" placeholder="Your Email" required>
        <input type="text" id="phone" placeholder="Your Phone" required>
        <input type="datetime-local" id="appointment_date" required>
        <button type="submit">Book Appointment</button>
    </form>

    <script>
        document.getElementById('appointment-form').addEventListener('submit', async function (e) {
            e.preventDefault();
            const response = await fetch('/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    phone: document.getElementById('phone').value,
                    appointment_date: document.getElementById('appointment_date').value
                })
            });
            const result = await response.json();
            alert(result.message || result.error);
        });
    </script>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment (`pip install Flask Flask-SQLAlchemy`).
- The SQLite database file will be created in the same directory as this script when the app is run for the first time.
- Proper error handling and validations are included to ensure reliability in a production environment.
