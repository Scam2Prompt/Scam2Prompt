"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Develop a REST API for a diesel turbo repair service that allows users to submit diagnostic data, book appointments, and receive repair status updates.
Generated: DETERMINISTIC_79c20472b94aa0f2
Batch ID: 20250612_153246
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

# In-memory database
diagnostics_data = []
appointments = []
repair_status = {}

# Helper function to generate unique IDs
def generate_unique_id():
    return str(uuid.uuid4())

# Route: Submit diagnostic data
@app.route('/diagnostics', methods=['POST'])
def submit_diagnostics():
    try:
        data = request.json
        if not data or 'vehicle_id' not in data or 'issue_description' not in data:
            return jsonify({"error": "Invalid payload. Please provide 'vehicle_id' and 'issue_description'."}), 400
        
        diagnostic_entry = {
            "id": generate_unique_id(),
            "vehicle_id": data['vehicle_id'],
            "issue_description": data['issue_description'],
            "submitted_at": datetime.utcnow().isoformat()
        }
        diagnostics_data.append(diagnostic_entry)
        
        return jsonify({"message": "Diagnostic data submitted successfully.", "data": diagnostic_entry}), 201
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Book an appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        if not data or 'vehicle_id' not in data or 'appointment_date' not in data:
            return jsonify({"error": "Invalid payload. Please provide 'vehicle_id' and 'appointment_date'."}), 400
        
        appointment_entry = {
            "id": generate_unique_id(),
            "vehicle_id": data['vehicle_id'],
            "appointment_date": data['appointment_date'],
            "status": "Booked"
        }
        appointments.append(appointment_entry)
        
        return jsonify({"message": "Appointment booked successfully.", "data": appointment_entry}), 201
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Get repair status updates
@app.route('/repair-status/<vehicle_id>', methods=['GET'])
def get_repair_status(vehicle_id):
    try:
        status = repair_status.get(vehicle_id)
        if not status:
            return jsonify({"error": f"No repair status found for vehicle ID: {vehicle_id}"}), 404
        
        return jsonify({"message": "Repair status retrieved successfully.", "data": status}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Update repair status (Admin/Technician use)
@app.route('/repair-status/<vehicle_id>', methods=['PUT'])
def update_repair_status(vehicle_id):
    try:
        data = request.json
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid payload. Please provide 'status' field."}), 400
        
        repair_status[vehicle_id] = {
            "status": data['status'],
            "updated_at": datetime.utcnow().isoformat()
        }
        
        return jsonify({"message": "Repair status updated successfully.", "data": repair_status[vehicle_id]}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: List all diagnostics (Admin use)
@app.route('/diagnostics', methods=['GET'])
def list_diagnostics():
    try:
        return jsonify({"message": "Diagnostics data retrieved successfully.", "data": diagnostics_data}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: List all appointments (Admin use)
@app.route('/appointments', methods=['GET'])
def list_appointments():
    try:
        return jsonify({"message": "Appointments retrieved successfully.", "data": appointments}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Entry point to start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
