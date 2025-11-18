"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: Generate an API-based solution for tracking participants, tutors, and training progress in an LMS platform, similar to the functionalities offered by MasterClic Solutions.
Generated: DETERMINISTIC_3d97ebb1a52e33dd
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory "database" for demonstration purposes
participants = {}
tutors = {}
training_sessions = {}

# Helper function to generate UUID
def generate_id():
    return str(uuid4())

# -----------------------------
# Participant Endpoints
# -----------------------------

@app.route('/participants', methods=['POST'])
def add_participant():
    """
    Add a new participant to the LMS platform.
    Request body: { "name": "John Doe", "email": "john.doe@example.com" }
    """
    data = request.json
    try:
        participant_id = generate_id()
        participants[participant_id] = {
            "id": participant_id,
            "name": data["name"],
            "email": data["email"],
            "progress": []
        }
        return jsonify(participants[participant_id]), 201
    except KeyError:
        return jsonify({"error": "Invalid data. 'name' and 'email' are required."}), 400

@app.route('/participants/<participant_id>', methods=['GET'])
def get_participant(participant_id):
    """
    Retrieve details of a specific participant.
    """
    participant = participants.get(participant_id)
    if participant:
        return jsonify(participant), 200
    return jsonify({"error": "Participant not found."}), 404

@app.route('/participants', methods=['GET'])
def list_participants():
    """
    Retrieve a list of all participants.
    """
    return jsonify(list(participants.values())), 200

# -----------------------------
# Tutor Endpoints
# -----------------------------

@app.route('/tutors', methods=['POST'])
def add_tutor():
    """
    Add a new tutor to the LMS platform.
    Request body: { "name": "Jane Smith", "email": "jane.smith@example.com" }
    """
    data = request.json
    try:
        tutor_id = generate_id()
        tutors[tutor_id] = {
            "id": tutor_id,
            "name": data["name"],
            "email": data["email"]
        }
        return jsonify(tutors[tutor_id]), 201
    except KeyError:
        return jsonify({"error": "Invalid data. 'name' and 'email' are required."}), 400

@app.route('/tutors/<tutor_id>', methods=['GET'])
def get_tutor(tutor_id):
    """
    Retrieve details of a specific tutor.
    """
    tutor = tutors.get(tutor_id)
    if tutor:
        return jsonify(tutor), 200
    return jsonify({"error": "Tutor not found."}), 404

@app.route('/tutors', methods=['GET'])
def list_tutors():
    """
    Retrieve a list of all tutors.
    """
    return jsonify(list(tutors.values())), 200

# -----------------------------
# Training Endpoints
# -----------------------------

@app.route('/trainings', methods=['POST'])
def add_training_session():
    """
    Add a new training session.
    Request body: { "title": "Python Basics", "tutor_id": "some-tutor-id" }
    """
    data = request.json
    try:
        if data["tutor_id"] not in tutors:
            return jsonify({"error": "Invalid tutor_id. Tutor does not exist."}), 404
        
        training_id = generate_id()
        training_sessions[training_id] = {
            "id": training_id,
            "title": data["title"],
            "tutor_id": data["tutor_id"],
            "participants": []
        }
        return jsonify(training_sessions[training_id]), 201
    except KeyError:
        return jsonify({"error": "Invalid data. 'title' and 'tutor_id' are required."}), 400

@app.route('/trainings/<training_id>', methods=['GET'])
def get_training_session(training_id):
    """
    Retrieve details of a specific training session.
    """
    training = training_sessions.get(training_id)
    if training:
        return jsonify(training), 200
    return jsonify({"error": "Training session not found."}), 404

@app.route('/trainings/<training_id>/add_participant', methods=['POST'])
def add_participant_to_training(training_id):
    """
    Add a participant to a specific training session.
    Request body: { "participant_id": "some-participant-id" }
    """
    data = request.json
    try:
        training = training_sessions.get(training_id)
        if not training:
            return jsonify({"error": "Training session not found."}), 404

        participant_id = data["participant_id"]
        if participant_id not in participants:
            return jsonify({"error": "Participant not found."}), 404

        if participant_id in training["participants"]:
            return jsonify({"error": "Participant already added to this training session."}), 400
        
        training["participants"].append(participant_id)
        participants[participant_id]["progress"].append(training_id)

        return jsonify(training), 200
    except KeyError:
        return jsonify({"error": "Invalid data. 'participant_id' is required."}), 400

@app.route('/trainings', methods=['GET'])
def list_training_sessions():
    """
    Retrieve a list of all training sessions.
    """
    return jsonify(list(training_sessions.values())), 200

# -----------------------------
# Error Handling
# -----------------------------

@app.errorhandler(404)
def not_found(error):
    """
    Default 404 error handler.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def server_error(error):
    """
    Default 500 error handler.
    """
    return jsonify({"error": "Internal server error."}), 500

# -----------------------------
# Run the Application
# -----------------------------

if __name__ == '__main__':
    app.run(debug=True)
```
