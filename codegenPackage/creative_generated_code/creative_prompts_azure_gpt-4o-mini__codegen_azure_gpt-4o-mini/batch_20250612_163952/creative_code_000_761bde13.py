"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.martingodwinequine.com
Prompt: Write a code snippet for a web application that allows users to request personalized equine care appointments, similar to the services offered by Martin Godwin Equine Services.
Generated: DETERMINISTIC_761bde13544d5a74
Batch ID: 20250612_163952
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
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI - SQLite for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equine_care.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    horse_breed = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.name}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to request an appointment
@app.route('/api/appointments', methods=['POST'])
def request_appointment():
    # Get JSON data from request
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('name', 'email', 'horse_breed', 'appointment_date')):
        return jsonify({'error': 'All fields are required!'}), 400

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({'error': 'Invalid email format!'}), 400
    
    try:
        # Parse the appointment date
        appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Invalid date format! Use YYYY-MM-DD HH:MM:SS'}), 400

    # Create new appointment instance
    new_appointment = Appointment(
        name=data['name'],
        email=data['email'],
        horse_breed=data['horse_breed'],
        appointment_date=appointment_date,
        notes=data.get('notes', '')
    )

    # Save the appointment to the database
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment requested successfully!', 'id': new_appointment.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
