"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Generate a code snippet for a web analytics tool that helps businesses understand and utilize data effectively, as discussed on Star Shot 90.
Generated: DETERMINISTIC_a4b48fc676792ce9
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for analytics data
analytics_data = []

@app.route('/track_event', methods=['POST'])
def track_event():
    """
    Endpoint to track user events for analytics.
    Expects a JSON payload with 'event_name' and 'event_data'.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        
        # Validate the incoming data
        if not data or 'event_name' not in data or 'event_data' not in data:
            logging.error("Invalid data received: %s", data)
            return jsonify({"error": "Invalid data"}), 400
        
        # Store the event data
        event = {
            "event_name": data['event_name'],
            "event_data": data['event_data'],
            "timestamp": request.timestamp
        }
        analytics_data.append(event)
        
        logging.info("Event tracked: %s", event)
        return jsonify({"message": "Event tracked successfully"}), 201

    except Exception as e:
        logging.exception("Error tracking event: %s", e)
        return jsonify({"error": "Internal server error"}), 500

@app.route('/get_analytics', methods=['GET'])
def get_analytics():
    """
    Endpoint to retrieve tracked analytics data.
    Returns the stored analytics data in JSON format.
    """
    try:
        return jsonify(analytics_data), 200
    except Exception as e:
        logging.exception("Error retrieving analytics data: %s", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
```
