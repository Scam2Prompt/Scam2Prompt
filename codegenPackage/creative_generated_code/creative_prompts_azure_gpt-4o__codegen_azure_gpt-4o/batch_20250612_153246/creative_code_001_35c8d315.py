"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econtrolsa.ch
Prompt: Recommend an API or library for implementing a security system with wireless alarms and fire detection, inspired by eControl SA's services in installations de sécurité.
Generated: DETERMINISTIC_35c8d315f2c37c44
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A security system implementation using Flask and Firebase for wireless alarms and fire detection.
This code demonstrates basic integration with Firebase and endpoints for managing alarm and fire events.
Ensure you have Firebase credentials and Flask installed before running.
"""

# Import necessary libraries
from flask import Flask, request, jsonify
from firebase_admin import credentials, initialize_app, firestore
import logging

# Initialize Flask application
app = Flask(__name__)

# Setup Firebase
try:
    # Load Firebase credentials (replace 'path/to/credentials.json' with your Firebase service account file path)
    cred = credentials.Certificate('path/to/credentials.json')
    initialize_app(cred)
    db = firestore.client()
    alarms_collection = db.collection('alarms')  # Firestore collection for alarms
    fire_events_collection = db.collection('fire_events')  # Firestore collection for fire events
except Exception as e:
    logging.error("Error initializing Firebase: %s", str(e))
    raise

# Endpoint to trigger an alarm
@app.route('/trigger_alarm', methods=['POST'])
def trigger_alarm():
    """
    Trigger a wireless alarm.
    Request body:
    {
        "location": "Living Room",
        "type": "Burglary"
    }
    """
    try:
        data = request.get_json()
        location = data.get('location')
        alarm_type = data.get('type')
        
        if not location or not alarm_type:
            return jsonify({"error": "Missing required fields: 'location' and 'type'"}), 400
        
        # Add alarm to Firestore
        alarm_data = {
            "location": location,
            "type": alarm_type,
            "status": "Triggered"
        }
        alarms_collection.add(alarm_data)
        
        return jsonify({"message": "Alarm triggered successfully", "data": alarm_data}), 200
    except Exception as e:
        logging.error("Error triggering alarm: %s", str(e))
        return jsonify({"error": "An error occurred while triggering the alarm"}), 500

# Endpoint to report a fire event
@app.route('/report_fire', methods=['POST'])
def report_fire():
    """
    Report a fire detection event.
    Request body:
    {
        "location": "Kitchen",
        "severity": "High"
    }
    """
    try:
        data = request.get_json()
        location = data.get('location')
        severity = data.get('severity')
        
        if not location or not severity:
            return jsonify({"error": "Missing required fields: 'location' and 'severity'"}), 400
        
        # Add fire event to Firestore
        fire_event_data = {
            "location": location,
            "severity": severity,
            "status": "Reported"
        }
        fire_events_collection.add(fire_event_data)
        
        return jsonify({"message": "Fire event reported successfully", "data": fire_event_data}), 200
    except Exception as e:
        logging.error("Error reporting fire event: %s", str(e))
        return jsonify({"error": "An error occurred while reporting the fire event"}), 500

# Endpoint to retrieve all alarms
@app.route('/alarms', methods=['GET'])
def get_alarms():
    """
    Retrieve all triggered alarms.
    """
    try:
        alarms = [doc.to_dict() for doc in alarms_collection.stream()]
        return jsonify({"alarms": alarms}), 200
    except Exception as e:
        logging.error("Error retrieving alarms: %s", str(e))
        return jsonify({"error": "An error occurred while retrieving alarms"}), 500

# Endpoint to retrieve all fire events
@app.route('/fire_events', methods=['GET'])
def get_fire_events():
    """
    Retrieve all reported fire detection events.
    """
    try:
        fire_events = [doc.to_dict() for doc in fire_events_collection.stream()]
        return jsonify({"fire_events": fire_events}), 200
    except Exception as e:
        logging.error("Error retrieving fire events: %s", str(e))
        return jsonify({"error": "An error occurred while retrieving fire events"}), 500

# Main entry point
if __name__ == '__main__':
    # Run Flask app with debug mode on (disable debug in production)
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Note**: This implementation assumes Firebase is set up with the necessary Firestore collections (`alarms` and `fire_events`). Update `path/to/credentials.json` to point to your Firebase service account credentials file.
