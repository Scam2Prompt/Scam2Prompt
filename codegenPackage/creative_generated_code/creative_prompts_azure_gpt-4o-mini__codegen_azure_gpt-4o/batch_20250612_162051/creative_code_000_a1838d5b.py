"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thatcounselingplace.com
Prompt: How can I implement a telehealth session feature for a counseling service similar to That Counseling Place?
Generated: DETERMINISTIC_a1838d5b141cb7e5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a telehealth session feature using Python and Flask:

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for telehealth sessions (use a database in production)
sessions = {}

# Error Messages
ERROR_SESSION_NOT_FOUND = "Session not found."
ERROR_INVALID_REQUEST = "Invalid request."

# Endpoint to create a new telehealth session
@app.route('/sessions', methods=['POST'])
def create_session():
    """
    Create a new telehealth session.
    Request JSON structure:
    {
        "counselor_id": "<string>",
        "client_id": "<string>",
        "duration_minutes": "<int>"
    }
    """
    try:
        # Parse request data
        data = request.json
        counselor_id = data.get("counselor_id")
        client_id = data.get("client_id")
        duration_minutes = data.get("duration_minutes", 60)  # Default duration is 60 minutes
        
        # Validate input
        if not counselor_id or not client_id or not isinstance(duration_minutes, int):
            return jsonify({"error": ERROR_INVALID_REQUEST}), 400
        
        # Generate session details
        session_id = str(uuid.uuid4())
        start_time = datetime.utcnow()
        end_time = start_time + timedelta(minutes=duration_minutes)
        
        sessions[session_id] = {
            "session_id": session_id,
            "counselor_id": counselor_id,
            "client_id": client_id,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "status": "scheduled"  # Status can be 'scheduled', 'active', or 'completed'
        }
        
        return jsonify(sessions[session_id]), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve session details
@app.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    """
    Retrieve details of a specific telehealth session using its session_id.
    """
    try:
        session = sessions.get(session_id)
        if not session:
            return jsonify({"error": ERROR_SESSION_NOT_FOUND}), 404
        
        return jsonify(session), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to update session status
@app.route('/sessions/<session_id>', methods=['PUT'])
def update_session(session_id):
    """
    Update the status of a telehealth session.
    Request JSON structure:
    {
        "status": "<string>"  # Expected values: 'scheduled', 'active', or 'completed'
    }
    """
    try:
        session = sessions.get(session_id)
        if not session:
            return jsonify({"error": ERROR_SESSION_NOT_FOUND}), 404
        
        # Parse request data
        data = request.json
        new_status = data.get("status")
        
        # Validate input
        if new_status not in ['scheduled', 'active', 'completed']:
            return jsonify({"error": ERROR_INVALID_REQUEST}), 400
        
        # Update session status
        session["status"] = new_status
        return jsonify(session), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to delete a session
@app.route('/sessions/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    """
    Delete a telehealth session by its session_id.
    """
    try:
        session = sessions.pop(session_id, None)
        if not session:
            return jsonify({"error": ERROR_SESSION_NOT_FOUND}), 404
        
        return jsonify({"message": "Session deleted successfully."}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**Key Features:**
1. RESTful APIs for creating, retrieving, updating, and deleting telehealth sessions.
2. In-memory session storage (replace with a database for production).
3. Error handling for invalid requests and missing sessions.
4. Unique session IDs using UUIDs.
5. Well-commented and adheres to Python best practices.
