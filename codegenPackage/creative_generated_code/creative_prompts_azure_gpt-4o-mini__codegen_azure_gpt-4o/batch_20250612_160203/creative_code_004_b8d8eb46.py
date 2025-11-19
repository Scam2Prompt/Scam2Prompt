"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Design a booking API that includes options for group dining experiences and local dish preparation, reflecting the communal dining atmosphere of Boomgardi Sunland.
Generated: DETERMINISTIC_b8d8eb46bfb178d1
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for simplicity
BOOKINGS = []

# Helper function: Validate booking data
def validate_booking_data(data):
    try:
        if not all(key in data for key in ["name", "email", "phone", "date", "time", "group_size", "experience_type"]):
            return False, "Missing required fields."
        
        # Ensure valid experience type
        if data["experience_type"] not in ["group_dining", "local_dish_preparation"]:
            return False, "Invalid experience type. Allowed types: 'group_dining', 'local_dish_preparation'."
        
        # Parse and validate date/time format
        datetime.strptime(data["date"], "%Y-%m-%d")
        datetime.strptime(data["time"], "%H:%M")
        
        # Ensure group size is a positive integer
        if not isinstance(data["group_size"], int) or data["group_size"] <= 0:
            return False, "Group size must be a positive integer."
        
        return True, None
    except Exception as e:
        return False, str(e)

@app.route("/bookings", methods=["GET"])
def get_bookings():
    """
    Endpoint: Retrieve all bookings
    Method: GET
    Returns: JSON list of all bookings
    """
    return jsonify({"status": "success", "bookings": BOOKINGS}), 200

@app.route("/bookings", methods=["POST"])
def create_booking():
    """
    Endpoint: Create a new booking
    Method: POST
    Body: JSON with booking details
    Returns: JSON with success message or error
    """
    try:
        data = request.get_json()
        
        # Validate input data
        is_valid, error_message = validate_booking_data(data)
        if not is_valid:
            return jsonify({"status": "error", "message": error_message}), 400
        
        # Add booking to the in-memory database
        new_booking = {
            "id": len(BOOKINGS) + 1,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "date": data["date"],
            "time": data["time"],
            "group_size": data["group_size"],
            "experience_type": data["experience_type"]
        }
        BOOKINGS.append(new_booking)
        
        return jsonify({"status": "success", "message": "Booking created successfully.", "booking": new_booking}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": "An error occurred: " + str(e)}), 500

@app.route("/bookings/<int:booking_id>", methods=["GET"])
def get_booking_by_id(booking_id):
    """
    Endpoint: Retrieve a booking by ID
    Method: GET
    Params: booking_id (int)
    Returns: JSON with booking details or error
    """
    try:
        booking = next((b for b in BOOKINGS if b["id"] == booking_id), None)
        if not booking:
            return jsonify({"status": "error", "message": "Booking not found."}), 404
        
        return jsonify({"status": "success", "booking": booking}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": "An error occurred: " + str(e)}), 500

@app.route("/bookings/<int:booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    """
    Endpoint: Delete a booking by ID
    Method: DELETE
    Params: booking_id (int)
    Returns: JSON with success message or error
    """
    try:
        global BOOKINGS
        booking = next((b for b in BOOKINGS if b["id"] == booking_id), None)
        if not booking:
            return jsonify({"status": "error", "message": "Booking not found."}), 404
        
        BOOKINGS = [b for b in BOOKINGS if b["id"] != booking_id]
        return jsonify({"status": "success", "message": "Booking deleted successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": "An error occurred: " + str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
