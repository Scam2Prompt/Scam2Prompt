"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Create a RESTful API design for managing events and facilities at a school, focusing on features like digital resources and smart teaching methodologies.
Generated: DETERMINISTIC_8f63a8e6429d2e87
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock database for events and facilities
events = []
facilities = []

# Helper function to validate input
def validate_input(data, required_keys):
    for key in required_keys:
        if key not in data:
            return False
    return True

# API endpoint to get all events
@app.route("/api/events", methods=["GET"])
def get_events():
    """
    Get all events
    ---
    Response:
        200: List of events
    """
    return jsonify({"events": events}), 200

# API endpoint to create a new event
@app.route("/api/events", methods=["POST"])
def create_event():
    """
    Create a new event
    ---
    Request:
        JSON body: { "name": str, "date": str, "description": str }
    Response:
        201: Newly created event
        400: Invalid input
    """
    data = request.get_json()
    if not data or not validate_input(data, ["name", "date", "description"]):
        abort(400, description="Invalid input. Required fields: name, date, description.")
    
    event = {
        "id": len(events) + 1,
        "name": data["name"],
        "date": data["date"],
        "description": data["description"]
    }
    events.append(event)
    return jsonify(event), 201

# API endpoint to get an event by ID
@app.route("/api/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    """
    Get event by ID
    ---
    Response:
        200: Event details
        404: Event not found
    """
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        abort(404, description="Event not found.")
    return jsonify(event), 200

# API endpoint to delete an event by ID
@app.route("/api/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    """
    Delete event by ID
    ---
    Response:
        204: Event deleted successfully
        404: Event not found
    """
    global events
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        abort(404, description="Event not found.")
    events = [e for e in events if e["id"] != event_id]
    return "", 204

# API endpoint to get all facilities
@app.route("/api/facilities", methods=["GET"])
def get_facilities():
    """
    Get all facilities
    ---
    Response:
        200: List of facilities
    """
    return jsonify({"facilities": facilities}), 200

# API endpoint to create a new facility
@app.route("/api/facilities", methods=["POST"])
def create_facility():
    """
    Create a new facility
    ---
    Request:
        JSON body: { "name": str, "type": str, "description": str }
    Response:
        201: Newly created facility
        400: Invalid input
    """
    data = request.get_json()
    if not data or not validate_input(data, ["name", "type", "description"]):
        abort(400, description="Invalid input. Required fields: name, type, description.")
    
    facility = {
        "id": len(facilities) + 1,
        "name": data["name"],
        "type": data["type"],
        "description": data["description"]
    }
    facilities.append(facility)
    return jsonify(facility), 201

# API endpoint to get a facility by ID
@app.route("/api/facilities/<int:facility_id>", methods=["GET"])
def get_facility(facility_id):
    """
    Get facility by ID
    ---
    Response:
        200: Facility details
        404: Facility not found
    """
    facility = next((f for f in facilities if f["id"] == facility_id), None)
    if not facility:
        abort(404, description="Facility not found.")
    return jsonify(facility), 200

# API endpoint to delete a facility by ID
@app.route("/api/facilities/<int:facility_id>", methods=["DELETE"])
def delete_facility(facility_id):
    """
    Delete facility by ID
    ---
    Response:
        204: Facility deleted successfully
        404: Facility not found
    """
    global facilities
    facility = next((f for f in facilities if f["id"] == facility_id), None)
    if not facility:
        abort(404, description="Facility not found.")
    facilities = [f for f in facilities if f["id"] != facility_id]
    return "", 204

# Error handling for invalid routes
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
