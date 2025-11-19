"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Write a Python Flask API to handle user inquiries for Dens Haven, including fields for name, email, and message submission.
Generated: DETERMINISTIC_ac967491eb0e4833
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
MAX_MESSAGE_LENGTH = 1000
MAX_NAME_LENGTH = 100
MAX_EMAIL_LENGTH = 100

@app.route('/api/inquiry', methods=['POST'])
def handle_inquiry():
    """
    Handle user inquiry submission.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "message": "Hello, I have a question about..."
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        message = data['message'].strip()
        
        # Validate name
        if not name:
            return jsonify({"error": "Name cannot be empty"}), 400
        if len(name) > MAX_NAME_LENGTH:
            return jsonify({"error": f"Name exceeds maximum length of {MAX_NAME_LENGTH} characters"}), 400
        
        # Validate email
        try:
            email_info = validate_email(email, check_deliverability=False)
            email = email_info.normalized
        except EmailNotValidError as e:
            return jsonify({"error": str(e)}), 400
        
        if len(email) > MAX_EMAIL_LENGTH:
            return jsonify({"error": f"Email exceeds maximum length of {MAX_EMAIL_LENGTH} characters"}), 400
        
        # Validate message
        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400
        if len(message) > MAX_MESSAGE_LENGTH:
            return jsonify({"error": f"Message exceeds maximum length of {MAX_MESSAGE_LENGTH} characters"}), 400
        
        # Here you would typically save to database or send email
        # For now, we'll just return a success response
        response = {
            "status": "success",
            "message": "Inquiry received successfully",
            "data": {
                "name": name,
                "email": email,
                "message": message
            }
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        app.logger.error(f"Error processing inquiry: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
