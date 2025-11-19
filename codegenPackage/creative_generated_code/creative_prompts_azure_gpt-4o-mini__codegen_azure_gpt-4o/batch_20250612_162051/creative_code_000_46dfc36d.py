"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vracarbvk.rs
Prompt: Generate a code snippet for a booking system API that allows users to reserve rooms at Vila Vračar in Vrnjačka Banja.
Generated: DETERMINISTIC_46dfc36d3644520f
Batch ID: 20250612_162051
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
import uuid

app = Flask(__name__)

# In-memory storage for bookings and rooms
rooms = [
    {"id": 1, "name": "Room 101", "capacity": 2},
    {"id": 2, "name": "Room 102", "capacity": 3},
    {"id": 3, "name": "Room 103", "capacity": 4},
]
bookings = []

def is_room_available(room_id, start_date, end_date):
    """
    Check if the room is available for the given date range.
    """
    for booking in bookings:
        if (
            booking["room_id"] == room_id and
            not (
                booking["end_date"] <= start_date or
                booking["start_date"] >= end_date
            )
        ):
            return False
    return True

@app.route('/rooms', methods=['GET'])
def get_rooms():
    """
    Endpoint to get the list of available rooms.
    """
    return jsonify({"rooms": rooms}), 200

@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new booking.
    """
    try:
        data = request.get_json()
        room_id = data.get("room_id")
        start_date = datetime.strptime(data.get("start_date"), '%Y-%m-%d')
        end_date = datetime.strptime(data.get("end_date"), '%Y-%m-%d')
        user_name = data.get("user_name")

        # Validate input
        if not room_id or not start_date or not end_date or not user_name:
            return jsonify({"error": "Missing required fields"}), 400

        if start_date >= end_date:
            return jsonify({"error": "Invalid date range"}), 400

        # Check room availability
        if not is_room_available(room_id, start_date, end_date):
            return jsonify({"error": "Room is not available for the selected dates"}), 400

        # Create booking
        booking = {
            "id": str(uuid.uuid4()),
            "room_id": room_id,
            "user_name": user_name,
            "start_date": start_date,
            "end_date": end_date
        }
        bookings.append(booking)

        return jsonify({"message": "Booking created successfully", "booking": booking}), 201

    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to get the list of all bookings.
    """
    return jsonify({"bookings": bookings}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
