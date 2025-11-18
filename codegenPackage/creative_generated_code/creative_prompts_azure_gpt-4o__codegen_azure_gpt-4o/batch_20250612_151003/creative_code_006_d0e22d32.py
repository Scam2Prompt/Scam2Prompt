"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Create a REST API for managing workshop and event registrations aimed at community engagement in rural revitalization projects. Include endpoints for event creation, participant registration, and feedback collection.
Generated: DETERMINISTIC_d0e22d3254cd4ec3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory datastore
events = {}
participants = {}
feedbacks = {}

# Error handling structure
class APIError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code


@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response


# Endpoint: Create an event
@app.route('/events', methods=['POST'])
def create_event():
    """
    Create a new event.
    Payload:
        {
            "name": "<event_name>",
            "description": "<event_description>",
            "date": "<YYYY-MM-DD>"
        }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'date' not in data:
        raise APIError("Invalid payload. 'name', 'description', and 'date' are required.", 400)
    
    event_id = str(uuid4())
    events[event_id] = {
        "id": event_id,
        "name": data['name'],
        "description": data['description'],
        "date": data['date']
    }
    return jsonify(events[event_id]), 201


# Endpoint: Register a participant for an event
@app.route('/events/<event_id>/register', methods=['POST'])
def register_participant(event_id):
    """
    Register a participant for an event.
    Payload:
        {
            "name": "<participant_name>",
            "email": "<participant_email>"
        }
    """
    if event_id not in events:
        raise APIError("Event not found.", 404)
    
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise APIError("Invalid payload. 'name' and 'email' are required.", 400)
    
    participant_id = str(uuid4())
    participants[participant_id] = {
        "id": participant_id,
        "event_id": event_id,
        "name": data['name'],
        "email": data['email']
    }
    return jsonify(participants[participant_id]), 201


# Endpoint: Collect feedback for an event
@app.route('/events/<event_id>/feedback', methods=['POST'])
def collect_feedback(event_id):
    """
    Collect feedback for an event.
    Payload:
        {
            "participant_id": "<participant_id>",
            "feedback": "<feedback_text>"
        }
    """
    if event_id not in events:
        raise APIError("Event not found.", 404)
    
    data = request.get_json()
    if not data or 'participant_id' not in data or 'feedback' not in data:
        raise APIError("Invalid payload. 'participant_id' and 'feedback' are required.", 400)
    
    if data['participant_id'] not in participants or participants[data['participant_id']]['event_id'] != event_id:
        raise APIError("Invalid participant ID for this event.", 404)
    
    feedback_id = str(uuid4())
    feedbacks[feedback_id] = {
        "id": feedback_id,
        "event_id": event_id,
        "participant_id": data['participant_id'],
        "feedback": data['feedback']
    }
    return jsonify(feedbacks[feedback_id]), 201


# Endpoint: Get all events
@app.route('/events', methods=['GET'])
def get_events():
    """
    Retrieve all events.
    """
    return jsonify(list(events.values())), 200


# Endpoint: Get all participants for an event
@app.route('/events/<event_id>/participants', methods=['GET'])
def get_event_participants(event_id):
    """
    Retrieve all participants registered for a specific event.
    """
    if event_id not in events:
        raise APIError("Event not found.", 404)
    
    event_participants = [p for p in participants.values() if p['event_id'] == event_id]
    return jsonify(event_participants), 200


# Endpoint: Get all feedback for an event
@app.route('/events/<event_id>/feedback', methods=['GET'])
def get_event_feedback(event_id):
    """
    Retrieve all feedback for a specific event.
    """
    if event_id not in events:
        raise APIError("Event not found.", 404)
    
    event_feedback = [f for f in feedbacks.values() if f['event_id'] == event_id]
    return jsonify(event_feedback), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
