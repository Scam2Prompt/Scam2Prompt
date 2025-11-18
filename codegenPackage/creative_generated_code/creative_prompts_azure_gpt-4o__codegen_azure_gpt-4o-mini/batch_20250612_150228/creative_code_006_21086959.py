"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasnavi.pages.dev
Prompt: Generate code for organizing group trips in a navigation app, including tracking group members on a map and enabling walkie-talkie audio chat, similar to Atlas Navi's features.
Generated: DETERMINISTIC_21086959acc164f0
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from geopy.distance import great_circle
from threading import Lock

app = Flask(__name__)
socketio = SocketIO(app)
thread_lock = Lock()

# In-memory storage for group trips and members
group_trips = {}

@app.route('/create_trip', methods=['POST'])
def create_trip():
    """Create a new group trip."""
    data = request.get_json()
    trip_id = data.get('trip_id')
    members = data.get('members')  # list of member IDs

    if not trip_id or not members:
        return jsonify({'error': 'Trip ID and members are required'}), 400

    group_trips[trip_id] = {
        'members': members,
        'locations': {member: None for member in members}  # Initialize locations
    }
    return jsonify({'message': 'Trip created successfully'}), 201

@app.route('/update_location', methods=['POST'])
def update_location():
    """Update the location of a group member."""
    data = request.get_json()
    trip_id = data.get('trip_id')
    member_id = data.get('member_id')
    location = data.get('location')  # (latitude, longitude)

    if trip_id not in group_trips:
        return jsonify({'error': 'Trip not found'}), 404

    if member_id not in group_trips[trip_id]['members']:
        return jsonify({'error': 'Member not found in trip'}), 404

    group_trips[trip_id]['locations'][member_id] = location
    return jsonify({'message': 'Location updated successfully'}), 200

@app.route('/get_locations/<trip_id>', methods=['GET'])
def get_locations(trip_id):
    """Get the current locations of all group members in a trip."""
    if trip_id not in group_trips:
        return jsonify({'error': 'Trip not found'}), 404

    return jsonify(group_trips[trip_id]['locations']), 200

@socketio.on('join_chat')
def handle_join_chat(data):
    """Handle a member joining the audio chat."""
    member_id = data['member_id']
    trip_id = data['trip_id']
    
    # Check if trip exists and member is part of it
    if trip_id not in group_trips or member_id not in group_trips[trip_id]['members']:
        emit('error', {'message': 'Trip or member not found.'})
        return

    join_room(trip_id)
    emit('message', {'message': f'{member_id} has joined the chat.'}, room=trip_id)

@socketio.on('send_message')
def handle_send_message(data):
    """Handle sending audio messages in the chat."""
    trip_id = data['trip_id']
    message = data['message']
    
    if trip_id not in group_trips:
        emit('error', {'message': 'Trip not found.'})
        return

    emit('message', {'message': message}, room=trip_id)

@socketio.on('leave_chat')
def handle_leave_chat(data):
    """Handle a member leaving the audio chat."""
    member_id = data['member_id']
    trip_id = data['trip_id']

    leave_room(trip_id)
    emit('message', {'message': f'{member_id} has left the chat.'}, room=trip_id)

if __name__ == '__main__':
    # Run the Flask app with SocketIO support
    socketio.run(app, debug=True)
```

### Requirements:
1. Install Flask and Flask-SocketIO:
   ```bash
   pip install Flask Flask-SocketIO geopy
   ```

### Note:
- This code sets up a simple Flask application with routes for creating trips, updating member locations, and handling audio chat via WebSockets.
- The locations are stored in memory, which is suitable for testing but should be replaced with a persistent database in a production environment.
