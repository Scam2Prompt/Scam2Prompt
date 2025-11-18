"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-automation.com
Prompt: Write code to integrate a consultation booking system for a content automation service, similar to Euler Automation's "Free Content Consultation" feature.
Generated: DETERMINISTIC_0de43b00c9d6c3ac
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# consultation_booking_system.py

import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for demonstration purposes
consultation_slots = [
    {"id": 1, "date": "2023-10-15", "time": "10:00", "available": True},
    {"id": 2, "date": "2023-10-15", "time": "11:00", "available": True},
    {"id": 3, "date": "2023-10-16", "time": "14:00", "available": True},
]

bookings = []

# API to get available consultation slots
@app.route("/api/consultation-slots", methods=["GET"])
def get_consultation_slots():
    """
    Endpoint: /api/consultation-slots
    Method: GET
    Description: Retrieves available consultation slots.
    """
    available_slots = [slot for slot in consultation_slots if slot["available"]]
    return jsonify({"slots": available_slots}), 200

# API to book a consultation slot
@app.route("/api/book-slot", methods=["POST"])
def book_slot():
    """
    Endpoint: /api/book-slot
    Method: POST
    Description: Books a consultation slot.
    Body Parameters:
        - slot_id (int): ID of the consultation slot to book
        - user_name (str): Name of the user booking the slot
        - user_email (str): Email of the user booking the slot
    """
    try:
        # Parse request data
        data = request.json
        slot_id = data.get("slot_id")
        user_name = data.get("user_name")
        user_email = data.get("user_email")

        # Input validation
        if not slot_id or not user_name or not user_email:
            return jsonify({"error": "Missing required fields"}), 400

        # Find the requested slot
        slot = next((s for s in consultation_slots if s["id"] == slot_id), None)
        if not slot:
            return jsonify({"error": "Slot not found"}), 404

        # Check availability
        if not slot["available"]:
            return jsonify({"error": "Slot is already booked"}), 400

        # Book the slot
        slot["available"] = False
        booking = {
            "slot_id": slot_id,
            "user_name": user_name,
            "user_email": user_email,
            "booking_time": datetime.datetime.utcnow().isoformat(),
        }
        bookings.append(booking)

        return jsonify({"message": "Slot booked successfully", "booking": booking}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API to view all bookings
@app.route("/api/bookings", methods=["GET"])
def view_bookings():
    """
    Endpoint: /api/bookings
    Method: GET
    Description: Retrieves all bookings.
    """
    return jsonify({"bookings": bookings}), 200

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
