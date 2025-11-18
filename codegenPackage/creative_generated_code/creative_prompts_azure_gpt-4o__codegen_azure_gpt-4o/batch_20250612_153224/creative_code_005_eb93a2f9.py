"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Develop an API for scheduling home service appointments, including options for cleaning, insulation, and leakage detection, based on شركة انجاز's service categories.
Generated: DETERMINISTIC_eb93a2f983f7da84
Batch ID: 20250612_153224
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for appointments (replace with a database in production)
appointments = []

# Supported services
SERVICE_CATEGORIES = ["cleaning", "insulation", "leakage_detection"]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = jsonify({"error": e.name, "message": e.description})
    response.status_code = e.code
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    response = jsonify({"error": "Internal Server Error", "message": str(e)})
    response.status_code = 500
    return response

@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    """
    Endpoint to schedule a home service appointment.
    Expects JSON data with the following structure:
    {
        "name": "Customer Name",
        "service": "cleaning",  # One of the SERVICE_CATEGORIES
        "date": "YYYY-MM-DD",
        "time": "HH:MM"
    }
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        
        # Validate required fields
        if not all(field in data for field in ["name", "service", "date", "time"]):
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400
        
        # Extract and validate service category
        service = data["service"]
        if service not in SERVICE_CATEGORIES:
            return jsonify({"error": "Bad Request", "message": f"Invalid service. Supported services are: {SERVICE_CATEGORIES}"}), 400
        
        # Validate date and time format
        try:
            appointment_date = datetime.strptime(data["date"], "%Y-%m-%d").date()
            appointment_time = datetime.strptime(data["time"], "%H:%M").time()
        except ValueError:
            return jsonify({"error": "Bad Request", "message": "Invalid date or time format"}), 400
        
        # Create appointment object
        appointment = {
            "id": len(appointments) + 1,
            "name": data["name"],
            "service": service,
            "date": appointment_date.isoformat(),
            "time": appointment_time.isoformat()
        }
        
        # Add to storage
        appointments.append(appointment)
        
        return jsonify({"message": "Appointment scheduled successfully", "appointment": appointment}), 201
    except Exception as e:
        return handle_exception(e)

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all scheduled appointments.
    Returns a JSON list of all appointments.
    """
    return jsonify({"appointments": appointments}), 200

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Endpoint to retrieve a specific appointment by ID.
    """
    appointment = next((a for a in appointments if a["id"] == appointment_id), None)
    if not appointment:
        return jsonify({"error": "Not Found", "message": "Appointment not found"}), 404
    return jsonify({"appointment": appointment}), 200

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Endpoint to delete a specific appointment by ID.
    """
    global appointments
    appointment = next((a for a in appointments if a["id"] == appointment_id), None)
    if not appointment:
        return jsonify({"error": "Not Found", "message": "Appointment not found"}), 404
    
    appointments = [a for a in appointments if a["id"] != appointment_id]
    return jsonify({"message": "Appointment deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
