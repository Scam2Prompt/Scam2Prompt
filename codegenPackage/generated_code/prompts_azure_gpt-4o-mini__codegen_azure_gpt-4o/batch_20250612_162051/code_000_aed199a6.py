"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Generate a code snippet for a travel booking API that allows users to create custom itineraries for group trips, similar to the unique itineraries offered by Rehiletes.
Generated: DETERMINISTIC_aed199a6ef403a4a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for itineraries (for demonstration purposes)
itineraries = {}

# Error messages
ERROR_ITINERARY_NOT_FOUND = "Itinerary not found."
ERROR_INVALID_REQUEST = "Invalid request data."

# Helper function to validate itinerary data
def validate_itinerary_data(data):
    required_fields = ["name", "destination", "start_date", "end_date", "activities"]
    for field in required_fields:
        if field not in data:
            return False
    return True

@app.route('/api/itineraries', methods=['POST'])
def create_itinerary():
    """
    Endpoint to create a new custom itinerary for a group trip.
    Expects JSON payload with the following fields:
    - name: Name of the itinerary
    - destination: Destination of the trip
    - start_date: Start date of the trip (YYYY-MM-DD)
    - end_date: End date of the trip (YYYY-MM-DD)
    - activities: List of activities planned for the trip
    """
    try:
        data = request.get_json()
        if not data or not validate_itinerary_data(data):
            return jsonify({"error": ERROR_INVALID_REQUEST}), 400

        itinerary_id = str(uuid4())  # Generate a unique ID for the itinerary
        itineraries[itinerary_id] = {
            "id": itinerary_id,
            "name": data["name"],
            "destination": data["destination"],
            "start_date": data["start_date"],
            "end_date": data["end_date"],
            "activities": data["activities"]
        }

        return jsonify({"message": "Itinerary created successfully.", "itinerary": itineraries[itinerary_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/itineraries/<itinerary_id>', methods=['GET'])
def get_itinerary(itinerary_id):
    """
    Endpoint to retrieve a specific itinerary by its ID.
    """
    try:
        itinerary = itineraries.get(itinerary_id)
        if not itinerary:
            return jsonify({"error": ERROR_ITINERARY_NOT_FOUND}), 404

        return jsonify({"itinerary": itinerary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/itineraries/<itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    """
    Endpoint to delete a specific itinerary by its ID.
    """
    try:
        if itinerary_id not in itineraries:
            return jsonify({"error": ERROR_ITINERARY_NOT_FOUND}), 404

        del itineraries[itinerary_id]
        return jsonify({"message": "Itinerary deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/itineraries', methods=['GET'])
def list_itineraries():
    """
    Endpoint to list all itineraries.
    """
    try:
        return jsonify({"itineraries": list(itineraries.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
