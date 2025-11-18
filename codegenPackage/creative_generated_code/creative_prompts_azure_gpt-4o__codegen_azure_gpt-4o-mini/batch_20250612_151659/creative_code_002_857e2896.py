"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Create a web application that allows users to schedule service appointments and inquire about parts availability, leveraging the "Website Integrated Apps" functionality mentioned on DriveCities.
Generated: DETERMINISTIC_857e2896d56934c0
Batch ID: 20250612_151659
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.customer_name} for {self.service_type}>'

# Define the Part model
class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Part {self.id} - {self.part_name} available: {self.available}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to schedule a service appointment
@app.route('/api/appointments', methods=['POST'])
def schedule_appointment():
    try:
        data = request.get_json()
        new_appointment = Appointment(
            customer_name=data['customer_name'],
            service_type=data['service_type'],
            appointment_date=datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
        )
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({"message": "Appointment scheduled successfully", "appointment_id": new_appointment.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to check part availability
@app.route('/api/parts/<int:part_id>', methods=['GET'])
def check_part_availability(part_id):
    try:
        part = Part.query.get(part_id)
        if part is None:
            return jsonify({"error": "Part not found"}), 404
        return jsonify({"part_name": part.part_name, "available": part.available}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Add a part (for demonstration purposes)
@app.route('/api/parts', methods=['POST'])
def add_part():
    try:
        data = request.get_json()
        new_part = Part(
            part_name=data['part_name'],
            available=data.get('available', True)
        )
        db.session.add(new_part)
        db.session.commit()
        return jsonify({"message": "Part added successfully", "part_id": new_part.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
