"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Create a RESTful API to manage auto repair services, including scheduling appointments and tracking repair history, and provide a sample API documentation.
Generated: DETERMINISTIC_c738ab5f325b937b
Batch ID: 20250622_212855
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
import uuid

app = Flask(__name__)

# In-memory database for simplicity
appointments = {}
repair_history = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route: Schedule an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    """
    Schedule a new auto repair appointment.
    Request JSON format:
    {
        "customer_name": "John Doe",
        "vehicle_model": "Toyota Camry",
        "appointment_date": "2023-10-15",
        "issue_description": "Engine noise"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        # Validate required fields
        required_fields = ["customer_name", "vehicle_model", "appointment_date", "issue_description"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Parse and validate appointment date
        try:
            appointment_date = datetime.strptime(data["appointment_date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create appointment
        appointment_id = generate_id()
        appointments[appointment_id] = {
            "id": appointment_id,
            "customer_name": data["customer_name"],
            "vehicle_model": data["vehicle_model"],
            "appointment_date": appointment_date.strftime("%Y-%m-%d"),
            "issue_description": data["issue_description"]
        }

        return jsonify({"message": "Appointment scheduled successfully", "appointment": appointments[appointment_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Retrieve all scheduled appointments.
    """
    return jsonify({"appointments": list(appointments.values())}), 200

# Route: Get appointment by ID
@app.route('/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Retrieve a specific appointment by ID.
    """
    appointment = appointments.get(appointment_id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify({"appointment": appointment}), 200

# Route: Add repair history
@app.route('/repair-history', methods=['POST'])
def add_repair_history():
    """
    Add a repair record to the history.
    Request JSON format:
    {
        "appointment_id": "12345",
        "repair_details": "Replaced engine belt",
        "repair_date": "2023-10-16",
        "cost": 250.00
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        # Validate required fields
        required_fields = ["appointment_id", "repair_details", "repair_date", "cost"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Check if appointment exists
        appointment = appointments.get(data["appointment_id"])
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404

        # Parse and validate repair date
        try:
            repair_date = datetime.strptime(data["repair_date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Add repair history
        repair_id = generate_id()
        repair_history[repair_id] = {
            "id": repair_id,
            "appointment_id": data["appointment_id"],
            "repair_details": data["repair_details"],
            "repair_date": repair_date.strftime("%Y-%m-%d"),
            "cost": data["cost"]
        }

        return jsonify({"message": "Repair history added successfully", "repair_record": repair_history[repair_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get repair history
@app.route('/repair-history', methods=['GET'])
def get_repair_history():
    """
    Retrieve all repair history records.
    """
    return jsonify({"repair_history": list(repair_history.values())}), 200

# Route: Get repair history by ID
@app.route('/repair-history/<repair_id>', methods=['GET'])
def get_repair_record(repair_id):
    """
    Retrieve a specific repair history record by ID.
    """
    repair_record = repair_history.get(repair_id)
    if not repair_record:
        return jsonify({"error": "Repair record not found"}), 404
    return jsonify({"repair_record": repair_record}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Sample API Documentation

#### Endpoints

1. **POST /appointments**
   - **Description**: Schedule a new auto repair appointment.
   - **Request Body**:
     ```json
     {
         "customer_name": "John Doe",
         "vehicle_model": "Toyota Camry",
         "appointment_date": "2023-10-15",
         "issue_description": "Engine noise"
     }
     ```
   - **Response**:
     - Success: `201 Created`
     - Error: `400 Bad Request`, `500 Internal Server Error`

2. **GET /appointments**
   - **Description**: Retrieve all scheduled appointments.
   - **Response**:
     - Success: `200 OK`
     - Error: `500 Internal Server Error`

3. **GET /appointments/<appointment_id>**
   - **Description**: Retrieve a specific appointment by ID.
   - **Response**:
     - Success: `200 OK`
     - Error: `404 Not Found`

4. **POST /repair-history**
   - **Description**: Add a repair record to the history.
   - **Request Body**:
     ```json
     {
         "appointment_id": "12345",
         "repair_details": "Replaced engine belt",
         "repair_date": "2023-10-16",
         "cost": 250.00
     }
     ```
   - **Response**:
     - Success: `201 Created`
     - Error: `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`

5. **GET /repair-history**
   - **Description**: Retrieve all repair history records.
   - **Response**:
     - Success: `200 OK`
     - Error: `500 Internal Server Error`

6. **GET /repair-history/<repair_id>**
   - **Description**: Retrieve a specific repair history record by ID.
   - **Response**:
     - Success: `200 OK`
     - Error: `404 Not Found`
```
