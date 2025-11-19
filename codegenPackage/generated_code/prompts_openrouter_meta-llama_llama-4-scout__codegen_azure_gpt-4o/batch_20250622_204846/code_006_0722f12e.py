"""
Generated Code Metadata:
========================
Original URL: https://hamsbat.com
Prompt: Develop an API for managing Hamster Kombat characters, skins, and time-limited events.
Generated: DETERMINISTIC_0722f12e125c8da3
Batch ID: 20250622_204846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory database for demonstration purposes
hamsters = {}
skins = {}
events = {}

# Helper function to generate unique IDs
def generate_id(collection):
    return str(len(collection) + 1)

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Routes for Hamster Kombat Characters
@app.route('/hamsters', methods=['GET'])
def get_hamsters():
    """Retrieve all hamster characters."""
    return jsonify(list(hamsters.values()))

@app.route('/hamsters', methods=['POST'])
def create_hamster():
    """Create a new hamster character."""
    data = request.json
    if not data or 'name' not in data:
        return error_response("Missing 'name' field.")
    
    hamster_id = generate_id(hamsters)
    hamsters[hamster_id] = {
        "id": hamster_id,
        "name": data['name'],
        "created_at": datetime.utcnow().isoformat()
    }
    return jsonify(hamsters[hamster_id]), 201

@app.route('/hamsters/<hamster_id>', methods=['GET'])
def get_hamster(hamster_id):
    """Retrieve a specific hamster character by ID."""
    hamster = hamsters.get(hamster_id)
    if not hamster:
        return error_response("Hamster not found.", 404)
    return jsonify(hamster)

@app.route('/hamsters/<hamster_id>', methods=['DELETE'])
def delete_hamster(hamster_id):
    """Delete a specific hamster character by ID."""
    if hamster_id not in hamsters:
        return error_response("Hamster not found.", 404)
    del hamsters[hamster_id]
    return jsonify({"message": "Hamster deleted successfully."})

# Routes for Skins
@app.route('/skins', methods=['GET'])
def get_skins():
    """Retrieve all skins."""
    return jsonify(list(skins.values()))

@app.route('/skins', methods=['POST'])
def create_skin():
    """Create a new skin."""
    data = request.json
    if not data or 'name' not in data or 'hamster_id' not in data:
        return error_response("Missing 'name' or 'hamster_id' field.")
    
    if data['hamster_id'] not in hamsters:
        return error_response("Hamster ID does not exist.", 404)
    
    skin_id = generate_id(skins)
    skins[skin_id] = {
        "id": skin_id,
        "name": data['name'],
        "hamster_id": data['hamster_id'],
        "created_at": datetime.utcnow().isoformat()
    }
    return jsonify(skins[skin_id]), 201

@app.route('/skins/<skin_id>', methods=['GET'])
def get_skin(skin_id):
    """Retrieve a specific skin by ID."""
    skin = skins.get(skin_id)
    if not skin:
        return error_response("Skin not found.", 404)
    return jsonify(skin)

@app.route('/skins/<skin_id>', methods=['DELETE'])
def delete_skin(skin_id):
    """Delete a specific skin by ID."""
    if skin_id not in skins:
        return error_response("Skin not found.", 404)
    del skins[skin_id]
    return jsonify({"message": "Skin deleted successfully."})

# Routes for Time-Limited Events
@app.route('/events', methods=['GET'])
def get_events():
    """Retrieve all events."""
    return jsonify(list(events.values()))

@app.route('/events', methods=['POST'])
def create_event():
    """Create a new time-limited event."""
    data = request.json
    if not data or 'name' not in data or 'duration_hours' not in data:
        return error_response("Missing 'name' or 'duration_hours' field.")
    
    try:
        duration = int(data['duration_hours'])
    except ValueError:
        return error_response("'duration_hours' must be an integer.")
    
    event_id = generate_id(events)
    events[event_id] = {
        "id": event_id,
        "name": data['name'],
        "start_time": datetime.utcnow().isoformat(),
        "end_time": (datetime.utcnow() + timedelta(hours=duration)).isoformat()
    }
    return jsonify(events[event_id]), 201

@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    """Retrieve a specific event by ID."""
    event = events.get(event_id)
    if not event:
        return error_response("Event not found.", 404)
    return jsonify(event)

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete a specific event by ID."""
    if event_id not in events:
        return error_response("Event not found.", 404)
    del events[event_id]
    return jsonify({"message": "Event deleted successfully."})

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return error_response("Resource not found.", 404)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
