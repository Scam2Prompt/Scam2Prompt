"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehemacare.com
Prompt: Illustrate how to implement a booking system for Habilitation services at Rehema Care using a RESTful API approach.
Generated: DETERMINISTIC_23d3b0f05c66193f
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: RESTful API for booking system at Rehema Care habilitation services.
# Author: [Your Name]
# Date: [Today's Date]

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for simplicity (replace with a real database in production)
habilitation_services = [
    {"id": 1, "name": "Physical Therapy", "available_slots": 10},
    {"id": 2, "name": "Speech Therapy", "available_slots": 5},
    {"id": 3, "name": "Occupational Therapy", "available_slots": 8},
]

bookings = {}

# Error messages
SERVICE_NOT_FOUND = {"error": "Service not found"}
INSUFFICIENT_SLOTS = {"error": "No available slots for the selected service"}
BOOKING_NOT_FOUND = {"error": "Booking not found"}

def find_service_by_id(service_id):
    """Helper function to find habilitation service by ID."""
    return next((service for service in habilitation_services if service["id"] == service_id), None)

@app.route("/services", methods=["GET"])
def get_services():
    """
    Endpoint to list all habilitation services.
    Returns:
        JSON list of services.
    """
    return jsonify(habilitation_services)

@app.route("/bookings", methods=["POST"])
def create_booking():
    """
    Endpoint to create a booking for habilitation services.
    Body JSON:
        - service_id (integer)
        - client_name (string)
    Returns:
        JSON with booking details or error message.
    """
    data = request.json

    # Validate input
    if "service_id" not in data or "client_name" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    service_id = data["service_id"]
    client_name = data["client_name"]

    # Find the requested service
    service = find_service_by_id(service_id)
    if not service:
        return jsonify(SERVICE_NOT_FOUND), 404

    # Check slot availability
    if service["available_slots"] <= 0:
        return jsonify(INSUFFICIENT_SLOTS), 400

    # Create booking
    booking_id = str(uuid.uuid4())  # Generate unique booking ID
    bookings[booking_id] = {
        "id": booking_id,
        "service_id": service_id,
        "client_name": client_name,
    }

    # Deduct available slot
    service["available_slots"] -= 1

    return jsonify(bookings[booking_id]), 201

@app.route("/bookings/<booking_id>", methods=["GET"])
def get_booking(booking_id):
    """
    Endpoint to retrieve booking details.
    URL Params:
        - booking_id (string)
    Returns:
        JSON with booking details or error message.
    """
    booking = bookings.get(booking_id)
    if not booking:
        return jsonify(BOOKING_NOT_FOUND), 404
    return jsonify(booking)

@app.route("/bookings/<booking_id>", methods=["DELETE"])
def cancel_booking(booking_id):
    """
    Endpoint to cancel a booking.
    URL Params:
        - booking_id (string)
    Returns:
        Success message or error message.
    """
    booking = bookings.pop(booking_id, None)
    if not booking:
        return jsonify(BOOKING_NOT_FOUND), 404

    # Restore slot availability
    service = find_service_by_id(booking["service_id"])
    if service:
        service["available_slots"] += 1

    return jsonify({"message": "Booking canceled successfully"}), 200

if __name__ == "__main__":
    # Run the Flask app
    # In production, use a proper WSGI server like Gunicorn.
    app.run(debug=True)
```
