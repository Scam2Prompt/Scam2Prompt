"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-welcome-fi.blogspot.com
Prompt: How can I use the information about Kranz Pneus' experience and service speed to develop a customer feedback API for tire service businesses?
Generated: DETERMINISTIC_f3bf54e0c181f282
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database to store feedback
feedback_db = []

# API route to submit customer feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to receive customer feedback.

    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "service_speed": 5,    # Scale from 1 (slow) to 5 (fast)
        "experience_rating": 4, # Scale from 1 (poor) to 5 (excellent)
        "comments": "Great service!"
    }
    """
    try:
        # Parse JSON from the request
        feedback = request.get_json()
        
        # Validate input data
        if not feedback or 'customer_name' not in feedback or 'service_speed' not in feedback or 'experience_rating' not in feedback:
            return jsonify({"error": "Invalid feedback data"}), 400
        
        # Ensure numeric values are within valid range
        if not (1 <= feedback['service_speed'] <= 5) or not (1 <= feedback['experience_rating'] <= 5):
            return jsonify({"error": "Rating values must be between 1 and 5"}), 400
        
        # Add timestamp to feedback
        feedback['timestamp'] = datetime.utcnow().isoformat()
        
        # Store feedback in the database
        feedback_db.append(feedback)

        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# API route to get all feedback
@app.route('/feedback', methods=['GET'])
def get_all_feedback():
    """
    Endpoint to retrieve all customer feedback.
    """
    try:
        return jsonify({"feedback": feedback_db}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use debug=True for development; set debug=False for production
    app.run(debug=True)
```
