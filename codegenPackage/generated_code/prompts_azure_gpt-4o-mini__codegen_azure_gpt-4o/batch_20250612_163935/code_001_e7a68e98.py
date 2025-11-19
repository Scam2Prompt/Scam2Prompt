"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Generate a code snippet for an API that schedules HVAC service appointments, incorporating features like 24/7 availability and priority service for Comfort Club members as described on RJW Mechanical's website.
Generated: DETERMINISTIC_e7a68e98573148b9
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock database for storing appointments and user information
appointments = []
users = {
    "john_doe": {"membership": "Comfort Club"},
    "jane_smith": {"membership": "Standard"},
}

# Helper function to check membership priority
def is_comfort_club_member(username):
    user = users.get(username)
    return user and user.get("membership") == "Comfort Club"

# Helper function to find the next available appointment slot
def find_next_available_slot(priority=False):
    now = datetime.now()
    # Priority members get the next available slot within 24 hours
    if priority:
        return now + timedelta(hours=1)
    # Standard members get the next available slot within 48 hours
    return now + timedelta(hours=48)

@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    """
    API endpoint to schedule an HVAC service appointment.
    Request JSON format:
    {
        "username": "john_doe",
        "service_type": "HVAC Repair"
    }
    """
    try:
        # Parse request data
        data = request.json
        username = data.get("username")
        service_type = data.get("service_type")

        if not username or not service_type:
            return jsonify({"error": "Missing required fields: username or service_type"}), 400

        # Check if user is a Comfort Club member
        priority = is_comfort_club_member(username)

        # Find the next available appointment slot
        appointment_time = find_next_available_slot(priority)

        # Create appointment record
        appointment = {
            "username": username,
            "service_type": service_type,
            "appointment_time": appointment_time.strftime("%Y-%m-%d %H:%M:%S"),
            "priority": priority
        }
        appointments.append(appointment)

        return jsonify({
            "message": "Appointment scheduled successfully",
            "appointment": appointment
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    API endpoint to retrieve all scheduled appointments.
    """
    return jsonify({"appointments": appointments}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
