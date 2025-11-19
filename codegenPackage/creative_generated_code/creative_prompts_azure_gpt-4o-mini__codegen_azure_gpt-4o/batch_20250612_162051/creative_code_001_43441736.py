"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Generate a code snippet for a web application that allows users to schedule appliance repairs, referencing the services provided by Felipe Muñoz Reparaciones in Murcia.
Generated: DETERMINISTIC_434417369c6f14ff
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Mock data for services provided by Felipe Muñoz Reparaciones
SERVICES = [
    {"id": 1, "name": "Refrigerator Repair", "description": "Repair of all brands and models"},
    {"id": 2, "name": "Washing Machine Repair", "description": "Fixing issues like leaks, noise, and spin failure"},
    {"id": 3, "name": "Microwave Repair", "description": "Repair for heating problems and other faults"},
]

# Mock schedule database
REPAIR_SCHEDULE = []

# Endpoint to fetch available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Fetch and return the list of repair services.
    """
    return jsonify({"services": SERVICES}), 200

# Endpoint to schedule a repair
@app.route('/schedule', methods=['POST'])
def schedule_repair():
    """
    Schedule a repair for an appliance.
    Request JSON format:
    {
        "customer_name": "John Doe",
        "contact_info": "john.doe@example.com",
        "service_id": 1,
        "preferred_date": "2023-11-01"
    }
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate request data
        customer_name = data.get("customer_name")
        contact_info = data.get("contact_info")
        service_id = data.get("service_id")
        preferred_date = data.get("preferred_date")

        if not customer_name or not contact_info or not service_id or not preferred_date:
            return jsonify({"error": "All fields are required"}), 400

        # Check if service ID is valid
        service = next((s for s in SERVICES if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Invalid service ID"}), 400

        # Validate preferred date format
        try:
            preferred_date_obj = datetime.strptime(preferred_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Add repair schedule to mock database
        schedule_id = len(REPAIR_SCHEDULE) + 1
        REPAIR_SCHEDULE.append({
            "id": schedule_id,
            "customer_name": customer_name,
            "contact_info": contact_info,
            "service": service,
            "preferred_date": preferred_date_obj.strftime("%Y-%m-%d"),
        })

        # Return success response
        return jsonify({"message": f"Repair scheduled successfully with ID {schedule_id}"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Endpoint to view scheduled repairs
@app.route('/scheduled', methods=['GET'])
def view_scheduled_repairs():
    """
    Fetch and return all the scheduled repairs.
    """
    return jsonify({"scheduled_repairs": REPAIR_SCHEDULE}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
