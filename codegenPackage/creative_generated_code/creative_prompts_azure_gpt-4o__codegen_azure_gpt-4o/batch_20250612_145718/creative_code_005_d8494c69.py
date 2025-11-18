"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Design a game API for managing Squad Kombat characters, skins, and time-limited events, referencing the Q3 2024 launch details from the Hamster Kombat roadmap.
Generated: DETERMINISTIC_d8494c69de523ae1
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory data storage (would be replaced with a database in production)
characters = {}
skins = {}
events = {}

# Helper function for generating unique IDs
def generate_id():
    return str(uuid.uuid4())

# Helper function for validating JSON requests
def validate_request(required_fields, data):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None

# API endpoint: Create a new character
@app.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    valid, error = validate_request(['name', 'abilities'], data)
    if not valid:
        return jsonify({'error': error}), 400
    
    character_id = generate_id()
    characters[character_id] = {
        'id': character_id,
        'name': data['name'],
        'abilities': data['abilities'],
        'created_at': datetime.utcnow()
    }
    return jsonify(characters[character_id]), 201

# API endpoint: Get all characters
@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(list(characters.values()))

# API endpoint: Create a new skin
@app.route('/skins', methods=['POST'])
def create_skin():
    data = request.json
    valid, error = validate_request(['name', 'character_id', 'rarity'], data)
    if not valid:
        return jsonify({'error': error}), 400

    if data['character_id'] not in characters:
        return jsonify({'error': 'Invalid character_id'}), 404

    skin_id = generate_id()
    skins[skin_id] = {
        'id': skin_id,
        'name': data['name'],
        'character_id': data['character_id'],
        'rarity': data['rarity'],
        'created_at': datetime.utcnow()
    }
    return jsonify(skins[skin_id]), 201

# API endpoint: Get all skins
@app.route('/skins', methods=['GET'])
def get_skins():
    return jsonify(list(skins.values()))

# API endpoint: Create a time-limited event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    valid, error = validate_request(['name', 'start_time', 'duration'], data)
    if not valid:
        return jsonify({'error': error}), 400

    try:
        start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
        duration = timedelta(hours=data['duration'])
    except ValueError:
        return jsonify({'error': 'Invalid date format or duration'}), 400

    event_id = generate_id()
    events[event_id] = {
        'id': event_id,
        'name': data['name'],
        'start_time': start_time,
        'end_time': start_time + duration,
        'created_at': datetime.utcnow()
    }
    return jsonify(events[event_id]), 201

# API endpoint: Get active events
@app.route('/events/active', methods=['GET'])
def get_active_events():
    current_time = datetime.utcnow()
    active_events = [
        event for event in events.values()
        if event['start_time'] <= current_time <= event['end_time']
    ]
    return jsonify(active_events)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

# Error handling for 500
@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
