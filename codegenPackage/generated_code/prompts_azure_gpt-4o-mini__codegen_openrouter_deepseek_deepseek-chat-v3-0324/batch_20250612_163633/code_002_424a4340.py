"""
Generated Code Metadata:
========================
Original URL: https://labvidadourados.com.br
Prompt: Create a RESTful API endpoint that enables users to schedule a home blood collection service, ensuring data validation for patient information.
Generated: DETERMINISTIC_424a4340e44f0d31
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import re
from typing import Dict, Optional

app = Flask(__name__)

# In-memory storage for scheduled appointments (production would use a database)
appointments = []

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_patient_info(patient_data: Dict) -> Optional[str]:
    """
    Validate patient information according to business rules.
    Returns error message if validation fails, None otherwise.
    """
    if not isinstance(patient_data.get('name'), str) or not patient_data['name'].strip():
        return "Name is required and must be a non-empty string."
    
    if not isinstance(patient_data.get('date_of_birth'), str):
        return "Date of birth is required."
    
    try:
        dob = datetime.strptime(patient_data['date_of_birth'], '%Y-%m-%d')
        if dob > datetime.now():
            return "Date of birth cannot be in the future."
    except ValueError:
        return "Invalid date format for date of birth. Use YYYY-MM-DD."
    
    if not isinstance(patient_data.get('phone'), str) or not re.match(r'^\+?[0-9\s-]{10,15}$', patient_data['phone']):
        return "Valid phone number is required."
    
    if not isinstance(patient_data.get('email'), str) or not re.match(r'^[^@]+@[^@]+\.[^@]+$', patient_data['email']):
        return "Valid email address is required."
    
    return None

def validate_appointment_info(appointment_data: Dict) -> Optional[str]:
    """
    Validate appointment information according to business rules.
    Returns error message if validation fails, None otherwise.
    """
    if not isinstance(appointment_data.get('collection_date'), str):
        return "Collection date is required."
    
    try:
        collection_date = datetime.strptime(appointment_data['collection_date'], '%Y-%m-%d %H:%M')
        if collection_date < datetime.now():
            return "Collection date must be in the future."
    except ValueError:
        return "Invalid datetime format for collection date. Use YYYY-MM-DD HH:MM."
    
    if not isinstance(appointment_data.get('test_type'), str) or not appointment_data['test_type'].strip():
        return "Test type is required."
    
    return None

@app.route('/api/appointments', methods=['POST'])
def schedule_appointment():
    """
    Endpoint to schedule a blood collection appointment.
    Accepts JSON with patient and appointment details.
    Returns appointment ID if successful, error otherwise.
    """
    try:
        data = request.get_json()
        if not data:
            raise ValidationError("Request body must be JSON.")
        
        # Validate required fields exist
        if 'patient' not in data or 'appointment' not in data:
            raise ValidationError("Both 'patient' and 'appointment' objects are required.")
        
        # Validate patient information
        patient_error = validate_patient_info(data['patient'])
        if patient_error:
            raise ValidationError(patient_error)
        
        # Validate appointment information
        appointment_error = validate_appointment_info(data['appointment'])
        if appointment_error:
            raise ValidationError(appointment_error)
        
        # Create appointment (in production, this would save to a database)
        appointment_id = len(appointments) + 1
        appointment = {
            'id': appointment_id,
            'patient': data['patient'],
            'appointment': data['appointment'],
            'created_at': datetime.now().isoformat(),
            'status': 'scheduled'
        }
        appointments.append(appointment)
        
        return jsonify({
            'status': 'success',
            'message': 'Appointment scheduled successfully.',
            'appointment_id': appointment_id
        }), 201
    
    except ValidationError as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'An unexpected error occurred.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
```
