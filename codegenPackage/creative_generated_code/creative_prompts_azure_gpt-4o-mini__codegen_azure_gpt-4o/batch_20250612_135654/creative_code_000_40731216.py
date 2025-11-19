"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Generate code for a web application that implements a self-development program similar to the METATIME concept, focusing on body and consciousness integration.
Generated: DETERMINISTIC_407312168737d4a0
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, List

# Initialize Flask application
app = Flask(__name__)

# Global list to store user progress data
user_progress: List[Dict] = []

# Sample exercises for body and consciousness integration
exercise_catalog = {
    "body": [
        {"id": 1, "name": "Stretching Routine", "description": "A 10-minute stretching routine to improve flexibility."},
        {"id": 2, "name": "Yoga Flow", "description": "A 20-minute yoga session to enhance body-mind synergy."}
    ],
    "consciousness": [
        {"id": 3, "name": "Mindfulness Meditation", "description": "15 minutes of guided mindfulness meditation."},
        {"id": 4, "name": "Journaling", "description": "Write thoughts for 10 minutes to improve self-awareness."}
    ]
}

# Error handling decorator for API routes
def error_handling(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    wrapper.__name__ = func.__name__
    return wrapper

@app.route("/exercises", methods=["GET"])
@error_handling
def get_exercises():
    """
    Endpoint to retrieve the catalog of exercises.
    Returns:
        JSON response with exercise catalog.
    """
    return jsonify({"exercises": exercise_catalog}), 200

@app.route("/progress", methods=["POST"])
@error_handling
def log_progress():
    """
    Endpoint to log user progress.
    Request payload should include:
        - username: str
        - exercise_id: int
        - completion_time: str (ISO 8601 format)
    Returns:
        JSON response confirming progress logging.
    """
    data = request.get_json()
    # Validate input
    if not data or not all(k in data for k in ("username", "exercise_id", "completion_time")):
        return jsonify({"error": "Invalid input. Provide 'username', 'exercise_id', and 'completion_time'."}), 400

    try:
        # Ensure correct datetime format
        completion_time = datetime.fromisoformat(data["completion_time"])
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO 8601 format."}), 400

    # Log progress
    user_progress.append({
        "username": data["username"],
        "exercise_id": data["exercise_id"],
        "completion_time": completion_time
    })

    return jsonify({"message": "Progress logged successfully."}), 201

@app.route("/progress/<username>", methods=["GET"])
@error_handling
def get_user_progress(username):
    """
    Endpoint to retrieve progress of a specific user.
    Args:
        username: str
    Returns:
        JSON response with the user's progress data.
    """
    user_data = [entry for entry in user_progress if entry["username"] == username]
    if not user_data:
        return jsonify({"message": "No progress found for the specified user."}), 404

    return jsonify({"progress": user_data}), 200

# Run the Flask application
if __name__ == "__main__":
    # Best practice: use environment variables for sensitive data in production
    app.run(host="0.0.0.0", port=5000, debug=True)
```
