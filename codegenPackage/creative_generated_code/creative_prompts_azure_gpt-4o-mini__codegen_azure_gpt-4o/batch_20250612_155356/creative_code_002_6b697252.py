"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Create an API endpoint that allows users to submit feedback on performances at Tree House Sessions, including artist names and performance ratings.
Generated: DETERMINISTIC_6b697252a1f88805
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for feedback. Replace with a database in production.
feedback_storage = []

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    API endpoint to submit feedback for Tree House Sessions performances.
    Expects a JSON payload with 'artist_name', 'performance_rating', and optionally 'comments'.
    """
    try:
        # Parse and validate input
        feedback = request.get_json()
        if not feedback:
            raise BadRequest("Invalid JSON payload.")

        artist_name = feedback.get('artist_name')
        performance_rating = feedback.get('performance_rating')
        comments = feedback.get('comments', '')

        # Validate required fields
        if not artist_name or not performance_rating:
            raise BadRequest("'artist_name' and 'performance_rating' are required fields.")

        # Validate performance_rating is numeric and within range 1-5
        if not isinstance(performance_rating, (int, float)) or not (1 <= performance_rating <= 5):
            raise BadRequest("'performance_rating' must be a number between 1 and 5.")

        # Store feedback (in-memory for now)
        feedback_entry = {
            'artist_name': artist_name,
            'performance_rating': performance_rating,
            'comments': comments
        }
        feedback_storage.append(feedback_entry)

        # Return success response
        return jsonify({'message': 'Feedback submitted successfully!', 'feedback': feedback_entry}), 201

    except BadRequest as e:
        # Handle validation errors
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Generic error handling
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    API endpoint to retrieve all feedback.
    """
    return jsonify({'feedback': feedback_storage}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
