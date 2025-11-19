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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data structure to hold room availability
# In a real application, this would likely be replaced with a database
rooms = {
    "101": {"type": "Single", "available": True, "booked_dates": []},
    "102": {"type": "Double", "available": True, "booked_dates": []},
    "201": {"type": "Suite", "available": True, "booked_dates": []},
}

def is_date_range_available(room, start_date, end_date):
    """Check if the room is available for the given date range."""
    for booked_date in room['booked_dates']:
        if (start_date <= booked_date['end'] and end_date >= booked_date['start']):
            return False
    return True

@app.route('/check_availability', methods=['GET'])
def check_availability():
    """Check room availability for a given date range."""
    try:
        start_date = datetime.strptime(request.args.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.args.get('end_date'), '%Y-%m-%d')
        
        if start_date >= end_date:
            raise BadRequest("Start date must be before end date.")

        available_rooms = {}
        for room_number, room in rooms.items():
            if is_date_range_available(room, start_date, end_date):
                available_rooms[room_number] = room['type']

        return jsonify(available_rooms), 200

    except ValueError:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/make_reservation', methods=['POST'])
def make_reservation():
    """Make a reservation for a room."""
    try:
        data = request.json
        room_number = data.get('room_number')
        start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d')

        if start_date >= end_date:
            raise BadRequest("Start date must be before end date.")
        
        room = rooms.get(room_number)
        if not room:
            raise BadRequest("Room not found.")

        if not is_date_range_available(room, start_date, end_date):
            return jsonify({"error": "Room is not available for the selected dates."}), 400

        # Reserve the room by adding the booked dates
        room['booked_dates'].append({'start': start_date, 'end': end_date})
        room['available'] = False  # Mark room as unavailable

        return jsonify({"message": "Reservation successful.", "room_number": room_number}), 201

    except ValueError:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
