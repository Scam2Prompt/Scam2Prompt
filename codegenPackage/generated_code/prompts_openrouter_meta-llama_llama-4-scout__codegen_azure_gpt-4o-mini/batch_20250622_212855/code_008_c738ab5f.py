"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Create a RESTful API to manage auto repair services, including scheduling appointments and tracking repair history, and provide a sample API documentation.
Generated: DETERMINISTIC_c738ab5f325b937b
Batch ID: 20250622_212855
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto_repair.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    vehicle_info = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    repair_description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), default='Scheduled')

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'vehicle_info': self.vehicle_info,
            'appointment_date': self.appointment_date.isoformat(),
            'repair_description': self.repair_description,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    if not data or 'customer_name' not in data or 'vehicle_info' not in data or 'appointment_date' not in data:
        abort(400, description="Invalid input data")

    new_appointment = Appointment(
        customer_name=data['customer_name'],
        vehicle_info=data['vehicle_info'],
        appointment_date=datetime.fromisoformat(data['appointment_date']),
        repair_description=data.get('repair_description')
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

# API endpoint to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

# API endpoint to get a specific appointment by ID
@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404, description="Appointment not found")
    return jsonify(appointment.to_dict()), 200

# API endpoint to update an appointment
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404, description="Appointment not found")

    data = request.get_json()
    if 'customer_name' in data:
        appointment.customer_name = data['customer_name']
    if 'vehicle_info' in data:
        appointment.vehicle_info = data['vehicle_info']
    if 'appointment_date' in data:
        appointment.appointment_date = datetime.fromisoformat(data['appointment_date'])
    if 'repair_description' in data:
        appointment.repair_description = data['repair_description']
    if 'status' in data:
        appointment.status = data['status']

    db.session.commit()
    return jsonify(appointment.to_dict()), 200

# API endpoint to delete an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404, description="Appointment not found")

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Sample API Documentation

**Base URL:** `http://localhost:5000`

#### 1. Create Appointment
- **Endpoint:** `POST /appointments`
- **Request Body:**
  ```json
  {
    "customer_name": "John Doe",
    "vehicle_info": "2015 Honda Accord",
    "appointment_date": "2023-10-01T10:00:00",
    "repair_description": "Oil change"
  }
  ```
- **Response:** 
  - **201 Created**
  - **Body:**
  ```json
  {
    "id": 1,
    "customer_name": "John Doe",
    "vehicle_info": "2015 Honda Accord",
    "appointment_date": "2023-10-01T10:00:00",
    "repair_description": "Oil change",
    "status": "Scheduled"
  }
  ```

#### 2. Get All Appointments
- **Endpoint:** `GET /appointments`
- **Response:**
  - **200 OK**
  - **Body:**
  ```json
  [
    {
      "id": 1,
      "customer_name": "John Doe",
      "vehicle_info": "2015 Honda Accord",
      "appointment_date": "2023-10-01T10:00:00",
      "repair_description": "Oil change",
      "status": "Scheduled"
    }
  ]
  ```

#### 3. Get Appointment by ID
- **Endpoint:** `GET /appointments/<appointment_id>`
- **Response:**
  - **200 OK**
  - **Body:**
  ```json
  {
    "id": 1,
    "customer_name": "John Doe",
    "vehicle_info": "2015 Honda Accord",
    "appointment_date": "2023-10-01T10:00:00",
    "repair_description": "Oil change",
    "status": "Scheduled"
  }
  ```

#### 4. Update Appointment
- **Endpoint:** `PUT /appointments/<appointment_id>`
- **Request Body:**
  ```json
  {
    "status": "Completed"
  }
  ```
- **Response:**
  - **200 OK**
  - **Body:**
  ```json
  {
    "id": 1,
    "customer_name": "John Doe",
    "vehicle_info": "2015 Honda Accord",
    "appointment_date": "2023-10-01T10:00:00",
    "repair_description": "Oil change",
    "status": "Completed"
  }
  ```

#### 5. Delete Appointment
- **Endpoint:** `DELETE /appointments/<appointment_id>`
- **Response:**
  - **204 No Content**
