"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuicalli.edu.mx
Prompt: Can you provide an API recommendation for integrating extracurricular activity management into an educational institution's website like Tecnológico Cuicalli?
Generated: DETERMINISTIC_3cbe9bff1bee0180
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database to store extracurricular activities (use a proper database in production)
activities = [
    {
        "id": 1,
        "name": "Basketball",
        "description": "A team sport involving dribbling, shooting, and passing.",
        "schedule": "Monday, Wednesday, Friday 4:00 PM - 6:00 PM",
    },
    {
        "id": 2,
        "name": "Chess Club",
        "description": "Learn strategies to play chess and compete in tournaments.",
        "schedule": "Tuesday 5:00 PM - 6:30 PM",
    },
]

# Error handling utilities
def activity_not_found_error(activity_id):
    return jsonify({"error": f"Activity with ID {activity_id} not found"}), 404


@app.route('/activities', methods=['GET'])
def get_activities():
    """
    Endpoint to retrieve all extracurricular activities.
    Returns:
        JSON response with the list of activities.
    """
    return jsonify({"activities": activities})


@app.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    """
    Endpoint to retrieve a specific activity by ID.
    Args:
        activity_id (int): The ID of the activity to retrieve.
    Returns:
        JSON response with the activity details or a 404 error if not found.
    """
    activity = next((act for act in activities if act["id"] == activity_id), None)
    if not activity:
        return activity_not_found_error(activity_id)
    return jsonify({"activity": activity})


@app.route('/activities', methods=['POST'])
def add_activity():
    """
    Endpoint to add a new extracurricular activity.
    Expects:
        JSON payload with 'name', 'description', and 'schedule'.
    Returns:
        JSON response with the newly added activity or 400 error if payload is invalid.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'schedule' not in data:
        return jsonify({"error": "Invalid input. 'name', 'description', and 'schedule' are required."}), 400

    new_activity = {
        "id": len(activities) + 1,
        "name": data["name"],
        "description": data["description"],
        "schedule": data["schedule"],
    }
    activities.append(new_activity)
    return jsonify({"activity": new_activity}), 201


@app.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    """
    Endpoint to update an existing extracurricular activity by ID.
    Expects:
        JSON payload with 'name', 'description', and/or 'schedule'.
    Returns:
        JSON response with the updated activity or 404 error if not found.
    """
    activity = next((act for act in activities if act["id"] == activity_id), None)
    if not activity:
        return activity_not_found_error(activity_id)

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input. Please provide data to update."}), 400

    activity["name"] = data.get("name", activity["name"])
    activity["description"] = data.get("description", activity["description"])
    activity["schedule"] = data.get("schedule", activity["schedule"])

    return jsonify({"activity": activity})


@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    """
    Endpoint to delete an extracurricular activity by ID.
    Args:
        activity_id (int): The ID of the activity to delete.
    Returns:
        JSON response confirming deletion or a 404 error if not found.
    """
    global activities
    activity = next((act for act in activities if act["id"] == activity_id), None)
    if not activity:
        return activity_not_found_error(activity_id)

    activities = [act for act in activities if act["id"] != activity_id]
    return jsonify({"message": f"Activity with ID {activity_id} has been deleted"}), 200


# Start the Flask application
if __name__ == '__main__':
    # Run the app in debug mode for development (disable debug mode for production)
    app.run(debug=True)
```
