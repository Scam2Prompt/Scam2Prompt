"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Develop a RESTful API that supports psychosocial counseling services for children in distress, reflecting the goals of Child Nepal.
Generated: DETERMINISTIC_7edd94f3866c7f19
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data (mock database)
counseling_sessions = [
    {
        "id": 1,
        "child_name": "John Doe",
        "age": 12,
        "session_date": "2023-10-01",
        "counselor": "Jane Smith",
        "notes": "Child shows signs of improvement in managing anxiety."
    },
    {
        "id": 2,
        "child_name": "Alice Green",
        "age": 9,
        "session_date": "2023-10-02",
        "counselor": "Mark Johnson",
        "notes": "Child is struggling with bullying issues at school."
    }
]

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({
            "error": e.description
        }).get_data()
        response.content_type = "application/json"
        return response
    return jsonify({"error": "An internal server error occurred"}), 500

# GET all counseling sessions
@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    return jsonify(counseling_sessions), 200

# GET a specific session by ID
@app.route('/api/sessions/<int:session_id>', methods=['GET'])
def get_session_by_id(session_id):
    session = next((s for s in counseling_sessions if s['id'] == session_id), None)
    if not session:
        return jsonify({"error": "Session not found"}), 404
    return jsonify(session), 200

# POST a new counseling session
@app.route('/api/sessions', methods=['POST'])
def create_session():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        
        required_fields = ["child_name", "age", "session_date", "counselor", "notes"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        new_session = {
            "id": len(counseling_sessions) + 1,
            "child_name": data["child_name"],
            "age": data["age"],
            "session_date": data["session_date"],
            "counselor": data["counselor"],
            "notes": data["notes"]
        }
        counseling_sessions.append(new_session)
        return jsonify(new_session), 201
    except Exception as e:
        return jsonify({"error": "Failed to create session"}), 500

# PUT (update) an existing counseling session
@app.route('/api/sessions/<int:session_id>', methods=['PUT'])
def update_session(session_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        session = next((s for s in counseling_sessions if s['id'] == session_id), None)
        if not session:
            return jsonify({"error": "Session not found"}), 404

        for key, value in data.items():
            if key in session:
                session[key] = value

        return jsonify(session), 200
    except Exception as e:
        return jsonify({"error": "Failed to update session"}), 500

# DELETE a counseling session
@app.route('/api/sessions/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    session = next((s for s in counseling_sessions if s['id'] == session_id), None)
    if not session:
        return jsonify({"error": "Session not found"}), 404

    counseling_sessions.remove(session)
    return jsonify({"message": "Session deleted successfully"}), 200

# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
