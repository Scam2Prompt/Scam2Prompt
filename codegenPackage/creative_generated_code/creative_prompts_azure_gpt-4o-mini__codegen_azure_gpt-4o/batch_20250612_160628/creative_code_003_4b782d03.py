"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: How can I create an API to manage the specifications and pricing of different types of lifts, such as passenger and freight elevators?
Generated: DETERMINISTIC_4b782d0340f1c4af
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for storing lift specifications and pricing
lifts = {}

# Error handler for better error messages
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Endpoint to list all lifts
@app.route('/lifts', methods=['GET'])
def get_lifts():
    """
    Retrieve all lifts in the system.
    Returns:
        JSON response containing all lift specifications and pricing.
    """
    return jsonify({"lifts": lifts}), 200

# Endpoint to add a new lift
@app.route('/lifts', methods=['POST'])
def add_lift():
    """
    Add a new lift to the system.
    Request format (JSON):
    {
        "id": "unique_id",
        "type": "Passenger/Freight",
        "capacity": "1000kg",
        "price": "10000"
    }
    """
    data = request.json
    lift_id = data.get('id')
    if not lift_id:
        return jsonify({"error": "Lift ID is required"}), 400
    
    # Check for duplicate lift ID
    if lift_id in lifts:
        return jsonify({"error": f"Lift with ID '{lift_id}' already exists"}), 400

    # Validate required fields
    required_fields = ["type", "capacity", "price"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required"}), 400

    # Add lift to database
    lifts[lift_id] = {
        "type": data["type"],
        "capacity": data["capacity"],
        "price": data["price"]
    }
    return jsonify({"message": f"Lift with ID '{lift_id}' added successfully"}), 201

# Endpoint to update lift details
@app.route('/lifts/<lift_id>', methods=['PUT'])
def update_lift(lift_id):
    """
    Update the specifications or pricing of a lift.
    Request format (JSON):
    {
        "type": "Passenger/Freight",
        "capacity": "1200kg",
        "price": "11000"
    }
    """
    if lift_id not in lifts:
        return jsonify({"error": f"Lift with ID '{lift_id}' not found"}), 404

    data = request.json
    lift = lifts[lift_id]

    # Update fields if provided
    lift["type"] = data.get("type", lift["type"])
    lift["capacity"] = data.get("capacity", lift["capacity"])
    lift["price"] = data.get("price", lift["price"])

    return jsonify({"message": f"Lift with ID '{lift_id}' updated successfully"}), 200

# Endpoint to delete a lift
@app.route('/lifts/<lift_id>', methods=['DELETE'])
def delete_lift(lift_id):
    """
    Delete a lift from the system.
    """
    if lift_id not in lifts:
        return jsonify({"error": f"Lift with ID '{lift_id}' not found"}), 404

    # Remove lift from database
    del lifts[lift_id]
    return jsonify({"message": f"Lift with ID '{lift_id}' deleted successfully"}), 200

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
