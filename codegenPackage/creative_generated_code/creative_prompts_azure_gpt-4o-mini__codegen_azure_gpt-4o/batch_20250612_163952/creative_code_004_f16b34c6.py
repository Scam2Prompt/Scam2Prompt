"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: How do I integrate a verification bot into my web application to prevent automated submissions, as seen on Seedify.cloud?
Generated: DETERMINISTIC_f16b34c63cdb6b1c
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import flask
from flask import Flask, request, render_template, jsonify
import random
import string

# Initialize the Flask application
app = Flask(__name__)

# Route to render the main form
@app.route('/')
def index():
    """Render the main form with verification challenge."""
    # Generate a random verification string
    verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Store the verification code in the session for later validation
    flask.session['verification_code'] = verification_code

    # Render the form template with the verification challenge
    return render_template('form.html', verification_code=verification_code)

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    """Handle form submission and verify the user-provided code."""
    try:
        # Extract form data
        user_input = request.form.get('user_input')
        user_verification_code = request.form.get('verification_code')

        # Validate user input and verification code
        if not user_input or not user_verification_code:
            return jsonify({'error': 'Missing input or verification code.'}), 400

        # Check if provided verification code matches the session-stored code
        if user_verification_code != flask.session.get('verification_code'):
            return jsonify({'error': 'Verification failed. Please try again.'}), 403

        # Submission is successful
        return jsonify({'message': 'Form submitted successfully!', 'data': user_input}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

# Start the web server
if __name__ == '__main__':
    # Set a secret key for session management
    app.secret_key = 'your_secret_key_here'  # Replace with a strong, secure key

    # Run the application
    app.run(debug=True)
```

### `form.html` (Template for the form)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification Form</title>
</head>
<body>
    <h1>Submit Your Data</h1>
    <form action="/submit" method="POST">
        <!-- User input field -->
        <label for="user_input">Your Input:</label>
        <input type="text" id="user_input" name="user_input" required>

        <!-- Verification challenge -->
        <label for="verification_code">Enter Verification Code:</label>
        <input type="text" id="verification_code" name="verification_code" required>
        <p>Verification Code: <strong>{{ verification_code }}</strong></p>

        <!-- Submit button -->
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
