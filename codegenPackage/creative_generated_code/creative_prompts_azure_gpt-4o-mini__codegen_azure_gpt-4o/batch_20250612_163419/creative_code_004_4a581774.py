"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Create a sample code snippet that demonstrates how to provide early audience feedback for video content within the MILC Community platform.
Generated: DETERMINISTIC_4a581774d482aaeb
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database to store feedback
feedback_db = []

# Endpoint to submit audience feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to allow users to submit feedback for video content.
    Expected JSON payload:
    {
        "video_id": "string",      # ID of the video
        "user_id": "string",       # ID of the user providing feedback
        "rating": 1-5,             # Rating given by the user (1 to 5)
        "comment": "string"        # Optional comment
    }
    """
    try:
        # Parse incoming JSON request
        feedback = request.get_json()

        # Validate required fields
        if 'video_id' not in feedback or 'user_id' not in feedback or 'rating' not in feedback:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate rating value
        if not (1 <= feedback['rating'] <= 5):
            return jsonify({"error": "Rating must be between 1 and 5"}), 400
        
        # Add feedback to the mock database
        feedback_db.append({
            "video_id": feedback['video_id'],
            "user_id": feedback['user_id'],
            "rating": feedback['rating'],
            "comment": feedback.get('comment', "")  # Default to empty string if no comment
        })

        return jsonify({"message": "Feedback submitted successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Endpoint to get feedback for a specific video
@app.route('/get_feedback/<video_id>', methods=['GET'])
def get_feedback(video_id):
    """
    Endpoint to retrieve audience feedback for a given video ID.
    :param video_id: The ID of the video to retrieve feedback for.
    """
    try:
        # Filter feedback for the specified video ID
        video_feedback = [fb for fb in feedback_db if fb['video_id'] == video_id]

        if not video_feedback:
            return jsonify({"message": "No feedback found for this video"}), 404

        return jsonify({"feedback": video_feedback}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
