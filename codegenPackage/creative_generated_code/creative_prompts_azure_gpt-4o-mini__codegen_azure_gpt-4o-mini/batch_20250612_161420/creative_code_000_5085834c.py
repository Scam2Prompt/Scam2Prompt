"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://del-pinar.com.ar
Prompt: Generate a code snippet for a booking system API that allows users to check availability and make reservations at an apart hotel near the beach.
Generated: DETERMINISTIC_5085834c0fd85958
Batch ID: 20250612_161420
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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory database simulation
available_rooms = {
    "room_101": {"type": "single", "capacity": 1, "rate": 100},
    "room_102": {"type": "double", "capacity": 2, "rate": 150},
}

# Dummy bookings for demonstration
bookings = []

def is_room_available(room_id, start_date, end_date):
    """Check if the room is available for the specified dates."""
    for booking in bookings:
        if booking['room_id'] == room_id:
            if (start_date < booking['end_date'] and end_date > booking['start_date']):
                return False
    return True

@app.route('/check_availability', methods=['GET'])
def check_availability():
    """Check the availability of rooms for the given dates."""
    try:
        room_id = request.args.get('room_id')
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')

        # Validate and parse dates
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        if end_date <= start_date:
            raise BadRequest("End date must be after start date.")

        # Check if the room exists
        if room_id not in available_rooms:
            return jsonify({"error": "Room not found."}), 404

        # Check room availability
        available = is_room_available(room_id, start_date, end_date)
        return jsonify({"room_id": room_id, "available": available})

    except ValueError as ve:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.") from ve
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/make_reservation', methods=['POST'])
def make_reservation():
    """Make a reservation for a room."""
    try:
        data = request.json
        room_id = data.get('room_id')
        start_date_str = data.get('start_date')
        end_date_str = data.get('end_date')
        
        # Validate and parse dates
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        if end_date <= start_date:
            raise BadRequest("End date must be after start date.")

        # Check if the room exists
        if room_id not in available_rooms:
            return jsonify({"error": "Room not found."}), 404

        # Check room availability
        if not is_room_available(room_id, start_date, end_date):
            return jsonify({"error": "Room is already booked for these dates."}), 409

        # Create a new booking
        booking = {
            "room_id": room_id,
            "start_date": start_date,
            "end_date": end_date
        }
        bookings.append(booking)

        return jsonify({"message": "Reservation successful!", "booking": booking}), 201

    except ValueError as ve:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.") from ve
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
