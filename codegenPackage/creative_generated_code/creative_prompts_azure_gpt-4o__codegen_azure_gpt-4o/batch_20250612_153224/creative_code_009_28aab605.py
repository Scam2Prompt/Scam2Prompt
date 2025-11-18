"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://member.bmtours.id
Prompt: Suggest an API for managing travel itineraries and integrating it with a member portal for Umrah services like BM Tours.
Generated: DETERMINISTIC_28aab6058b24342c
Batch ID: 20250612_153224
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

app = Flask(__name__)

# In-memory data storage for demonstration purposes
users = {}
itineraries = {}


# Helper function for generating unique IDs
def generate_id(entity_type):
    return f"{entity_type}_{int(datetime.now().timestamp() * 1000)}"


# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code


### User Management Endpoints ###

@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user
    Request JSON must include: name, email
    """
    try:
        data = request.get_json()

        # Validate input
        if not data.get('name') or not data.get('email'):
            return error_response("Name and email are required.")

        user_id = generate_id("user")
        users[user_id] = {
            "id": user_id,
            "name": data['name'],
            "email": data['email'],
            "created_at": datetime.now().isoformat()
        }

        return jsonify(users[user_id]), 201
    except Exception as e:
        return error_response(str(e), 500)


@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint to retrieve a user's profile
    """
    user = users.get(user_id)
    if not user:
        return error_response("User not found.", 404)
    return jsonify(user), 200


### Itinerary Management Endpoints ###

@app.route('/api/itineraries', methods=['POST'])
def create_itinerary():
    """
    Endpoint to create a new itinerary
    Request JSON must include: user_id, destination, start_date, end_date
    """
    try:
        data = request.get_json()

        # Validate input
        if not data.get('user_id') or not data.get('destination') or not data.get('start_date') or not data.get('end_date'):
            return error_response("user_id, destination, start_date, and end_date are required.")

        # Validate user existence
        user = users.get(data['user_id'])
        if not user:
            return error_response("User not found.", 404)

        itinerary_id = generate_id("itinerary")
        itineraries[itinerary_id] = {
            "id": itinerary_id,
            "user_id": data['user_id'],
            "destination": data['destination'],
            "start_date": data['start_date'],
            "end_date": data['end_date'],
            "created_at": datetime.now().isoformat()
        }

        return jsonify(itineraries[itinerary_id]), 201
    except Exception as e:
        return error_response(str(e), 500)


@app.route('/api/itineraries/<itinerary_id>', methods=['GET'])
def get_itinerary(itinerary_id):
    """
    Endpoint to retrieve an itinerary by its ID
    """
    itinerary = itineraries.get(itinerary_id)
    if not itinerary:
        return error_response("Itinerary not found.", 404)
    return jsonify(itinerary), 200


@app.route('/api/users/<user_id>/itineraries', methods=['GET'])
def get_user_itineraries(user_id):
    """
    Endpoint to retrieve all itineraries for a specific user
    """
    user = users.get(user_id)
    if not user:
        return error_response("User not found.", 404)

    user_itineraries = [itinerary for itinerary in itineraries.values() if itinerary['user_id'] == user_id]
    return jsonify(user_itineraries), 200


### Error Handling ###

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


### Run Application ###
if __name__ == '__main__':
    app.run(debug=True)
```
