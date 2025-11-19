"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labvidadourados.com.br
Prompt: Create a RESTful API endpoint that enables users to schedule a home blood collection service, ensuring data validation for patient information.
Generated: DETERMINISTIC_424a4340e44f0d31
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# In-memory storage for demonstration purposes (not production-ready)
appointments = []

# Utility function to validate patient information
def validate_patient_info(data):
    errors = []
    # Validate name (must be non-empty and alphabetic)
    if not data.get('name') or not re.fullmatch(r'[A-Za-z ]+', data['name']):
        errors.append("Invalid name. Name must contain only letters and spaces.")
    
    # Validate contact number (10-digit numeric string)
    if not data.get('contact_number') or not re.fullmatch(r'\d{10}', data['contact_number']):
        errors.append("Invalid contact number. Must be a 10-digit numeric string.")
    
    # Validate email (basic email pattern check)
    if not data.get('email') or not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', data['email']):
        errors.append("Invalid email address.")
    
    # Validate preferred collection date (must be a valid future date)
    try:
        preferred_date = datetime.strptime(data.get('preferred_date', ''), '%Y-%m-%d')
        if preferred_date <= datetime.now():
            errors.append("Preferred date must be in the future.")
    except ValueError:
        errors.append("Invalid preferred date format. Use YYYY-MM-DD.")
    
    return errors

@app.route('/schedule', methods=['POST'])
def schedule_service():
    """
    API endpoint to schedule a home blood collection service.
    Expects patient information and preferred collection date.
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        # Validate patient information
        validation_errors = validate_patient_info(data)
        if validation_errors:
            return jsonify({"errors": validation_errors}), 400
        
        # Create appointment record
        appointment = {
            "id": len(appointments) + 1,  # Simple ID generation
            "name": data['name'],
            "contact_number": data['contact_number'],
            "email": data['email'],
            "preferred_date": data['preferred_date'],
            "status": "Scheduled"
        }
        appointments.append(appointment)
        
        return jsonify({"message": "Appointment successfully scheduled", "appointment": appointment}), 201
    
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
