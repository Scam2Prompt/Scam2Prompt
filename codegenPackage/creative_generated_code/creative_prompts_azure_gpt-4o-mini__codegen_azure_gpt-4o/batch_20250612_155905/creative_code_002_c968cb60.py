"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctorvitaly.pro
Prompt: Create an API endpoint that handles form submissions, ensuring it validates email input and checks for CAPTCHA verification, as seen on doctorvitaly.pro.
Generated: DETERMINISTIC_c968cb605929800d
Batch ID: 20250612_155905
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/recaptcha/api/siteverify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

# Helper function to validate email format
def is_valid_email(email):
    # Basic regex for email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Helper function to verify CAPTCHA using Google's reCAPTCHA API
def verify_captcha(token):
    secret_key = "YOUR_SECRET_RECAPTCHA_KEY"  # Replace with your reCAPTCHA secret key
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {
        'secret': secret_key,
        'response': token
    }
    try:
        response = requests.post(url, data=data)
        response_data = response.json()
        return response_data.get('success', False)
    except requests.RequestException:
        return False

# API endpoint to handle form submissions
@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # Parse the incoming JSON request
        form_data = request.json
        
        # Extract fields
        email = form_data.get('email')
        captcha_token = form_data.get('captchaToken')
        
        # Validate email
        if not email or not is_valid_email(email):
            return jsonify({
                'success': False,
                'message': 'Invalid email format.'
            }), 400

        # Validate CAPTCHA
        if not captcha_token or not verify_captcha(captcha_token):
            return jsonify({
                'success': False,
                'message': 'CAPTCHA verification failed.'
            }), 400
        
        # Process the form submission (this is where you'd handle the actual form data)
        # For example, store in database, send email notification, etc.
        # For now, we'll just return a success message.
        return jsonify({
            'success': True,
            'message': 'Form submitted successfully!'
        }), 200
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing the form submission.',
            'error': str(e)
        }), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Replace `"YOUR_SECRET_RECAPTCHA_KEY"` with your actual reCAPTCHA secret key.
