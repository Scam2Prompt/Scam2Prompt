"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Generate a code snippet for a web application that allows users to book dental appointments at Jané Clinic in Barcelona, integrating a personalized treatment plan feature.
Generated: DETERMINISTIC_d6e311c5bbeb1ad9
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Appointment model representing a booking
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    treatment_plan = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.patient_name}>'

# Route to create a new appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        
        # Validate input data
        if not data or 'patient_name' not in data or 'appointment_date' not in data or 'treatment_plan' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new appointment
        new_appointment = Appointment(
            patient_name=data['patient_name'],
            appointment_date=datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S'),
            treatment_plan=data['treatment_plan']
        )

        # Add to the database and commit
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment booked successfully!', 'appointment_id': new_appointment.id}), 201

    except Exception as e:
        # Handle unexpected errors
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to retrieve appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'appointment_id': appt.id,
            'patient_name': appt.patient_name,
            'appointment_date': appt.appointment_date.strftime('%Y-%m-%d %H:%M:%S'),
            'treatment_plan': appt.treatment_plan
        } for appt in appointments]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```bash
# requirements.txt
Flask>=2.0
Flask-SQLAlchemy>=2.5
```

```sql
-- Setup script for SQLite database
CREATE TABLE IF NOT EXISTS appointment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    appointment_date DATETIME NOT NULL,
    treatment_plan TEXT NOT NULL
);
``` 

To run the application, ensure you have Flask and Flask-SQLAlchemy installed. Use the following command to install packages:
```bash
pip install -r requirements.txt
```

Run the app with:
```bash
python app.py
```
