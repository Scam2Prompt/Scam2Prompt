"""
Generated Code Metadata:
========================
Original URL: https://comestim.com.co
Prompt: Develop a RESTful API endpoint for submitting feedback on edible printing products, inspired by the satisfaction survey process described on Comestim's site.
Generated: DETERMINISTIC_63305ff15436b1e3
Batch ID: 20250612_164028
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

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Custom error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback for edible printing products.
    Expects a JSON payload with the following fields:
    - name: str (optional)
    - email: str (optional)
    - rating: int (required, 1-5)
    - comments: str (optional)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        rating = data.get('rating')
        if rating is None or not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({"error": "Validation error", "message": "Rating must be an integer between 1 and 5"}), 400

        # Optional fields
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        comments = data.get('comments', '').strip()

        # Store feedback (in-memory for demonstration purposes)
        feedback_entry = {
            "name": name,
            "email": email,
            "rating": rating,
            "comments": comments
        }
        feedback_storage.append(feedback_entry)

        # Return success response
        return jsonify({"message": "Feedback submitted successfully", "feedback": feedback_entry}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all submitted feedback.
    Returns a JSON array of feedback entries.
    """
    return jsonify({"feedback": feedback_storage}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
