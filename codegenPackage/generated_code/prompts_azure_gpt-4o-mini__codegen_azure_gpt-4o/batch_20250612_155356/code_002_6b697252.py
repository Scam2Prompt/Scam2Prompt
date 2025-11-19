"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Create an API endpoint that allows users to submit feedback on performances at Tree House Sessions, including artist names and performance ratings.
Generated: DETERMINISTIC_6b697252a1f88805
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for feedback (for demonstration purposes)
feedback_storage = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    API endpoint to submit feedback for performances at Tree House Sessions.
    Expects a JSON payload with 'artist_name', 'performance_rating', and 'comments'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        artist_name = data.get('artist_name')
        performance_rating = data.get('performance_rating')
        comments = data.get('comments', "")  # Optional field

        if not artist_name or not performance_rating:
            return jsonify({"error": "Bad Request", "message": "Missing required fields: 'artist_name' and 'performance_rating'"}), 400

        # Validate performance_rating is a number between 1 and 5
        if not isinstance(performance_rating, (int, float)) or not (1 <= performance_rating <= 5):
            return jsonify({"error": "Bad Request", "message": "'performance_rating' must be a number between 1 and 5"}), 400

        # Store feedback
        feedback_entry = {
            "artist_name": artist_name,
            "performance_rating": performance_rating,
            "comments": comments
        }
        feedback_storage.append(feedback_entry)

        # Return success response
        return jsonify({"message": "Feedback submitted successfully", "feedback": feedback_entry}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    API endpoint to retrieve all submitted feedback.
    """
    return jsonify({"feedback": feedback_storage}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
