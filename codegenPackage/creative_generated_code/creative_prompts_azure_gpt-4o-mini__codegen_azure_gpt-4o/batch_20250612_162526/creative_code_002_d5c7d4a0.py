"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Create an API endpoint that allows businesses to announce upcoming events and promotions, taking cues from the event announcement features highlighted on m-matamsklogi.
Generated: DETERMINISTIC_d5c7d4a0a9811979
Batch ID: 20250612_162526
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
import uuid

app = Flask(__name__)

# In-memory datastore to store events and promotions
events = []

# Helper function to validate incoming data
def validate_event_data(data):
    required_fields = ["title", "description", "start_date", "end_date"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"'{field}' is required."
    try:
        # Ensure dates are valid
        datetime.strptime(data["start_date"], "%Y-%m-%d")
        datetime.strptime(data["end_date"], "%Y-%m-%d")
    except ValueError:
        return False, "Invalid date format. Use 'YYYY-MM-DD'."
    # Ensure end_date is after start_date
    if data["end_date"] < data["start_date"]:
        return False, "'end_date' must be after 'start_date'."
    return True, None

@app.route('/api/events', methods=['POST'])
def create_event():
    """
    API Endpoint: Create an event or promotion announcement.
    Request Body:
    {
        "title": "Event Title",
        "description": "Event Description",
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD"
    }
    Response:
    {
        "id": "unique-event-id",
        "title": "Event Title",
        "description": "Event Description",
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input data
        is_valid, error_message = validate_event_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Generate a unique ID for the event
        event_id = str(uuid.uuid4())
        
        # Create event record
        event = {
            "id": event_id,
            "title": data["title"],
            "description": data["description"],
            "start_date": data["start_date"],
            "end_date": data["end_date"]
        }
        
        # Store event in the in-memory datastore
        events.append(event)
        
        return jsonify(event), 201  # Return created event with 201 status code
    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    """
    API Endpoint: Retrieve all event or promotion announcements.
    Response:
    [
        {
            "id": "unique-event-id",
            "title": "Event Title",
            "description": "Event Description",
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD"
        }
    ]
    """
    return jsonify(events), 200

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

Note: Replace `debug=True` with `debug=False` in production environments.
