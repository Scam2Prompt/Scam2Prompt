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

app = Flask(__name__)

# Sample data for room availability
rooms = [
    {"room_id": 1, "type": "single", "availability": []},
    {"room_id": 2, "type": "double", "availability": []},
    {"room_id": 3, "type": "suite", "availability": []},
]

# Helper function to check date overlap
def is_date_available(room_id, start_date, end_date):
    room = next((room for room in rooms if room['room_id'] == room_id), None)
    if not room:
        return False

    for booking in room['availability']:
        if (start_date <= booking['end_date'] and end_date >= booking['start_date']):
            return False

    return True

@app.route('/check_availability', methods=['GET'])
def check_availability():
    """
    Endpoint to check room availability.
    Parameters:
        room_id: ID of the room
        start_date: Start date of desired booking (YYYY-MM-DD)
        end_date: End date of desired booking (YYYY-MM-DD)
    Returns:
        JSON response with availability status
    """
    try:
        room_id = int(request.args.get('room_id'))
        start_date = datetime.strptime(request.args.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.args.get('end_date'), '%Y-%m-%d').date()

        if start_date >= end_date:
            return jsonify({"error": "End date must be after start date"}), 400

        if is_date_available(room_id, start_date, end_date):
            return jsonify({"available": True}), 200
        else:
            return jsonify({"available": False}), 200

    except ValueError as ve:
        return jsonify({"error": "Invalid date format or input"}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/make_reservation', methods=['POST'])
def make_reservation():
    """
    Endpoint to make a room reservation.
    Parameters:
        room_id: ID of the room
        start_date: Start date of reservation (YYYY-MM-DD)
        end_date: End date of reservation (YYYY-MM-DD)
    Returns:
        JSON response with reservation confirmation or error message
    """
    try:
        data = request.json
        room_id = int(data['room_id'])
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()

        if start_date >= end_date:
            return jsonify({"error": "End date must be after start date"}), 400

        if is_date_available(room_id, start_date, end_date):
            room = next((room for room in rooms if room['room_id'] == room_id), None)
            if not room:
                return jsonify({"error": "Room does not exist"}), 404

            # Add booking to room availability
            room['availability'].append({"start_date": start_date, "end_date": end_date})
            return jsonify({"message": "Reservation successful"}), 201
        else:
            return jsonify({"error": "Room is not available for the selected dates"}), 400

    except ValueError as ve:
        return jsonify({"error": "Invalid date format or input"}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
