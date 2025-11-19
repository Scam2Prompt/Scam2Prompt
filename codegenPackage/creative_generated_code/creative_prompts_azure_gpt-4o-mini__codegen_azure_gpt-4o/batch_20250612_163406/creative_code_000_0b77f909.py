"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autocarescosme.com
Prompt: Generate a code snippet for a web application that allows users to book a bus from Salamanca to Aldeatejada using the Autocares Cosme service.
Generated: DETERMINISTIC_0b77f90985112365
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask - Web application to book a bus from Salamanca to Aldeatejada using Autocares Cosme service.

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data for bus schedules and booking
BUS_SCHEDULES = [
    {"id": 1, "departure": "Salamanca", "destination": "Aldeatejada", "time": "08:00"},
    {"id": 2, "departure": "Salamanca", "destination": "Aldeatejada", "time": "10:00"},
    {"id": 3, "departure": "Salamanca", "destination": "Aldeatejada", "time": "14:00"},
]

BOOKINGS = []  # Store bookings

def validate_booking(data):
    """
    Validates the booking request payload.
    """
    if "name" not in data or not data["name"]:
        return "Name is required."
    if "email" not in data or not data["email"]:
        return "Email is required."
    if "schedule_id" not in data or not isinstance(data["schedule_id"], int):
        return "Valid schedule_id is required."
    return None

@app.route("/schedules", methods=["GET"])
def get_schedules():
    """
    Endpoint to retrieve available bus schedules.
    """
    return jsonify({"schedules": BUS_SCHEDULES})

@app.route("/book", methods=["POST"])
def book_bus():
    """
    Endpoint to book a bus trip.
    """
    try:
        data = request.json
        # Validate incoming payload
        validation_error = validate_booking(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Check if the schedule exists
        schedule = next((s for s in BUS_SCHEDULES if s["id"] == data["schedule_id"]), None)
        if not schedule:
            return jsonify({"error": "Invalid schedule_id. Schedule not found."}), 404

        # Create a booking record
        booking = {
            "id": len(BOOKINGS) + 1,
            "name": data["name"],
            "email": data["email"],
            "schedule": schedule,
            "booking_time": datetime.utcnow().isoformat(),
        }
        BOOKINGS.append(booking)

        return jsonify({"message": "Booking successful!", "booking": booking}), 201

    except Exception as e:
        # General error handling
        return jsonify({"error": "An error occurred while processing the booking.", "details": str(e)}), 500

@app.route("/bookings", methods=["GET"])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    """
    return jsonify({"bookings": BOOKINGS})

if __name__ == "__main__":
    app.run(debug=True)
```
