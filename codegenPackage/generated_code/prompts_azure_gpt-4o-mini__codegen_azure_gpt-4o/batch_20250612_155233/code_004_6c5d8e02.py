"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Suggest an API that could help automate the management of training sessions related to Coordination SPS, as mentioned in the AFCO's training initiatives.
Generated: DETERMINISTIC_6c5d8e0234d475e4
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import datetime

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to store training sessions
training_sessions = []

# Error handling utility function
def validate_training_session(data):
    """
    Validates the input data for creating or updating a training session.
    Returns a tuple (is_valid, error_message).
    """
    required_fields = ["title", "description", "date", "duration", "trainer"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.datetime.strptime(data["date"], "%Y-%m-%d")
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."
    if not isinstance(data["duration"], int) or data["duration"] <= 0:
        return False, "Duration must be a positive integer."
    return True, None

# API endpoint to create a new training session
@app.route('/api/training_sessions', methods=['POST'])
def create_training_session():
    """
    Endpoint to create a new training session.
    Expects JSON payload with fields: title, description, date, duration, trainer.
    """
    data = request.get_json()
    is_valid, error_message = validate_training_session(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Create a new training session
    session = {
        "id": len(training_sessions) + 1,
        "title": data["title"],
        "description": data["description"],
        "date": data["date"],
        "duration": data["duration"],
        "trainer": data["trainer"]
    }
    training_sessions.append(session)
    return jsonify(session), 201

# API endpoint to retrieve all training sessions
@app.route('/api/training_sessions', methods=['GET'])
def get_training_sessions():
    """
    Endpoint to retrieve all training sessions.
    Returns a list of training sessions in JSON format.
    """
    return jsonify(training_sessions), 200

# API endpoint to retrieve a specific training session by ID
@app.route('/api/training_sessions/<int:session_id>', methods=['GET'])
def get_training_session(session_id):
    """
    Endpoint to retrieve a specific training session by ID.
    """
    session = next((s for s in training_sessions if s["id"] == session_id), None)
    if not session:
        return jsonify({"error": "Training session not found"}), 404
    return jsonify(session), 200

# API endpoint to update a training session by ID
@app.route('/api/training_sessions/<int:session_id>', methods=['PUT'])
def update_training_session(session_id):
    """
    Endpoint to update a specific training session by ID.
    Expects JSON payload with fields: title, description, date, duration, trainer.
    """
    session = next((s for s in training_sessions if s["id"] == session_id), None)
    if not session:
        return jsonify({"error": "Training session not found"}), 404

    data = request.get_json()
    is_valid, error_message = validate_training_session(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Update the training session
    session.update({
        "title": data["title"],
        "description": data["description"],
        "date": data["date"],
        "duration": data["duration"],
        "trainer": data["trainer"]
    })
    return jsonify(session), 200

# API endpoint to delete a training session by ID
@app.route('/api/training_sessions/<int:session_id>', methods=['DELETE'])
def delete_training_session(session_id):
    """
    Endpoint to delete a specific training session by ID.
    """
    global training_sessions
    session = next((s for s in training_sessions if s["id"] == session_id), None)
    if not session:
        return jsonify({"error": "Training session not found"}), 404

    training_sessions = [s for s in training_sessions if s["id"] != session_id]
    return jsonify({"message": "Training session deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
