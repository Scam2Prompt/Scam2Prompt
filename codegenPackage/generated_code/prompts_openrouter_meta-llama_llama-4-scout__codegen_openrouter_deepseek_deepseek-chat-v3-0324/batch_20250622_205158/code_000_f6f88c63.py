"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Write a contact form submission API using Python and JSON payload with fields for name, email, subject, and message.
Generated: DETERMINISTIC_f6f88c63f67ad674
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import re
import os

app = Flask(__name__)

# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
    """Validate email format using regex."""
    return re.match(EMAIL_REGEX, email) is not None

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """
    Handle contact form submissions.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "subject": "Inquiry",
        "message": "Hello, I have a question."
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            raise BadRequest("No JSON payload provided")
        
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                raise BadRequest(f"Missing or empty required field: {field}")
        
        # Validate email format
        if not validate_email(data['email']):
            raise BadRequest("Invalid email format")
        
        # Here you would typically process the data (e.g., send email, save to DB)
        # For this example, we'll just return a success response
        
        response = {
            'status': 'success',
            'message': 'Contact form submitted successfully',
            'data': {
                'name': data['name'],
                'email': data['email'],
                'subject': data['subject'],
                'message': data['message']
            }
        }
        
        return jsonify(response), 200
    
    except BadRequest as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    # Run the app with production settings
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
