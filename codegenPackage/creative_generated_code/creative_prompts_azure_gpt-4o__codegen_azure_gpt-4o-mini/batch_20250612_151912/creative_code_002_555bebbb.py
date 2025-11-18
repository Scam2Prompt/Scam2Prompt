"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Generate code for a web application that allows clients to book appointments with a family law attorney, referencing the structure and services provided by Majeli Avocat, such as consultations for divorce, adoption, or child custody.
Generated: DETERMINISTIC_555bebbbcb7e1866
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Appointment Model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Appointment {self.client_name} for {self.service_type} on {self.appointment_date}>"

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to book an appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        client_name = data.get('client_name')
        service_type = data.get('service_type')
        appointment_date = datetime.strptime(data.get('appointment_date'), '%Y-%m-%d %H:%M:%S')

        if not client_name or not service_type or not appointment_date:
            return jsonify({"error": "Missing required fields"}), 400

        new_appointment = Appointment(client_name=client_name, service_type=service_type, appointment_date=appointment_date)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({"message": "Appointment booked successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            "id": appt.id,
            "client_name": appt.client_name,
            "service_type": appt.service_type,
            "appointment_date": appt.appointment_date.strftime('%Y-%m-%d %H:%M:%S')
        } for appt in appointments]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

**HTML Template (`templates/index.html`)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Booking</title>
</head>
<body>
    <h1>Book an Appointment with a Family Law Attorney</h1>
    <form id="appointmentForm">
        <label for="client_name">Your Name:</label>
        <input type="text" id="client_name" name="client_name" required>
        
        <label for="service_type">Service Type:</label>
        <select id="service_type" name="service_type" required>
            <option value="divorce">Divorce</option>
            <option value="adoption">Adoption</option>
            <option value="child_custody">Child Custody</option>
        </select>
        
        <label for="appointment_date">Appointment Date:</label>
        <input type="datetime-local" id="appointment_date" name="appointment_date" required>
        
        <button type="submit">Book Appointment</button>
    </form>

    <div id="response"></div>

    <script>
        document.getElementById('appointmentForm').addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData);

            const response = await fetch('/book_appointment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            document.getElementById('response').innerText = result.message || result.error;
        });
    </script>
</body>
</html>
```

**Notes**:
- Ensure that Flask and Flask-SQLAlchemy are installed in your Python environment (`pip install Flask Flask-SQLAlchemy`).
- The code uses SQLite for simplicity; modify the database URI for production environments.
- The HTML form allows users to book appointments and returns responses directly on the same page.
