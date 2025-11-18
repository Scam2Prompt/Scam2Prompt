"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: Develop a feedback form for a blockchain project like "Owy," allowing users to submit suggestions and report issues.
Generated: DETERMINISTIC_21d58b757274a126
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_form.py

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for feedback (In production, use a database)
feedback_storage = []

# Utility function to validate email addresses
def is_valid_email(email):
    email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return email_regex.match(email)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint for submitting feedback.
    Expects JSON payload with fields: 'name', 'email', 'type', 'message'.
    """

    try:
        # Parse feedback data from request
        feedback = request.json
        
        # Ensure all required fields are provided
        required_fields = ['name', 'email', 'type', 'message']
        for field in required_fields:
            if field not in feedback:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Validate email address format
        if not is_valid_email(feedback['email']):
            return jsonify({"error": "Invalid email address"}), 400
        
        # Validate 'type' field (must be 'suggestion' or 'issue')
        if feedback['type'] not in ['suggestion', 'issue']:
            return jsonify({"error": "Invalid feedback type. Use 'suggestion' or 'issue'"}), 400
        
        # Validate 'message' length (non-empty, reasonable length)
        if not feedback['message'] or len(feedback['message']) > 500:
            return jsonify({"error": "Message must be non-empty and up to 500 characters long"}), 400
        
        # Append feedback to storage
        feedback_storage.append({
            "name": feedback['name'],
            "email": feedback['email'],
            "type": feedback['type'],
            "message": feedback['message']
        })

        # Return success response
        return jsonify({"success": "Feedback submitted successfully"}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/get_feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint for retrieving all submitted feedback.
    Returns a JSON array of feedback entries.
    """
    try:
        return jsonify(feedback_storage), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
