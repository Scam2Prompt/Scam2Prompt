"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Develop a RESTful API endpoint that allows users to book appointments with specialists for custom projects related to windows and doors in the Oise region.
Generated: DETERMINISTIC_2d99dc985b5b133d
Batch ID: 20250612_140107
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
import uuid

app = Flask(__name__)

# In-memory storage for appointments (simulation of database)
appointments = {}

# Available specialists (hardcoded for simplicity)
specialists = [
    {"id": "1", "name": "Alice", "specialty": "Windows"},
    {"id": "2", "name": "Bob", "specialty": "Doors"}
]

@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment with a specialist.
    Request payload should include:
    - user_name: Name of the user booking the appointment
    - user_email: Email of the user booking the appointment
    - specialist_id: ID of the specialist
    - project_details: Description of the project
    - appointment_date: Desired appointment date in the format 'YYYY-MM-DD'
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        
        # Validate the required fields
        required_fields = ['user_name', 'user_email', 'specialist_id', 'project_details', 'appointment_date']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Validate appointment date
        try:
            appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d').date()
            if appointment_date < datetime.now().date():
                return jsonify({"error": "Appointment date must be in the future"}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Expected YYYY-MM-DD"}), 400
        
        # Validate specialist ID
        specialist = next((s for s in specialists if s['id'] == data['specialist_id']), None)
        if not specialist:
            return jsonify({"error": "Invalid specialist ID"}), 404
        
        # Generate a unique appointment ID
        appointment_id = str(uuid.uuid4())
        
        # Store the appointment in memory
        appointments[appointment_id] = {
            "appointment_id": appointment_id,
            "user_name": data['user_name'],
            "user_email": data['user_email'],
            "specialist_id": data['specialist_id'],
            "specialist_name": specialist['name'],
            "project_details": data['project_details'],
            "appointment_date": appointment_date.strftime('%Y-%m-%d'),
            "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Return success response
        return jsonify({"message": "Appointment booked successfully", "appointment_id": appointment_id}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while booking the appointment", "details": str(e)}), 500

@app.route('/api/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Endpoint to retrieve the details of a specific appointment by ID.
    """
    appointment = appointments.get(appointment_id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify(appointment)

@app.route('/api/specialists', methods=['GET'])
def list_specialists():
    """
    Endpoint to list all available specialists.
    """
    return jsonify(specialists)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
