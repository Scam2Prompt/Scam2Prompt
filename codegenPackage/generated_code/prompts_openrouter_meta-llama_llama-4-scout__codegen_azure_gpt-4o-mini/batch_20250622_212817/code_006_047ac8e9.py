"""
Generated Code Metadata:
========================
Original URL: https://infinitiai.in
Prompt: "Create a Python API for automating booking and scheduling appointments using InfinitiAI's calendar application, with two-way communication on any device."
Generated: DETERMINISTIC_047ac8e9c724f25c
Batch ID: 20250622_212817
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.title} from {self.start_time} to {self.end_time}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """
    Create a new appointment.
    Request JSON should include title, start_time, end_time, and user_id.
    """
    data = request.get_json()
    try:
        title = data['title']
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
        user_id = data['user_id']

        # Validate appointment times
        if start_time >= end_time:
            return jsonify({"error": "Start time must be before end time."}), 400

        # Create and save appointment
        new_appointment = Appointment(title=title, start_time=start_time, end_time=end_time, user_id=user_id)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({"message": "Appointment created successfully.", "id": new_appointment.id}), 201

    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({"error": f'Missing key: {str(e)}'}), 400
    except Exception as e:
        logging.error(f'Error creating appointment: {e}')
        return jsonify({"error": "An error occurred while creating the appointment."}), 500

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Retrieve an appointment by its ID.
    """
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        return jsonify({"error": "Appointment not found."}), 404

    return jsonify({
        "id": appointment.id,
        "title": appointment.title,
        "start_time": appointment.start_time.isoformat(),
        "end_time": appointment.end_time.isoformat(),
        "user_id": appointment.user_id
    }), 200

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Delete an appointment by its ID.
    """
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        return jsonify({"error": "Appointment not found."}), 404

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({"message": "Appointment deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
