"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Create an API that allows users to view and register for mentorship sessions on sexual reproductive health, gender-based violence, and FGM awareness, as part of the Girls Empowerment Programme on the Kibera Hamlets website.
Generated: DETERMINISTIC_76bda1a327fa4a94
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory data storage for mentorship sessions and registrations
sessions = [
    {
        "id": str(uuid.uuid4()),
        "topic": "Sexual Reproductive Health",
        "mentor": "Dr. Jane Doe",
        "date": "2023-11-10",
        "time": "10:00 AM",
        "available_slots": 10
    },
    {
        "id": str(uuid.uuid4()),
        "topic": "Gender-Based Violence Awareness",
        "mentor": "Ms. Sarah Smith",
        "date": "2023-11-12",
        "time": "2:00 PM",
        "available_slots": 15
    },
    {
        "id": str(uuid.uuid4()),
        "topic": "FGM Awareness",
        "mentor": "Dr. John Kennedy",
        "date": "2023-11-14",
        "time": "11:00 AM",
        "available_slots": 8
    },
]

registrations = []

# API endpoint to view all mentorship sessions
@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    """
    Retrieve the list of all mentorship sessions available.

    Returns:
        JSON response containing the mentorship sessions.
    """
    return jsonify({"sessions": sessions}), 200

# API endpoint to register for a mentorship session
@app.route('/api/register', methods=['POST'])
def register_for_session():
    """
    Register a user for a mentorship session.

    Request Body:
        {
            "session_id": "<session_id>",
            "participant_name": "<participant_name>",
            "participant_email": "<participant_email>"
        }

    Returns:
        JSON response indicating success or failure of the registration.
    """
    try:
        # Extract data from the request body
        data = request.get_json()
        session_id = data.get("session_id")
        participant_name = data.get("participant_name")
        participant_email = data.get("participant_email")

        # Validate input data
        if not session_id or not participant_name or not participant_email:
            return jsonify({"error": "Missing required fields"}), 400

        # Find the session by ID
        session = next((s for s in sessions if s["id"] == session_id), None)
        if not session:
            return jsonify({"error": "Session not found"}), 404

        # Check if there are available slots
        if session["available_slots"] <= 0:
            return jsonify({"error": "No available slots for this session"}), 400

        # Register the participant
        registration = {
            "id": str(uuid.uuid4()),
            "session_id": session_id,
            "participant_name": participant_name,
            "participant_email": participant_email
        }
        registrations.append(registration)

        # Decrease the available slots for the session
        session["available_slots"] -= 1

        return jsonify({"message": "Registration successful", "registration": registration}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred during registration", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
