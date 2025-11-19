"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Develop a RESTful API endpoint that allows users to submit feedback on construction services, similar to the testimonials shared by clients of ECOLUX, including fields for rating and comments.
Generated: DETERMINISTIC_d849b3151c58552a
Batch ID: 20250612_162051
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

# In-memory storage for feedback (would typically use a database)
feedback_storage = []

# Define the feedback endpoint
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback on construction services.
    Body must include 'rating' (integer between 1 and 5) and 'comments' (string).
    Returns a success message with the feedback details.
    """
    try:
        # Parse and validate the request body
        data = request.json
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        rating = data.get('rating')
        comments = data.get('comments')

        # Validate rating
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({"error": "Rating must be an integer between 1 and 5"}), 400
        
        # Validate comments
        if not isinstance(comments, str) or len(comments.strip()) == 0:
            return jsonify({"error": "Comments must be a non-empty string"}), 400
        
        # Store feedback
        feedback_entry = {
            "rating": rating,
            "comments": comments,
        }
        feedback_storage.append(feedback_entry)

        # Return success response
        return jsonify({
            "message": "Feedback submitted successfully",
            "feedback": feedback_entry
        }), 201

    except HTTPException as e:
        # Handle HTTP-specific errors
        return jsonify({"error": str(e)}), e.code

    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
