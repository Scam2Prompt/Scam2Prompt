"""
Generated Code Metadata:
========================
Original URL: https://saldias.net
Prompt: Create a code snippet to handle contact form submissions for a spare parts supplier website, including fields for name, email, phone number, and message.
Generated: DETERMINISTIC_408e033383697ce8
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re
from typing import Dict, Optional

app = Flask(__name__)

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Validate phone number format (basic international format)."""
    pattern = r'^\+?[0-9\s\-\(\)]{7,}$'
    return re.match(pattern, phone) is not None

@app.route('/submit_contact', methods=['POST'])
def handle_contact_submission():
    """
    Handle contact form submissions.
    Expected JSON payload:
    {
        "name": str,
        "email": str,
        "phone": str,
        "message": str
    }
    """
    try:
        data: Dict[str, str] = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({
                    'status': 'error',
                    'message': f'Missing or empty required field: {field}'
                }), 400
        
        # Validate field formats
        if not validate_email(data['email']):
            return jsonify({
                'status': 'error',
                'message': 'Invalid email format'
            }), 400
        
        if not validate_phone(data['phone']):
            return jsonify({
                'status': 'error',
                'message': 'Invalid phone number format'
            }), 400
        
        # Process the submission (in a real app, this would save to DB/send email/etc)
        # Here we just return a success message
        return jsonify({
            'status': 'success',
            'message': 'Contact form submitted successfully',
            'data': {
                'name': data['name'],
                'email': data['email'],
                'phone': data['phone']
            }
        }), 200
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'An unexpected error occurred',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```
