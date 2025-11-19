"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Generate a code snippet for an API that schedules HVAC service appointments, incorporating features like 24/7 availability and priority service for Comfort Club members as described on RJW Mechanical's website.
Generated: DETERMINISTIC_e7a68e98573148b9
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Simulated database for appointments and Comfort Club members
appointments = []
comfort_club_members = {"john_doe@example.com", "jane_smith@example.com"}  # Example members

# Error messages
ERROR_MESSAGES = {
    "invalid_data": "Invalid request data provided.",
    "conflict": "Appointment time conflict. Please choose another time."
}


def is_time_available(time):
    """
    Check if the requested appointment time is available.
    """
    for appointment in appointments:
        if appointment["time"] == time:
            return False
    return True


@app.route("/schedule", methods=["POST"])
def schedule_appointment():
    """
    API endpoint to schedule an HVAC service appointment.
    Handles 24/7 availability and prioritizes Comfort Club members.
    """
    try:
        # Extract data from request
        data = request.json
        email = data.get("email")
        requested_time = data.get("time")

        # Validate input
        if not email or not requested_time:
            return jsonify({"error": ERROR_MESSAGES["invalid_data"]}), 400

        # Convert requested_time to datetime
        try:
            requested_time = datetime.strptime(requested_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid time format. Use YYYY-MM-DD HH:MM:SS"}), 400

        # Check if requested time is available
        if not is_time_available(requested_time):
            return jsonify({"error": ERROR_MESSAGES["conflict"]}), 409

        # Determine priority based on Comfort Club membership
        priority = email in comfort_club_members

        # Create new appointment
        new_appointment = {
            "email": email,
            "time": requested_time,
            "priority": priority
        }
        appointments.append(new_appointment)

        # Sort appointments to ensure priority members are handled first
        appointments.sort(key=lambda x: (not x["priority"], x["time"]))

        return jsonify({"message": "Appointment scheduled successfully.", "appointment": new_appointment}), 201
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/appointments", methods=["GET"])
def get_appointments():
    """
    Fetch all scheduled appointments.
    """
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
