"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Write code to integrate a contact form for equipment inquiries, similar to the one on SCOUT.kz, with validation for phone numbers and email formats.
Generated: DETERMINISTIC_ab94aea5136ee4d0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Regular expressions for validating email and phone number formats
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+?[1-9]\d{1,14}$'  # E.164 format phone number validation

@app.route('/')
def contact_form():
    """
    Render the contact form.
    """
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handle submission of the contact form.
    Validate email and phone number formats and return appropriate responses.
    """
    try:
        # Retrieve form data from the request
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('message', '').strip()

        # Validation checks
        if not name:
            return jsonify({'status': 'error', 'message': 'Name is required.'}), 400
        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({'status': 'error', 'message': 'Invalid email format.'}), 400
        if not phone or not re.match(PHONE_REGEX, phone):
            return jsonify({'status': 'error', 'message': 'Invalid phone number format.'}), 400
        if not message:
            return jsonify({'status': 'error', 'message': 'Message is required.'}), 400

        # In production, you might save this data to a database or send an email here
        # For now, just return a success response
        return jsonify({'status': 'success', 'message': 'Form submitted successfully!'}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'status': 'error', 'message': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Template (contact_form.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equipment Inquiry Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
