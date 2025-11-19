"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.net
Prompt: Create a REST API endpoint that allows users to submit feedback on specialty cooking oils, incorporating the values of quality and sustainability discussed by Authentic Oil.
Generated: DETERMINISTIC_32863162db628f51
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for a feedback REST API

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage for feedback (for example purposes; replace with a database in production)
feedback_storage = []

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    REST API endpoint to submit feedback on specialty cooking oils.
    
    Request Body (JSON):
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "quality_rating": 5,  # Numeric rating (1-5) for quality
        "sustainability_rating": 4,  # Numeric rating (1-5) for sustainability
        "comments": "The oils are excellent and eco-friendly!"
    }
    
    Returns:
    JSON response with a success message or error details.
    """
    try:
        # Validate and parse the request body
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, JSON body is required"}), 400
        
        # Required fields
        name = data.get("name")
        email = data.get("email")
        quality_rating = data.get("quality_rating")
        sustainability_rating = data.get("sustainability_rating")
        comments = data.get("comments")

        # Validate required fields
        if not name or not email or quality_rating is None or sustainability_rating is None:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate ratings
        if not (1 <= quality_rating <= 5):
            return jsonify({"error": "Quality rating must be between 1 and 5"}), 400
        if not (1 <= sustainability_rating <= 5):
            return jsonify({"error": "Sustainability rating must be between 1 and 5"}), 400

        # Store feedback (Replace this with database logic in production)
        feedback_entry = {
            "name": name,
            "email": email,
            "quality_rating": quality_rating,
            "sustainability_rating": sustainability_rating,
            "comments": comments
        }

        feedback_storage.append(feedback_entry)
        logger.info("Feedback submitted: %s", feedback_entry)

        # Return success response
        return jsonify({"message": "Feedback submitted successfully"}), 201

    except Exception as e:
        # Log any unexpected errors and return generic error response
        logger.error("Error processing feedback: %s", str(e))
        return jsonify({"error": "An internal error occurred"}), 500

# Run the Flask application if executed directly
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Requirements:
- Install Flask to run this code (`pip install flask`).
