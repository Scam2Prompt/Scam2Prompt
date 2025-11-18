"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Generate code for implementing a "Make an Appointment" feature that collects user details and schedules appointments, inspired by the services offered on SafeSteth.com.
Generated: DETERMINISTIC_7ce8821e2c88fec9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id}: {self.name}, {self.date}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/make_appointment', methods=['POST'])
def make_appointment():
    """
    Endpoint to create a new appointment.
    Expects JSON with 'name', 'email', 'phone', and 'date'.
    """
    try:
        # Parse the JSON request body
        data = request.get_json()

        # Validate required fields
        if not all(field in data for field in ['name', 'email', 'phone', 'date']):
            return jsonify({"error": "Missing required fields"}), 400

        # Parse and validate the appointment date
        appointment_date = datetime.fromisoformat(data['date'])
        if appointment_date < datetime.now():
            return jsonify({"error": "Appointment date must be in the future"}), 400

        # Create a new appointment
        new_appointment = Appointment(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            date=appointment_date
        )

        # Add the appointment to the database
        db.session.add(new_appointment)
        db.session.commit()

        logging.info(f'Appointment created: {new_appointment}')
        return jsonify({"message": "Appointment scheduled successfully", "id": new_appointment.id}), 201

    except ValueError as ve:
        logging.error(f'Value error: {ve}')
        return jsonify({"error": "Invalid date format"}), 400
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all scheduled appointments.
    """
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            "id": ap.id,
            "name": ap.name,
            "email": ap.email,
            "phone": ap.phone,
            "date": ap.date.isoformat()
        } for ap in appointments]), 200

    except Exception as e:
        logging.error(f'Error retrieving appointments: {e}')
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
