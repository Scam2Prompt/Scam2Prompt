"""
Generated Code Metadata:
========================
Original URL: https://del-pinar.com.ar
Prompt: Generate a code snippet for a booking system API that allows users to check availability and make reservations at an apart hotel near the beach.
Generated: DETERMINISTIC_5085834c0fd85958
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for rooms and reservations
rooms = [
    {"id": 1, "type": "Standard", "price": 100},
    {"id": 2, "type": "Deluxe", "price": 150},
    {"id": 3, "type": "Suite", "price": 200},
]

reservations = []  # List to store reservations

# Helper function to check room availability
def is_room_available(room_id, check_in, check_out):
    for reservation in reservations:
        if reservation["room_id"] == room_id:
            # Check for date overlap
            if not (check_out <= reservation["check_in"] or check_in >= reservation["check_out"]):
                return False
    return True

@app.route('/availability', methods=['GET'])
def check_availability():
    """
    Endpoint to check room availability.
    Query parameters: check_in (YYYY-MM-DD), check_out (YYYY-MM-DD)
    """
    try:
        check_in = request.args.get('check_in')
        check_out = request.args.get('check_out')

        # Validate input dates
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
        if check_in_date >= check_out_date:
            return jsonify({"error": "Check-out date must be after check-in date"}), 400

        # Check availability for each room
        available_rooms = []
        for room in rooms:
            if is_room_available(room["id"], check_in_date, check_out_date):
                available_rooms.append(room)

        return jsonify({"available_rooms": available_rooms}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/reserve', methods=['POST'])
def make_reservation():
    """
    Endpoint to make a reservation.
    Request body: { "room_id": int, "check_in": "YYYY-MM-DD", "check_out": "YYYY-MM-DD", "guest_name": str }
    """
    try:
        data = request.get_json()

        # Validate input data
        room_id = data.get("room_id")
        check_in = data.get("check_in")
        check_out = data.get("check_out")
        guest_name = data.get("guest_name")

        if not room_id or not check_in or not check_out or not guest_name:
            return jsonify({"error": "Missing required fields"}), 400

        check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
        if check_in_date >= check_out_date:
            return jsonify({"error": "Check-out date must be after check-in date"}), 400

        # Check if the room is available
        if not is_room_available(room_id, check_in_date, check_out_date):
            return jsonify({"error": "Room is not available for the selected dates"}), 400

        # Create reservation
        reservation = {
            "room_id": room_id,
            "check_in": check_in_date,
            "check_out": check_out_date,
            "guest_name": guest_name
        }
        reservations.append(reservation)

        return jsonify({"message": "Reservation successful", "reservation": reservation}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
