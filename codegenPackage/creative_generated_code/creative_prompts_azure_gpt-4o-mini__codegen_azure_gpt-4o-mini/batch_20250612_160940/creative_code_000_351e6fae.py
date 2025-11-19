"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Generate a code snippet for a web application that allows users to book appointments with legal and accounting professionals, similar to the services offered by Carthew Chau & Co.
Generated: DETERMINISTIC_351e6fae52901e08
Batch ID: 20250612_160940
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

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professional_type = db.Column(db.String(50), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.professional_type} - {self.client_name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/book', methods=['POST'])
def book_appointment():
    """Endpoint to book an appointment"""
    data = request.get_json()
    
    # Validate input data
    if not data or 'professional_type' not in data or 'client_name' not in data or 'appointment_date' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        # Parse appointment date
        appointment_date = datetime.fromisoformat(data['appointment_date'])
        
        # Create a new appointment
        new_appointment = Appointment(
            professional_type=data['professional_type'],
            client_name=data['client_name'],
            appointment_date=appointment_date
        )
        
        # Add to the session and commit
        db.session.add(new_appointment)
        db.session.commit()
        
        return jsonify({'message': 'Appointment booked successfully', 'appointment_id': new_appointment.id}), 201

    except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Endpoint to retrieve all appointments"""
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'id': appt.id,
            'professional_type': appt.professional_type,
            'client_name': appt.client_name,
            'appointment_date': appt.appointment_date.isoformat()
        } for appt in appointments]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the application
    app.run(debug=False)
```
