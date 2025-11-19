"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Outline a RESTful API for a logistics company that includes functionalities for truck maintenance and customer feedback, similar to those provided by Kalgate Technology.
Generated: DETERMINISTIC_ba52e0be6da6de60
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: RESTful API for a logistics company with functionalities for truck maintenance and customer feedback.

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage (For demonstration purposes, use a database in production)
trucks = []
feedbacks = []

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for 404 errors."""
    return jsonify({"error": "Resource not found"}), 404


# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """Return a JSON response for 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


# -----------------------------------------------
# Truck Maintenance Endpoints
# -----------------------------------------------

@app.route('/trucks', methods=['GET'])
def get_trucks():
    """
    Endpoint to retrieve all trucks.
    Returns:
        JSON list of all trucks.
    """
    return jsonify(trucks), 200


@app.route('/trucks', methods=['POST'])
def add_truck():
    """
    Endpoint to add a new truck.
    Request Body:
        {
            "truck_id": str,
            "model": str,
            "year": int,
            "last_maintenance_date": str
        }
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.json
        truck_id = data.get('truck_id')
        model = data.get('model')
        year = data.get('year')
        last_maintenance_date = data.get('last_maintenance_date')

        if not truck_id or not model or not year or not last_maintenance_date:
            return jsonify({"error": "Missing required fields"}), 400

        new_truck = {
            "truck_id": truck_id,
            "model": model,
            "year": year,
            "last_maintenance_date": last_maintenance_date
        }
        trucks.append(new_truck)
        return jsonify({"message": "Truck added successfully", "truck": new_truck}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/trucks/<string:truck_id>', methods=['PUT'])
def update_truck(truck_id):
    """
    Endpoint to update truck details.
    Request Body:
        {
            "model": str,
            "year": int,
            "last_maintenance_date": str
        }
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.json
        for truck in trucks:
            if truck['truck_id'] == truck_id:
                truck['model'] = data.get('model', truck['model'])
                truck['year'] = data.get('year', truck['year'])
                truck['last_maintenance_date'] = data.get('last_maintenance_date', truck['last_maintenance_date'])
                return jsonify({"message": "Truck updated successfully", "truck": truck}), 200
        return jsonify({"error": "Truck not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/trucks/<string:truck_id>', methods=['DELETE'])
def delete_truck(truck_id):
    """
    Endpoint to delete a truck.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        global trucks
        trucks = [truck for truck in trucks if truck['truck_id'] != truck_id]
        return jsonify({"message": "Truck deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------------------------
# Customer Feedback Endpoints
# -----------------------------------------------

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    """
    Endpoint to retrieve all customer feedbacks.
    Returns:
        JSON list of all feedbacks.
    """
    return jsonify(feedbacks), 200


@app.route('/feedbacks', methods=['POST'])
def add_feedback():
    """
    Endpoint to add customer feedback.
    Request Body:
        {
            "feedback_id": str,
            "customer_name": str,
            "feedback": str,
            "rating": int
        }
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.json
        feedback_id = data.get('feedback_id')
        customer_name = data.get('customer_name')
        feedback = data.get('feedback')
        rating = data.get('rating')

        if not feedback_id or not customer_name or not feedback or not rating:
            return jsonify({"error": "Missing required fields"}), 400

        new_feedback = {
            "feedback_id": feedback_id,
            "customer_name": customer_name,
            "feedback": feedback,
            "rating": rating
        }
        feedbacks.append(new_feedback)
        return jsonify({"message": "Feedback added successfully", "feedback": new_feedback}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/feedbacks/<string:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    """
    Endpoint to update customer feedback.
    Request Body:
        {
            "feedback": str,
            "rating": int
        }
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.json
        for feedback in feedbacks:
            if feedback['feedback_id'] == feedback_id:
                feedback['feedback'] = data.get('feedback', feedback['feedback'])
                feedback['rating'] = data.get('rating', feedback['rating'])
                return jsonify({"message": "Feedback updated successfully", "feedback": feedback}), 200
        return jsonify({"error": "Feedback not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/feedbacks/<string:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """
    Endpoint to delete customer feedback.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        global feedbacks
        feedbacks = [feedback for feedback in feedbacks if feedback['feedback_id'] != feedback_id]
        return jsonify({"message": "Feedback deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------------------------
# Run the Flask application
# -----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
```
