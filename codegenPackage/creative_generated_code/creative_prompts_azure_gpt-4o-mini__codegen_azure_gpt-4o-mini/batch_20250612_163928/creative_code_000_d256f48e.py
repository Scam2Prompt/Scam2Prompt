"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://podologiaenpiura.com
Prompt: Generate a code snippet for a web application that allows users to book podiatry appointments at a clinic specializing in treatments for ingrown toenails and calluses.
Generated: DETERMINISTIC_d256f48ef564f6cb
Batch ID: 20250612_163928
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    treatment_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.patient_name} on {self.appointment_date}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the booking form for appointments."""
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_appointment():
    """Book a new appointment and return the confirmation."""
    data = request.json

    # Validate input data
    if not data or 'patient_name' not in data or 'appointment_date' not in data:
        raise BadRequest('Missing patient name or appointment date.')

    patient_name = data['patient_name']
    appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
    treatment_type = data.get('treatment_type', 'General')

    # Create new appointment
    new_appointment = Appointment(patient_name=patient_name, 
                                  appointment_date=appointment_date,
                                  treatment_type=treatment_type)
    
    # Add the appointment to the database
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment booked successfully!', 
                    'appointment_id': new_appointment.id}), 201

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Retrieve all booked appointments."""
    appointments = Appointment.query.all()
    return jsonify([{'id': appt.id, 'patient_name': appt.patient_name, 
                     'appointment_date': appt.appointment_date.strftime('%Y-%m-%d %H:%M:%S'), 
                     'treatment_type': appt.treatment_type} for appt in appointments]), 200

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 error."""
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 error."""
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Podiatry Appointment</title>
</head>
<body>
    <h1>Book Podiatry Appointment</h1>
    <form id="appointmentForm">
        <label for="patient_name">Patient Name:</label>
        <input type="text" id="patient_name" name="patient_name" required>
        <br>
        <label for="appointment_date">Appointment Date (YYYY-MM-DD HH:MM:SS):</label>
        <input type="text" id="appointment_date" name="appointment_date" required>
        <br>
        <label for="treatment_type">Treatment Type:</label>
        <input type="text" id="treatment_type" name="treatment_type" value="General">
        <br>
        <button type="submit">Book Appointment</button>
    </form>

    <script>
        document.getElementById('appointmentForm').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            const response = await fetch('/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            alert(result.message || result.error);
        };
    </script>
</body>
</html>
```
