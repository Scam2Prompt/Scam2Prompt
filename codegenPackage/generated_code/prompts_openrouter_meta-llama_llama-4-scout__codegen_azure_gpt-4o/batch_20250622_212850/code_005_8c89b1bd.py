"""
Generated Code Metadata:
========================
Original URL: https://greencreditbuilder.com
Prompt: "Design a RESTful API for a Green Credit Builder-like platform that accepts climate-positive activity data and returns credit scores or recommendations."
Generated: DETERMINISTIC_8c89b1bddf0f1683
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
# In production, replace with a proper database
user_data = {}

# Helper function to calculate credit score based on activity data
def calculate_credit_score(activity_data):
    """
    Calculate credit score based on climate-positive activity data.
    :param activity_data: List of activity dictionaries
    :return: Integer credit score
    """
    score = 0
    for activity in activity_data:
        if activity.get("type") == "tree_planting":
            score += activity.get("quantity", 0) * 10
        elif activity.get("type") == "solar_installation":
            score += activity.get("quantity", 0) * 20
        elif activity.get("type") == "recycling":
            score += activity.get("quantity", 0) * 5
    return score

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions and return JSON responses.
    """
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.route('/api/users/<user_id>/activities', methods=['POST'])
def add_activity(user_id):
    """
    Endpoint to add climate-positive activity data for a user.
    :param user_id: ID of the user
    :return: JSON response with success message
    """
    try:
        activity_data = request.json
        if not activity_data or not isinstance(activity_data, dict):
            return jsonify({"error": "Invalid activity data"}), 400

        user_data.setdefault(user_id, []).append(activity_data)
        return jsonify({"message": "Activity added successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@app.route('/api/users/<user_id>/credit-score', methods=['GET'])
def get_credit_score(user_id):
    """
    Endpoint to retrieve the credit score for a user based on their activities.
    :param user_id: ID of the user
    :return: JSON response with credit score
    """
    try:
        activities = user_data.get(user_id, [])
        credit_score = calculate_credit_score(activities)
        return jsonify({"user_id": user_id, "credit_score": credit_score}), 200
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@app.route('/api/users/<user_id>/recommendations', methods=['GET'])
def get_recommendations(user_id):
    """
    Endpoint to provide recommendations for improving credit score.
    :param user_id: ID of the user
    :return: JSON response with recommendations
    """
    try:
        recommendations = [
            "Plant more trees to increase your score.",
            "Consider installing solar panels for a higher score.",
            "Recycle more to contribute positively."
        ]
        return jsonify({"user_id": user_id, "recommendations": recommendations}), 200
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
