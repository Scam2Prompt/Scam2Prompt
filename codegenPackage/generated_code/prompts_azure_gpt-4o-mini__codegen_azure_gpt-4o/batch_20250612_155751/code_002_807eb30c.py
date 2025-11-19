"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Create an API endpoint that allows users to submit their own radio program ideas to ECBC Radio, incorporating the submission process outlined in the content.
Generated: DETERMINISTIC_807eb30c0f853801
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for radio program submissions
radio_program_submissions = []

@app.route('/submit-radio-program', methods=['POST'])
def submit_radio_program():
    """
    API endpoint to submit a radio program idea to ECBC Radio.
    Expects a JSON payload with 'title', 'description', and 'submitted_by'.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        
        # Validate required fields
        if not data or 'title' not in data or 'description' not in data or 'submitted_by' not in data:
            return jsonify({"error": "Missing required fields: 'title', 'description', 'submitted_by'"}), 400
        
        # Create a unique ID for the submission
        submission_id = str(uuid.uuid4())
        
        # Construct the submission object
        submission = {
            "id": submission_id,
            "title": data['title'],
            "description": data['description'],
            "submitted_by": data['submitted_by']
        }
        
        # Store the submission
        radio_program_submissions.append(submission)
        
        # Return success response
        return jsonify({
            "message": "Radio program idea submitted successfully!",
            "submission_id": submission_id
        }), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
