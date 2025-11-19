"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mayayogaofficial.com
Prompt: Generate a REST API that provides yoga session recommendations based on the holistic practices highlighted by Maya Yoga.
Generated: DETERMINISTIC_d55e9a907ee24142
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a REST API in Python using Flask:

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample yoga session recommendations
YOGA_SESSIONS = [
    {
        "id": 1,
        "title": "Morning Energizing Flow",
        "duration": 30,  # minutes
        "focus": "Energy Boost",
        "description": "Start your day with this energizing yoga flow to awaken your body and mind."
    },
    {
        "id": 2,
        "title": "Evening Relaxation Practice",
        "duration": 45,  # minutes
        "focus": "Stress Relief",
        "description": "Relax and unwind in this evening session designed to reduce stress and improve sleep quality."
    },
    {
        "id": 3,
        "title": "Holistic Balance Flow",
        "duration": 60,  # minutes
        "focus": "Holistic Wellness",
        "description": "Achieve balance and harmony with this session focused on holistic practices."
    }
]

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the API."""
    if isinstance(e, HTTPException):
        response = e.get_response()
        return jsonify({
            "error": e.name,
            "message": e.description
        }), e.code
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500


@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Endpoint to retrieve yoga session recommendations.
    You can filter by 'focus' using query parameters.
    """
    focus = request.args.get('focus')  # Optional query parameter
    if focus:
        # Filter by focus if provided
        filtered_sessions = [session for session in YOGA_SESSIONS if session["focus"].lower() == focus.lower()]
        return jsonify(filtered_sessions), 200
    return jsonify(YOGA_SESSIONS), 200


@app.route('/recommendations/<int:session_id>', methods=['GET'])
def get_session_by_id(session_id):
    """
    Endpoint to retrieve a specific yoga session by its ID.
    """
    session = next((session for session in YOGA_SESSIONS if session["id"] == session_id), None)
    if not session:
        return jsonify({
            "error": "Not Found",
            "message": f"Yoga session with ID {session_id} not found."
        }), 404
    return jsonify(session), 200


@app.route('/recommendations', methods=['POST'])
def add_recommendation():
    """
    Endpoint to add a new yoga session recommendation.
    Expects a JSON payload with 'title', 'duration', 'focus', and 'description'.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ('title', 'duration', 'focus', 'description')):
            return jsonify({
                "error": "Bad Request",
                "message": "Missing required fields: 'title', 'duration', 'focus', and 'description'."
            }), 400

        # Create new recommendation
        new_session = {
            "id": YOGA_SESSIONS[-1]["id"] + 1 if YOGA_SESSIONS else 1,
            "title": data["title"],
            "duration": data["duration"],
            "focus": data["focus"],
            "description": data["description"]
        }
        YOGA_SESSIONS.append(new_session)
        return jsonify(new_session), 201
    except Exception as e:
        return jsonify({
            "error": "Bad Request",
            "message": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True)
```
