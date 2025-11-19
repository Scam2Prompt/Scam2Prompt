"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melikataheri.com
Prompt: Generate a code snippet for a web application that allows users to book online therapy sessions, incorporating features for individual therapy and webinars as described on Melika Taheri's website.
Generated: DETERMINISTIC_39ca9c47f8aa7d52
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database simulation
sessions_db = []

# Error messages
ERROR_INVALID_INPUT = {"error": "Invalid input data"}
ERROR_SESSION_NOT_FOUND = {"error": "Session not found"}

# Helper function to validate date format
def validate_date(date_string, format="%Y-%m-%d %H:%M"):
    try:
        return datetime.strptime(date_string, format)
    except ValueError:
        return None

@app.route('/book_session', methods=['POST'])
def book_session():
    """
    Endpoint for booking an online therapy session.
    Accepts JSON input with session type, user details, and date/time.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'type' not in data or 'user_name' not in data or 'date_time' not in data:
        return jsonify(ERROR_INVALID_INPUT), 400

    session_type = data['type'].lower()
    user_name = data['user_name']
    date_time = validate_date(data['date_time'])

    if session_type not in ['individual', 'webinar'] or not user_name or not date_time:
        return jsonify(ERROR_INVALID_INPUT), 400

    # Create a new session entry
    session_id = str(uuid.uuid4())
    session_entry = {
        'id': session_id,
        'type': session_type,
        'user_name': user_name,
        'date_time': date_time.strftime("%Y-%m-%d %H:%M")
    }
    sessions_db.append(session_entry)

    return jsonify({"message": "Session booked successfully", "session_id": session_id}), 201

@app.route('/get_sessions', methods=['GET'])
def get_sessions():
    """
    Endpoint to retrieve all booked sessions.
    """
    return jsonify(sessions_db), 200

@app.route('/cancel_session/<session_id>', methods=['DELETE'])
def cancel_session(session_id):
    """
    Endpoint to cancel a booked session by session ID.
    """
    global sessions_db
    session_to_cancel = next((session for session in sessions_db if session['id'] == session_id), None)
    
    if not session_to_cancel:
        return jsonify(ERROR_SESSION_NOT_FOUND), 404
    
    sessions_db = [session for session in sessions_db if session['id'] != session_id]
    return jsonify({"message": "Session cancelled successfully", "session_id": session_id}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
