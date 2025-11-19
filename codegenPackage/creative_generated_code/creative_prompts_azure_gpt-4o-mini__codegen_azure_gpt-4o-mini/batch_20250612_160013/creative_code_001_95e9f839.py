"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crypto-io.com
Prompt: Write a code snippet for a web application that allows users to find and book appointments at barbershops across the country, inspired by the services offered by Gould Barbers.
Generated: DETERMINISTIC_95e9f8399c599c26
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///appointments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barber_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Appointment {self.id}>'

# Route to create a new appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    try:
        # Parse request data
        data = request.get_json()
        barber_id = data.get('barber_id')
        user_name = data.get('user_name')
        appointment_time = data.get('appointment_time')

        # Validate input
        if not barber_id or not user_name or not appointment_time:
            return jsonify({"error": "Missing required fields"}), 400

        # Convert appointment_time to datetime object
        appointment_time = datetime.fromisoformat(appointment_time)
        
        # Check if appointment time is in the future
        if appointment_time <= datetime.utcnow():
            return jsonify({"error": "Appointment time must be in the future"}), 400

        # Create a new appointment
        new_appointment = Appointment(barber_id=barber_id, user_name=user_name, appointment_time=appointment_time)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({"message": "Appointment booked successfully", "appointment_id": new_appointment.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        result = [
            {
                "id": app.id,
                "barber_id": app.barber_id,
                "user_name": app.user_name,
                "appointment_time": app.appointment_time.isoformat(),
                "created_at": app.created_at.isoformat()
            } for app in appointments
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the environment variable `DATABASE_URL` to your preferred database.
