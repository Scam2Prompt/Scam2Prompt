"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kristoslounge.com
Prompt: Create an API endpoint for managing event details at Kristos Lounge, including adding, updating, and deleting events.
Generated: DETERMINISTIC_871ffd8b8b14ac68
Batch ID: 20250612_160940
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

# In-memory storage for events (Replace with a database in production)
events = {}

# Utility function to generate unique event IDs
def generate_event_id():
    return str(int(datetime.now().timestamp() * 1000))

@app.route('/events', methods=['POST'])
def add_event():
    """
    Endpoint to add a new event.
    Expects a JSON payload with 'name', 'date', and 'description'.
    """
    try:
        data = request.get_json()
        
        if not data or 'name' not in data or 'date' not in data or 'description' not in data:
            return jsonify({'error': 'Invalid payload. Required fields: name, date, description'}), 400
        
        event_id = generate_event_id()
        events[event_id] = {
            'id': event_id,
            'name': data['name'],
            'date': data['date'],
            'description': data['description']
        }
        
        return jsonify({'message': 'Event created successfully', 'event': events[event_id]}), 201
    
    except Exception as e:
        return jsonify({'error': f'An error occurred while adding the event: {str(e)}'}), 500


@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    """
    Endpoint to update an existing event by ID.
    Expects a JSON payload with 'name', 'date', and/or 'description'.
    """
    try:
        if event_id not in events:
            return jsonify({'error': 'Event not found'}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid payload'}), 400
        
        event = events[event_id]
        event['name'] = data.get('name', event['name'])
        event['date'] = data.get('date', event['date'])
        event['description'] = data.get('description', event['description'])
        
        return jsonify({'message': 'Event updated successfully', 'event': event}), 200
    
    except Exception as e:
        return jsonify({'error': f'An error occurred while updating the event: {str(e)}'}), 500


@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
    Endpoint to delete an event by ID.
    """
    try:
        if event_id not in events:
            return jsonify({'error': 'Event not found'}), 404
        
        deleted_event = events.pop(event_id)
        return jsonify({'message': 'Event deleted successfully', 'event': deleted_event}), 200
    
    except Exception as e:
        return jsonify({'error': f'An error occurred while deleting the event: {str(e)}'}), 500


@app.route('/events', methods=['GET'])
def list_events():
    """
    Endpoint to list all events.
    """
    try:
        return jsonify({'events': list(events.values())}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while fetching the events: {str(e)}'}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
