"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payidarsaglik.com
Prompt: Create a RESTful API specification for a home healthcare service that includes endpoints for booking medical consultations and ambulance requests.
Generated: DETERMINISTIC_c09326e67a77d41c
Batch ID: 20250612_160526
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_service.db'
db = SQLAlchemy(app)

# Database model for medical consultations
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(50), nullable=False)
    doctor_name = db.Column(db.String(50), nullable=False)
    date_time = db.Column(db.String(50), nullable=False)  # e.g. "2023-10-01 14:30"
    status = db.Column(db.String(20), default='booked')

# Database model for ambulance requests
class AmbulanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(50), nullable=False)
    pickup_location = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    request_time = db.Column(db.String(50), nullable=False)  # e.g. "2023-10-01 14:30"
    status = db.Column(db.String(20), default='pending')

# Endpoint to book a medical consultation
@app.route('/api/consultations', methods=['POST'])
def book_consultation():
    """Book a new medical consultation."""
    data = request.json
    try:
        new_consultation = Consultation(
            patient_name=data['patient_name'],
            doctor_name=data['doctor_name'],
            date_time=data['date_time']
        )
        db.session.add(new_consultation)
        db.session.commit()
        return jsonify({'message': 'Consultation booked successfully!', 'consultation_id': new_consultation.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to retrieve all consultations
@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    """Retrieve all booked consultations."""
    consultations = Consultation.query.all()
    return jsonify([{'id': c.id, 'patient_name': c.patient_name, 'doctor_name': c.doctor_name, 'date_time': c.date_time, 'status': c.status} for c in consultations]), 200

# Endpoint to request an ambulance
@app.route('/api/ambulance_requests', methods=['POST'])
def request_ambulance():
    """Request a new ambulance service."""
    data = request.json
    try:
        new_request = AmbulanceRequest(
            patient_name=data['patient_name'],
            pickup_location=data['pickup_location'],
            destination=data['destination'],
            request_time=data['request_time']
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Ambulance requested successfully!', 'request_id': new_request.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to retrieve all ambulance requests
@app.route('/api/ambulance_requests', methods=['GET'])
def get_ambulance_requests():
    """Retrieve all ambulance requests."""
    requests = AmbulanceRequest.query.all()
    return jsonify([{'id': r.id, 'patient_name': r.patient_name, 'pickup_location': r.pickup_location, 'destination': r.destination, 'request_time': r.request_time, 'status': r.status} for r in requests]), 200

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': 'Bad request, please check the input data.'}), 400

if __name__ == '__main__':
    # Create the database tables if they don't exist
    db.create_all()
    app.run(debug=True)
```
