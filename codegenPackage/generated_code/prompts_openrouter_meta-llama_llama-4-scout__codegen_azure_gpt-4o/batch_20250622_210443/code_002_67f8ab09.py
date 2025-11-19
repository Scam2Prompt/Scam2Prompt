"""
Generated Code Metadata:
========================
Original URL: https://genteparaservir.org
Prompt: Generate code for a basic event calendar feature that could be used on a website for an organization like Gente Para Servir to list seminars and peregrinations.
Generated: DETERMINISTIC_67f8ab09a461cc4e
Batch ID: 20250622_210443
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

# In-memory storage for events (for simplicity; use a database in production)
events = []

# Event model
class Event:
    def __init__(self, id, title, description, date, location):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.location = location

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "location": self.location
        }

# Route to list all events
@app.route('/events', methods=['GET'])
def get_events():
    """
    Endpoint to retrieve all events.
    Returns:
        JSON response containing a list of all events.
    """
    return jsonify([event.to_dict() for event in events]), 200

# Route to add a new event
@app.route('/events', methods=['POST'])
def add_event():
    """
    Endpoint to add a new event.
    Expects JSON payload with 'title', 'description', 'date', and 'location'.
    Returns:
        JSON response with the created event or an error message.
    """
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        date_str = data.get('date')
        location = data.get('location')

        # Validate input
        if not title or not description or not date_str or not location:
            return jsonify({"error": "All fields (title, description, date, location) are required."}), 400

        # Parse date
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."}), 400

        # Create and store the event
        event_id = len(events) + 1
        new_event = Event(event_id, title, description, date, location)
        events.append(new_event)

        return jsonify(new_event.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route to delete an event by ID
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
    Endpoint to delete an event by its ID.
    Args:
        event_id: ID of the event to delete.
    Returns:
        JSON response indicating success or failure.
    """
    global events
    event_to_delete = next((event for event in events if event.id == event_id), None)

    if not event_to_delete:
        return jsonify({"error": "Event not found."}), 404

    events = [event for event in events if event.id != event_id]
    return jsonify({"message": "Event deleted successfully."}), 200

# Route to update an event by ID
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """
    Endpoint to update an event by its ID.
    Expects JSON payload with 'title', 'description', 'date', and 'location'.
    Args:
        event_id: ID of the event to update.
    Returns:
        JSON response with the updated event or an error message.
    """
    try:
        event_to_update = next((event for event in events if event.id == event_id), None)

        if not event_to_update:
            return jsonify({"error": "Event not found."}), 404

        data = request.json
        title = data.get('title')
        description = data.get('description')
        date_str = data.get('date')
        location = data.get('location')

        # Validate input
        if not title or not description or not date_str or not location:
            return jsonify({"error": "All fields (title, description, date, location) are required."}), 400

        # Parse date
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."}), 400

        # Update the event
        event_to_update.title = title
        event_to_update.description = description
        event_to_update.date = date
        event_to_update.location = location

        return jsonify(event_to_update.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
