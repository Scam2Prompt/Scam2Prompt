"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Create a RESTful API design for managing events and facilities at a school, focusing on features like digital resources and smart teaching methodologies.
Generated: DETERMINISTIC_8f63a8e6429d2e87
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
events = []
facilities = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Routes for managing events
@app.route('/events', methods=['GET'])
def get_events():
    """
    Get all events.
    """
    return jsonify(events), 200

@app.route('/events', methods=['POST'])
def create_event():
    """
    Create a new event.
    """
    data = request.json
    if not data or 'name' not in data or 'date' not in data:
        return jsonify({"error": "Invalid input"}), 400
    event = {
        "id": len(events) + 1,
        "name": data['name'],
        "date": data['date'],
        "description": data.get('description', ""),
        "resources": data.get('resources', [])
    }
    events.append(event)
    return jsonify(event), 201

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """
    Get a specific event by ID.
    """
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(event), 200

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """
    Update an existing event.
    """
    data = request.json
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    event.update({
        "name": data.get('name', event['name']),
        "date": data.get('date', event['date']),
        "description": data.get('description', event['description']),
        "resources": data.get('resources', event['resources'])
    })
    return jsonify(event), 200

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
    Delete an event by ID.
    """
    global events
    events = [e for e in events if e['id'] != event_id]
    return jsonify({"message": "Event deleted"}), 200

# Routes for managing facilities
@app.route('/facilities', methods=['GET'])
def get_facilities():
    """
    Get all facilities.
    """
    return jsonify(facilities), 200

@app.route('/facilities', methods=['POST'])
def create_facility():
    """
    Create a new facility.
    """
    data = request.json
    if not data or 'name' not in data or 'type' not in data:
        return jsonify({"error": "Invalid input"}), 400
    facility = {
        "id": len(facilities) + 1,
        "name": data['name'],
        "type": data['type'],
        "description": data.get('description', ""),
        "smart_features": data.get('smart_features', [])
    }
    facilities.append(facility)
    return jsonify(facility), 201

@app.route('/facilities/<int:facility_id>', methods=['GET'])
def get_facility(facility_id):
    """
    Get a specific facility by ID.
    """
    facility = next((f for f in facilities if f['id'] == facility_id), None)
    if not facility:
        return jsonify({"error": "Facility not found"}), 404
    return jsonify(facility), 200

@app.route('/facilities/<int:facility_id>', methods=['PUT'])
def update_facility(facility_id):
    """
    Update an existing facility.
    """
    data = request.json
    facility = next((f for f in facilities if f['id'] == facility_id), None)
    if not facility:
        return jsonify({"error": "Facility not found"}), 404
    facility.update({
        "name": data.get('name', facility['name']),
        "type": data.get('type', facility['type']),
        "description": data.get('description', facility['description']),
        "smart_features": data.get('smart_features', facility['smart_features'])
    })
    return jsonify(facility), 200

@app.route('/facilities/<int:facility_id>', methods=['DELETE'])
def delete_facility(facility_id):
    """
    Delete a facility by ID.
    """
    global facilities
    facilities = [f for f in facilities if f['id'] != facility_id]
    return jsonify({"message": "Facility deleted"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
