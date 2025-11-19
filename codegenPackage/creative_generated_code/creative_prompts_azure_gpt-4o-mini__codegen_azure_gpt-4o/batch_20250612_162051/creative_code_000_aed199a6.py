"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Generate a code snippet for a travel booking API that allows users to create custom itineraries for group trips, similar to the unique itineraries offered by Rehiletes.
Generated: DETERMINISTIC_aed199a6ef403a4a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for itineraries
itineraries = {}

# Utility function for error response
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

@app.route('/api/itineraries', methods=['POST'])
def create_itinerary():
    """
    Create a custom itinerary for a group trip.
    Request format: JSON
    {
        "name": "Beach Getaway",
        "destination": "Cancun",
        "start_date": "2023-12-01",
        "end_date": "2023-12-07",
        "group_size": 5,
        "activities": ["Snorkeling", "Visit Ruins", "Relax on the Beach"]
    }
    """
    try:
        data = request.json

        # Validate required fields
        required_fields = ["name", "destination", "start_date", "end_date", "group_size", "activities"]
        for field in required_fields:
            if field not in data:
                return error_response(f"Missing required field: {field}")

        # Validate data types
        if not isinstance(data["group_size"], int) or data["group_size"] <= 0:
            return error_response("Group size must be a positive integer.")
        if not isinstance(data["activities"], list) or len(data["activities"]) == 0:
            return error_response("Activities must be a non-empty list.")

        # Generate unique ID for the itinerary
        itinerary_id = str(uuid.uuid4())

        # Create the itinerary object
        itinerary = {
            "id": itinerary_id,
            "name": data["name"],
            "destination": data["destination"],
            "start_date": data["start_date"],
            "end_date": data["end_date"],
            "group_size": data["group_size"],
            "activities": data["activities"]
        }

        # Store the itinerary
        itineraries[itinerary_id] = itinerary

        return jsonify({"message": "Itinerary created successfully!", "itinerary": itinerary}), 201

    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

@app.route('/api/itineraries/<itinerary_id>', methods=['GET'])
def get_itinerary(itinerary_id):
    """
    Retrieve itinerary details by ID.
    """
    try:
        itinerary = itineraries.get(itinerary_id)
        if not itinerary:
            return error_response("Itinerary not found.", 404)
        return jsonify(itinerary), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

@app.route('/api/itineraries/<itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    """
    Delete an itinerary by ID.
    """
    try:
        if itinerary_id not in itineraries:
            return error_response("Itinerary not found.", 404)
        
        del itineraries[itinerary_id]
        return jsonify({"message": "Itinerary deleted successfully."}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask to create a RESTful API.
- In-memory storage (`itineraries`) is used for simplicity. In production, replace this with a database.
- Proper error handling is included.
- JSON input validation checks ensure robustness.
