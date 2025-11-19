"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Design a RESTful API endpoint for submitting feedback on photography services, including fields for client name, rating, and comments, reflecting the testimonials highlighted on the Perth Real Estate Photography webpage.
Generated: DETERMINISTIC_6409d364c028480f
Batch ID: 20250612_161353
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

# In-memory storage for feedback (In production, use a database)
feedback_list = []

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback on photography services.
    Accepts JSON payload with fields: 'client_name', 'rating', and 'comments'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        client_name = data.get("client_name")
        rating = data.get("rating")
        comments = data.get("comments")
        
        if not client_name or not isinstance(client_name, str):
            return jsonify({"error": "client_name is required and must be a string"}), 400
        if not rating or not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({"error": "rating is required and must be an integer between 1 and 5"}), 400
        if not comments or not isinstance(comments, str):
            return jsonify({"error": "comments are required and must be a string"}), 400
        
        # Construct feedback object
        feedback = {
            "client_name": client_name,
            "rating": rating,
            "comments": comments
        }
        
        # Store feedback
        feedback_list.append(feedback)
        
        # Return success response
        return jsonify({"message": "Feedback submitted successfully", "feedback": feedback}), 201
    
    except HTTPException as e:
        # Handle specific HTTP exceptions
        return jsonify({"error": str(e)}), e.code
    
    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all submitted feedback.
    Returns a list of feedback entries.
    """
    return jsonify({"feedback": feedback_list}), 200

# Run the application (Do not use in production; use a WSGI server)
if __name__ == '__main__':
    # Development server
    app.run(debug=True)
```
