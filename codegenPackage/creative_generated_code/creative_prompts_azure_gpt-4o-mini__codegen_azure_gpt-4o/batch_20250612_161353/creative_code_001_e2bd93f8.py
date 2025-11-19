"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Write a code snippet for a booking system API that allows users to reserve event spaces at DCITY, including options for different types of events like weddings and conferences.
Generated: DETERMINISTIC_e2bd93f84feff1e8
Batch ID: 20250612_161353
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

# In-memory "database" for storage
event_spaces = [
    {"id": 1, "name": "Grand Hall", "capacity": 500, "type": "wedding"},
    {"id": 2, "name": "Conference Center", "capacity": 300, "type": "conference"},
    {"id": 3, "name": "Banquet Room", "capacity": 200, "type": "wedding"},
]
reservations = []

# Error messages
ERROR_MESSAGES = {
    "space_not_found": "Event space not found.",
    "invalid_date_format": "Invalid date format. Use YYYY-MM-DD.",
    "conflict": "The event space is already reserved for the selected date.",
}


@app.route('/reserve', methods=['POST'])
def reserve_event_space():
    """
    API Endpoint for reserving an event space.
    Expects JSON payload with:
        - space_id (int): ID of the event space
        - event_date (str): Date of the event in YYYY-MM-DD format
        - event_type (str): Type of event (e.g., 'wedding', 'conference')
        - organizer_name (str): Name of the person organizing the event
    """
    data = request.get_json()

    # Validate input
    space_id = data.get('space_id')
    event_date = data.get('event_date')
    event_type = data.get('event_type')
    organizer_name = data.get('organizer_name')

    if not all([space_id, event_date, event_type, organizer_name]):
        return jsonify({"error": "All fields (space_id, event_date, event_type, organizer_name) are required."}), 400

    try:
        # Validate date format
        event_date_parsed = datetime.strptime(event_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": ERROR_MESSAGES["invalid_date_format"]}), 400

    # Check if event space exists
    event_space = next((space for space in event_spaces if space["id"] == space_id and space["type"] == event_type), None)
    if not event_space:
        return jsonify({"error": ERROR_MESSAGES["space_not_found"]}), 404

    # Check for conflicts in reservations
    conflict = any(
        reservation for reservation in reservations
        if reservation["space_id"] == space_id and reservation["event_date"] == event_date_parsed
    )
    if conflict:
        return jsonify({"error": ERROR_MESSAGES["conflict"]}), 409

    # Create reservation
    reservation = {
        "reservation_id": len(reservations) + 1,
        "space_id": space_id,
        "event_date": event_date_parsed,
        "event_type": event_type,
        "organizer_name": organizer_name,
    }
    reservations.append(reservation)

    return jsonify({"message": "Reservation successful.", "reservation": reservation}), 201


@app.route('/reservations', methods=['GET'])
def get_reservations():
    """
    API Endpoint for retrieving all reservations.
    Returns a list of reservations with details.
    """
    return jsonify({"reservations": reservations}), 200


@app.route('/spaces', methods=['GET'])
def get_event_spaces():
    """
    API Endpoint for retrieving available event spaces.
    Returns a list of event spaces with details.
    """
    return jsonify({"event_spaces": event_spaces}), 200


# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
