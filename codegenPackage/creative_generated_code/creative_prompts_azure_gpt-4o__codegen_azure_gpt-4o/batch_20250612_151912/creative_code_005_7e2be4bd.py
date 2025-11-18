"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Recommend an API to automate appointment scheduling for Majeli Avocat's legal services, with features for managing availability based on office hours (Monday to Friday, 9:00-12:30 and 14:00-18:00).
Generated: DETERMINISTIC_7e2be4bdab42b982
Batch ID: 20250612_151912
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

# Define the office hours
OFFICE_HOURS = {
    "Monday": {"start": "09:00", "end": "12:30", "afternoon_start": "14:00", "afternoon_end": "18:00"},
    "Tuesday": {"start": "09:00", "end": "12:30", "afternoon_start": "14:00", "afternoon_end": "18:00"},
    "Wednesday": {"start": "09:00", "end": "12:30", "afternoon_start": "14:00", "afternoon_end": "18:00"},
    "Thursday": {"start": "09:00", "end": "12:30", "afternoon_start": "14:00", "afternoon_end": "18:00"},
    "Friday": {"start": "09:00", "end": "12:30", "afternoon_start": "14:00", "afternoon_end": "18:00"},
}

# In-memory storage for scheduled appointments
appointments = []

# Helper function to validate if a datetime falls within office hours
def is_within_office_hours(datetime_obj):
    day_name = datetime_obj.strftime("%A")
    if day_name not in OFFICE_HOURS:
        return False

    hours = OFFICE_HOURS[day_name]
    morning_start = datetime.strptime(hours["start"], "%H:%M").time()
    morning_end = datetime.strptime(hours["end"], "%H:%M").time()
    afternoon_start = datetime.strptime(hours["afternoon_start"], "%H:%M").time()
    afternoon_end = datetime.strptime(hours["afternoon_end"], "%H:%M").time()

    appointment_time = datetime_obj.time()
    return (
        morning_start <= appointment_time <= morning_end or
        afternoon_start <= appointment_time <= afternoon_end
    )

# Route to schedule an appointment
@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    try:
        # Parse the request body
        data = request.json
        client_name = data.get("client_name")
        appointment_datetime_str = data.get("appointment_datetime")

        # Validate required fields
        if not client_name or not appointment_datetime_str:
            return jsonify({"error": "Missing required fields: client_name or appointment_datetime"}), 400

        # Convert string to datetime object
        appointment_datetime = datetime.strptime(appointment_datetime_str, "%Y-%m-%d %H:%M:%S")

        # Check if the appointment is within office hours
        if not is_within_office_hours(appointment_datetime):
            return jsonify({"error": "Appointment time is outside office hours"}), 400

        # Check for conflicting appointments
        for appointment in appointments:
            if appointment["appointment_datetime"] == appointment_datetime:
                return jsonify({"error": "Appointment time is already booked"}), 409

        # Schedule the appointment
        appointments.append({
            "client_name": client_name,
            "appointment_datetime": appointment_datetime
        })
        return jsonify({"message": "Appointment scheduled successfully"}), 201

    except ValueError:
        return jsonify({"error": "Invalid datetime format. Use 'YYYY-MM-DD HH:MM:SS'"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view all scheduled appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
