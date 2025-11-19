"""
Generated Code Metadata:
========================
Original URL: https://drivemiami.com
Prompt: Create a web application that allows users to schedule service appointments and inquire about parts availability, leveraging the "Website Integrated Apps" functionality mentioned on DriveCities.
Generated: DETERMINISTIC_857e2896d56934c0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.name} on {self.service_date}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to schedule an appointment
@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    try:
        data = request.json
        name = data.get('name')
        service_date = datetime.strptime(data.get('service_date'), '%Y-%m-%d %H:%M:%S')
        service_type = data.get('service_type')

        # Validate input
        if not name or not service_date or not service_type:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new appointment
        new_appointment = Appointment(name=name, service_date=service_date, service_type=service_type)
        db.session.add(new_appointment)
        db.session.commit()

        logging.info(f'Appointment scheduled: {new_appointment}')
        return jsonify({'message': 'Appointment scheduled successfully'}), 201

    except Exception as e:
        logging.error(f'Error scheduling appointment: {e}')
        return jsonify({'error': 'An error occurred while scheduling the appointment'}), 500

# Route to inquire about parts availability
@app.route('/parts_availability', methods=['GET'])
def parts_availability():
    # Simulated parts availability data
    parts_data = {
        'brake pads': True,
        'oil filter': False,
        'spark plugs': True
    }
    return jsonify(parts_data)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Appointment Scheduler</title>
</head>
<body>
    <h1>Schedule a Service Appointment</h1>
    <form id="appointmentForm">
        <label for="name">Your Name:</label>
        <input type="text" id="name" required>
        <br>
        <label for="service_date">Service Date (YYYY-MM-DD HH:MM:SS):</label>
        <input type="text" id="service_date" required>
        <br>
        <label for="service_type">Service Type:</label>
        <input type="text" id="service_type" required>
        <br>
        <button type="submit">Schedule Appointment</button>
    </form>

    <h2>Check Parts Availability</h2>
    <button id="checkParts">Check Availability</button>
    <div id="partsResult"></div>

    <script>
        document.getElementById('appointmentForm').onsubmit = async function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const service_date = document.getElementById('service_date').value;
            const service_type = document.getElementById('service_type').value;

            const response = await fetch('/schedule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, service_date, service_type })
            });

            const result = await response.json();
            alert(result.message || result.error);
        };

        document.getElementById('checkParts').onclick = async function() {
            const response = await fetch('/parts_availability');
            const parts = await response.json();
            document.getElementById('partsResult').innerText = JSON.stringify(parts, null, 2);
        };
    </script>
</body>
</html>
```
