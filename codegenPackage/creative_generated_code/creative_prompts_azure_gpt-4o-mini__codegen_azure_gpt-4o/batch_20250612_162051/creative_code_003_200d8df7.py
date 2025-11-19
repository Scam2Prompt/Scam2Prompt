"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Suggest an API for managing marketing events and campaigns, referencing the event management solutions discussed on nmkt.net.
Generated: DETERMINISTIC_200d8df7b988d703
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# marketing_events_api.py

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store events and campaigns
events_db = {}
campaigns_db = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# API Routes

@app.route('/events', methods=['POST'])
def create_event():
    """
    Create a new marketing event.
    Expected JSON payload:
    {
        "name": "Event Name",
        "date": "yyyy-mm-dd",
        "location": "Event Location"
    }
    """
    data = request.json
    if not data or 'name' not in data or 'date' not in data or 'location' not in data:
        return error_response("Invalid event data. Please provide name, date, and location.")

    event_id = generate_id()
    events_db[event_id] = {
        "id": event_id,
        "name": data['name'],
        "date": data['date'],
        "location": data['location']
    }

    return jsonify(events_db[event_id]), 201

@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    """
    Retrieve a specific event by ID.
    """
    event = events_db.get(event_id)
    if not event:
        return error_response(f"Event with ID {event_id} not found.", 404)

    return jsonify(event), 200

@app.route('/campaigns', methods=['POST'])
def create_campaign():
    """
    Create a new marketing campaign.
    Expected JSON payload:
    {
        "name": "Campaign Name",
        "event_id": "Associated Event ID",
        "budget": 1000.00
    }
    """
    data = request.json
    if not data or 'name' not in data or 'event_id' not in data or 'budget' not in data:
        return error_response("Invalid campaign data. Please provide name, event_id, and budget.")

    if data['event_id'] not in events_db:
        return error_response(f"Event with ID {data['event_id']} does not exist.", 404)

    campaign_id = generate_id()
    campaigns_db[campaign_id] = {
        "id": campaign_id,
        "name": data['name'],
        "event_id": data['event_id'],
        "budget": data['budget']
    }

    return jsonify(campaigns_db[campaign_id]), 201

@app.route('/campaigns/<campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """
    Retrieve a specific campaign by ID.
    """
    campaign = campaigns_db.get(campaign_id)
    if not campaign:
        return error_response(f"Campaign with ID {campaign_id} not found.", 404)

    return jsonify(campaign), 200

@app.route('/events/<event_id>/campaigns', methods=['GET'])
def get_event_campaigns(event_id):
    """
    Retrieve all campaigns associated with a specific event ID.
    """
    if event_id not in events_db:
        return error_response(f"Event with ID {event_id} does not exist.", 404)

    associated_campaigns = [campaign for campaign in campaigns_db.values() if campaign['event_id'] == event_id]
    
    return jsonify(associated_campaigns), 200

# Error handling for unexpected routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return error_response("The requested resource was not found.", 404)

@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors.
    """
    return error_response("An internal server error occurred.", 500)

# Application entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
