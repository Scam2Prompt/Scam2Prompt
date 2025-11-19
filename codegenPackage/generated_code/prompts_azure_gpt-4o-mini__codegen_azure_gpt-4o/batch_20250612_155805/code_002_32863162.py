"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.net
Prompt: Create a REST API endpoint that allows users to submit feedback on specialty cooking oils, incorporating the values of quality and sustainability discussed by Authentic Oil.
Generated: DETERMINISTIC_32863162db628f51
Batch ID: 20250612_155805
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

# Define the feedback endpoint
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback on specialty cooking oils.
    Expects JSON payload with 'user_name', 'quality_rating', 'sustainability_rating', and 'comments'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ['user_name', 'quality_rating', 'sustainability_rating', 'comments']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate ratings
        if not (1 <= data['quality_rating'] <= 5):
            return jsonify({"error": "quality_rating must be between 1 and 5"}), 400
        if not (1 <= data['sustainability_rating'] <= 5):
            return jsonify({"error": "sustainability_rating must be between 1 and 5"}), 400

        # Store feedback
        feedback = {
            "user_name": data['user_name'],
            "quality_rating": data['quality_rating'],
            "sustainability_rating": data['sustainability_rating'],
            "comments": data['comments']
        }
        feedback_storage.append(feedback)

        # Return success response
        return jsonify({"message": "Feedback submitted successfully", "feedback": feedback}), 201

    except HTTPException as e:
        # Handle HTTP exceptions
        return jsonify({"error": str(e)}), e.code
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed_error(e):
    return jsonify({"error": "Method not allowed"}), 405

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
