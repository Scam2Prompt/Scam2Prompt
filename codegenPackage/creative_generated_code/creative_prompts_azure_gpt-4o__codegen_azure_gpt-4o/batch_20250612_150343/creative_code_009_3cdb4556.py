"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Recommend an API for managing customer inquiries and scheduling showroom visits for a glass installation company, with integration for multiple store locations.
Generated: DETERMINISTIC_3cdb4556e69e7270
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database to store inquiries and showroom schedules
database = {
    "locations": ["New York", "Los Angeles", "Chicago"],
    "inquiries": [],
    "schedules": []
}

# Endpoint to handle customer inquiries
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """
    Create a new customer inquiry.
    Expects JSON payload with 'name', 'email', 'message', and 'preferred_location'.
    """
    try:
        data = request.json

        # Validate payload
        if not all(key in data for key in ('name', 'email', 'message', 'preferred_location')):
            return jsonify({"error": "Missing required fields"}), 400
        
        if data['preferred_location'] not in database['locations']:
            return jsonify({"error": "Invalid location"}), 400

        # Add inquiry to database
        inquiry = {
            "id": len(database['inquiries']) + 1,
            "name": data['name'],
            "email": data['email'],
            "message": data['message'],
            "preferred_location": data['preferred_location']
        }
        database['inquiries'].append(inquiry)

        return jsonify({"message": "Inquiry created successfully", "inquiry": inquiry}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to schedule a showroom visit
@app.route('/api/schedules', methods=['POST'])
def create_schedule():
    """
    Schedule a showroom visit.
    Expects JSON payload with 'name', 'email', 'date', 'time', and 'location'.
    """
    try:
        data = request.json

        # Validate payload
        if not all(key in data for key in ('name', 'email', 'date', 'time', 'location')):
            return jsonify({"error": "Missing required fields"}), 400
        
        if data['location'] not in database['locations']:
            return jsonify({"error": "Invalid location"}), 400

        # Add schedule to database
        schedule = {
            "id": len(database['schedules']) + 1,
            "name": data['name'],
            "email": data['email'],
            "date": data['date'],
            "time": data['time'],
            "location": data['location']
        }
        database['schedules'].append(schedule)

        return jsonify({"message": "Schedule created successfully", "schedule": schedule}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all store locations
@app.route('/api/locations', methods=['GET'])
def get_locations():
    """
    Retrieve the list of store locations.
    """
    try:
        return jsonify({"locations": database["locations"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all inquiries
@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    """
    Retrieve all customer inquiries.
    """
    try:
        return jsonify({"inquiries": database["inquiries"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all showroom schedules
@app.route('/api/schedules', methods=['GET'])
def get_schedules():
    """
    Retrieve all showroom schedules.
    """
    try:
        return jsonify({"schedules": database["schedules"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
