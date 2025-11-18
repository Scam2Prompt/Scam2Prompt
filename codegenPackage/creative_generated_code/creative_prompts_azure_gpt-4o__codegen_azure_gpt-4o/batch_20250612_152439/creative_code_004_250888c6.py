"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-fi.pages.dev
Prompt: Write code to simulate a virtual meeting room in a metaverse environment, incorporating features like portfolio showcases and job fairs, inspired by DeeLance's thematic rooms.
Generated: DETERMINISTIC_250888c67b1717e6
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# In-memory database to simulate room functionality and user data
rooms = {
    "portfolio_showcase": {
        "name": "Portfolio Showcase Room",
        "description": "A virtual space to showcase portfolios and creative work.",
        "events": [],
        "users": []
    },
    "job_fair": {
        "name": "Job Fair Room",
        "description": "A virtual space for job seekers and recruiters to connect.",
        "events": [],
        "users": []
    }
}

# Error handling: Custom exception for invalid room access
class RoomNotFoundError(Exception):
    pass

@app.errorhandler(RoomNotFoundError)
def handle_room_not_found_error(e):
    return jsonify({"error": str(e)}), 404

# Endpoint to get details of all rooms
@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms)

# Endpoint to join a room
@app.route('/rooms/<room_name>/join', methods=['POST'])
def join_room(room_name):
    user_data = request.json
    if room_name not in rooms:
        raise RoomNotFoundError(f"Room '{room_name}' not found.")
    
    # Add user to the room
    user = {
        "name": user_data.get("name"),
        "joined_at": datetime.datetime.now().isoformat()
    }
    rooms[room_name]["users"].append(user)
    return jsonify({"message": f"User '{user['name']}' has joined the room '{room_name}'."})

# Endpoint to add an event to a room
@app.route('/rooms/<room_name>/events', methods=['POST'])
def add_event(room_name):
    event_data = request.json
    if room_name not in rooms:
        raise RoomNotFoundError(f"Room '{room_name}' not found.")
    
    # Add event to the room
    event = {
        "title": event_data.get("title"),
        "description": event_data.get("description"),
        "scheduled_date": event_data.get("scheduled_date")
    }
    rooms[room_name]["events"].append(event)
    return jsonify({"message": f"Event '{event['title']}' has been added to room '{room_name}'."})

# Endpoint to list users in a room
@app.route('/rooms/<room_name>/users', methods=['GET'])
def list_users(room_name):
    if room_name not in rooms:
        raise RoomNotFoundError(f"Room '{room_name}' not found.")
    
    return jsonify(rooms[room_name]["users"])

# Endpoint to list events in a room
@app.route('/rooms/<room_name>/events', methods=['GET'])
def list_events(room_name):
    if room_name not in rooms:
        raise RoomNotFoundError(f"Room '{room_name}' not found.")
    
    return jsonify(rooms[room_name]["events"])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic simulation of a virtual meeting environment using Flask, with features for portfolio showcases and job fairs. It includes endpoints for room management, user interactions, and event planning, all while following best practices for clean and maintainable production-ready code.
