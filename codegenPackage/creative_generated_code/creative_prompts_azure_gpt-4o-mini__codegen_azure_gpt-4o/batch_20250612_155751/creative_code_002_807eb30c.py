"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Create an API endpoint that allows users to submit their own radio program ideas to ECBC Radio, incorporating the submission process outlined in the content.
Generated: DETERMINISTIC_807eb30c0f853801
Batch ID: 20250612_155751
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
import re

app = Flask(__name__)

# In-memory storage for submitted ideas (for demonstration purposes)
radio_program_ideas = []

# Utility function: Validate email format
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

@app.route('/submit_program_idea', methods=['POST'])
def submit_program_idea():
    """
    API endpoint to submit a radio program idea to ECBC Radio.

    Request payload format:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "title": "Morning Jazz Hour",
        "description": "A relaxing hour of jazz music to start the day."
    }

    Returns:
        JSON response confirming submission or indicating errors.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'title', 'description']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f"Missing required fields: {', '.join(missing_fields)}"
            }), 400

        # Validate email format
        if not is_valid_email(data['email']):
            return jsonify({
                'success': False,
                'message': "Invalid email format."
            }), 400

        # Create a new program idea entry
        program_idea = {
            'id': len(radio_program_ideas) + 1,  # Generate a simple ID
            'name': data['name'],
            'email': data['email'],
            'title': data['title'],
            'description': data['description'],
            'submitted_at': datetime.utcnow().isoformat()  # Timestamp in ISO format
        }

        # Store the idea (in-memory for now)
        radio_program_ideas.append(program_idea)

        # Return success response
        return jsonify({
            'success': True,
            'message': "Program idea submitted successfully.",
            'program_idea': program_idea
        }), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            'success': False,
            'message': f"An unexpected error occurred: {str(e)}"
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
