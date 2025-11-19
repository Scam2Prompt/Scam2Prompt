"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Develop a REST API for a cleaning service company that allows users to book cleaning appointments, specify their location (e.g., Spotsylvania or Locust Grove), and select a cleaning package.
Generated: DETERMINISTIC_af8f457f445fd0eb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    package = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'package': self.package,
            'appointment_time': self.appointment_time.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to book a cleaning appointment
@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    try:
        # Get data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'location' not in data or 'package' not in data or 'appointment_time' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new appointment
        new_appointment = Appointment(
            location=data['location'],
            package=data['package'],
            appointment_time=datetime.fromisoformat(data['appointment_time'])
        )

        # Add the appointment to the database
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify(new_appointment.to_dict()), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to get all appointments
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    try:
        # Retrieve all appointments from the database
        appointments = Appointment.query.all()
        return jsonify([appointment.to_dict() for appointment in appointments]), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
