"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: How can I design a self-booking appointment system that filters out unqualified leads, based on the techniques shared by Client Fuel?
Generated: DETERMINISTIC_2084e75d8269e3de
Batch ID: 20250612_140403
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    qualified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Appointment {self.name} at {self.date_time}>"

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate phone number format
def is_valid_phone(phone):
    return len(phone) >= 10 and phone.isdigit()

# Endpoint to book an appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data or 'date_time' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    name = data['name']
    email = data['email']
    phone = data['phone']
    date_time_str = data['date_time']

    # Validate email and phone format
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    if not is_valid_phone(phone):
        return jsonify({"error": "Invalid phone number format"}), 400

    # Parse the date and time
    try:
        date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    except ValueError:
        return jsonify({"error": "Invalid date_time format, use 'YYYY-MM-DD HH:MM'"}), 400

    # Filter unqualified leads (example criteria)
    qualified = True  # Replace with actual qualification logic

    # Create and save the appointment
    new_appointment = Appointment(name=name, email=email, phone=phone, date_time=date_time, qualified=qualified)
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({"message": "Appointment booked successfully", "appointment_id": new_appointment.id}), 201

# Endpoint to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    result = [
        {
            "id": appt.id,
            "name": appt.name,
            "email": appt.email,
            "phone": appt.phone,
            "date_time": appt.date_time.strftime('%Y-%m-%d %H:%M'),
            "qualified": appt.qualified
        }
        for appt in appointments
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to install the required dependencies using:
```bash
pip install Flask Flask-SQLAlchemy
```
