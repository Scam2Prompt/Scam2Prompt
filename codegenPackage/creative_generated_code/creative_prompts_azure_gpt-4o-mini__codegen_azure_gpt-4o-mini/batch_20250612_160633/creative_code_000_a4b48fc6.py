"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starshot90.com
Prompt: Generate a code snippet for a web analytics tool that helps businesses understand and utilize data effectively, as discussed on Star Shot 90.
Generated: DETERMINISTIC_a4b48fc676792ce9
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# In-memory storage for analytics data
analytics_data = []

@app.route('/track_event', methods=['POST'])
def track_event():
    """
    Endpoint to track user events.

    Expected JSON payload:
    {
        "event": "string",
        "user_id": "string",
        "timestamp": "string" (ISO 8601 format)
    }
    """
    try:
        # Validate request data
        data = request.get_json()
        if not data or 'event' not in data or 'user_id' not in data or 'timestamp' not in data:
            raise ValueError("Invalid payload. 'event', 'user_id', and 'timestamp' are required.")

        # Log the received event
        logging.info(f"Tracking event: {data['event']} for user: {data['user_id']} at {data['timestamp']}")

        # Store the event data
        analytics_data.append(data)

        return jsonify({"status": "success", "message": "Event tracked successfully."}), 201

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({"status": "error", "message": str(ve)}), 400
    except Exception as e:
        logging.error(f"Exception: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500

@app.route('/get_data', methods=['GET'])
def get_data():
    """
    Endpoint to retrieve tracked analytics data.

    Returns:
    JSON array of tracked events.
    """
    try:
        # Return the stored analytics data
        return jsonify({"status": "success", "data": analytics_data}), 200

    except Exception as e:
        logging.error(f"Exception while retrieving data: {e}")
        return jsonify({"status": "error", "message": "An error occurred while retrieving data."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
