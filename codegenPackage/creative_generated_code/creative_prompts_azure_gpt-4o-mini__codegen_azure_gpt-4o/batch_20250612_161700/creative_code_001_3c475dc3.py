"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viafuar.com
Prompt: Recommend an API for managing event schedules similar to the Tuzla Boat Show, focusing on features like attendee tracking and exhibitor management.
Generated: DETERMINISTIC_3c475dc35746a4a4
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database to store events, attendees, and exhibitors
events_db = {}
attendees_db = {}
exhibitors_db = {}

# Error handling function
def error_response(message, code=400):
    return jsonify({'error': message}), code

# Endpoint to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    try:
        event_data = request.json
        if 'id' not in event_data or 'name' not in event_data or 'date' not in event_data:
            return error_response("Event data must include 'id', 'name', and 'date' fields.")
        
        event_id = event_data['id']
        if event_id in events_db:
            return error_response(f"Event with ID {event_id} already exists.", 409)
        
        events_db[event_id] = {
            'name': event_data['name'],
            'date': event_data['date'],
            'attendees': [],
            'exhibitors': []
        }
        return jsonify({'message': f"Event '{event_data['name']}' created successfully."}), 201
    except Exception as e:
        return error_response(str(e))

# Endpoint to retrieve all events
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(list(events_db.values())), 200

# Endpoint to add an attendee to an event
@app.route('/events/<event_id>/attendees', methods=['POST'])
def add_attendee(event_id):
    try:
        attendee_data = request.json
        if 'id' not in attendee_data or 'name' not in attendee_data:
            return error_response("Attendee data must include 'id' and 'name' fields.")
        
        if event_id not in events_db:
            return error_response(f"Event with ID {event_id} not found.", 404)
        
        attendee_id = attendee_data['id']
        if attendee_id in attendees_db:
            return error_response(f"Attendee with ID {attendee_id} already exists. Use a unique ID.", 409)
        
        attendees_db[attendee_id] = {
            'name': attendee_data['name'],
            'event_id': event_id
        }
        events_db[event_id]['attendees'].append(attendee_data)
        return jsonify({'message': f"Attendee '{attendee_data['name']}' added to event '{events_db[event_id]['name']}'."}), 201
    except Exception as e:
        return error_response(str(e))

# Endpoint to add an exhibitor to an event
@app.route('/events/<event_id>/exhibitors', methods=['POST'])
def add_exhibitor(event_id):
    try:
        exhibitor_data = request.json
        if 'id' not in exhibitor_data or 'name' not in exhibitor_data:
            return error_response("Exhibitor data must include 'id' and 'name' fields.")
        
        if event_id not in events_db:
            return error_response(f"Event with ID {event_id} not found.", 404)
        
        exhibitor_id = exhibitor_data['id']
        if exhibitor_id in exhibitors_db:
            return error_response(f"Exhibitor with ID {exhibitor_id} already exists. Use a unique ID.", 409)
        
        exhibitors_db[exhibitor_id] = {
            'name': exhibitor_data['name'],
            'event_id': event_id
        }
        events_db[event_id]['exhibitors'].append(exhibitor_data)
        return jsonify({'message': f"Exhibitor '{exhibitor_data['name']}' added to event '{events_db[event_id]['name']}'."}), 201
    except Exception as e:
        return error_response(str(e))

# Endpoint to retrieve all attendees for an event
@app.route('/events/<event_id>/attendees', methods=['GET'])
def get_attendees(event_id):
    if event_id not in events_db:
        return error_response(f"Event with ID {event_id} not found.", 404)
    return jsonify(events_db[event_id]['attendees']), 200

# Endpoint to retrieve all exhibitors for an event
@app.route('/events/<event_id>/exhibitors', methods=['GET'])
def get_exhibitors(event_id):
    if event_id not in events_db:
        return error_response(f"Event with ID {event_id} not found.", 404)
    return jsonify(events_db[event_id]['exhibitors']), 200

# Entry point for the API
if __name__ == '__main__':
    app.run(debug=True)
```
