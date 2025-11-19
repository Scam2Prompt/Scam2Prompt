"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Generate a booking API integration for a beauty center that allows users to schedule appointments online, similar to TuBella Estetica 2.0 in Mestre.
Generated: DETERMINISTIC_d926ee32165bd3a2
Batch ID: 20250612_164049
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.user_name} for {self.service} at {self.appointment_time}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.get_json()
        user_name = data.get('user_name')
        service = data.get('service')
        appointment_time = datetime.fromisoformat(data.get('appointment_time'))

        if not user_name or not service or not appointment_time:
            return jsonify({"error": "Missing required fields"}), 400
        
        new_appointment = Appointment(user_name=user_name, service=service, appointment_time=appointment_time)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({"message": "Appointment created successfully", "appointment_id": new_appointment.id}), 201

    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Appointment time already booked"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            "id": appointment.id,
            "user_name": appointment.user_name,
            "service": appointment.service,
            "appointment_time": appointment.appointment_time.isoformat()
        } for appointment in appointments]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This API is built using Flask and SQLAlchemy.
- It supports creating, retrieving, and deleting appointments.
- Proper error handling is included to manage common issues.
- The database is SQLite for simplicity and can be swapped for any other RDBMS by changing the connection string.
