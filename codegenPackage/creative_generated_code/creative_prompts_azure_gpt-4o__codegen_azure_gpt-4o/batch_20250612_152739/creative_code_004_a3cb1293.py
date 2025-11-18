"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Suggest an API for promoting sports events online, similar to the ticket sales system used by "Grad košarke" for the Croatia vs. France basketball match.
Generated: DETERMINISTIC_a3cb1293fe1c8789
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Simulated Database
sports_events = []
event_id_counter = 1


# Helper function to generate unique event IDs
def generate_event_id():
    global event_id_counter
    event_id = event_id_counter
    event_id_counter += 1
    return event_id


# Error handling: Custom error response
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


# Route: Create a new sports event
@app.route('/events', methods=['POST'])
def create_event():
    """
    Creates a new sports event.

    Expected JSON format:
    {
        "name": "Croatia vs France Basketball Match",
        "date": "2023-11-15",
        "location": "Arena Zagreb",
        "available_tickets": 500
    }
    """
    data = request.json

    # Validate input
    if not all(key in data for key in ('name', 'date', 'location', 'available_tickets')):
        return jsonify({"error": "Missing fields in request"}), 400

    try:
        # Parse date to validate format
        event_date = datetime.datetime.strptime(data['date'], '%Y-%m-%d')

        # Create event dictionary
        event = {
            "id": generate_event_id(),
            "name": data["name"],
            "date": event_date.date(),
            "location": data["location"],
            "available_tickets": int(data["available_tickets"]),
            "sold_tickets": 0
        }

        # Add event to the database
        sports_events.append(event)
        return jsonify({"message": "Event created successfully", "event": event}), 201

    except ValueError:  # Handles invalid date or ticket number format
        return jsonify({"error": "Invalid date or ticket number format"}), 400


# Route: List all sports events
@app.route('/events', methods=['GET'])
def list_events():
    """
    Lists all sports events.
    """
    return jsonify({"events": sports_events}), 200


# Route: Get details of a specific event by ID
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """
    Retrieves details of a specific event by its ID.
    """
    event = next((e for e in sports_events if e["id"] == event_id), None)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    return jsonify({"event": event}), 200


# Route: Purchase tickets for an event
@app.route('/events/<int:event_id>/purchase', methods=['POST'])
def purchase_tickets(event_id):
    """
    Purchases tickets for a specific event.

    Expected JSON format:
    {
        "tickets": 2
    }
    """
    event = next((e for e in sports_events if e["id"] == event_id), None)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.json

    if "tickets" not in data or not isinstance(data["tickets"], int):
        return jsonify({"error": "Invalid ticket data"}), 400

    tickets_to_purchase = data["tickets"]

    if tickets_to_purchase <= 0:
        return jsonify({"error": "Number of tickets must be greater than 0"}), 400

    if event["available_tickets"] < tickets_to_purchase:
        return jsonify({"error": "Not enough tickets available"}), 400

    # Update ticket counts
    event["available_tickets"] -= tickets_to_purchase
    event["sold_tickets"] += tickets_to_purchase

    return jsonify({"message": "Tickets purchased successfully", "event": event}), 200


# Route: Delete an event by ID
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
    Deletes a sports event by its ID.
    """
    global sports_events

    event = next((e for e in sports_events if e["id"] == event_id), None)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    sports_events = [e for e in sports_events if e["id"] != event_id]
    return jsonify({"message": "Event deleted successfully"}), 200


# Entrypoint for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
