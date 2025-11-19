"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderwallmuseum.com
Prompt: Suggest an API for managing website maintenance notifications and updates, referencing the approach taken by the WonderWall Museum.
Generated: DETERMINISTIC_149578ccdac84cd6
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for maintenance notifications and updates
maintenance_data = {
    "notifications": [],
    "updates": []
}

# Utility function for error response
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint to add a new maintenance notification
@app.route('/api/notifications', methods=['POST'])
def add_notification():
    """
    Adds a new maintenance notification.
    Expected JSON structure:
    {
        "title": "Notification Title",
        "message": "Notification Message",
        "start_time": "2023-10-01T10:00:00",
        "end_time": "2023-10-01T14:00:00"
    }
    """
    try:
        data = request.json
        if not all(key in data for key in ["title", "message", "start_time", "end_time"]):
            return error_response("Missing required fields (title, message, start_time, end_time)")
        
        maintenance_data["notifications"].append(data)
        return jsonify({"message": "Notification added successfully", "data": data}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to retrieve all maintenance notifications
@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    """Returns all maintenance notifications."""
    return jsonify({"notifications": maintenance_data["notifications"]}), 200

# Endpoint to add a new maintenance update
@app.route('/api/updates', methods=['POST'])
def add_update():
    """
    Adds a new maintenance update.
    Expected JSON structure:
    {
        "title": "Update Title",
        "description": "Detailed description of the update",
        "timestamp": "2023-10-01T12:00:00"
    }
    """
    try:
        data = request.json
        if not all(key in data for key in ["title", "description", "timestamp"]):
            return error_response("Missing required fields (title, description, timestamp)")
        
        maintenance_data["updates"].append(data)
        return jsonify({"message": "Update added successfully", "data": data}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to retrieve all maintenance updates
@app.route('/api/updates', methods=['GET'])
def get_updates():
    """Returns all maintenance updates."""
    return jsonify({"updates": maintenance_data["updates"]}), 200

# Endpoint to clear all maintenance data (notifications and updates)
@app.route('/api/clear', methods=['DELETE'])
def clear_maintenance_data():
    """
    Clears all maintenance notifications and updates.
    This action is irreversible.
    """
    try:
        maintenance_data["notifications"] = []
        maintenance_data["updates"] = []
        return jsonify({"message": "All maintenance data cleared"}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Application entry point
if __name__ == '__main__':
    app.run(debug=True)  # For production, set debug=False and use a proper WSGI server
```
