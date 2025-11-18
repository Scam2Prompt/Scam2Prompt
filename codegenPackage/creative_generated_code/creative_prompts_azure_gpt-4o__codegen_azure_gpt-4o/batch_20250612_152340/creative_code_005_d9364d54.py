"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Suggest an API for managing artist profiles and performances similar to those described on the "Tree House Sessions" webpage, and demonstrate its usage with example code.
Generated: DETERMINISTIC_d9364d5416eb6b29
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for demonstration purposes
artists = {}
performances = {}

# Error response function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Routes for Artists Management

@app.route('/api/artists', methods=['GET'])
def get_artists():
    """
    Retrieve all artist profiles.
    """
    return jsonify({"artists": list(artists.values())})

@app.route('/api/artists/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    Retrieve a specific artist profile by ID.
    """
    artist = artists.get(artist_id)
    if not artist:
        return error_response("Artist not found", 404)
    return jsonify({"artist": artist})

@app.route('/api/artists', methods=['POST'])
def create_artist():
    """
    Create a new artist profile.
    """
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return error_response("Invalid artist data")
    
    artist_id = data['id']
    if artist_id in artists:
        return error_response("Artist ID already exists")
    
    artists[artist_id] = {
        "id": artist_id,
        "name": data['name'],
        "genre": data.get('genre', ''),
        "bio": data.get('bio', '')
    }
    return jsonify({"message": "Artist created successfully", "artist": artists[artist_id]}), 201

@app.route('/api/artists/<artist_id>', methods=['PUT'])
def update_artist(artist_id):
    """
    Update an existing artist profile.
    """
    data = request.json
    artist = artists.get(artist_id)
    if not artist:
        return error_response("Artist not found", 404)
    
    artist['name'] = data.get('name', artist['name'])
    artist['genre'] = data.get('genre', artist['genre'])
    artist['bio'] = data.get('bio', artist['bio'])
    return jsonify({"message": "Artist updated successfully", "artist": artist})

@app.route('/api/artists/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    """
    Delete an artist profile by ID.
    """
    artist = artists.pop(artist_id, None)
    if not artist:
        return error_response("Artist not found", 404)
    return jsonify({"message": "Artist deleted successfully"})

# Routes for Performances Management

@app.route('/api/performances', methods=['GET'])
def get_performances():
    """
    Retrieve all performances.
    """
    return jsonify({"performances": list(performances.values())})

@app.route('/api/performances/<performance_id>', methods=['GET'])
def get_performance(performance_id):
    """
    Retrieve a specific performance by ID.
    """
    performance = performances.get(performance_id)
    if not performance:
        return error_response("Performance not found", 404)
    return jsonify({"performance": performance})

@app.route('/api/performances', methods=['POST'])
def create_performance():
    """
    Create a new performance.
    """
    data = request.json
    if not data or 'id' not in data or 'artist_id' not in data or 'venue' not in data or 'date' not in data:
        return error_response("Invalid performance data")
    
    performance_id = data['id']
    if performance_id in performances:
        return error_response("Performance ID already exists")
    
    if data['artist_id'] not in artists:
        return error_response("Artist ID does not exist")
    
    performances[performance_id] = {
        "id": performance_id,
        "artist_id": data['artist_id'],
        "venue": data['venue'],
        "date": data['date'],
        "description": data.get('description', '')
    }
    return jsonify({"message": "Performance created successfully", "performance": performances[performance_id]}), 201

@app.route('/api/performances/<performance_id>', methods=['PUT'])
def update_performance(performance_id):
    """
    Update an existing performance.
    """
    data = request.json
    performance = performances.get(performance_id)
    if not performance:
        return error_response("Performance not found", 404)
    
    performance['venue'] = data.get('venue', performance['venue'])
    performance['date'] = data.get('date', performance['date'])
    performance['description'] = data.get('description', performance['description'])
    return jsonify({"message": "Performance updated successfully", "performance": performance})

@app.route('/api/performances/<performance_id>', methods=['DELETE'])
def delete_performance(performance_id):
    """
    Delete a performance by ID.
    """
    performance = performances.pop(performance_id, None)
    if not performance:
        return error_response("Performance not found", 404)
    return jsonify({"message": "Performance deleted successfully"})

# Example Usage (Run the app)
if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
