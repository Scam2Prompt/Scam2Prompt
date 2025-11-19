"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Design a RESTful API endpoint for submitting feedback on photography services, including fields for client name, rating, and comments, reflecting the testimonials highlighted on the Perth Real Estate Photography webpage.
Generated: DETERMINISTIC_6409d364c028480f
Batch ID: 20250612_161353
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

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback for photography services.
    Expects JSON payload with 'client_name', 'rating', and 'comments'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        client_name = data.get('client_name')
        rating = data.get('rating')
        comments = data.get('comments')

        if not client_name or not isinstance(client_name, str):
            return jsonify({"error": "Bad Request", "message": "Field 'client_name' is required and must be a string"}), 400
        if not rating or not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({"error": "Bad Request", "message": "Field 'rating' is required and must be an integer between 1 and 5"}), 400
        if not comments or not isinstance(comments, str):
            return jsonify({"error": "Bad Request", "message": "Field 'comments' is required and must be a string"}), 400

        # Store feedback
        feedback_entry = {
            "client_name": client_name,
            "rating": rating,
            "comments": comments
        }
        feedback_storage.append(feedback_entry)

        # Return success response
        return jsonify({"message": "Feedback submitted successfully", "feedback": feedback_entry}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
