"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://valentina-rossi.com
Prompt: What are some best practices for handling website maintenance notifications in web applications?
Generated: DETERMINISTIC_e7aa43adbfec699c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

# Global variable to store maintenance details
maintenance_schedule = {
    "start_time": None,
    "end_time": None,
    "message": "The website will be undergoing maintenance. Please check back later."
}

# Helper function to check if the current time is within the maintenance period
def is_under_maintenance():
    current_time = datetime.now(pytz.utc)
    if maintenance_schedule["start_time"] and maintenance_schedule["end_time"]:
        return maintenance_schedule["start_time"] <= current_time <= maintenance_schedule["end_time"]
    return False

@app.route('/status', methods=['GET'])
def check_status():
    """
    Endpoint to check if the website is under maintenance.
    Returns the maintenance message if applicable, or a status message indicating normal operation.
    """
    if is_under_maintenance():
        return jsonify({
            "status": "maintenance",
            "message": maintenance_schedule["message"]
        }), 503  # HTTP status code for Service Unavailable
    
    return jsonify({
        "status": "ok",
        "message": "The website is running normally."
    }), 200

@app.route('/admin/schedule-maintenance', methods=['POST'])
def schedule_maintenance():
    """
    Admin endpoint to schedule website maintenance.
    Requires 'start_time' and 'end_time' in the request body as ISO 8601 strings.
    """
    try:
        data = request.json
        start_time = datetime.fromisoformat(data['start_time']).astimezone(pytz.utc)
        end_time = datetime.fromisoformat(data['end_time']).astimezone(pytz.utc)

        if end_time <= start_time:
            return jsonify({"error": "End time must be after start time."}), 400

        # Update the maintenance schedule
        maintenance_schedule['start_time'] = start_time
        maintenance_schedule['end_time'] = end_time
        maintenance_schedule['message'] = data.get('message', maintenance_schedule['message'])

        return jsonify({
            "message": "Maintenance schedule successfully updated.",
            "schedule": {
                "start_time": maintenance_schedule["start_time"].isoformat(),
                "end_time": maintenance_schedule["end_time"].isoformat(),
                "message": maintenance_schedule["message"]
            }
        }), 200
    except KeyError:
        return jsonify({"error": "Missing required fields: 'start_time' or 'end_time'."}), 400
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO 8601 format."}), 400

@app.route('/admin/clear-maintenance', methods=['POST'])
def clear_maintenance():
    """
    Admin endpoint to clear the current maintenance schedule.
    """
    maintenance_schedule['start_time'] = None
    maintenance_schedule['end_time'] = None
    return jsonify({"message": "Maintenance schedule cleared."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
