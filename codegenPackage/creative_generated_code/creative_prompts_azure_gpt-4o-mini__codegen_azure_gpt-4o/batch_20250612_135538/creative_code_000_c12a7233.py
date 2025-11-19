"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giorgiobarbagelata.eu
Prompt: Write a Python script to handle service maintenance notifications for a web application, similar to the message on the Giorgiobarbagelata website.
Generated: DETERMINISTIC_c12a72330e4d5bf0
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration for maintenance notifications
MAINTENANCE_CONFIG = {
    "enabled": True,
    "start_time": "2023-11-01T00:00:00",  # Maintenance start time (ISO format)
    "end_time": "2023-11-01T06:00:00",    # Maintenance end time (ISO format)
    "message": "The service is undergoing maintenance. Please try again later."
}

def parse_iso_datetime(iso_string):
    """
    Parse an ISO 8601 datetime string into a Python datetime object.
    """
    try:
        return datetime.datetime.fromisoformat(iso_string)
    except ValueError:
        raise ValueError(f"Invalid ISO datetime string: {iso_string}")

def is_maintenance_period():
    """
    Check if the current time falls within the maintenance period.
    """
    if not MAINTENANCE_CONFIG.get("enabled"):
        return False

    try:
        start_time = parse_iso_datetime(MAINTENANCE_CONFIG["start_time"])
        end_time = parse_iso_datetime(MAINTENANCE_CONFIG["end_time"])
        current_time = datetime.datetime.utcnow()

        return start_time <= current_time <= end_time
    except ValueError as e:
        # Log the error and return False (safe fallback)
        print(f"Error parsing maintenance configuration: {e}")
        return False

@app.route("/")
def home():
    """
    Main route for the web application.
    Handles service maintenance notifications.
    """
    if is_maintenance_period():
        # Return maintenance message if maintenance is active
        response = {
            "status": "maintenance",
            "message": MAINTENANCE_CONFIG["message"]
        }
        return jsonify(response), 503  # HTTP status code 503: Service Unavailable

    # Normal response when no maintenance is scheduled
    response = {
        "status": "ok",
        "message": "Welcome to the web application!"
    }
    return jsonify(response)

if __name__ == "__main__":
    # Run the Flask web application
    app.run(debug=True)
```
