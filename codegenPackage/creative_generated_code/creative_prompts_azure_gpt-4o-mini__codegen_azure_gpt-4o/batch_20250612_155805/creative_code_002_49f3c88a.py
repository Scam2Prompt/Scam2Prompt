"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.com
Prompt: Create a REST API endpoint that allows users to submit feedback on their favorite cooking oils, incorporating features that reflect the values of Authentic Oil.
Generated: DETERMINISTIC_49f3c88aff7631b6
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Simulated in-memory database for feedback storage
feedback_db = []

# Feedback schema validation utility
def validate_feedback(data):
    required_fields = ['user_name', 'oil_name', 'rating', 'comments']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
        return False, "Rating must be an integer between 1 and 5."
    return True, "Validation successful."

# Global error handler for clean error responses
@app.errorhandler(Exception)
def handle_generic_error(error):
    if isinstance(error, HTTPException):
        response = {
            "status": "error",
            "message": error.description
        }
        return jsonify(response), error.code
    response = {
        "status": "error",
        "message": str(error)
    }
    return jsonify(response), 500

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    REST API Endpoint to submit feedback about cooking oils.
    Expects a JSON payload with 'user_name', 'oil_name', 'rating', and 'comments'.
    """
    try:
        # Parse the JSON request body
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Request body must be JSON."}), 400

        # Validate the feedback data
        is_valid, message = validate_feedback(data)
        if not is_valid:
            return jsonify({"status": "error", "message": message}), 400

        # Save the feedback to the in-memory "database"
        feedback_entry = {
            "user_name": data['user_name'],
            "oil_name": data['oil_name'],
            "rating": data['rating'],
            "comments": data['comments']
        }
        feedback_db.append(feedback_entry)

        # Send success response
        return jsonify({"status": "success", "message": "Feedback submitted successfully.", "feedback": feedback_entry}), 201
    except Exception as e:
        # Catch-all error handler for unexpected issues
        return handle_generic_error(e)

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    REST API Endpoint to retrieve all feedback entries.
    Returns a list of feedback.
    """
    return jsonify({"status": "success", "feedback": feedback_db}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
