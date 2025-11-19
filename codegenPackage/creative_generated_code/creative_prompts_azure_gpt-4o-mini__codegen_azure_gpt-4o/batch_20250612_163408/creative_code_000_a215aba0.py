"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: How can I implement a refuse and recycling collection API for a city similar to the City of York?
Generated: DETERMINISTIC_a215aba0b1f652ea
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# Static data - In a real-world scenario, this would likely be retrieved from a database
COLLECTION_SCHEDULE = {
    "ZoneA": {
        "refuse": ["Monday", "Thursday"],
        "recycling": ["Tuesday", "Friday"]
    },
    "ZoneB": {
        "refuse": ["Wednesday", "Saturday"],
        "recycling": ["Thursday", "Sunday"]
    }
}

# Error handler for invalid zones
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Zone not found"}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Invalid request"}), 400

# Helper function to validate zone input
def validate_zone(zone):
    if zone not in COLLECTION_SCHEDULE:
        return False
    return True

# Route to get refuse and recycling collection days for a given zone
@app.route('/api/collection_schedule/<zone>', methods=['GET'])
def get_collection_schedule(zone):
    # Check if the zone exists in the schedule
    if not validate_zone(zone):
        return not_found_error("Zone not found")
    
    # Fetch the schedule for the requested zone
    schedule = COLLECTION_SCHEDULE[zone]
    return jsonify({
        "zone": zone,
        "collection_days": schedule
    })

# Route to check if there's a collection today for a given zone
@app.route('/api/collection_today/<zone>', methods=['GET'])
def check_collection_today(zone):
    # Check if the zone exists
    if not validate_zone(zone):
        return not_found_error("Zone not found")
    
    # Get today's weekday name
    today = datetime.datetime.now().strftime('%A')
    
    # Fetch the schedule for the requested zone
    schedule = COLLECTION_SCHEDULE[zone]
    
    # Determine if there is a collection today
    collection_types = []
    if today in schedule["refuse"]:
        collection_types.append("refuse")
    if today in schedule["recycling"]:
        collection_types.append("recycling")
    
    return jsonify({
        "zone": zone,
        "date": today,
        "collection_today": collection_types
    })

# Route to add a new collection schedule for a zone
@app.route('/api/add_schedule', methods=['POST'])
def add_schedule():
    data = request.get_json()
    
    # Validate request data
    if not data or 'zone' not in data or 'refuse' not in data or 'recycling' not in data:
        return bad_request_error("Invalid request data")
    
    zone = data['zone']
    refuse_days = data['refuse']
    recycling_days = data['recycling']
    
    # Check if schedule already exists for the zone
    if zone in COLLECTION_SCHEDULE:
        return jsonify({"error": f"Schedule already exists for zone {zone}"}), 400
    
    # Add the new schedule
    COLLECTION_SCHEDULE[zone] = {
        "refuse": refuse_days,
        "recycling": recycling_days
    }
    
    return jsonify({"message": f"Schedule added for zone {zone}"}), 201

# Route to update an existing collection schedule
@app.route('/api/update_schedule/<zone>', methods=['PUT'])
def update_schedule(zone):
    if not validate_zone(zone):
        return not_found_error("Zone not found")
    
    data = request.get_json()
    
    # Validate request data
    if not data or 'refuse' not in data or 'recycling' not in data:
        return bad_request_error("Invalid request data")
    
    refuse_days = data['refuse']
    recycling_days = data['recycling']
    
    # Update the schedule
    COLLECTION_SCHEDULE[zone] = {
        "refuse": refuse_days,
        "recycling": recycling_days
    }
    
    return jsonify({"message": f"Schedule updated for zone {zone}"}), 200

# Route to delete a zone's collection schedule
@app.route('/api/delete_schedule/<zone>', methods=['DELETE'])
def delete_schedule(zone):
    if not validate_zone(zone):
        return not_found_error("Zone not found")
    
    # Delete the schedule
    del COLLECTION_SCHEDULE[zone]
    return jsonify({"message": f"Schedule deleted for zone {zone}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
