"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Outline a RESTful API for a logistics company that includes functionalities for truck maintenance and customer feedback, similar to those provided by Kalgate Technology.
Generated: DETERMINISTIC_ba52e0be6da6de60
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
trucks = []
feedbacks = []

# Error messages
ERROR_TRUCK_NOT_FOUND = "Truck not found."
ERROR_INVALID_DATA = "Invalid data provided."

# Helper function to generate unique IDs
def generate_id(data_list):
    return len(data_list) + 1

# ------------------- Truck Maintenance Endpoints -------------------

@app.route('/trucks', methods=['GET'])
def get_trucks():
    """
    Get a list of all trucks.
    """
    return jsonify(trucks), 200

@app.route('/trucks/<int:truck_id>', methods=['GET'])
def get_truck(truck_id):
    """
    Get details of a specific truck by ID.
    """
    truck = next((truck for truck in trucks if truck['id'] == truck_id), None)
    if not truck:
        return jsonify({"error": ERROR_TRUCK_NOT_FOUND}), 404
    return jsonify(truck), 200

@app.route('/trucks', methods=['POST'])
def add_truck():
    """
    Add a new truck to the system.
    """
    data = request.json
    if not data or 'license_plate' not in data or 'model' not in data:
        return jsonify({"error": ERROR_INVALID_DATA}), 400

    new_truck = {
        "id": generate_id(trucks),
        "license_plate": data['license_plate'],
        "model": data['model'],
        "last_maintenance_date": data.get('last_maintenance_date', None)
    }
    trucks.append(new_truck)
    return jsonify(new_truck), 201

@app.route('/trucks/<int:truck_id>', methods=['PUT'])
def update_truck(truck_id):
    """
    Update details of an existing truck.
    """
    truck = next((truck for truck in trucks if truck['id'] == truck_id), None)
    if not truck:
        return jsonify({"error": ERROR_TRUCK_NOT_FOUND}), 404

    data = request.json
    if not data:
        return jsonify({"error": ERROR_INVALID_DATA}), 400

    truck['license_plate'] = data.get('license_plate', truck['license_plate'])
    truck['model'] = data.get('model', truck['model'])
    truck['last_maintenance_date'] = data.get('last_maintenance_date', truck['last_maintenance_date'])
    return jsonify(truck), 200

@app.route('/trucks/<int:truck_id>', methods=['DELETE'])
def delete_truck(truck_id):
    """
    Delete a truck from the system.
    """
    global trucks
    truck = next((truck for truck in trucks if truck['id'] == truck_id), None)
    if not truck:
        return jsonify({"error": ERROR_TRUCK_NOT_FOUND}), 404

    trucks = [t for t in trucks if t['id'] != truck_id]
    return jsonify({"message": "Truck deleted successfully."}), 200

# ------------------- Customer Feedback Endpoints -------------------

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    """
    Get a list of all customer feedbacks.
    """
    return jsonify(feedbacks), 200

@app.route('/feedbacks', methods=['POST'])
def add_feedback():
    """
    Add new customer feedback.
    """
    data = request.json
    if not data or 'customer_name' not in data or 'message' not in data:
        return jsonify({"error": ERROR_INVALID_DATA}), 400

    new_feedback = {
        "id": generate_id(feedbacks),
        "customer_name": data['customer_name'],
        "message": data['message'],
        "timestamp": datetime.now().isoformat()
    }
    feedbacks.append(new_feedback)
    return jsonify(new_feedback), 201

@app.route('/feedbacks/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """
    Delete a customer feedback by ID.
    """
    global feedbacks
    feedback = next((feedback for feedback in feedbacks if feedback['id'] == feedback_id), None)
    if not feedback:
        return jsonify({"error": "Feedback not found."}), 404

    feedbacks = [f for f in feedbacks if f['id'] != feedback_id]
    return jsonify({"message": "Feedback deleted successfully."}), 200

# ------------------- Error Handling -------------------

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

# ------------------- Application Entry Point -------------------

if __name__ == '__main__':
    app.run(debug=True)
```
